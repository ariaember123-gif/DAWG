// $DAWG — PFP Generator

const sel = { hair: '', outfit: '', accessory: '', background: '', style: '' };

const QUOTES = [
  'DAWG is putting on his fit...',
  'Styling the goodest boi...',
  'Activating degen mode...',
  'Combing the spiky hair...',
  'Polishing the laser eyes...',
  'Pulling on the hoodie...',
  'Diamond paws incoming...',
  'Based energy loading...',
  'To the moon… after this fit change…',
  'The pack awaits your PFP…',
  'Applying maximum drip...',
  'FAL.ai working its magic...',
];

const PRESETS = {
  supergoku: { hair:'Super Saiyan spiky golden anime hair', outfit:'orange karate gi martial arts', accessory:'futuristic silver visor shield sunglasses', background:'deep space galaxy stars nebula cosmic purple background', style:'anime cel-shaded Japanese illustration style' },
  ninja:     { hair:'white spiky anime ninja hair', outfit:'black ninja outfit with bandana scarf', accessory:'leaf village konoha ninja forehead headband', background:'Tokyo neon cyberpunk city rainy night background', style:'anime cel-shaded Japanese illustration style' },
  bullish:   { hair:'slicked back mafia boss hair', outfit:'luxury Gucci designer tracksuit gold chains', accessory:'thick gold chains diamond necklace bling', background:'green neon up arrows stock market bullish pumping background', style:'photorealistic ultra high detail photography' },
  cyber:     { hair:'blue streaked emo hair', outfit:'streetwear oversized hoodie chains sneakers', accessory:'glowing red neon laser eyes effect', background:'Tokyo neon cyberpunk city rainy night background', style:'neon glowing outline synthwave retro 80s style' },
  royal:     { hair:'slicked back mafia boss hair', outfit:'black tuxedo white shirt bow tie', accessory:'golden crown royal king headpiece', background:'clean white minimal background', style:'3D CGI render stylized Pixar-like style' },
  moon:      { hair:'wild rainbow colored afro hair', outfit:'NASA astronaut space suit helmet', accessory:'futuristic silver visor shield sunglasses', background:'deep space galaxy stars nebula cosmic purple background', style:'photorealistic ultra high detail photography' },
};

/* ── chip wiring ──────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.chips').forEach(group => {
    const field = group.dataset.field;
    group.querySelectorAll('.chip').forEach(chip => {
      chip.addEventListener('click', () => {
        if (chip.classList.contains('active')) {
          chip.classList.remove('active');
          sel[field] = '';
        } else {
          group.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          sel[field] = chip.dataset.val;
        }
        syncTraitsBar();
      });
    });
  });
});

function syncTraitsBar() {
  const icons = { hair:'💈', outfit:'👗', accessory:'🕶️', background:'🌆', style:'✨' };
  const chips = document.getElementById('traitsChips');
  const active = Object.entries(sel).filter(([,v]) => v);
  if (!active.length) {
    chips.innerHTML = '<span class="no-traits">None selected</span>';
    return;
  }
  chips.innerHTML = active.map(([k]) => {
    const el = document.querySelector(`.chips[data-field="${k}"] .chip.active`);
    return `<span class="t-tag">${icons[k]} ${el ? el.textContent : ''}</span>`;
  }).join('');
}

/* ── generate ─────────────────────────────── */
async function generatePFP() {
  const custom = document.getElementById('customPrompt').value.trim();
  if (!Object.values(sel).some(v => v) && !custom) {
    toast('🐾 Pick some traits first!'); return;
  }

  // ui → loading
  const btn = document.getElementById('genBtn');
  btn.disabled = true;
  document.getElementById('genBtnText').style.display = 'none';
  document.getElementById('genBtnLoad').style.display  = '';

  hide('statePlaceholder'); hide('outputImg'); hide('stateError');
  hide('outputActions'); hide('promptBox');
  show('stateLoading');

  const lq = document.getElementById('loadQuote');
  lq.textContent = rndQuote();
  const qi = setInterval(() => { lq.textContent = rndQuote(); }, 3000);

  try {
    const res = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ ...sel, prompt: custom }),
    });
    const data = await res.json();
    clearInterval(qi);

    if (data.error) {
      showError(data.error);
    } else {
      const img = document.getElementById('outputImg');
      img.onload = () => {
        hide('stateLoading');
        show('outputImg');
        show('outputActions');
        show('promptBox');
        document.getElementById('promptTxt').textContent = data.prompt;
        document.getElementById('dlBtn').href = data.image_url;
      };
      img.onerror = () => showError('Failed to load generated image.');
      img.src = data.image_url;
    }
  } catch (err) {
    clearInterval(qi);
    showError(err.message);
  } finally {
    btn.disabled = false;
    document.getElementById('genBtnText').style.display = '';
    document.getElementById('genBtnLoad').style.display  = 'none';
  }
}

function showError(msg) {
  hide('stateLoading');
  show('stateError');
  document.getElementById('errDetail').textContent = msg;
}

/* ── presets ──────────────────────────────── */
function applyPreset(name) {
  const p = PRESETS[name]; if (!p) return;
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
  Object.assign(sel, p);
  Object.entries(p).forEach(([field, val]) => {
    const grp = document.querySelector(`.chips[data-field="${field}"]`);
    grp?.querySelectorAll('.chip').forEach(c => { if (c.dataset.val === val) c.classList.add('active'); });
  });
  syncTraitsBar();
  document.querySelector('.pfp-wrap')?.scrollIntoView({ behavior: 'smooth' });
  toast('✨ Preset applied!');
}

/* ── share ────────────────────────────────── */
function tweetIt() {
  const txt = encodeURIComponent('Just generated my $DAWG PFP with the DAWG PFP Generator 🐶🔥\n\nCA: 6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump\n\n#DAWG #Solana #memecoins');
  window.open(`https://twitter.com/intent/tweet?text=${txt}`, '_blank');
}

/* ── helpers ──────────────────────────────── */
const rndQuote = () => QUOTES[Math.floor(Math.random() * QUOTES.length)];
const show = id => { const el = document.getElementById(id); if (el) el.style.display = ''; };
const hide = id => { const el = document.getElementById(id); if (el) el.style.display = 'none'; };
