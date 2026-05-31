/* =========================================================
# ADA PROMAX IA - MAIN.CSS (Versión Premium 2030)
   ========================================================= */

/* ------------------------------
   FONDO ANIMADO
------------------------------ */
body {
    background: linear-gradient(135deg, #12092c, #031a33, #12092c);
    background-size: 300% 300%;
    animation: bgShift 18s ease infinite;
    font-family: 'Inter', sans-serif;
}

@keyframes bgShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* ------------------------------
   HERO CARD (Glass + Animación)
------------------------------ */
.hero-card {
    backdrop-filter: blur(25px);
    background: rgba(255, 255, 255, 0.06);
    border-radius: 22px;
    padding: 25px 40px;
    margin-top: -30px; /* 🔧 Corrige el espacio vacío superior */
    box-shadow: 0 0 40px rgba(147, 197, 253, 0.25);
    transition: all 0.4s ease;
    animation: fadeSlide 1.2s ease forwards;
    opacity: 0;
}

.hero-card:hover {
    transform: scale(1.015);
    box-shadow: 0 0 60px rgba(147, 197, 253, 0.45);
}

@keyframes fadeSlide {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

/* ------------------------------
   ROBOT — Flotación elegante
------------------------------ */
.hero-card img {
    display: block;
    margin: 0 auto;
    animation: floatBot 4s ease-in-out infinite;
    filter: drop-shadow(0 0 18px rgba(147,197,253,0.45));
}

@keyframes floatBot {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

/* ------------------------------
   TEXTOS HERO
------------------------------ */
.hero-label {
    font-size: 14px;
    color: #a5b4fc;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 8px;
}

.hero-title span {
    font-size: 50px;
    font-weight: 800;
    color: #d8ccff;
    text-shadow: 0 0 25px rgba(147,197,253,0.45);
    animation: glowPulse 4s ease-in-out infinite;
}

@keyframes glowPulse {
    0%, 100% { text-shadow: 0 0 20px rgba(147,197,253,0.25); }
    50% { text-shadow: 0 0 45px rgba(147,197,253,0.55); }
}

.hero-subtitle {
    font-size: 20px;
    color: #e0e7ff;
    margin-bottom: 10px;
}

.hero-description {
    font-size: 16px;
    color: #cbd5e1;
    max-width: 480px;
    text-align: justify;
}

/* ------------------------------
   MESSAGE BOX
------------------------------ */
.message-box {
    margin-top: 20px;
    padding: 14px 22px;
    border-radius: 12px;
    background: rgba(255,255,255,0.08);
    color: #e0e7ff;
    transition: all 0.3s ease;
}

.message-box:hover {
    background: rgba(147,197,253,0.18);
    transform: translateY(-4px);
}

/* ------------------------------
   SECCIÓN — TÍTULOS
------------------------------ */
.section-title {
    color: #e2e8f0;
    font-size: 26px;
    font-weight: 700;
    margin-bottom: 20px;
    animation: fadeSlide 1.2s ease forwards;
}

/* ------------------------------
   FEATURE CARDS
------------------------------ */
.feature-card {
    backdrop-filter: blur(18px);
    background: rgba(255,255,255,0.07);
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    transition: all 0.35s ease;
    cursor: pointer;
    animation: fadeSlide 1.4s ease forwards;
    opacity: 0;
}

.feature-card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 0 35px rgba(255,255,255,0.25);
}

.feature-title {
    font-size: 20px;
    font-weight: 700;
    color: #d8ccff;
    margin-bottom: 10px;
}

.feature-desc {
    font-size: 15px;
    color: #cbd5e1;
}

/* ------------------------------
   SIDE PANELS
------------------------------ */
.side-panel {
    backdrop-filter: blur(18px);
    background: rgba(255,255,255,0.06);
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
    animation: fadeSlide 1.4s ease forwards;
    opacity: 0;
}

.side-title {
    font-size: 18px;
    font-weight: 700;
    color: #d8ccff;
    margin-bottom: 12px;
}

.side-item {
    font-size: 15px;
    color: #cbd5e1;
    margin-bottom: 8px;
    transition: all 0.3s ease;
}

.side-item:hover {
    transform: translateX(6px);
    color: #ffffff;
}

/* ------------------------------
   CHAT MESSAGES
------------------------------ */
.user-message, .assistant-message {
    border-radius: 12px;
    padding: 12px 18px;
    margin-bottom: 12px;
    backdrop-filter: blur(12px);
    animation: fadeSlide 0.6s ease forwards;
    opacity: 0;
}

.user-message {
    background: rgba(255,255,255,0.12);
    color: #fff;
}

.assistant-message {
    background: rgba(96,165,250,0.18);
    color: #dbeafe;
}

/* ------------------------------
   RESPONSIVE
------------------------------ */
@media (max-width: 900px) {
    .hero-title span { font-size: 38px; }
    .hero-card { padding: 20px; }
    .feature-card { padding: 20px; }
}
