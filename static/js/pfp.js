// $DAWG — PFP Generator JS

const selections = {
  hair: '',
  outfit: '',
  accessory: '',
  background: '',
  style: '',
};

const loadingQuotes = [
  "DAWG is putting on his fit...",
  "Styling the goodest boi...",
  "Activating degen mode...",
  "Combing the spiky hair...",
  "Polishing the laser eyes...",
  "Pulling on the hoodie...",
  "Diamond paws incoming...",
  "Based energy loading...",
  "To the moon... after this outfit...",
  "The pack awaits your PFP...",
];

// Chip selection logic
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.chip-group').forEach(group => {
    const field = group.dataset.field;
    group.querySelectorAll('.chip').forEach(chip => {
      chip.addEventListener('click', () => {
        // Toggle off if already active
        if (chip.classList.contains('active')) {
          chip.classList.remove('active');
          selections[field] = '';
        } else {
          // Remove active from siblings
          group.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
          chip.classList.add('active');
          selections[field] = chip.dataset.val;
        }
        updateTraitsSummary();
      });
    });
  });
});

function updateTraitsSummary() {
  const list = document.getElementById('traitsList');
  if (!list) return;

  const labels = {
    hair: '💈',
    outfit: '👗',
    accessory: '🕶️',
    background: '🎨',
    style: '✨',
  };

  const active = Object.entries(selections).filter(([, v]) => v);

  if (active.length === 0) {
    list.innerHTML = '<span class="trait-empty">No traits selected yet</span>';
    return;
  }

  list.innerHTML = active.map(([k, v]) => {
    // Get chip label for display
    const chip = document.querySelector(`.chip-group[data-field="${k}"] .chip.active`);
    const label = chip ? chip.textContent : v.substring(0, 20);
    return `<span class="trait-tag">${labels[k]} ${label}</span>`;
  }).join('');
}

async function generatePFP() {
  const btn = document.getElementById('generateBtn');
  const btnText = btn.querySelector('.gen-btn-text');
  const btnLoading = btn.querySelector('.gen-btn-loading');
  const placeholder = document.getElementById('outputPlaceholder');
  const loadingEl = document.getElementById('outputLoading');
  const imgEl = document.getElementById('generatedImg');
  const errorEl = document.getElementById('outputError');
  const errorDetail = document.getElementById('errorDetail');
  const actions = document.getElementById('outputActions');
  const promptDisplay = document.getElementById('promptDisplay');
  const promptText = document.getElementById('promptText');
  const loadingQuote = document.getElementById('loadingQuote');

  const customPrompt = document.getElementById('customPrompt').value.trim();

  // Must have at least one trait or custom prompt
  const hasSelection = Object.values(selections).some(v => v) || customPrompt;
  if (!hasSelection) {
    showToast('🐾 Pick some traits first!');
    return;
  }

  // UI state: loading
  btn.disabled = true;
  btnText.style.display = 'none';
  btnLoading.style.display = '';
  placeholder.style.display = 'none';
  imgEl.style.display = 'none';
  errorEl.style.display = 'none';
  actions.style.display = 'none';
  promptDisplay.style.display = 'none';
  loadingEl.style.display = 'flex';
  loadingQuote.textContent = loadingQuotes[Math.floor(Math.random() * loadingQuotes.length)];

  // Rotate loading quotes
  const quoteInterval = setInterval(() => {
    loadingQuote.textContent = loadingQuotes[Math.floor(Math.random() * loadingQuotes.length)];
  }, 3000);

  try {
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        hair: selections.hair,
        outfit: selections.outfit,
        accessory: selections.accessory,
        background: selections.background,
        style: selections.style,
        prompt: customPrompt,
      }),
    });

    const data = await response.json();
    clearInterval(quoteInterval);

    if (data.error) {
      errorEl.style.display = 'flex';
      errorDetail.textContent = data.error;
      loadingEl.style.display = 'none';
    } else {
      // Show generated image
      imgEl.onload = () => {
        loadingEl.style.display = 'none';
        imgEl.style.display = 'block';
        actions.style.display = 'flex';
        promptDisplay.style.display = 'block';
        promptText.textContent = data.prompt;

        // Set download link
        document.getElementById('downloadBtn').href = data.image_url;
      };
      imgEl.onerror = () => {
        loadingEl.style.display = 'none';
        errorEl.style.display = 'flex';
        errorDetail.textContent = 'Failed to load the generated image.';
      };
      imgEl.src = data.image_url;
    }
  } catch (err) {
    clearInterval(quoteInterval);
    loadingEl.style.display = 'none';
    errorEl.style.display = 'flex';
    errorDetail.textContent = err.message;
  } finally {
    btn.disabled = false;
    btnText.style.display = '';
    btnLoading.style.display = 'none';
  }
}

function shareOnTwitter() {
  const text = encodeURIComponent('Just made my $DAWG PFP using the DAWG PFP generator 🐶🔥\n\nCA: 6dKMmBzboiytxnKqAzUpSiarK7LWoFWicq5T8ZEZpump\n\n#DAWG #Solana #memecoins');
  window.open(`https://twitter.com/intent/tweet?text=${text}`, '_blank');
}

// PRESETS
const presets = {
  supergoku: {
    hair: 'Super Saiyan spiky golden',
    outfit: 'orange karate gi martial arts',
    accessory: 'futuristic visor sunglasses',
    background: 'galaxy stars and nebula cosmic',
    style: 'anime cel-shaded illustration',
  },
  ninja: {
    hair: 'white spiky anime ninja',
    outfit: 'black ninja outfit with bandana scarf',
    accessory: 'leaf village ninja headband',
    background: 'Tokyo neon cyberpunk city night',
    style: 'anime cel-shaded illustration',
  },
  bullish: {
    hair: 'slicked back mafia boss',
    outfit: 'luxury Gucci designer tracksuit',
    accessory: 'gold chains and bling',
    background: 'green neon arrows pointing up, stock market bullish',
    style: 'photorealistic high detail',
  },
  cyber: {
    hair: 'blue streaked emo',
    outfit: 'streetwear hoodie and chains',
    accessory: 'neon laser eyes glowing',
    background: 'Tokyo neon cyberpunk city night',
    style: 'neon glowing outline synthwave',
  },
  royal: {
    hair: 'slicked back mafia boss',
    outfit: 'tuxedo and bow tie',
    accessory: 'crown and royal scepter',
    background: 'white clean minimal',
    style: '3D render CGI stylized',
  },
  moonbound: {
    hair: 'wild rainbow colored afro',
    outfit: 'astronaut space suit',
    accessory: 'futuristic visor sunglasses',
    background: 'galaxy stars and nebula cosmic',
    style: 'photorealistic high detail',
  },
};

function applyPreset(name) {
  const p = presets[name];
  if (!p) return;

  // Clear all chips
  document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));

  // Apply preset values
  Object.entries(p).forEach(([field, val]) => {
    selections[field] = val;
    // Find matching chip
    const group = document.querySelector(`.chip-group[data-field="${field}"]`);
    if (group) {
      group.querySelectorAll('.chip').forEach(chip => {
        if (chip.dataset.val === val) chip.classList.add('active');
      });
    }
  });

  updateTraitsSummary();

  // Scroll to generator
  document.querySelector('.pfp-container').scrollIntoView({ behavior: 'smooth' });
  showToast('✨ Preset applied!');
}

function showToast(msg) {
  const toast = document.getElementById('toast');
  if (!toast) return;
  toast.textContent = msg;
  toast.classList.add('show');
  setTimeout(() => toast.classList.remove('show'), 2500);
}
