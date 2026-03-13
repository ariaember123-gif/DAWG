from http.server import BaseHTTPRequestHandler

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>$DAWG PFP Generator — Make Your Dawg</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@400;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/main.css">
  <link rel="stylesheet" href="/static/pfp.css">
</head>
<body class="pfp-page">

<nav class="nav">
  <div class="nav-logo">
    <div class="nav-icon">🐶</div>
    <span>$DAWG</span>
  </div>
  <ul class="nav-links">
    <li><a href="/">Home</a></li>
    <li><a href="/#tokenomics">Tokenomics</a></li>
    <li><a href="/#how-to-buy">Buy</a></li>
    <li><a href="/pfp" class="nav-cta active">PFP Generator 🎨</a></li>
  </ul>
  <button class="hamburger" onclick="toggleMenu()">☰</button>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <a href="/">Home</a>
  <a href="/#tokenomics">Tokenomics</a>
  <a href="/#how-to-buy">Buy</a>
  <a href="/pfp">PFP Generator 🎨</a>
</div>

<div class="pfp-hero">
  <h1 class="pfp-title">DAWG <span class="accent">PFP</span> Generator</h1>
  <p class="pfp-sub">Create your legendary Dawg profile picture. Powered by AI. 100% Degen.</p>
</div>

<div class="pfp-wrap">

  <!-- LEFT PANEL: trait pickers -->
  <div class="pfp-left">

    <div class="trait-block">
      <h3 class="trait-title">💈 Hair Style</h3>
      <div class="chips" data-field="hair">
        <button class="chip" data-val="Super Saiyan spiky golden anime hair">Super Saiyan</button>
        <button class="chip" data-val="white spiky anime ninja hair">Ninja</button>
        <button class="chip" data-val="mohawk punk rock colorful hair">Mohawk</button>
        <button class="chip" data-val="slicked back mafia boss hair">Slicked Back</button>
        <button class="chip" data-val="wild rainbow colored afro hair">Rainbow Afro</button>
        <button class="chip" data-val="blue streaked emo hair">Emo Blue</button>
        <button class="chip" data-val="samurai top knot hair bun">Samurai Bun</button>
        <button class="chip" data-val="bald no hair clean shaved head">Bald 😂</button>
      </div>
    </div>

    <div class="trait-block">
      <h3 class="trait-title">👗 Outfit</h3>
      <div class="chips" data-field="outfit">
        <button class="chip" data-val="black ninja outfit with bandana scarf">Ninja Fit</button>
        <button class="chip" data-val="luxury Gucci designer tracksuit gold chains">Gucci Drip</button>
        <button class="chip" data-val="NASA astronaut space suit helmet">Astronaut</button>
        <button class="chip" data-val="streetwear oversized hoodie chains sneakers">Streetwear</button>
        <button class="chip" data-val="black tuxedo white shirt bow tie">Tuxedo</button>
        <button class="chip" data-val="viking warrior fur armor horned helmet">Viking</button>
        <button class="chip" data-val="white karate gi black belt martial arts">Karate</button>
        <button class="chip" data-val="punk rock leather jacket metal spikes">Punk</button>
      </div>
    </div>

    <div class="trait-block">
      <h3 class="trait-title">🕶️ Accessories</h3>
      <div class="chips" data-field="accessory">
        <button class="chip" data-val="futuristic silver visor shield sunglasses">Visor Shades</button>
        <button class="chip" data-val="classic black wayfarer sunglasses">Wayfarers</button>
        <button class="chip" data-val="leaf village konoha ninja forehead headband">Ninja Band</button>
        <button class="chip" data-val="thick gold chains diamond necklace bling">Gold Chains</button>
        <button class="chip" data-val="brown cowboy hat western style">Cowboy Hat</button>
        <button class="chip" data-val="golden crown royal king headpiece">Crown 👑</button>
        <button class="chip" data-val="pirate eye patch and tricorn hat">Pirate</button>
        <button class="chip" data-val="glowing red neon laser eyes effect">Laser Eyes</button>
      </div>
    </div>

    <div class="trait-block">
      <h3 class="trait-title">🌆 Background</h3>
      <div class="chips" data-field="background">
        <button class="chip" data-val="green neon up arrows stock market bullish pumping background">Bullish 📈</button>
        <button class="chip" data-val="deep space galaxy stars nebula cosmic purple background">Galaxy</button>
        <button class="chip" data-val="Tokyo neon cyberpunk city rainy night background">Cyberpunk</button>
        <button class="chip" data-val="clean white minimal background">White</button>
        <button class="chip" data-val="golden sunset ocean rooftop city skyline background">Rooftop</button>
        <button class="chip" data-val="dramatic orange fire flames burning background">On Fire 🔥</button>
        <button class="chip" data-val="raining dollar bills money cash background">Money Rain</button>
        <button class="chip" data-val="solana blockchain purple gradient abstract background">Solana</button>
      </div>
    </div>

    <div class="trait-block">
      <h3 class="trait-title">✨ Art Style</h3>
      <div class="chips" data-field="style">
        <button class="chip" data-val="photorealistic ultra high detail photography">Photorealistic</button>
        <button class="chip" data-val="anime cel-shaded Japanese illustration style">Anime</button>
        <button class="chip" data-val="pixel art 8-bit retro video game style">Pixel Art</button>
        <button class="chip" data-val="classic oil painting artistic brushwork style">Oil Paint</button>
        <button class="chip" data-val="comic book bold ink lines pop art style">Comic</button>
        <button class="chip" data-val="soft watercolor dreamy pastel painting style">Watercolor</button>
        <button class="chip" data-val="3D CGI render stylized Pixar-like style">3D Render</button>
        <button class="chip" data-val="neon glowing outline synthwave retro 80s style">Neon Glow</button>
      </div>
    </div>

    <div class="trait-block">
      <h3 class="trait-title">📝 Custom Details</h3>
      <textarea id="customPrompt" class="custom-input"
        placeholder="e.g. 'holding a bag of $DAWG coins', 'winking', 'smoking a cigar', 'flexing muscles'..."></textarea>
    </div>

    <button class="gen-btn" id="genBtn" onclick="generatePFP()">
      <span id="genBtnText">🎨 Generate My DAWG PFP</span>
      <span id="genBtnLoad" style="display:none">⏳ Generating...</span>
    </button>
    <p class="gen-note">Powered by <strong>fal.ai FLUX</strong> · ~15–25s per generation</p>
  </div>

  <!-- RIGHT PANEL: output -->
  <div class="pfp-right">

    <div class="output-box" id="outputBox">
      <div id="statePlaceholder" class="state-placeholder">
        <div class="ph-dawg">🐶</div>
        <p>Your legendary DAWG PFP<br>will appear here</p>
        <p class="ph-hint">Pick traits → hit Generate</p>
      </div>

      <div id="stateLoading" class="state-loading" style="display:none">
        <div class="spinner"></div>
        <p class="load-title">DAWG is getting dressed...</p>
        <p class="load-quote" id="loadQuote"></p>
      </div>

      <img id="outputImg" src="" alt="Generated DAWG PFP" style="display:none"/>

      <div id="stateError" class="state-error" style="display:none">
        <p>😢 Generation failed</p>
        <p class="err-detail" id="errDetail"></p>
        <button class="btn-secondary" onclick="generatePFP()">Try Again</button>
      </div>
    </div>

    <div class="traits-bar" id="traitsBar">
      <span class="traits-label">Traits:</span>
      <div class="traits-chips" id="traitsChips"><span class="no-traits">None selected</span></div>
    </div>

    <div id="outputActions" class="output-actions" style="display:none">
      <a id="dlBtn" href="#" download="dawg-pfp.png" class="btn-primary">⬇ Download</a>
      <button class="btn-secondary" onclick="generatePFP()">🔄 Regenerate</button>
      <button class="btn-tweet" onclick="tweetIt()">𝕏 Share</button>
    </div>

    <div id="promptBox" class="prompt-box" style="display:none">
      <p class="prompt-lbl">AI Prompt Used:</p>
      <p class="prompt-txt" id="promptTxt"></p>
    </div>
  </div>
</div>

<!-- PRESETS -->
<div class="presets-section">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title">Quick <span class="accent">Presets</span></h2>
      <p class="sec-sub">One click to apply a full look — then customise from there</p>
    </div>
    <div class="presets-grid">
      <div class="preset-card reveal" onclick="applyPreset('supergoku')">
        <div class="preset-icon">⚡</div><p>Super Saiyan DAWG</p>
      </div>
      <div class="preset-card reveal" onclick="applyPreset('ninja')">
        <div class="preset-icon">🥷</div><p>Ninja DAWG</p>
      </div>
      <div class="preset-card reveal" onclick="applyPreset('bullish')">
        <div class="preset-icon">📈</div><p>Bullish DAWG</p>
      </div>
      <div class="preset-card reveal" onclick="applyPreset('cyber')">
        <div class="preset-icon">🤖</div><p>Cyberpunk DAWG</p>
      </div>
      <div class="preset-card reveal" onclick="applyPreset('royal')">
        <div class="preset-icon">👑</div><p>Royal DAWG</p>
      </div>
      <div class="preset-card reveal" onclick="applyPreset('moon')">
        <div class="preset-icon">🚀</div><p>Moon DAWG</p>
      </div>
    </div>
  </div>
</div>

<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-logo">🐶 $DAWG</div>
    <p class="footer-disc">$DAWG is a meme coin with no intrinsic value. Not financial advice. DYOR.</p>
    <p class="footer-copy">© 2025 $DAWG · All rights reserved · Woof.</p>
  </div>
</footer>

<div id="toast" class="toast"></div>
<script src="/static/main.js"></script>
<script src="/static/pfp.js"></script>
</body>
</html>"""


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))
