from flask import Flask, render_template, request, jsonify
import os
import requests

app = Flask(__name__)

FAL_KEY = os.environ.get("FAL_KEY", "")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pfp")
def pfp():
    return render_template("pfp.html")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    user_prompt = data.get("prompt", "")
    style = data.get("style", "")
    hair = data.get("hair", "")
    outfit = data.get("outfit", "")
    accessory = data.get("accessory", "")
    background = data.get("background", "")
    vibe = data.get("vibe", "")

    full_prompt = (
        f"A portrait profile picture of a cute Shiba Inu dog (Doge/Dawg), "
        f"photorealistic fluffy golden-cream fur, smiling expression, "
    )

    if hair:
        full_prompt += f"{hair} hair style, "
    if outfit:
        full_prompt += f"wearing {outfit}, "
    if accessory:
        full_prompt += f"with {accessory}, "
    if background:
        full_prompt += f"background: {background}, "
    if vibe:
        full_prompt += f"vibe: {vibe}, "
    if style:
        full_prompt += f"art style: {style}, "
    if user_prompt:
        full_prompt += user_prompt

    full_prompt += (
        ", centered portrait composition, square format, high quality, "
        "detailed, vibrant, NFT profile picture style, 1:1 aspect ratio"
    )

    if not FAL_KEY:
        return jsonify({"error": "FAL_KEY not configured"}), 500

    try:
        headers = {
            "Authorization": f"Key {FAL_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "prompt": full_prompt,
            "image_size": "square_hd",
            "num_inference_steps": 28,
            "guidance_scale": 3.5,
            "num_images": 1,
            "enable_safety_checker": True,
        }
        resp = requests.post(
            "https://fal.run/fal-ai/flux/dev",
            headers=headers,
            json=payload,
            timeout=120,
        )
        resp.raise_for_status()
        result = resp.json()
        image_url = result["images"][0]["url"]
        return jsonify({"image_url": image_url, "prompt": full_prompt})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
