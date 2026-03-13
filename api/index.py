from http.server import BaseHTTPRequestHandler

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>$DAWG — The Goodest Boi on Solana</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Bangers&family=Nunito:wght@400;700;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/static/main.css">
</head>
<body>

<nav class="nav">
  <div class="nav-logo">
    <div class="nav-icon">🐶</div>
    <span>$DAWG</span>
  </div>
  <ul class="nav-links">
    <li><a href="#about">About</a></li>
    <li><a href="#tokenomics">Tokenomics</a></li>
    <li><a href="#how-to-buy">Buy</a></li>
    <li><a href="#community">Community</a></li>
    <li><a href="/pfp" class="nav-cta">PFP Generator 🎨</a></li>
  </ul>
  <button class="hamburger" onclick="toggleMenu()">☰</button>
</nav>
<div class="mobile-menu" id="mobileMenu">
  <a href="#about">About</a>
  <a href="#tokenomics">Tokenomics</a>
  <a href="#how-to-buy">Buy</a>
  <a href="#community">Community</a>
  <a href="/pfp">PFP Generator 🎨</a>
</div>

<!-- HERO -->
<section class="hero" id="home">
  <div class="hero-glow"></div>
  <div class="hero-content">
    <div class="hero-badge">🔥 Live on Solana</div>
    <h1 class="hero-title">$DAWG</h1>
    <p class="hero-sub">The Goodest Boi in all of Crypto</p>
    <p class="hero-desc">No roadmap. No utility. Just pure dawg energy.<br>The only coin that barks back at the bears. 🐾</p>
    <div class="hero-btns">
      <a href="https://pump.fun/coin/6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump" target="_blank" class="btn-primary">Buy $DAWG 🚀</a>
      <a href="/pfp" class="btn-secondary">Make My PFP 🎨</a>
    </div>
    <div class="ca-box">
      <span class="ca-label">CA</span>
      <code class="ca-addr" id="caText">6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump</code>
      <button class="ca-copy" onclick="copyCA()">Copy</button>
    </div>
  </div>
  <div class="hero-visual">
    <div class="hero-img-wrap">
      <!-- SWAP: <img src="/static/images/hero.png" alt="DAWG"> -->
      <div class="hero-placeholder"><span>🐶</span><p>Hero Image</p></div>
    </div>
    <div class="ring r1"></div>
    <div class="ring r2"></div>
    <div class="ring r3"></div>
  </div>
</section>

<!-- TICKER -->
<div class="ticker-wrap">
  <div class="ticker-track">
    <span>🐾 $DAWG TO THE MOON</span><span>💰 BUY THE DIP</span><span>🚀 1000X INCOMING</span>
    <span>🐶 WOOF WOOF</span><span>💎 DIAMOND PAWS</span><span>🔥 BULLISH AF</span>
    <span>🐾 $DAWG TO THE MOON</span><span>💰 BUY THE DIP</span><span>🚀 1000X INCOMING</span>
    <span>🐶 WOOF WOOF</span><span>💎 DIAMOND PAWS</span><span>🔥 BULLISH AF</span>
  </div>
</div>

<!-- ABOUT -->
<section class="section" id="about">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title">Who is <span class="accent">$DAWG</span>?</h2>
      <p class="sec-sub">Born in the trenches. Raised on green candles.</p>
    </div>
    <div class="about-grid">
      <div class="card reveal">
        <div class="card-icon">🐕</div>
        <h3>Pure Dawg Energy</h3>
        <p>$DAWG doesn't need a whitepaper. He just needs good vibes, diamond paws, and a community that goes absolutely feral when the chart pumps.</p>
      </div>
      <div class="card reveal">
        <div class="card-icon">🌕</div>
        <h3>Moon Bound</h3>
        <p>Every dip is just $DAWG sitting. Every pump is $DAWG standing up. He's been sitting a while. He's about to stand up REAL hard.</p>
      </div>
      <div class="card reveal">
        <div class="card-icon">💪</div>
        <h3>Community First</h3>
        <p>The dawg pack moves together. No rugs, no devs dumping, no nonsense. Just the most loyal community on Solana holding strong.</p>
      </div>
      <div class="card reveal">
        <div class="card-icon">🎨</div>
        <h3>Culture Coin</h3>
        <p>From viral memes to custom PFPs, $DAWG is building a brand. Generate your own DAWG PFP and flex on CT every single day.</p>
      </div>
    </div>
  </div>
</section>

<!-- GALLERY -->
<section class="section gallery-section" id="gallery">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title">The <span class="accent">DAWG</span> Gallery</h2>
      <p class="sec-sub">Drop your meme images here</p>
    </div>
    <div class="gallery-grid">
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 1</p></div>
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 2</p></div>
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 3</p></div>
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 4</p></div>
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 5</p></div>
      <div class="gal-slot reveal"><span>🖼️</span><p>Image Slot 6</p></div>
    </div>
  </div>
</section>

<!-- TOKENOMICS -->
<section class="section toke-section" id="tokenomics">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title"><span class="accent">Tokenomics</span></h2>
      <p class="sec-sub">Simple. Clean. Fair. Just like a good dawg.</p>
    </div>
    <div class="toke-grid">
      <div class="toke-card big reveal"><div class="toke-num">1B</div><div class="toke-lbl">Total Supply</div></div>
      <div class="toke-card reveal"><div class="toke-num">0%</div><div class="toke-lbl">Buy Tax</div></div>
      <div class="toke-card reveal"><div class="toke-num">0%</div><div class="toke-lbl">Sell Tax</div></div>
      <div class="toke-card reveal"><div class="toke-num">🔥</div><div class="toke-lbl">LP Burned</div></div>
      <div class="toke-card reveal"><div class="toke-num">🔒</div><div class="toke-lbl">Mint Revoked</div></div>
    </div>
    <div class="ca-block">
      <p class="ca-block-label">Contract Address</p>
      <div class="ca-block-inner">
        <code>6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump</code>
        <button onclick="copyCA()">📋 Copy</button>
      </div>
    </div>
  </div>
</section>

<!-- HOW TO BUY -->
<section class="section htb-section" id="how-to-buy">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title">How to Buy <span class="accent">$DAWG</span></h2>
      <p class="sec-sub">Even your grandma can do this. (Teach her.)</p>
    </div>
    <div class="steps-row">
      <div class="step reveal">
        <div class="step-n">01</div>
        <h3>Get a Wallet</h3>
        <p>Download <strong>Phantom</strong> or <strong>Solflare</strong>. Available on iOS, Android &amp; Chrome.</p>
      </div>
      <div class="step-arrow">→</div>
      <div class="step reveal">
        <div class="step-n">02</div>
        <h3>Get SOL</h3>
        <p>Buy <strong>SOL</strong> on Coinbase, Binance or Kraken and send to your wallet.</p>
      </div>
      <div class="step-arrow">→</div>
      <div class="step reveal">
        <div class="step-n">03</div>
        <h3>Swap for $DAWG</h3>
        <p>Go to <strong>pump.fun</strong> or <strong>Raydium</strong>, paste the CA and swap.</p>
      </div>
      <div class="step-arrow">→</div>
      <div class="step reveal">
        <div class="step-n">04</div>
        <h3>HODL &amp; Woof</h3>
        <p>You're in the pack. <strong>Hold tight</strong>, spread the word, watch $DAWG run.</p>
      </div>
    </div>
    <div class="htb-cta">
      <a href="https://pump.fun/coin/6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump" target="_blank" class="btn-primary big">Buy on pump.fun 🚀</a>
    </div>
  </div>
</section>

<!-- COMMUNITY -->
<section class="section community-section" id="community">
  <div class="container">
    <div class="sec-head">
      <h2 class="sec-title">Join the <span class="accent">Pack</span></h2>
      <p class="sec-sub">The dawg pack never sleeps. Never sells. Never stops woofing.</p>
    </div>
    <div class="social-grid">
      <a href="#" target="_blank" class="social-card twitter reveal">
        <div class="s-icon">𝕏</div>
        <div class="s-name">Twitter / X</div>
        <div class="s-sub">Follow for alpha &amp; memes</div>
      </a>
      <a href="#" target="_blank" class="social-card telegram reveal">
        <div class="s-icon">✈️</div>
        <div class="s-name">Telegram</div>
        <div class="s-sub">Join the pack chat</div>
      </a>
      <a href="https://pump.fun/coin/6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump" target="_blank" class="social-card pump reveal">
        <div class="s-icon">🔥</div>
        <div class="s-name">pump.fun</div>
        <div class="s-sub">Buy &amp; track live</div>
      </a>
      <a href="/pfp" class="social-card pfp-card reveal">
        <div class="s-icon">🎨</div>
        <div class="s-name">PFP Generator</div>
        <div class="s-sub">Make your DAWG PFP</div>
      </a>
    </div>
  </div>
</section>

<footer class="footer">
  <div class="container footer-inner">
    <div class="footer-logo">🐶 $DAWG</div>
    <p class="footer-disc">$DAWG is a meme coin with no intrinsic value or expectation of financial return. For entertainment purposes only. Not financial advice. DYOR.</p>
    <p class="footer-ca">CA: 6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump</p>
    <p class="footer-copy">© 2025 $DAWG · All rights reserved · Woof.</p>
  </div>
</footer>

<div id="toast" class="toast"></div>
<script src="/static/main.js"></script>
</body>
</html>"""


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))
