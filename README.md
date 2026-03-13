# $DAWG — Serverless Website + PFP Generator

Fully serverless Python on Vercel. No Flask. No server. Just clean `BaseHTTPRequestHandler` functions.

## Project Structure

```
dawg-serverless/
├── api/
│   ├── index.py       ← GET /           (landing page)
│   ├── pfp.py         ← GET /pfp        (PFP generator page)
│   └── generate.py    ← POST /api/generate  (fal.ai call)
├── public/
│   ├── main.css       ← shared styles
│   ├── pfp.css        ← PFP page styles
│   ├── main.js        ← shared JS (nav, CA copy, scroll reveal)
│   ├── pfp.js         ← PFP generator logic
│   └── images/        ← drop your images here
├── requirements.txt
├── vercel.json
└── README.md
```

## Deploy to Vercel (2 minutes)

1. Push this folder to a GitHub repo
2. Go to [vercel.com](https://vercel.com) → Import project
3. Add environment variable:
   - **Name:** `FAL_KEY`
   - **Value:** your fal.ai API key
4. Click Deploy ✅

## Local Dev

```bash
pip install requests
vercel dev
# or test individual handlers with Python's built-in HTTP server
```

## Adding Images

### Hero image
In `api/index.py`, find:
```html
<!-- SWAP: <img src="/static/images/hero.png" alt="DAWG"> -->
<div class="hero-placeholder">...</div>
```
Replace with:
```html
<img src="/static/images/hero.png" alt="DAWG">
```

### Gallery images
In `api/index.py`, replace each `.gal-slot` div:
```html
<div class="gal-slot"><img src="/static/images/meme1.png" alt="DAWG meme"></div>
```

### Favicon
Add to `<head>` in both `api/index.py` and `api/pfp.py`:
```html
<link rel="icon" href="/static/images/icon.png">
```

## Social Links
Update `href="#"` in the community section inside `api/index.py`:
- Twitter/X: your Twitter URL
- Telegram: your Telegram group URL

## Customising Colours
Edit `:root` variables in `public/main.css`:
```css
--y:  #FFD700;   /* yellow accent */
--yo: #FF6B1A;   /* orange shadow */
```

## fal.ai Model
Currently using `fal-ai/flux/dev` (FLUX.1 Dev).
To switch models, change `FAL_URL` in `api/generate.py`.
Other options: `fal-ai/flux/schnell` (faster), `fal-ai/flux-pro` (higher quality).
