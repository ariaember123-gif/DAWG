# $DAWG — Memecoin Website + PFP Generator

## Project Structure
```
dawg/
├── app.py                 # Flask backend
├── requirements.txt       # Python dependencies
├── vercel.json            # Vercel deployment config
├── templates/
│   ├── index.html         # Landing page
│   └── pfp.html           # PFP Generator page
└── static/
    ├── css/
    │   ├── main.css        # Main styles
    │   └── pfp.css         # PFP generator styles
    ├── js/
    │   ├── main.js         # Nav, copy CA, animations
    │   └── pfp.js          # PFP generation logic
    └── images/             # Add your images here
```

## Setup (Local)
```bash
pip install -r requirements.txt
python app.py
# Visit http://localhost:5000
```

## Deploy to Vercel
1. Push to GitHub
2. Import repo on vercel.com
3. Add environment variable: `FAL_KEY = your_fal_api_key`
4. Deploy!

## Adding Images
- **Favicon/Icon**: Add to `static/images/icon.png` and add `<link rel="icon" href="/static/images/icon.png">` in both HTML `<head>` tags
- **Hero image**: Replace the `.hero-img-placeholder` div in `index.html` with `<img src="/static/images/hero.png" alt="DAWG" />`
- **Gallery images**: Replace the `.placeholder-card` divs in `index.html` with `<img>` tags

## PFP Generator
- Uses **fal.ai FLUX** model for AI generation
- Set `FAL_KEY` environment variable in Vercel
- Users pick traits (hair, outfit, accessories, background, style) via chips
- 6 presets available (Super Saiyan, Ninja, Bullish, Cyberpunk, Royal, Moon)
- Custom prompt field for extra details
- Download & share to X functionality

## Customization
- Social links: Update `href="#"` in `index.html` community section
- CA: Already set to `6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump`
- Colors: Edit CSS variables in `main.css` (`:root` block)
