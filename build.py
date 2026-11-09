import base64
import os

img_path = "/Users/airi/.gemini/antigravity/scratch/scarameow-petter/scarameow.png"
with open(img_path, "rb") as f:
    img_b64 = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

html_content = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Scarameow Kitty Petting Simulator | Cookie Clicker</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600;700&family=Nunito:wght@400;600;700;800;900&display=swap');

    :root {{
      --bg-dark: #0c0d19;
      --bg-panel: #16182c;
      --bg-card: #20233d;
      --border-color: #313659;
      --accent-anemo: #3be2c5;
      --accent-electro: #a855f7;
      --accent-gold: #fbbf24;
      --accent-pink: #f472b6;
      --scara-navy: #181d36;
    }}

    body {{
      font-family: 'Nunito', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background-color: var(--bg-dark);
      color: #f1f5f9;
      user-select: none;
      -webkit-user-select: none;
      overflow-x: hidden;
    }}

    .font-fredoka {{
      font-family: 'Fredoka', cursive, sans-serif;
    }}

    /* Teacup idle floating */
    @keyframes floaty {{
      0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
      50% {{ transform: translateY(-8px) rotate(-1deg); }}
    }}

    .animate-float {{
      animation: floaty 4s ease-in-out infinite;
    }}

    /* Steam animation */
    @keyframes steamFloat {{
      0% {{ transform: translateY(0) scale(0.8); opacity: 0; }}
      50% {{ opacity: 0.6; }}
      100% {{ transform: translateY(-35px) scale(1.4); opacity: 0; }}
    }}

    .steam-particle {{
      animation: steamFloat 2.5s infinite ease-out;
    }}

    /* Click squash-stretch */
    .pet-target {{
      transition: transform 0.08s cubic-bezier(0.34, 1.56, 0.64, 1);
      cursor: pointer;
    }}
    .pet-target:active {{
      transform: scale(0.92, 1.08) translateY(6px);
    }}
    .pet-squish {{
      transform: scale(1.08, 0.92) translateY(-4px) !important;
    }}

    /* Floating numbers */
    @keyframes floatUpFade {{
      0% {{
        opacity: 1;
        transform: translate(-50%, 0) scale(0.8) rotate(0deg);
      }}
      50% {{
        transform: translate(calc(-50% + var(--dx)), -50px) scale(1.15) rotate(var(--rot));
      }}
      100% {{
        opacity: 0;
        transform: translate(calc(-50% + var(--dx) * 1.5), -100px) scale(0.9) rotate(calc(var(--rot) * 1.5));
      }}
    }}

    .floating-text {{
      position: absolute;
      pointer-events: none;
      animation: floatUpFade 1.1s cubic-bezier(0.22, 1, 0.36, 1) forwards;
      font-weight: 800;
      text-shadow: 0 2px 8px rgba(0,0,0,0.8), 0 0 12px currentColor;
      z-index: 50;
    }}

    /* Golden item flying */
    @keyframes goldenDrift {{
      0% {{ transform: translateY(0) rotate(0deg); }}
      25% {{ transform: translateY(-20px) rotate(8deg); }}
      50% {{ transform: translateY(15px) rotate(-6deg); }}
      75% {{ transform: translateY(-15px) rotate(4deg); }}
      100% {{ transform: translateY(0) rotate(0deg); }}
    }}

    .golden-item {{
      animation: goldenDrift 3s ease-in-out infinite;
      filter: drop-shadow(0 0 14px rgba(251, 191, 36, 0.9));
      cursor: pointer;
      transition: transform 0.15s;
    }}
    .golden-item:hover {{
      transform: scale(1.2) rotate(15deg);
    }}

    /* Custom scrollbar */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: rgba(15, 23, 42, 0.5);
    }}
    ::-webkit-scrollbar-thumb {{
      background: #334155;
      border-radius: 9999px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: #475569;
    }}

    /* Glow highlights */
    .glow-anemo {{
      box-shadow: 0 0 25px -4px rgba(59, 226, 197, 0.3);
    }}
    .glow-electro {{
      box-shadow: 0 0 25px -4px rgba(168, 85, 247, 0.35);
    }}
    .glow-gold {{
      box-shadow: 0 0 25px -4px rgba(251, 191, 36, 0.4);
    }}

    /* Dialogue bubble bounce */
    @keyframes bubblePop {{
      0% {{ transform: scale(0.6) translateY(10px); opacity: 0; }}
      70% {{ transform: scale(1.04) translateY(-2px); opacity: 1; }}
      100% {{ transform: scale(1) translateY(0); opacity: 1; }}
    }}
    .bubble-animate {{
      animation: bubblePop 0.3s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
    }}

    /* Pulsing button when affordable */
    .affordable-item {{
      border-color: rgba(59, 226, 197, 0.4) !important;
      background: rgba(30, 41, 74, 0.7) !important;
    }}
    .affordable-item:hover {{
      background: rgba(43, 58, 102, 0.9) !important;
      border-color: rgba(59, 226, 197, 0.9) !important;
      transform: translateY(-2px);
    }}
  </style>
</head>
<body class="min-h-screen bg-[#0c0d19] text-slate-100 flex flex-col justify-between selection:bg-teal-500 selection:text-black">

  <!-- TOP HEADER & NEWS TICKER -->
  <header class="w-full bg-[#121424] border-b border-[#25294a] px-4 py-2.5 flex flex-wrap items-center justify-between gap-3 shadow-md z-40 relative">
    <div class="flex items-center gap-3">
      <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-purple-600 via-indigo-600 to-teal-400 p-0.5 flex items-center justify-center shadow-lg">
        <div class="w-full h-full bg-[#121424] rounded-[10px] flex items-center justify-center text-lg">
          🐾
        </div>
      </div>
      <div>
        <h1 class="text-base sm:text-lg font-bold font-fredoka tracking-wide bg-gradient-to-r from-teal-300 via-indigo-200 to-purple-300 bg-clip-text text-transparent">
          Scarameow Kitty Petting Simulator
        </h1>
        <p class="text-xs text-slate-400 flex items-center gap-2">
          <span>The Sovereign of Teacups</span>
          <span class="inline-block w-1 h-1 rounded-full bg-slate-500"></span>
          <span id="header-version" class="text-teal-400 font-medium">v1.2 Genshin Edition</span>
        </p>
      </div>
    </div>

    <!-- News Ticker -->
    <div class="hidden md:flex flex-1 max-w-xl mx-4 bg-[#181a30] border border-[#2b2f54] rounded-full px-4 py-1.5 items-center gap-2 text-xs overflow-hidden shadow-inner">
      <span class="text-amber-400 font-bold uppercase tracking-wider text-[11px] flex items-center gap-1 shrink-0">
        <span class="inline-block w-2 h-2 rounded-full bg-amber-400 animate-ping"></span>
        Teyvat Herald:
      </span>
      <div class="overflow-hidden whitespace-nowrap w-full">
        <div id="news-ticker-text" class="text-slate-300 transition-opacity duration-300 truncate">
          Scarameow seen menacingly curling toes inside ceramic mug...
        </div>
      </div>
    </div>

    <!-- Quick action buttons -->
    <div class="flex items-center gap-2">
      <button id="btn-sound" title="Toggle Sound" class="p-2 rounded-lg bg-[#1c203b] hover:bg-[#282d52] border border-[#2e345e] text-slate-300 transition flex items-center gap-1.5 text-xs font-semibold">
        <span id="sound-icon">🔊</span>
        <span class="hidden sm:inline" id="sound-text">Sound</span>
      </button>

      <button id="btn-stats" title="View Statistics" class="p-2 rounded-lg bg-[#1c203b] hover:bg-[#282d52] border border-[#2e345e] text-slate-300 transition flex items-center gap-1.5 text-xs font-semibold">
        <span>📊</span>
        <span class="hidden sm:inline">Stats</span>
      </button>

      <button id="btn-achievements" title="Achievements" class="p-2 rounded-lg bg-[#1c203b] hover:bg-[#282d52] border border-[#2e345e] text-amber-300 transition flex items-center gap-1.5 text-xs font-semibold relative">
        <span>🏆</span>
        <span class="hidden sm:inline">Badges</span>
        <span id="achieve-count-badge" class="ml-0.5 px-1.5 py-0.2 bg-amber-500 text-slate-950 font-extrabold text-[10px] rounded-full">0/24</span>
      </button>

      <button id="btn-prestige" title="Ascension (Prestige)" class="p-2 rounded-lg bg-gradient-to-r from-purple-900 to-indigo-900 hover:from-purple-800 hover:to-indigo-800 border border-purple-500/40 text-purple-200 transition flex items-center gap-1.5 text-xs font-semibold">
        <span>✨</span>
        <span class="hidden sm:inline">Ascend</span>
      </button>
    </div>
  </header>

  <!-- MAIN 3-COLUMN PLAYSPACE -->
  <main class="flex-1 w-full max-w-7xl mx-auto p-3 sm:p-5 grid grid-cols-1 lg:grid-cols-12 gap-5 items-start">

    <!-- LEFT COLUMN: THE PETTING ARENA -->
    <section class="lg:col-span-5 flex flex-col items-center bg-[#131526]/80 backdrop-blur-md border border-[#24294a] rounded-2xl p-5 shadow-2xl relative overflow-hidden">
      <!-- Background cosmetic aura -->
      <div class="absolute -top-24 -left-24 w-64 h-64 bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div class="absolute -bottom-24 -right-24 w-64 h-64 bg-purple-600/15 rounded-full blur-3xl pointer-events-none"></div>

      <!-- Bank & PPS Counters -->
      <div class="w-full text-center mb-3">
        <div class="text-xs uppercase font-extrabold tracking-widest text-teal-400/80 mb-0.5">Purr Reservoir</div>
        <div class="flex items-center justify-center gap-2">
          <span class="text-4xl sm:text-5xl font-black font-fredoka tracking-tight text-white drop-shadow-md" id="purr-counter">0</span>
          <span class="text-2xl sm:text-3xl" title="Purrs">🐾</span>
        </div>
        <div class="mt-1 flex items-center justify-center gap-3 text-xs sm:text-sm text-slate-300">
          <span class="flex items-center gap-1 text-teal-300 font-bold bg-teal-950/40 border border-teal-800/50 px-2.5 py-0.5 rounded-full">
            <span class="text-xs">⚡</span> <span id="pps-counter">0.0</span> /sec
          </span>
          <span class="flex items-center gap-1 text-amber-300 font-bold bg-amber-950/40 border border-amber-800/50 px-2.5 py-0.5 rounded-full">
            <span class="text-xs">👆</span> <span id="click-power-counter">1</span> /pet
          </span>
        </div>
      </div>

      <!-- Tsundere Speech Bubble -->
      <div class="relative w-full max-w-xs h-16 flex items-center justify-center mb-2">
        <div id="speech-bubble" class="bubble-animate bg-[#1f233f] border border-[#3b4173] text-purple-200 text-xs sm:text-sm font-semibold px-4 py-2 rounded-2xl shadow-xl text-center relative max-w-xs transition-all duration-200">
          <span id="speech-text">"Don't touch me, mortal! ...Unless it's right under the chin."</span>
          <!-- Bubble tail pointing down -->
          <div class="w-3 h-3 bg-[#1f233f] border-r border-b border-[#3b4173] transform rotate-45 absolute -bottom-1.5 left-1/2 -translate-x-1/2"></div>
        </div>
      </div>

      <!-- PETTING TARGET AREA -->
      <div class="relative w-64 h-64 sm:w-80 sm:h-80 flex items-center justify-center my-1" id="pet-area">
        <!-- Ambient decorative steam rising from cup -->
        <div class="absolute -top-4 flex gap-4 pointer-events-none opacity-40">
          <div class="w-2 h-6 bg-amber-200 rounded-full blur-[2px] steam-particle" style="animation-delay: 0s;"></div>
          <div class="w-2.5 h-8 bg-amber-100 rounded-full blur-[2px] steam-particle" style="animation-delay: 0.8s;"></div>
          <div class="w-2 h-7 bg-amber-200 rounded-full blur-[2px] steam-particle" style="animation-delay: 1.6s;"></div>
        </div>

        <!-- Pulse Ring behind cat -->
        <div id="pulse-ring" class="absolute inset-4 rounded-full border-2 border-teal-400/20 pointer-events-none scale-90 transition-transform duration-300"></div>

        <!-- The Scarameow Cat Container -->
        <div id="cat-wrapper" class="pet-target animate-float relative flex items-center justify-center p-2 rounded-full focus:outline-none" tabindex="0" role="button" aria-label="Pet Scarameow">
          <img id="scarameow-img" 
               src="{img_b64}" 
               alt="Scarameow in Yellow Teacup" 
               class="w-56 h-56 sm:w-72 sm:h-72 object-contain drop-shadow-[0_15px_25px_rgba(0,0,0,0.7)] pointer-events-none select-none transition-transform" 
               draggable="false" />
        </div>

        <!-- Floating Particles Layer -->
        <div id="particle-container" class="absolute inset-0 pointer-events-none overflow-visible"></div>
      </div>

      <!-- PETTING COMBO / ZOOMIES METER -->
      <div class="w-full max-w-sm mt-3 bg-[#181b33] border border-[#2b305c] p-2.5 rounded-xl shadow-inner">
        <div class="flex justify-between items-center text-xs mb-1">
          <span class="font-bold flex items-center gap-1.5 text-amber-300">
            <span>🔥</span> Petting Cadence / Zoomies
          </span>
          <span id="zoomies-status" class="text-[11px] text-slate-400 font-mono">Calm & Grumpy</span>
        </div>
        <div class="w-full h-3 bg-[#0f1122] rounded-full overflow-hidden border border-[#2b305a] relative">
          <div id="zoomies-bar" class="h-full bg-gradient-to-r from-teal-400 via-amber-400 to-pink-500 rounded-full transition-all duration-100" style="width: 0%;"></div>
        </div>
        <div class="text-[10px] text-slate-400 mt-1 flex justify-between">
          <span>Rapid scritches fill the bar!</span>
          <span id="frenzy-timer" class="text-pink-400 font-bold hidden">ZOOMIES ACTIVE (3x)! <span id="frenzy-secs">8</span>s</span>
        </div>
      </div>

      <!-- Current Mood / Affection Rank -->
      <div class="w-full mt-3 pt-3 border-t border-[#24294a] flex items-center justify-between text-xs text-slate-400 px-1">
        <div class="flex items-center gap-2">
          <span class="text-base" id="mood-emoji">😾</span>
          <div>
            <div class="font-bold text-slate-200" id="mood-title">Tsundere Teacup Inhabitant</div>
            <div class="text-[11px] text-slate-400" id="mood-desc">Pretends to hate the scritches.</div>
          </div>
        </div>
        <div class="text-right">
          <div class="font-mono text-teal-400 font-bold" id="total-pets-count">0 pets</div>
          <div class="text-[10px] text-slate-500">lifetime scritches</div>
        </div>
      </div>
    </section>

    <!-- RIGHT/CENTER COLUMNS: SHOP & UPGRADES -->
    <section class="lg:col-span-7 flex flex-col gap-4">

      <!-- UPGRADES RACK (CLICK PERKS & MULTIPLIERS) -->
      <div class="bg-[#131526]/80 backdrop-blur-md border border-[#24294a] rounded-2xl p-4 shadow-xl">
        <div class="flex items-center justify-between mb-2.5">
          <div class="flex items-center gap-2">
            <span class="text-base">✨</span>
            <h2 class="font-fredoka font-bold text-slate-200 text-sm sm:text-base">Scritch Mastery & Techniques</h2>
          </div>
          <span class="text-xs text-slate-400" id="upgrades-unlocked-count">0 unlocked</span>
        </div>
        
        <!-- Upgrades horizontal scroll / wrap grid -->
        <div id="upgrades-grid" class="flex flex-wrap gap-2 min-h-[58px] p-1.5 bg-[#0f1122]/70 rounded-xl border border-[#222648] items-center">
          <!-- Dynamically populated upgrade icons -->
        </div>
      </div>

      <!-- BUILDINGS / CARETAKERS SHOP -->
      <div class="bg-[#131526]/80 backdrop-blur-md border border-[#24294a] rounded-2xl p-4 sm:p-5 shadow-xl flex-1 flex flex-col">
        <div class="flex items-center justify-between mb-3 border-b border-[#24294a] pb-2.5">
          <div class="flex items-center gap-2">
            <span class="text-lg">🏡</span>
            <div>
              <h2 class="font-fredoka font-bold text-slate-100 text-base sm:text-lg">Cat Comfort & Caretakers</h2>
              <p class="text-xs text-slate-400">Enlist automated cuddle apparatuses to gather purrs</p>
            </div>
          </div>

          <!-- Buy Multiplier Selector (1x, 10x, 100x, Max) -->
          <div class="flex items-center bg-[#1a1d36] p-0.5 rounded-lg border border-[#2f3560] text-xs">
            <button class="buy-mult-btn px-2.5 py-1 rounded-md font-bold text-teal-400 bg-[#252a4d] transition" data-mult="1">1x</button>
            <button class="buy-mult-btn px-2.5 py-1 rounded-md font-bold text-slate-400 hover:text-white transition" data-mult="10">10x</button>
            <button class="buy-mult-btn px-2.5 py-1 rounded-md font-bold text-slate-400 hover:text-white transition" data-mult="100">100x</button>
          </div>
        </div>

        <!-- Buildings list container -->
        <div id="buildings-list" class="flex flex-col gap-2.5 max-h-[520px] overflow-y-auto pr-1">
          <!-- Dynamically populated building cards -->
        </div>
      </div>

    </section>

  </main>

  <!-- BOTTOM FOOTER -->
  <footer class="w-full bg-[#101221] border-t border-[#202444] px-4 py-2.5 text-xs text-slate-400 flex flex-wrap items-center justify-between gap-3 z-30">
    <div class="flex items-center gap-4">
      <span>Auto-saved to your browser.</span>
      <button id="btn-save-manual" class="text-teal-400 hover:underline flex items-center gap-1 font-semibold">
        <span>💾</span> Save Now
      </button>
      <button id="btn-export-save" class="text-indigo-400 hover:underline flex items-center gap-1 font-semibold">
        <span>📤</span> Export/Import
      </button>
      <button id="btn-wipe-save" class="text-rose-400/80 hover:text-rose-300 hover:underline flex items-center gap-1 font-semibold">
        <span>⚠️</span> Reset Progress
      </button>
    </div>
    <div class="text-slate-500 flex items-center gap-2">
      <span>Made with purrs for Genshin Impact fans</span>
      <span>•</span>
      <span class="text-amber-400">Enjoy the scritches!</span>
    </div>
  </footer>

  <!-- FLOATING GOLDEN ANEMO FEATHER / GOLDEN TUNA SPAWNER -->
  <div id="golden-cookie" class="golden-item fixed z-50 hidden cursor-pointer select-none text-4xl sm:text-5xl" style="top: 20%; left: 10%;">
    🪶
  </div>

  <!-- MODAL: STATS -->
  <div id="modal-stats" class="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[#181a33] border border-[#2f3563] rounded-2xl w-full max-w-lg p-5 shadow-2xl relative">
      <button class="modal-close absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">✕</button>
      <div class="flex items-center gap-2 mb-4">
        <span class="text-2xl">📊</span>
        <h3 class="font-fredoka text-xl font-bold text-white">Petting Ledger & Statistics</h3>
      </div>
      <div class="space-y-2 text-xs sm:text-sm text-slate-300 max-h-96 overflow-y-auto pr-1">
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Current Purrs in Bank:</span>
          <span class="font-bold text-teal-300 font-mono" id="stat-current-purrs">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">All-Time Purrs Accumulated:</span>
          <span class="font-bold text-teal-300 font-mono" id="stat-alltime-purrs">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Total Scritches Clicked:</span>
          <span class="font-bold text-amber-300 font-mono" id="stat-clicks">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Purrs from Manual Petting:</span>
          <span class="font-bold text-amber-300 font-mono" id="stat-pet-purrs">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Purrs Per Second (Passive):</span>
          <span class="font-bold text-teal-300 font-mono" id="stat-pps">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Golden Feathers Bathed:</span>
          <span class="font-bold text-amber-400 font-mono" id="stat-golden-caught">0</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Ascension Bells (Prestige):</span>
          <span class="font-bold text-purple-400 font-mono" id="stat-ascension-bells">0 (+0%)</span>
        </div>
        <div class="flex justify-between py-1.5 border-b border-[#24294a]">
          <span class="text-slate-400">Time Spent Pampering:</span>
          <span class="font-bold text-slate-200 font-mono" id="stat-time-played">0s</span>
        </div>
      </div>
      <div class="mt-5 flex justify-end">
        <button class="modal-close px-4 py-2 bg-[#252a50] hover:bg-[#32396b] text-white rounded-xl text-xs font-bold transition">Close</button>
      </div>
    </div>
  </div>

  <!-- MODAL: ACHIEVEMENTS -->
  <div id="modal-achievements" class="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[#181a33] border border-[#2f3563] rounded-2xl w-full max-w-2xl p-5 shadow-2xl relative">
      <button class="modal-close absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">✕</button>
      <div class="flex items-center gap-2 mb-1">
        <span class="text-2xl">🏆</span>
        <h3 class="font-fredoka text-xl font-bold text-white">Hall of Feline Conquests</h3>
      </div>
      <p class="text-xs text-slate-400 mb-4">Milestones accomplished in the honorable pursuit of pampering the Balladeer.</p>
      
      <div id="achievements-gallery" class="grid grid-cols-1 sm:grid-cols-2 gap-2.5 max-h-[420px] overflow-y-auto pr-1">
        <!-- Dynamically rendered achievements -->
      </div>

      <div class="mt-4 flex justify-between items-center pt-3 border-t border-[#24294a]">
        <span class="text-xs text-slate-400" id="achievements-total-progress">0 of 24 Unlocked (0%)</span>
        <button class="modal-close px-4 py-2 bg-[#252a50] hover:bg-[#32396b] text-white rounded-xl text-xs font-bold transition">Back to Petting</button>
      </div>
    </div>
  </div>

  <!-- MODAL: PRESTIGE / ASCENSION -->
  <div id="modal-prestige" class="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[#1a1738] border border-purple-500/50 rounded-2xl w-full max-w-md p-6 shadow-2xl relative text-center">
      <button class="modal-close absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">✕</button>
      <div class="w-16 h-16 rounded-full bg-gradient-to-tr from-purple-700 via-indigo-600 to-teal-400 p-0.5 mx-auto mb-3 flex items-center justify-center">
        <div class="w-full h-full bg-[#181736] rounded-full flex items-center justify-center text-3xl">
          🔔
        </div>
      </div>
      <h3 class="font-fredoka text-2xl font-bold text-purple-200 mb-1">Ascend into Wanderer Mode</h3>
      <p class="text-xs text-slate-300 mb-4">
        Reset your purrs, buildings, and upgrades in exchange for sacred <span class="text-purple-300 font-bold">Starlight Cat Bells</span>!
        Each bell grants a permanent <span class="text-teal-300 font-bold">+10% boost</span> to all future purr generation.
      </p>

      <div class="bg-[#121128] border border-purple-500/30 rounded-xl p-3 mb-4 text-left text-xs space-y-1.5">
        <div class="flex justify-between">
          <span class="text-slate-400">Current Bells Held:</span>
          <span class="font-bold text-purple-300 font-mono" id="prestige-current-bells">0 (+0%)</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Bells Earned on Reset:</span>
          <span class="font-bold text-amber-300 font-mono" id="prestige-pending-bells">+0 Bells</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Purrs Needed for Next Bell:</span>
          <span class="font-bold text-slate-300 font-mono" id="prestige-next-cost">1,000,000</span>
        </div>
      </div>

      <div class="flex gap-2 justify-center">
        <button class="modal-close px-4 py-2 bg-[#25284b] hover:bg-[#313563] text-slate-300 rounded-xl text-xs font-bold transition">Cancel</button>
        <button id="btn-confirm-ascend" class="px-5 py-2.5 bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-bold rounded-xl text-xs shadow-lg transition disabled:opacity-40 disabled:cursor-not-allowed">
          Ascend Now!
        </button>
      </div>
    </div>
  </div>

  <!-- MODAL: SAVE EXPORT / IMPORT -->
  <div id="modal-save" class="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center p-4 hidden">
    <div class="bg-[#181a33] border border-[#2f3563] rounded-2xl w-full max-w-lg p-5 shadow-2xl relative">
      <button class="modal-close absolute top-4 right-4 text-slate-400 hover:text-white text-xl font-bold">✕</button>
      <div class="flex items-center gap-2 mb-2">
        <span class="text-2xl">💾</span>
        <h3 class="font-fredoka text-xl font-bold text-white">Save Management</h3>
      </div>
      <p class="text-xs text-slate-400 mb-3">Copy your save code to backup your progress, or paste one below to load.</p>

      <div class="space-y-3">
        <div>
          <label class="block text-xs font-semibold text-slate-300 mb-1">Save Code:</label>
          <textarea id="save-data-textarea" class="w-full h-28 bg-[#0e1021] border border-[#2c315c] rounded-xl p-2.5 font-mono text-xs text-teal-300 focus:outline-none focus:border-teal-500" spellcheck="false"></textarea>
        </div>
        <div class="flex flex-wrap gap-2 justify-between">
          <button id="btn-copy-save" class="px-3.5 py-1.5 bg-[#252a50] hover:bg-[#32396b] text-teal-300 text-xs font-bold rounded-lg transition">
            📋 Copy to Clipboard
          </button>
          <button id="btn-import-save" class="px-4 py-1.5 bg-teal-600 hover:bg-teal-500 text-slate-950 font-bold text-xs rounded-lg transition">
            📥 Import Save Code
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- FLOATING TOAST CONTAINER -->
  <div id="toast-container" class="fixed bottom-5 right-5 z-50 flex flex-col gap-2 pointer-events-none max-w-sm"></div>

  <!-- GAME JAVASCRIPT LOGIC -->
  <script>
    /* =======================================================================
       1. PROCEDURAL SOUND SYNTHESIS (Web Audio API - Zero External Dependencies)
       ======================================================================= */
    class SoundEngine {{
      constructor() {{
        this.ctx = null;
        this.enabled = true;
        this.volume = 0.3;
      }}

      init() {{
        if (!this.ctx) {{
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) {{
            this.ctx = new AudioContext();
          }}
        }}
        if (this.ctx && this.ctx.state === 'suspended') {{
          this.ctx.resume();
        }}
      }}

      playPet() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {{
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();

          // Cute cat chirp/mew pitch envelope
          const baseFreq = 480 + Math.random() * 80;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(baseFreq, now);
          osc.frequency.exponentialRampToValueAtTime(baseFreq * 1.45, now + 0.05);
          osc.frequency.exponentialRampToValueAtTime(baseFreq * 0.9, now + 0.16);

          gain.gain.setValueAtTime(0.001, now);
          gain.gain.linearRampToValueAtTime(this.volume * 0.5, now + 0.02);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.18);

          osc.connect(gain);
          gain.connect(this.ctx.destination);

          osc.start(now);
          osc.stop(now + 0.2);
        }} catch(e) {{}}
      }}

      playCrit() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {{
          const now = this.ctx.currentTime;
          [587.33, 880, 1174.66].forEach((freq, idx) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(freq, now + idx * 0.04);
            gain.gain.setValueAtTime(0.001, now + idx * 0.04);
            gain.gain.linearRampToValueAtTime(this.volume * 0.4, now + idx * 0.04 + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.04 + 0.25);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + idx * 0.04);
            osc.stop(now + idx * 0.04 + 0.3);
          }});
        }} catch(e) {{}}
      }}

      playBuy() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {{
          const now = this.ctx.currentTime;
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(523.25, now);
          osc.frequency.setValueAtTime(659.25, now + 0.06);
          osc.frequency.setValueAtTime(783.99, now + 0.12);

          gain.gain.setValueAtTime(this.volume * 0.3, now);
          gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);

          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now);
          osc.stop(now + 0.26);
        }} catch(e) {{}}
      }}

      playGolden() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {{
          const now = this.ctx.currentTime;
          [440, 554.37, 659.25, 880, 1108.73].forEach((f, i) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'sine';
            osc.frequency.setValueAtTime(f, now + i * 0.05);
            gain.gain.setValueAtTime(this.volume * 0.4, now + i * 0.05);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.05 + 0.4);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.05);
            osc.stop(now + i * 0.05 + 0.45);
          }});
        }} catch(e) {{}}
      }}

      playAchievement() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;

        try {{
          const now = this.ctx.currentTime;
          [523.25, 659.25, 783.99, 1046.50].forEach((f, i) => {{
            const osc = this.ctx.createOscillator();
            const gain = this.ctx.createGain();
            osc.type = 'triangle';
            osc.frequency.setValueAtTime(f, now + i * 0.08);
            gain.gain.setValueAtTime(this.volume * 0.45, now + i * 0.08);
            gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.5);
            osc.connect(gain);
            gain.connect(this.ctx.destination);
            osc.start(now + i * 0.08);
            osc.stop(now + i * 0.08 + 0.55);
          }});
        }} catch(e) {{}}
      }}
    }}

    const sound = new SoundEngine();

    /* =======================================================================
       2. TSUNDERE DIALOGUE & NEWS DATABASE
       ======================================================================= */
    const SCARAMEOW_QUOTES = [
      "Hmph! Who gave you permission to touch my royal fur?!",
      "D-don't look at me like that, worm!",
      "That spot behind my left ear... don't you dare stop.",
      "Purr... wait! Silence! Forget you heard that acoustic malfunction!",
      "I am the God of... wait, is that a floating silver feather?!",
      "A cat? Me?! Ridiculous. Now scratch beneath my chin.",
      "Mwehehe... wait, did a meow just slip out?! Preposterous!",
      "You insolent mortal! ...More scritches on the forehead, please.",
      "My heart was carved from puppet wood, yet... this feels acceptable.",
      "Bow before the Meow-shogun! Or bring me more dried fish.",
      "If you touch my toe beans again, you shall face divine retribution!",
      "I didn't ask to sit in this oversized tea mug, but it is warm.",
      "One more pet and I'll... I'll allow one additional pet, that's all!",
      "You think you've tamed me? I'm simply using you for grooming labor.",
      "H-hey! The paws are strictly off-limits! (Unless you are gentle...)",
      "Look into my purple eyes! Feel the terror! ...Now scritch!"
    ];

    const NEWS_HEADLINES = [
      "Nahida spotted taking 4,000 commemorative photos of teacup Scarameow.",
      "Local traveler accused of abandoning daily commissions to pet cat for 6 consecutive hours.",
      "Fatui Harbingers reportedly baffled by Sixth Harbinger's sudden feline cup transformation.",
      "Dottore attempts to engineer artificial electro-catnip; immediately shredded by angry kitten claws.",
      "Bongo Head and Poko Poko Bini express jealousy over Scarameow's newfound viral fame.",
      "Wanderer insists: 'I did NOT purr. That was a high-frequency acoustic shockwave of sheer hatred.'",
      "Local teacup artisans report a 500% surge in demand for extra-large yellow ceramic mugs.",
      "Kazuha spotted composing an impromptu haiku regarding soft pink toe beans.",
      "Raiden Shogun attempts to cook cat treats; Inazuma City experiences nationwide power blackout.",
      "Paimon tries to eat Scarameow's catnip treats; gets swiped across the cheek.",
      "Akademiya scholars classify the phenomenon of 'aggressive purring' as a new elemental reaction."
    ];

    /* =======================================================================
       3. GAME DATA DEFINITIONS (Buildings, Upgrades, Achievements)
       ======================================================================= */
    const BUILDINGS = [
      {{
        id: 'box',
        name: 'Cardboard Box of Solitude',
        icon: '📦',
        desc: 'A simple haven. Even former Harbingers cannot resist an enclosed cardboard space.',
        baseCost: 15,
        basePps: 0.5
      }},
      {{
        id: 'fish',
        name: 'Dried Fish Nibbles',
        icon: '🐟',
        desc: 'Sun-dried Inazuman treats. Highly effective in lowering his defensive guard.',
        baseCost: 100,
        basePps: 4
      }},
      {{
        id: 'naku',
        name: 'Naku Weed Catnip Sachet',
        icon: '🌿',
        desc: 'Mildly infused with Electro energy. Makes his tail swish erratically.',
        baseCost: 1100,
        basePps: 16
      }},
      {{
        id: 'coaster',
        name: 'Teacup Ceramic Heated Pad',
        icon: '☕',
        desc: 'Keeps his yellow teacup cozy at a steady 38°C. Promotes involuntary loafing.',
        baseCost: 12000,
        basePps: 64
      }},
      {{
        id: 'feather_wand',
        name: 'Silver Feather Dangly Wand',
        icon: '🪶',
        desc: 'Dangled gently overhead. Reminds him of his past, but mostly it is fun to bat.',
        baseCost: 130000,
        basePps: 260
      }},
      {{
        id: 'mini_hat',
        name: 'Miniature Kasa Hat with Veils',
        icon: '👒',
        desc: 'Restores his signature Wanderer silhouette. Amplifies his haughty aura.',
        baseCost: 1400000,
        basePps: 1400
      }},
      {{
        id: 'anemo_fan',
        name: 'Anemo Updraft Floating Cushion',
        icon: '🍃',
        desc: 'Suspends the teacup in mid-air so he can look down upon all earthly creatures.',
        baseCost: 20000000,
        basePps: 7800
      }},
      {{
        id: 'gnosis_laser',
        name: 'Gnosis Resonant Laser Pointer',
        icon: '🔦',
        desc: 'Projects a glowing divine dot across the floor that must be pounced at all costs.',
        baseCost: 330000000,
        basePps: 44000
      }},
      {{
        id: 'mech_paws',
        name: 'Shouki no Meow (Cat Mech)',
        icon: '🤖',
        desc: 'A giant automated puppet suit equipped with 6 padded paws to pamper him continuously.',
        baseCost: 5100000000,
        basePps: 260000
      }},
      {{
        id: 'irminsul_tree',
        name: 'Irminsul Memory Scratch Post',
        icon: '🌳',
        desc: 'Rewrites world history so all beings are born solely to give him chin scritches.',
        baseCost: 75000000000,
        basePps: 1600000
      }},
      {{
        id: 'celestial_throne',
        name: 'Celestial Teacup Cat Galaxy',
        icon: '🌌',
        desc: 'Ascends into a cosmic feline deity resting upon a constellation of warm teacups.',
        baseCost: 1000000000000,
        basePps: 10000000
      }}
    ];

    const UPGRADES = [
      {{
        id: 'soft_fingers',
        name: 'Velvet Fingertips',
        icon: '🧤',
        cost: 100,
        desc: 'Gentle petting technique. +1 Base Purr per pet.',
        effect: (state) => {{ state.clickFlatBonus += 1; }}
      }},
      {{
        id: 'chin_focus',
        name: 'Chin Scritch Precision',
        icon: '🎯',
        cost: 600,
        desc: 'Targeting his sweet spot. Clicking gains +2% of current PPS.',
        effect: (state) => {{ state.clickPpsPercent += 0.02; }}
      }},
      {{
        id: 'ear_technique',
        name: 'Behind-The-Ear Massage',
        icon: '👂',
        cost: 3000,
        desc: 'He melts into the cup. Doubles click petting power (2x).',
        effect: (state) => {{ state.clickMultiplier *= 2; }}
      }},
      {{
        id: 'box_tape',
        name: 'Reinforced Corrugated Box',
        icon: '📦',
        cost: 1200,
        desc: 'Boxes are 2x more effective.',
        buildingId: 'box',
        effect: (state) => {{ state.buildingMults['box'] = (state.buildingMults['box'] || 1) * 2; }}
      }},
      {{
        id: 'belly_gamble',
        name: 'Forbidden Belly Rub Gamble',
        icon: '🎲',
        cost: 15000,
        desc: 'Risky maneuver! 10% chance per pet to trigger a 7x Critical Purr burst.',
        effect: (state) => {{ state.critChance += 0.10; state.critMultiplier = 7; }}
      }},
      {{
        id: 'fresh_salmon',
        name: 'Prime Inazuman Sashimi',
        icon: '🍣',
        cost: 10000,
        desc: 'Fish Nibbles are 2x more effective.',
        buildingId: 'fish',
        effect: (state) => {{ state.buildingMults['fish'] = (state.buildingMults['fish'] || 1) * 2; }}
      }},
      {{
        id: 'organic_naku',
        name: 'Purified Naku Weed Infusion',
        icon: '🔮',
        cost: 120000,
        desc: 'Catnip Sachets are 2x more effective.',
        buildingId: 'naku',
        effect: (state) => {{ state.buildingMults['naku'] = (state.buildingMults['naku'] || 1) * 2; }}
      }},
      {{
        id: 'cup_gold_leaf',
        name: '24K Gold Leaf Teacup Trim',
        icon: '✨',
        cost: 1500000,
        desc: 'Heated Ceramic Pads are 2x more effective.',
        buildingId: 'coaster',
        effect: (state) => {{ state.buildingMults['coaster'] = (state.buildingMults['coaster'] || 1) * 2; }}
      }},
      {{
        id: 'feather_glide',
        name: 'Aerodynamic Wand Tassels',
        icon: '🪽',
        cost: 16000000,
        desc: 'Feather Wands are 2x more effective.',
        buildingId: 'feather_wand',
        effect: (state) => {{ state.buildingMults['feather_wand'] = (state.buildingMults['feather_wand'] || 1) * 2; }}
      }},
      {{
        id: 'wind_whisper',
        name: 'Wanderer Wind Resonance',
        icon: '🍃',
        cost: 50000000,
        desc: 'The wind aids your touch. Clicking gains an additional +3% of PPS.',
        effect: (state) => {{ state.clickPpsPercent += 0.03; }}
      }},
      {{
        id: 'bell_chimes',
        name: 'Golden Wind Chime Hat Bells',
        icon: '🔔',
        cost: 180000000,
        desc: 'Miniature Kasa Hats are 2x more effective.',
        buildingId: 'mini_hat',
        effect: (state) => {{ state.buildingMults['mini_hat'] = (state.buildingMults['mini_hat'] || 1) * 2; }}
      }},
      {{
        id: 'divine_scritch',
        name: 'Puppet Master Touch',
        icon: '👑',
        cost: 1000000000,
        desc: 'Doubles click petting power (2x) and boosts all passive production by 15%.',
        effect: (state) => {{ 
          state.clickMultiplier *= 2; 
          state.globalMultiplier *= 1.15;
        }}
      }},
      {{
        id: 'laser_optics',
        name: 'Hyper-Charged Laser Lens',
        icon: '⚡',
        cost: 40000000000,
        desc: 'Gnosis Laser Pointers are 2x more effective.',
        buildingId: 'gnosis_laser',
        effect: (state) => {{ state.buildingMults['gnosis_laser'] = (state.buildingMults['gnosis_laser'] || 1) * 2; }}
      }},
      {{
        id: 'feline_nirvana',
        name: 'Universal Catnip Enlightenment',
        icon: '🌌',
        cost: 500000000000,
        desc: 'Scarameow accepts his destiny. All purr production doubled (2x)!',
        effect: (state) => {{ state.globalMultiplier *= 2; }}
      }}
    ];

    const ACHIEVEMENTS = [
      {{ id: 'first_pet', name: 'First Contact', icon: '🐾', desc: 'Pet Scarameow for the very first time.', check: (s) => s.totalClicks >= 1 }},
      {{ id: 'pets_50', name: 'Scritch Novice', icon: '🖐️', desc: 'Pet Scarameow 50 times.', check: (s) => s.totalClicks >= 50 }},
      {{ id: 'pets_250', name: 'Toe Bean Fanatic', icon: '🫘', desc: 'Pet Scarameow 250 times.', check: (s) => s.totalClicks >= 250 }},
      {{ id: 'pets_1000', name: 'Master Groomer', icon: '🌟', desc: 'Pet Scarameow 1,000 times.', check: (s) => s.totalClicks >= 1000 }},
      {{ id: 'purrs_100', name: 'Gentle Rumble', icon: '🐱', desc: 'Accumulate 100 total purrs.', check: (s) => s.allTimePurrs >= 100 }},
      {{ id: 'purrs_10k', name: 'Purr Resonator', icon: '🔊', desc: 'Accumulate 10,000 total purrs.', check: (s) => s.allTimePurrs >= 10000 }},
      {{ id: 'purrs_1m', name: 'Balladeer of Cuddles', icon: '💖', desc: 'Accumulate 1,000,000 total purrs.', check: (s) => s.allTimePurrs >= 1000000 }},
      {{ id: 'purrs_100m', name: 'Sovereign of the Mug', icon: '👑', desc: 'Accumulate 100,000,000 total purrs.', check: (s) => s.allTimePurrs >= 100000000 }},
      {{ id: 'purrs_1b', name: 'Divine Cat Ascendant', icon: '🌌', desc: 'Accumulate 1,000,000,000 total purrs.', check: (s) => s.allTimePurrs >= 1000000000 }},
      {{ id: 'pps_10', name: 'Steady Warmth', icon: '☕', desc: 'Reach 10 Purrs Per Second.', check: (s) => s.pps >= 10 }},
      {{ id: 'pps_1k', name: 'Purr Turbine', icon: '⚡', desc: 'Reach 1,000 Purrs Per Second.', check: (s) => s.pps >= 1000 }},
      {{ id: 'pps_100k', name: 'Feline Resonance', icon: '🌀', desc: 'Reach 100,000 Purrs Per Second.', check: (s) => s.pps >= 100000 }},
      {{ id: 'has_box', name: 'If It Fits, I Sits', icon: '📦', desc: 'Purchase your first Cardboard Box.', check: (s) => (s.buildings['box'] || 0) >= 1 }},
      {{ id: 'has_hat', name: 'The Brim Returns', icon: '👒', desc: 'Equip Scarameow with the Mini Kasa Hat.', check: (s) => (s.buildings['mini_hat'] || 0) >= 1 }},
      {{ id: 'has_mech', name: 'Shouki No Meow', icon: '🤖', desc: 'Deploy the giant automated petting mech.', check: (s) => (s.buildings['mech_paws'] || 0) >= 1 }},
      {{ id: 'has_tree', name: 'Rewriting Irminsul', icon: '🌳', desc: 'Purchase the Irminsul Scratch Post.', check: (s) => (s.buildings['irminsul_tree'] || 0) >= 1 }},
      {{ id: 'first_golden', name: 'Anemo Miracle', icon: '🪶', desc: 'Catch a floating Golden Anemo Feather.', check: (s) => s.goldenFeathersCaught >= 1 }},
      {{ id: 'golden_10', name: 'Feather Collector', icon: '✨', desc: 'Catch 10 Golden Anemo Feathers.', check: (s) => s.goldenFeathersCaught >= 10 }},
      {{ id: 'zoomies_activated', name: 'Sudden Zoomies', icon: '🔥', desc: 'Fill the Petting Cadence meter to trigger Zoomies Mode.', check: (s) => s.zoomiesTriggered >= 1 }},
      {{ id: 'belly_crit', name: 'Sweet Spot!', icon: '💥', desc: 'Trigger a Critical Scritch on Scarameow.', check: (s) => s.critTriggered >= 1 }},
      {{ id: 'upgrades_5', name: 'Technique Student', icon: '📜', desc: 'Unlock 5 scritch upgrades.', check: (s) => s.upgrades.length >= 5 }},
      {{ id: 'upgrades_all', name: 'Cat Whispering Master', icon: '🎓', desc: 'Unlock 10 or more scritch upgrades.', check: (s) => s.upgrades.length >= 10 }},
      {{ id: 'first_ascension', name: 'Reincarnation of the Cat', icon: '🔔', desc: 'Ascend for the first time and earn Starlight Bells.', check: (s) => s.ascensions >= 1 }},
      {{ id: 'speed_paws', name: 'Swift Paws of Inazuma', icon: '💨', desc: 'Pet Scarameow at least 8 times in under 1 second.', check: (s) => s.maxCadence >= 8 }}
    ];

    /* =======================================================================
       4. GAME STATE
       ======================================================================= */
    class Game {{
      constructor() {{
        this.purrs = 0;
        this.allTimePurrs = 0;
        this.totalClicks = 0;
        this.manualPurrsEarned = 0;
        this.goldenFeathersCaught = 0;
        this.zoomiesTriggered = 0;
        this.critTriggered = 0;
        this.maxCadence = 0;
        this.timePlayedSecs = 0;
        
        // Prestige
        this.ascensions = 0;
        this.starlightBells = 0;

        // Dynamic stats
        this.pps = 0;
        this.clickBase = 1;
        this.clickFlatBonus = 0;
        this.clickMultiplier = 1;
        this.clickPpsPercent = 0;
        this.critChance = 0;
        this.critMultiplier = 1;
        this.globalMultiplier = 1;

        // Inventories
        this.buildings = {{}};
        this.buildingMults = {{}};
        this.upgrades = [];
        this.unlockedAchievements = [];

        // Buy multiplier mode (1, 10, 100)
        this.buyMultiplier = 1;

        // Rapid click combo tracking
        this.recentClicks = [];
        this.zoomiesMeter = 0; // 0 to 100
        this.isZoomiesActive = false;
        this.zoomiesTimer = 0;

        // Golden cookie buff
        this.buffMultiplier = 1;
        this.buffTimer = 0;
        this.buffName = '';

        // Quotes & news timers
        this.quoteCooldown = 0;
        this.newsIndex = 0;

        // Golden cookie spawn timer
        this.goldenTimer = 60 + Math.random() * 40;

        this.init();
      }}

      init() {{
        this.loadSave();
        this.recalcStats();
        this.setupAudioListeners();
        this.setupEvents();
        this.renderAll();

        // Game Loop (20 FPS tick for smooth animation & math)
        setInterval(() => this.tick(0.05), 50);

        // Autosave every 5s
        setInterval(() => this.save(), 5000);

        // News rotation every 9s
        setInterval(() => this.rotateNews(), 9000);
      }}

      setupAudioListeners() {{
        const unlock = () => {{
          sound.init();
          window.removeEventListener('click', unlock);
          window.removeEventListener('keydown', unlock);
        }};
        window.addEventListener('click', unlock);
        window.addEventListener('keydown', unlock);
      }}

      recalcStats() {{
        // Reset base multipliers
        this.clickFlatBonus = 0;
        this.clickMultiplier = 1;
        this.clickPpsPercent = 0;
        this.critChance = 0;
        this.critMultiplier = 1;
        this.globalMultiplier = 1 + (this.starlightBells * 0.10);
        this.buildingMults = {{}};

        // Apply purchased upgrades
        for (const upId of this.upgrades) {{
          const def = UPGRADES.find(u => u.id === upId);
          if (def && def.effect) {{
            def.effect(this);
          }}
        }}

        // Calculate building PPS
        let rawPps = 0;
        for (const b of BUILDINGS) {{
          const count = this.buildings[b.id] || 0;
          const bMult = this.buildingMults[b.id] || 1;
          rawPps += count * b.basePps * bMult;
        }}

        // Buffs & Zoomies
        let activeMultiplier = this.globalMultiplier;
        if (this.buffMultiplier > 1) {{
          activeMultiplier *= this.buffMultiplier;
        }}

        this.pps = rawPps * activeMultiplier;

        // Click power formula
        let basePet = (this.clickBase + this.clickFlatBonus) * this.clickMultiplier;
        if (this.clickPpsPercent > 0) {{
          basePet += (this.pps * this.clickPpsPercent);
        }}
        if (this.isZoomiesActive) {{
          basePet *= 3;
        }}
        if (this.buffName === 'Scritch Overdrive!') {{
          basePet *= 77;
        }}

        this.currentClickPower = Math.max(1, basePet * activeMultiplier);
      }}

      getBuildingCost(bDef, amount = 1) {{
        const currentCount = this.buildings[bDef.id] || 0;
        let total = 0;
        for (let i = 0; i < amount; i++) {{
          total += Math.floor(bDef.baseCost * Math.pow(1.15, currentCount + i));
        }}
        return total;
      }}

      buyBuilding(bDef) {{
        const cost = this.getBuildingCost(bDef, this.buyMultiplier);
        if (this.purrs >= cost) {{
          this.purrs -= cost;
          this.buildings[bDef.id] = (this.buildings[bDef.id] || 0) + this.buyMultiplier;
          sound.playBuy();
          this.recalcStats();
          this.checkAchievements();
          this.renderCounters();
          this.renderBuildings();
          this.renderUpgrades();
        }}
      }}

      buyUpgrade(upDef) {{
        if (this.purrs >= upDef.cost && !this.upgrades.includes(upDef.id)) {{
          this.purrs -= upDef.cost;
          this.upgrades.push(upDef.id);
          sound.playBuy();
          this.recalcStats();
          this.checkAchievements();
          this.renderAll();
          this.showToast(`✨ Upgrade Acquired: ${upDef.name}`, 'bg-purple-900/90 border-purple-500');
        }}
      }}

      /* PET CLICK ACTION */
      pet(e) {{
        sound.init();
        const now = Date.now();
        this.recentClicks.push(now);
        this.recentClicks = this.recentClicks.filter(t => now - t <= 1000);
        const cadence = this.recentClicks.length;
        if (cadence > this.maxCadence) this.maxCadence = cadence;

        // Petting meter charge
        if (!this.isZoomiesActive) {{
          this.zoomiesMeter = Math.min(100, this.zoomiesMeter + 4.5);
          if (this.zoomiesMeter >= 100) {{
            this.triggerZoomies();
          }}
        }}

        // Check for Crit Pet
        let isCrit = false;
        let finalGain = this.currentClickPower;
        if (this.critChance > 0 && Math.random() < this.critChance) {{
          isCrit = true;
          finalGain *= this.critMultiplier;
          this.critTriggered++;
          sound.playCrit();
        }} else {{
          sound.playPet();
        }}

        this.purrs += finalGain;
        this.allTimePurrs += finalGain;
        this.manualPurrsEarned += finalGain;
        this.totalClicks += 1;

        // Visual squish animation
        const wrapper = document.getElementById('cat-wrapper');
        wrapper.classList.remove('animate-float');
        wrapper.classList.add('pet-squish');
        setTimeout(() => {{
          wrapper.classList.remove('pet-squish');
          wrapper.classList.add('animate-float');
        }}, 90);

        // Spawn visual float text & hearts
        this.spawnFloatingPetEffect(e, finalGain, isCrit);

        // Reactive dialogue trigger on random clicks
        if (Math.random() < 0.12 && now - this.quoteCooldown > 2000) {{
          this.quoteCooldown = now;
          this.triggerRandomDialogue();
        }}

        this.checkAchievements();
        this.renderCounters();
      }}

      triggerZoomies() {{
        this.isZoomiesActive = true;
        this.zoomiesTimer = 8.0;
        this.zoomiesTriggered++;
        sound.playGolden();
        this.recalcStats();
        this.showToast("🔥 ZOOMIES ACTIVE! 3x Petting Power!", "bg-pink-900/90 border-pink-500");
      }}

      spawnFloatingPetEffect(e, amount, isCrit) {{
        const container = document.getElementById('particle-container');
        const petArea = document.getElementById('pet-area');
        const rect = petArea.getBoundingClientRect();

        let clientX = rect.left + rect.width / 2;
        let clientY = rect.top + rect.height / 2;

        if (e && e.clientX) {{
          clientX = e.clientX;
          clientY = e.clientY;
        }}

        const x = clientX - rect.left;
        const y = clientY - rect.top;

        // Floating Number
        const el = document.createElement('div');
        el.className = `floating-text text-sm sm:text-base font-fredoka ${{isCrit ? 'text-amber-300 text-lg sm:text-xl font-black' : 'text-teal-300'}}`;
        el.style.left = `${{x}}px`;
        el.style.top = `${{y}}px`;
        el.style.setProperty('--dx', `${{(Math.random() - 0.5) * 60}}px`);
        el.style.setProperty('--rot', `${{(Math.random() - 0.5) * 30}}deg`);
        el.innerHTML = isCrit ? `CRIT! +${{this.formatNumber(amount)}} ⚡` : `+${{this.formatNumber(amount)}}`;

        container.appendChild(el);
        setTimeout(() => el.remove(), 1100);

        // Spawn 1-2 cute particle hearts / paws / sparks
        const icons = isCrit ? ['⚡', '💥', '✨', '🐾'] : ['❤️', '🐾', '✨', '🌸', '💫'];
        for (let i = 0; i < (isCrit ? 3 : 2); i++) {{
          const p = document.createElement('div');
          p.className = 'floating-text text-base select-none';
          p.style.left = `${{x + (Math.random() - 0.5) * 40}}px`;
          p.style.top = `${{y + (Math.random() - 0.5) * 40}}px`;
          p.style.setProperty('--dx', `${{(Math.random() - 0.5) * 90}}px`);
          p.style.setProperty('--rot', `${{(Math.random() - 0.5) * 60}}deg`);
          p.textContent = icons[Math.floor(Math.random() * icons.length)];
          container.appendChild(p);
          setTimeout(() => p.remove(), 1000);
        }}
      }}

      triggerRandomDialogue() {{
        const bubble = document.getElementById('speech-bubble');
        const text = document.getElementById('speech-text');
        const q = SCARAMEOW_QUOTES[Math.floor(Math.random() * SCARAMEOW_QUOTES.length)];
        text.textContent = `"${{q}}"`;
        bubble.classList.remove('bubble-animate');
        void bubble.offsetWidth; // re-trigger animation
        bubble.classList.add('bubble-animate');
      }}

      rotateNews() {{
        this.newsIndex = (this.newsIndex + 1) % NEWS_HEADLINES.length;
        const el = document.getElementById('news-ticker-text');
        el.style.opacity = '0';
        setTimeout(() => {{
          el.textContent = NEWS_HEADLINES[this.newsIndex];
          el.style.opacity = '1';
        }}, 300);
      }}

      /* GOLDEN COOKIE SYSTEM (Golden Anemo Feather) */
      spawnGoldenCookie() {{
        const el = document.getElementById('golden-cookie');
        const screenW = window.innerWidth - 80;
        const screenH = window.innerHeight - 150;
        const randX = 40 + Math.random() * screenW;
        const randY = 80 + Math.random() * screenH;

        el.style.left = `${{randX}}px`;
        el.style.top = `${{randY}}px`;
        el.classList.remove('hidden');

        // Automatically vanish after 14s if unclicked
        this.goldenVanishTimer = setTimeout(() => {{
          el.classList.add('hidden');
        }}, 14000);
      }}

      clickGoldenCookie() {{
        const el = document.getElementById('golden-cookie');
        el.classList.add('hidden');
        clearTimeout(this.goldenVanishTimer);

        this.goldenFeathersCaught++;
        sound.playGolden();

        const outcomes = ['frenzy', 'click_frenzy', 'lucky'];
        const choice = outcomes[Math.floor(Math.random() * outcomes.length)];

        if (choice === 'frenzy') {{
          this.buffMultiplier = 7;
          this.buffTimer = 30.0;
          this.buffName = 'Catnip Frenzy! (7x PPS)';
          this.showToast('🪶 GOLDEN FEATHER! 7x Purr Frenzy for 30s!', 'bg-amber-900/90 border-amber-500');
        }} else if (choice === 'click_frenzy') {{
          this.buffMultiplier = 1;
          this.buffTimer = 13.0;
          this.buffName = 'Scritch Overdrive!';
          this.showToast('🪶 GOLDEN FEATHER! 77x Click Scritch Power for 13s!', 'bg-amber-900/90 border-amber-500');
        }} else {{
          const bonus = Math.max(15, Math.floor(this.purrs * 0.15) + (this.pps * 120));
          this.purrs += bonus;
          this.allTimePurrs += bonus;
          this.showToast(`🪶 LUCKY FIND! +${{this.formatNumber(bonus)}} Purrs instantly!`, 'bg-amber-900/90 border-amber-500');
        }}

        this.recalcStats();
        this.checkAchievements();
        this.renderCounters();
      }}

      /* MAIN TICK */
      tick(dt) {{
        this.timePlayedSecs += dt;

        // Passive Purr generation
        if (this.pps > 0) {{
          const gain = this.pps * dt;
          this.purrs += gain;
          this.allTimePurrs += gain;
        }}

        // Zoomies Decay & Timer
        if (this.isZoomiesActive) {{
          this.zoomiesTimer -= dt;
          if (this.zoomiesTimer <= 0) {{
            this.isZoomiesActive = false;
            this.zoomiesMeter = 0;
            this.recalcStats();
          }}
        }} else {{
          this.zoomiesMeter = Math.max(0, this.zoomiesMeter - (dt * 12));
        }}

        // Buff Timers
        if (this.buffTimer > 0) {{
          this.buffTimer -= dt;
          if (this.buffTimer <= 0) {{
            this.buffTimer = 0;
            this.buffMultiplier = 1;
            this.buffName = '';
            this.recalcStats();
          }}
        }}

        // Golden cookie timer
        this.goldenTimer -= dt;
        if (this.goldenTimer <= 0) {{
          this.spawnGoldenCookie();
          this.goldenTimer = 60 + Math.random() * 50;
        }}

        // Refresh UI
        this.renderCounters();
        this.updateDynamicUi();
      }}

      checkAchievements() {{
        for (const a of ACHIEVEMENTS) {{
          if (!this.unlockedAchievements.includes(a.id) && a.check(this)) {{
            this.unlockedAchievements.push(a.id);
            sound.playAchievement();
            this.showToast(`🏆 Achievement Unlocked: ${a.name}!`, 'bg-amber-900/95 border-amber-400');
            this.renderAchievementsModal();
            this.renderBadgesCount();
          }}
        }}
      }}

      /* PRESTIGE / ASCENSION */
      calculateBellsOnReset() {{
        if (this.allTimePurrs < 1000000) return 0;
        return Math.floor(Math.cbrt(this.allTimePurrs / 1000000));
      }}

      ascend() {{
        const earnedBells = this.calculateBellsOnReset();
        if (earnedBells <= 0) return;

        this.starlightBells += earnedBells;
        this.ascensions += 1;

        // Reset soft progress
        this.purrs = 0;
        this.buildings = {{}};
        this.upgrades = [];
        this.zoomiesMeter = 0;
        this.isZoomiesActive = false;
        this.buffMultiplier = 1;
        this.buffTimer = 0;

        sound.playGolden();
        this.recalcStats();
        this.checkAchievements();
        this.save();
        this.renderAll();
        this.showToast(`✨ Ascended! Gained +${{earnedBells}} Starlight Bells!`, 'bg-purple-900 border-purple-400');
      }}

      /* FORMATTING UTILS */
      formatNumber(n) {{
        if (n === undefined || isNaN(n)) return '0';
        if (n < 1000) return Math.floor(n).toLocaleString();
        const suffixes = ['', 'k', 'M', 'B', 'T', 'Qa', 'Qi', 'Sx', 'Sp', 'Oc', 'No', 'Dc'];
        const i = Math.floor(Math.log10(n) / 3);
        if (i < suffixes.length) {{
          const formatted = (n / Math.pow(10, i * 3)).toFixed(2);
          return `${{formatted}} ${{suffixes[i]}}`;
        }}
        return n.toExponential(2);
      }}

      formatTime(secs) {{
        const s = Math.floor(secs % 60);
        const m = Math.floor((secs / 60) % 60);
        const h = Math.floor(secs / 3600);
        if (h > 0) return `${{h}}h ${{m}}m ${{s}}s`;
        if (m > 0) return `${{m}}m ${{s}}s`;
        return `${{s}}s`;
      }}

      /* RENDERING */
      renderCounters() {{
        document.getElementById('purr-counter').textContent = this.formatNumber(this.purrs);
        document.getElementById('pps-counter').textContent = this.formatNumber(this.pps);
        document.getElementById('click-power-counter').textContent = this.formatNumber(this.currentClickPower);
        document.getElementById('total-pets-count').textContent = `${{this.totalClicks.toLocaleString()}} pets`;
      }}

      updateDynamicUi() {{
        // Zoomies Bar
        const bar = document.getElementById('zoomies-bar');
        const status = document.getElementById('zoomies-status');
        const frenzyTimer = document.getElementById('frenzy-timer');
        const frenzySecs = document.getElementById('frenzy-secs');

        if (this.isZoomiesActive) {{
          bar.style.width = '100%';
          status.textContent = '🔥 ZOOMIES ACTIVE!';
          status.className = 'text-[11px] text-pink-400 font-extrabold animate-pulse';
          frenzyTimer.classList.remove('hidden');
          frenzySecs.textContent = this.zoomiesTimer.toFixed(1);
        }} else {{
          bar.style.width = `${{this.zoomiesMeter}}%`;
          frenzyTimer.classList.add('hidden');
          if (this.zoomiesMeter > 70) {{
            status.textContent = '⚡ Agitated Purring!';
            status.className = 'text-[11px] text-amber-300 font-bold';
          }} else if (this.zoomiesMeter > 30) {{
            status.textContent = '✨ Secretly Enjoying It';
            status.className = 'text-[11px] text-teal-300';
          }} else {{
            status.textContent = 'Calm & Grumpy';
            status.className = 'text-[11px] text-slate-400';
          }}
        }}

        // Update Mood label based on all-time purrs
        const moodEmoji = document.getElementById('mood-emoji');
        const moodTitle = document.getElementById('mood-title');
        const moodDesc = document.getElementById('mood-desc');

        if (this.allTimePurrs > 1000000000) {{
          moodEmoji.textContent = '🌌';
          moodTitle.textContent = 'Omnipresent Celestial Kitty';
          moodDesc.textContent = 'Ruler of Irminsul, purrs across galaxies.';
        }} else if (this.allTimePurrs > 10000000) {{
          moodEmoji.textContent = '😻';
          moodTitle.textContent = 'Completely Domesticated Sovereign';
          moodDesc.textContent = 'Vigorously kneading the teacup edge.';
        }} else if (this.allTimePurrs > 50000) {{
          moodEmoji.textContent = '😼';
          moodTitle.textContent = 'Secretly Addicted to Scritches';
          moodDesc.textContent = 'Pretends to hate it, but leans into your palm.';
        }} else {{
          moodEmoji.textContent = '😾';
          moodTitle.textContent = 'Tsundere Teacup Inhabitant';
          moodDesc.textContent = 'Glares menacingly from inside his mug.';
        }}

        // Update Buildings affordability buttons
        for (const b of BUILDINGS) {{
          const btn = document.getElementById(`building-card-${{b.id}}`);
          if (btn) {{
            const cost = this.getBuildingCost(b, this.buyMultiplier);
            const canAfford = this.purrs >= cost;
            if (canAfford) {{
              btn.classList.add('affordable-item');
              btn.classList.remove('opacity-60');
            }} else {{
              btn.classList.remove('affordable-item');
              btn.classList.add('opacity-60');
            }}
            const costEl = document.getElementById(`building-cost-${{b.id}}`);
            if (costEl) costEl.textContent = this.formatNumber(cost);
          }}
        }}

        // Update Upgrades affordability
        for (const u of UPGRADES) {{
          const upBtn = document.getElementById(`upgrade-icon-${{u.id}}`);
          if (upBtn) {{
            const canAfford = this.purrs >= u.cost;
            if (canAfford) {{
              upBtn.classList.remove('opacity-40', 'border-slate-700');
              upBtn.classList.add('border-teal-400', 'shadow-[0_0_10px_rgba(59,226,197,0.4)]');
            }} else {{
              upBtn.classList.add('opacity-40', 'border-slate-700');
              upBtn.classList.remove('border-teal-400', 'shadow-[0_0_10px_rgba(59,226,197,0.4)]');
            }}
          }}
        }}
      }}

      renderBuildings() {{
        const container = document.getElementById('buildings-list');
        container.innerHTML = '';

        for (const b of BUILDINGS) {{
          const count = this.buildings[b.id] || 0;
          const cost = this.getBuildingCost(b, this.buyMultiplier);
          const bMult = this.buildingMults[b.id] || 1;
          const currentPps = count * b.basePps * bMult * this.globalMultiplier;

          const card = document.createElement('div');
          card.id = `building-card-${{b.id}}`;
          card.className = `p-3 bg-[#181b33] border border-[#2b305a] rounded-xl flex items-center justify-between gap-3 cursor-pointer transition select-none opacity-60`;
          
          card.onclick = () => this.buyBuilding(b);

          card.innerHTML = `
            <div class="flex items-center gap-3">
              <div class="w-11 h-11 rounded-xl bg-[#22274c] border border-[#333b6e] flex items-center justify-center text-2xl shrink-0 shadow-md">
                ${{b.icon}}
              </div>
              <div>
                <div class="font-bold text-slate-100 text-xs sm:text-sm flex items-center gap-2">
                  <span>${{b.name}}</span>
                </div>
                <div class="text-[11px] text-slate-400 line-clamp-1">${{b.desc}}</div>
                <div class="text-[10px] text-teal-400 mt-0.5">
                  +${{this.formatNumber(b.basePps * bMult)}} PPS each • Generating ${{this.formatNumber(currentPps)}}/s
                </div>
              </div>
            </div>

            <div class="text-right shrink-0 flex flex-col items-end">
              <span class="text-lg sm:text-xl font-fredoka font-black text-slate-300 font-mono">${{count}}</span>
              <div class="flex items-center gap-1 text-xs font-bold font-mono text-amber-300 mt-0.5">
                <span>🐾</span>
                <span id="building-cost-${{b.id}}">${{this.formatNumber(cost)}}</span>
              </div>
            </div>
          `;

          container.appendChild(card);
        }}
      }}

      renderUpgrades() {{
        const grid = document.getElementById('upgrades-grid');
        grid.innerHTML = '';

        const available = UPGRADES.filter(u => !this.upgrades.includes(u.id));

        if (available.length === 0) {{
          grid.innerHTML = `<span class="text-xs text-teal-400 font-semibold p-2">🎉 All current scritch upgrades mastered!</span>`;
          return;
        }}

        for (const u of available) {{
          const iconBtn = document.createElement('button');
          iconBtn.id = `upgrade-icon-${{u.id}}`;
          iconBtn.title = `${{u.name}} (${{this.formatNumber(u.cost)}} Purrs)\n${{u.desc}}`;
          iconBtn.className = `w-11 h-11 rounded-xl bg-[#1d2140] border border-slate-700 flex items-center justify-center text-xl transition transform hover:scale-110 relative opacity-40`;
          iconBtn.innerHTML = `
            ${{u.icon}}
            <span class="absolute -bottom-1 -right-1 text-[9px] bg-slate-900/90 text-amber-300 font-bold px-1 rounded border border-slate-700 font-mono">
              ${{this.formatNumber(u.cost)}}
            </span>
          `;
          iconBtn.onclick = () => this.buyUpgrade(u);
          grid.appendChild(iconBtn);
        }}

        document.getElementById('upgrades-unlocked-count').textContent = `${{this.upgrades.length}} / ${{UPGRADES.length}} unlocked`;
      }}

      renderBadgesCount() {{
        const el = document.getElementById('achieve-count-badge');
        el.textContent = `${{this.unlockedAchievements.length}}/${{ACHIEVEMENTS.length}}`;
      }}

      renderAchievementsModal() {{
        const gallery = document.getElementById('achievements-gallery');
        gallery.innerHTML = '';

        for (const a of ACHIEVEMENTS) {{
          const unlocked = this.unlockedAchievements.includes(a.id);
          const item = document.createElement('div');
          item.className = `p-3 rounded-xl border flex items-center gap-3 transition ${{
            unlocked 
              ? 'bg-[#1e2348] border-amber-500/40 text-slate-100 shadow-md' 
              : 'bg-[#121426] border-[#222544] text-slate-500 opacity-60'
          }}`;

          item.innerHTML = `
            <div class="w-10 h-10 rounded-lg ${{unlocked ? 'bg-amber-500/20 text-amber-300' : 'bg-slate-800 text-slate-600'}} flex items-center justify-center text-2xl shrink-0">
              ${{unlocked ? a.icon : '🔒'}}
            </div>
            <div>
              <div class="font-bold text-xs sm:text-sm ${{unlocked ? 'text-amber-200' : 'text-slate-400'}}">${{a.name}}</div>
              <div class="text-[11px] text-slate-400">${{a.desc}}</div>
            </div>
          `;
          gallery.appendChild(item);
        }}

        const pct = Math.round((this.unlockedAchievements.length / ACHIEVEMENTS.length) * 100);
        document.getElementById('achievements-total-progress').textContent = 
          `${{this.unlockedAchievements.length}} of ${{ACHIEVEMENTS.length}} Unlocked (${{pct}}%)`;
      }}

      renderStatsModal() {{
        document.getElementById('stat-current-purrs').textContent = this.formatNumber(this.purrs);
        document.getElementById('stat-alltime-purrs').textContent = this.formatNumber(this.allTimePurrs);
        document.getElementById('stat-clicks').textContent = this.totalClicks.toLocaleString();
        document.getElementById('stat-pet-purrs').textContent = this.formatNumber(this.manualPurrsEarned);
        document.getElementById('stat-pps').textContent = `${{this.formatNumber(this.pps)}}/sec`;
        document.getElementById('stat-golden-caught').textContent = this.goldenFeathersCaught;
        document.getElementById('stat-ascension-bells').textContent = 
          `${{this.starlightBells}} bells (+${{this.starlightBells * 10}}% global bonus)`;
        document.getElementById('stat-time-played').textContent = this.formatTime(this.timePlayedSecs);
      }}

      renderPrestigeModal() {{
        const pending = this.calculateBellsOnReset();
        document.getElementById('prestige-current-bells').textContent = 
          `${{this.starlightBells}} (+${{this.starlightBells * 10}}%)`;
        document.getElementById('prestige-pending-bells').textContent = `+${{pending}} Bells`;
        
        const nextTarget = Math.pow(pending + 1, 3) * 1000000;
        document.getElementById('prestige-next-cost').textContent = `${{this.formatNumber(nextTarget)}} All-Time Purrs`;

        const btn = document.getElementById('btn-confirm-ascend');
        btn.disabled = pending <= 0;
      }}

      renderAll() {{
        this.renderCounters();
        this.renderBuildings();
        this.renderUpgrades();
        this.renderBadgesCount();
        this.updateDynamicUi();
      }}

      showToast(msg, colorClass = 'bg-slate-900 border-slate-700') {{
        const container = document.getElementById('toast-container');
        const toast = document.createElement('div');
        toast.className = `p-3 rounded-xl border text-xs sm:text-sm font-bold shadow-2xl text-slate-100 flex items-center gap-2 transform transition-all duration-300 translate-y-3 opacity-0 ${{colorClass}}`;
        toast.innerHTML = msg;
        container.appendChild(toast);

        // Animate in
        requestAnimationFrame(() => {{
          toast.classList.remove('translate-y-3', 'opacity-0');
        }});

        // Remove after 3.5s
        setTimeout(() => {{
          toast.classList.add('opacity-0', 'translate-y-2');
          setTimeout(() => toast.remove(), 300);
        }}, 3500);
      }}

      /* EVENT LISTENERS */
      setupEvents() {{
        // Pet Target (Click & Keypress Space/Enter)
        const catTarget = document.getElementById('cat-wrapper');
        catTarget.addEventListener('mousedown', (e) => this.pet(e));
        catTarget.addEventListener('keydown', (e) => {{
          if (e.key === ' ' || e.key === 'Enter') {{
            e.preventDefault();
            this.pet(null);
          }}
        }});

        // Golden cookie click
        document.getElementById('golden-cookie').addEventListener('click', () => this.clickGoldenCookie());

        // Multiplier buttons
        document.querySelectorAll('.buy-mult-btn').forEach(btn => {{
          btn.addEventListener('click', () => {{
            document.querySelectorAll('.buy-mult-btn').forEach(b => {{
              b.classList.remove('bg-[#252a4d]', 'text-teal-400');
              b.classList.add('text-slate-400');
            }});
            btn.classList.add('bg-[#252a4d]', 'text-teal-400');
            btn.classList.remove('text-slate-400');
            this.buyMultiplier = parseInt(btn.dataset.mult, 10);
            this.renderBuildings();
          }});
        }});

        // Sound Toggle
        const soundBtn = document.getElementById('btn-sound');
        const soundIcon = document.getElementById('sound-icon');
        soundBtn.addEventListener('click', () => {{
          sound.enabled = !sound.enabled;
          soundIcon.textContent = sound.enabled ? '🔊' : '🔇';
          this.showToast(sound.enabled ? '🔊 Sound Enabled' : '🔇 Sound Muted');
        }});

        // Modals
        this.bindModal('btn-stats', 'modal-stats', () => this.renderStatsModal());
        this.bindModal('btn-achievements', 'modal-achievements', () => this.renderAchievementsModal());
        this.bindModal('btn-prestige', 'modal-prestige', () => this.renderPrestigeModal());
        this.bindModal('btn-export-save', 'modal-save', () => {{
          document.getElementById('save-data-textarea').value = this.exportSave();
        }});

        // Prestige confirm
        document.getElementById('btn-confirm-ascend').addEventListener('click', () => {{
          this.ascend();
          document.getElementById('modal-prestige').classList.add('hidden');
        }});

        // Manual Save
        document.getElementById('btn-save-manual').addEventListener('click', () => {{
          this.save();
          this.showToast('💾 Game Saved Successfully!', 'bg-teal-900 border-teal-500');
        }});

        // Copy Save
        document.getElementById('btn-copy-save').addEventListener('click', () => {{
          const txt = document.getElementById('save-data-textarea');
          txt.select();
          navigator.clipboard.writeText(txt.value);
          this.showToast('📋 Save copied to clipboard!');
        }});

        // Import Save
        document.getElementById('btn-import-save').addEventListener('click', () => {{
          const txt = document.getElementById('save-data-textarea').value;
          if (this.importSave(txt)) {{
            document.getElementById('modal-save').classList.add('hidden');
            this.showToast('📥 Save data restored successfully!', 'bg-teal-900 border-teal-500');
          }} else {{
            alert('Invalid save code!');
          }}
        }});

        // Wipe Save
        document.getElementById('btn-wipe-save').addEventListener('click', () => {{
          if (confirm('Are you sure you want to reset all progress? Scarameow will forget your scritches!')) {{
            localStorage.removeItem('scarameow_clicker_save');
            location.reload();
          }}
        }});

        // Close buttons on all modals
        document.querySelectorAll('.modal-close').forEach(btn => {{
          btn.addEventListener('click', (e) => {{
            e.target.closest('.fixed').classList.add('hidden');
          }});
        }});
      }}

      bindModal(btnId, modalId, onOpen) {{
        document.getElementById(btnId).addEventListener('click', () => {{
          if (onOpen) onOpen();
          document.getElementById(modalId).classList.remove('hidden');
        }});
      }}

      /* SAVE / LOAD */
      exportSave() {{
        const data = {{
          purrs: this.purrs,
          allTimePurrs: this.allTimePurrs,
          totalClicks: this.totalClicks,
          manualPurrsEarned: this.manualPurrsEarned,
          goldenFeathersCaught: this.goldenFeathersCaught,
          zoomiesTriggered: this.zoomiesTriggered,
          critTriggered: this.critTriggered,
          maxCadence: this.maxCadence,
          timePlayedSecs: this.timePlayedSecs,
          ascensions: this.ascensions,
          starlightBells: this.starlightBells,
          buildings: this.buildings,
          upgrades: this.upgrades,
          unlockedAchievements: this.unlockedAchievements
        }};
        return btoa(unescape(encodeURIComponent(JSON.stringify(data))));
      }}

      importSave(encodedStr) {{
        try {{
          const decoded = JSON.parse(decodeURIComponent(escape(atob(encodedStr.trim()))));
          if (decoded && typeof decoded.purrs === 'number') {{
            this.purrs = decoded.purrs || 0;
            this.allTimePurrs = decoded.allTimePurrs || 0;
            this.totalClicks = decoded.totalClicks || 0;
            this.manualPurrsEarned = decoded.manualPurrsEarned || 0;
            this.goldenFeathersCaught = decoded.goldenFeathersCaught || 0;
            this.zoomiesTriggered = decoded.zoomiesTriggered || 0;
            this.critTriggered = decoded.critTriggered || 0;
            this.maxCadence = decoded.maxCadence || 0;
            this.timePlayedSecs = decoded.timePlayedSecs || 0;
            this.ascensions = decoded.ascensions || 0;
            this.starlightBells = decoded.starlightBells || 0;
            this.buildings = decoded.buildings || {{}};
            this.upgrades = decoded.upgrades || [];
            this.unlockedAchievements = decoded.unlockedAchievements || [];
            this.recalcStats();
            this.renderAll();
            return true;
          }}
        }} catch(e) {{
          console.error(e);
        }}
        return false;
      }}

      save() {{
        try {{
          localStorage.setItem('scarameow_clicker_save', this.exportSave());
        }} catch(e) {{}}
      }}

      loadSave() {{
        try {{
          const saved = localStorage.getItem('scarameow_clicker_save');
          if (saved) {{
            this.importSave(saved);
          }}
        }} catch(e) {{}}
      }}
    }}

    // Boot game once DOM is loaded
    window.addEventListener('DOMContentLoaded', () => {{
      window.game = new Game();
    }});
  </script>
</body>
</html>
'''

# Write to scratch project directory
scratch_dir = "/Users/airi/.gemini/antigravity/scratch/scarameow-petter"
os.makedirs(scratch_dir, exist_ok=True)
with open(os.path.join(scratch_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

# Write to brain artifact directory
artifact_dir = "/Users/airi/.gemini/antigravity/brain/24616610-e6f6-4d6a-b4fb-040c79607b10"
os.makedirs(artifact_dir, exist_ok=True)
with open(os.path.join(artifact_dir, "scarameow_petter.html"), "w", encoding="utf-8") as f:
    f.write(html_content)

print("Game built successfully in both scratch and artifact directories!")
