import json
import os
from http.server import BaseHTTPRequestHandler

import requests


FAL_KEY = os.environ.get("FAL_KEY", "")
FAL_URL = "https://fal.run/fal-ai/flux/dev"


def build_prompt(data: dict) -> str:
    """Compose a detailed FLUX prompt from selected traits."""
    parts = [
        "A square portrait profile picture of a cute fluffy Shiba Inu dog "
        "(Doge / Dawg meme), golden-cream fur, smiling face, front-facing,"
    ]

    if data.get("hair"):
        parts.append(f"{data['hair']},")
    if data.get("outfit"):
        parts.append(f"wearing {data['outfit']},")
    if data.get("accessory"):
        parts.append(f"with {data['accessory']},")
    if data.get("background"):
        parts.append(f"background: {data['background']},")
    if data.get("style"):
        parts.append(f"rendered in {data['style']},")
    if data.get("prompt"):
        parts.append(data["prompt"] + ",")

    parts += [
        "centered portrait composition, 1:1 aspect ratio,",
        "high quality, vibrant colors, sharp details, NFT profile picture style.",
    ]
    return " ".join(parts)


class handler(BaseHTTPRequestHandler):

    def _send_json(self, status: int, body: dict):
        payload = json.dumps(body).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        if not FAL_KEY:
            self._send_json(500, {"error": "FAL_KEY environment variable is not set."})
            return

        length = int(self.headers.get("Content-Length", 0))
        try:
            raw = self.rfile.read(length)
            data = json.loads(raw)
        except (json.JSONDecodeError, ValueError):
            self._send_json(400, {"error": "Invalid JSON body."})
            return

        prompt = build_prompt(data)

        headers = {
            "Authorization": f"Key {FAL_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "prompt": prompt,
            "image_size": "square_hd",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": True,
        }

        try:
            resp = requests.post(FAL_URL, headers=headers, json=payload, timeout=120)
            resp.raise_for_status()
            result = resp.json()
            image_url = result["images"][0]["url"]
            self._send_json(200, {"image_url": image_url, "prompt": prompt})
        except requests.exceptions.HTTPError as e:
            self._send_json(502, {"error": f"fal.ai error: {e.response.status_code} — {e.response.text[:200]}"})
        except requests.exceptions.Timeout:
            self._send_json(504, {"error": "fal.ai request timed out. Try again."})
        except requests.exceptions.RequestException as e:
            self._send_json(502, {"error": str(e)})
        except (KeyError, IndexError):
            self._send_json(502, {"error": "Unexpected response structure from fal.ai."})
