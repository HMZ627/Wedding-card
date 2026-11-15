import streamlit as st
import streamlit.components.v1 as components

# Configure the page setting
st.set_page_config(
    page_title="Wedding Invitation - Rimsha Fatima & Mr. Asad",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's native header, footer, toolbar, and internal badges
st.markdown(
    """
    <style>
        .block-container { padding: 0rem !important; }
        #MainMenu, header, footer,
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stHeader"],
        .stAppDeployButton,
        .stDeployButton,
        .viewerBadge_container__1QSob,
        .viewerBadge_link__1S137,
        div[class*="viewerBadge"],
        div[class*="profileContainer"],
        div[class*="StatusWidget"],
        a[href*="streamlit.io"] {
            display: none !important;
            visibility: hidden !important;
        }
        iframe {
            height: 100vh !important;
            width: 100vw !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML, CSS, JS payload with WebGL silk curtains, pre-warmed GPU split-curtain, Red Part 2 theme & 60fps parallax
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Wedding Invitation</title>
    <link href="https://fonts.googleapis.com/css2?family=Alex+Brush&family=Amiri:wght@700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        /* --- Base & Vintage Old Paper Background (Part 1) --- */
        html, body {
            margin: 0; padding: 0;
            overflow-x: clip;
        }
        body {
            font-family: 'Playfair Display', serif;
            background-color: #f7ecd3;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(168, 124, 72, 0.14) 0%, transparent 45%),
                radial-gradient(circle at 85% 35%, rgba(139, 94, 52, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 25% 75%, rgba(168, 124, 72, 0.13) 0%, transparent 50%),
                radial-gradient(circle at 80% 85%, rgba(120, 75, 40, 0.14) 0%, transparent 45%),
                url('https://www.transparenttextures.com/patterns/aged-paper.png');
            color: #4a3b32;
        }

        /* --- Royal Crimson Red Theme Backdrop (Revealed Under Split Curtains!) --- */
        #red-theme-backdrop {
            position: fixed;
            inset: 0;
            z-index: 0;
            pointer-events: none;
            opacity: 0;
            background-color: #5c0612;
            background-image:
                radial-gradient(circle at 50% 25%, rgba(185, 22, 48, 0.45) 0%, transparent 58%),
                radial-gradient(circle at 18% 75%, rgba(45, 0, 7, 0.55) 0%, transparent 50%),
                radial-gradient(circle at 85% 80%, rgba(45, 0, 7, 0.55) 0%, transparent 50%),
                radial-gradient(ellipse at center, transparent 38%, rgba(26, 0, 4, 0.68) 100%),
                url('https://www.transparenttextures.com/patterns/aged-paper.png');
            background-blend-mode: normal, normal, normal, normal, multiply;
            will-change: opacity;
        }

        /* --- High-FPS Fixed Parallax Decor Canvases --- */
        .decor-canvas {
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
            opacity: 0;
            filter: blur(18px);
            transition: opacity 1.8s ease-out, filter 1.8s ease-out;
        }
        #bg-decor-canvas { z-index: 1; }
        #fg-decor-canvas { z-index: 50; }
        .decor-canvas.decor-revealed {
            opacity: 1;
            filter: blur(0px);
        }

        /* --- WebGL / Canvas Silky Cloth Curtain --- */
        #curtain-wrapper {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: 9999; pointer-events: auto; overflow: hidden;
        }
        #curtain-canvas {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            display: block;
        }

        .open-btn {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: linear-gradient(145deg, #fdf8ec, #eadbc0);
            color: #800000;
            padding: 18px 48px; font-size: 38px; cursor: pointer;
            border-radius: 12px; border: 2px solid #d4af37;
            box-shadow: 0 10px 28px rgba(0,0,0,0.55), inset 0 0 10px rgba(212, 175, 55, 0.35);
            z-index: 10000; font-family: 'Great Vibes', cursive;
            transition: opacity 0.6s ease, transform 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            -webkit-tap-highlight-color: transparent;
            user-select: none;
        }
        .open-btn:hover { transform: translate(-50%, -50%) scale(1.08); }
        #curtain-wrapper.opened { pointer-events: none; }
        #curtain-wrapper.opened .open-btn {
            opacity: 0;
            pointer-events: none;
            transform: translate(-50%, -35%) scale(0.75);
        }

        /* --- Post-Curtain Blur-In-Fade-In Reveal --- */
        .content {
            min-height: 100vh;
            padding: 0;
            text-align: center;
            position: relative;
            z-index: 10;
            opacity: 0;
            filter: blur(22px);
            transform: scale(0.98);
            transition: opacity 1.8s ease-out, filter 1.8s ease-out, transform 1.8s ease-out;
        }
        .content.site-revealed {
            opacity: 1;
            filter: blur(0px);
            transform: scale(1);
        }

        /* --- Part 1 Container (Styled by Class so Split Clones Match Exactly!) --- */
        .part1-container {
            padding: 10vh 20px 6vh 20px;
            position: relative;
            z-index: 20;
            box-sizing: border-box;
            width: 100%;
        }

        /* Bismillah Responsive Wrapper */
        .bismillah-wrap {
            width: 100%;
            display: flex;
            justify-content: center;
            margin-bottom: 12vh;
        }
        .bismillah {
            display: inline-block;
            font-family: 'Amiri', serif;
            font-size: clamp(1.5rem, 7.8vw, 3.6rem);
            opacity: 0;
            filter: blur(14px);
            transform: translateY(25px);
            transition: opacity 1.6s ease-out, filter 1.6s ease-out, transform 1.6s ease-out;
            line-height: 1.5;
            white-space: nowrap;
            direction: rtl;
        }
        .bismillah.visible-up {
            opacity: 1 !important;
            filter: blur(0px) !important;
            transform: translateY(0) !important;
        }

        /* Type-in Fade-in */
        .type-fade {
            font-size: 1.95rem;
            margin: 0 auto 18vh auto;
            max-width: 820px;
            padding: 0 15px;
            line-height: 1.5;
            font-style: italic;
            opacity: 0;
            filter: blur(8px);
            transition: opacity 1.5s ease-in, filter 1.5s ease-out;
            min-height: 70px;
        }
        .type-fade.visible-fade {
            opacity: 1 !important;
            filter: blur(0px) !important;
        }

        /* --- Hadith Section --- */
        .hadith-box {
            margin: 0 auto 20vh auto;
            max-width: 780px;
            opacity: 0;
            filter: blur(12px);
            transform: translateY(30px);
            transition: opacity 1.5s ease-out, filter 1.5s ease-out, transform 1.5s ease-out;
        }
        .hadith-arabic {
            font-family: 'Amiri', serif;
            font-size: clamp(1.9rem, 7vw, 3.2rem);
            color: #800000;
            margin-bottom: 10px;
            line-height: 1.5;
            direction: rtl;
        }
        .hadith-trans {
            font-size: 1.45rem;
            font-style: italic;
            color: #4a3b32;
        }

        /* --- Ink Spread Hosts & Invitation Section --- */
        .ink-spread-anim {
            clip-path: circle(0% at center);
            filter: blur(20px);
            opacity: 0;
            transition: clip-path 2.5s cubic-bezier(0.25, 1, 0.5, 1), filter 2.5s ease-out, opacity 1.5s ease-in;
            padding: 20px 0;
            max-width: 860px;
            margin: 0 auto;
        }
        .sub-header-text {
            font-size: 1.65rem;
            line-height: 1.75;
            position: relative;
        }
        .blessings-line {
            font-style: italic;
            font-size: 1.4rem;
            color: #6b5344;
            margin-bottom: 14px;
            display: block;
        }
        .hosts-names {
            font-size: 1.95rem;
            font-weight: 700;
            color: #800000;
            display: block;
            margin: 12px 0;
            line-height: 1.5;
        }
        .hosts-sub {
            font-weight: 400;
            font-size: 1.35rem;
            color: #5c473b;
        }
        .wedding-word {
            color: #ff033e;
            font-weight: bold;
            font-style: italic;
        }

        /* --- Detailed Blooming Garden Sequence --- */
        .garden-container { display: flex; justify-content: center; gap: 100px; margin-top: 30px; height: 130px; }
        .plant { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .flower { font-size: 6rem; display: flex; align-items: center; justify-content: center; }
        .butterfly { font-size: 3rem; position: absolute; bottom: 20px; opacity: 0; transition: bottom 1.5s ease-in-out, opacity 1.5s ease-in-out; z-index: 10; }

        .visible-ink .ink-spread-anim { opacity: 1; clip-path: circle(150% at center); filter: blur(0px); }
        .visible-ink .butterfly { bottom: 100px; opacity: 1; transition-delay: 2.2s; animation: hoverfly 2.5s infinite ease-in-out alternate 3.7s; }
        .plant.delayed .butterfly { transition-delay: 2.6s; animation-delay: 4.1s; }

        .flower-layer-1, .flower-layer-2, .flower-layer-3, .flower-center {
            transform-origin: 16px 16px;
            transform: scale(0);
        }

        .visible-ink .flower-layer-1 { animation: bloomLayer 1.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards 1s; }
        .visible-ink .flower-layer-2 { animation: bloomLayer 1.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards 1.3s; }
        .visible-ink .flower-layer-3 { animation: bloomLayer 1.5s cubic-bezier(0.34, 1.56, 0.64, 1) forwards 1.6s; }
        .visible-ink .flower-center { animation: bloomLayer 1.2s cubic-bezier(0.34, 1.56, 0.64, 1) forwards 1.9s; }

        .visible-ink .flower svg { animation: continuousBloom 4s infinite alternate ease-in-out 3.5s; }

        .plant.delayed .flower-layer-1 { animation-delay: 1.4s; }
        .plant.delayed .flower-layer-2 { animation-delay: 1.7s; }
        .plant.delayed .flower-layer-3 { animation-delay: 2.0s; }
        .plant.delayed .flower-center { animation-delay: 2.3s; }
        .plant.delayed .flower svg { animation-delay: 3.9s; }

        @keyframes bloomLayer { 0% { transform: scale(0) rotate(-15deg); } 100% { transform: scale(1) rotate(0deg); } }
        @keyframes continuousBloom { 0% { transform: scale(1) rotate(-3deg); } 100% { transform: scale(1.08) rotate(3deg); } }
        @keyframes hoverfly { 0% { transform: translateY(0) translateX(0) rotate(-10deg); } 100% { transform: translateY(-15px) translateX(15px) rotate(15deg); } }

        /* --- Scratch Card & Mobile Scaler --- */
        .scratch-wrapper {
            margin: 0 auto 30px auto;
            display: flex; justify-content: center;
            opacity: 0; filter: blur(12px); transform: translateY(30px);
            transition: opacity 1.5s ease-out, filter 1.5s ease-out, transform 1.5s ease-out;
        }
        .scratch-scaler { transform: scale(1); transition: transform 0.3s; }
        .scratch-container {
            position: relative; width: 320px; height: 320px;
            clip-path: path("M 160,90 C 160,90 110,0 20,50 C -50,120 160,300 160,300 C 160,300 370,120 300,50 C 210,0 160,90 160,90 Z");
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }
        .scratch-bg { width: 100%; height: 100%; background: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        .heart-text {
            font-family: 'Alex Brush', cursive;
            color: #9e001c;
            font-size: 2.85rem;
            line-height: 1.08;
            letter-spacing: 0.5px;
            text-align: center;
            margin-top: 24px;
            text-shadow: 0 1px 2px rgba(158, 0, 28, 0.12);
        }
        canvas#scratchCard { position: absolute; top: 0; left: 0; z-index: 10; cursor: pointer; touch-action: none; }

        /* --- Scroll Unlock Prompt Below Heart (Smooth Blur-In & Blurred-Out-Fade-Out!) --- */
        .unlock-hint {
            font-size: 1.15rem;
            font-style: italic;
            color: #800000;
            margin: 12px auto 0 auto;
            min-height: 36px;
            opacity: 0;
            filter: blur(10px);
            transform: translateY(8px);
            transition: opacity 0.8s ease-out, filter 0.8s ease-out, transform 0.8s ease-out;
        }
        .unlock-hint.active {
            opacity: 1;
            filter: blur(0px);
            transform: translateY(0px);
            animation: hintPulse 2s infinite ease-in-out 0.8s;
        }
        .clone-unlock-hint {
            opacity: 1;
            filter: blur(0px);
            transform: translateY(0px);
            transition: opacity 0.65s ease-out, filter 0.65s ease-out, transform 0.65s ease-out;
        }
        .unlock-hint.blur-out-away,
        .clone-unlock-hint.blur-out-away {
            animation: none !important;
            opacity: 0 !important;
            filter: blur(14px) !important;
            transform: translateY(14px) scale(0.95) !important;
            transition: opacity 0.65s ease-out, filter 0.65s ease-out, transform 0.65s ease-out !important;
        }
        @keyframes hintPulse {
            0%, 100% { transform: translateY(0px); opacity: 0.78; }
            50% { transform: translateY(6px); opacity: 1; }
        }

        /* =========================================================
           PRE-WARMED 60FPS GPU SPLIT-PAGE CURTAIN STAGE
           ========================================================= */
        #split-stage {
            position: fixed;
            inset: 0;
            z-index: -1;
            display: none;
            opacity: 0;
            pointer-events: none;
            overflow: hidden;
        }
        .split-half {
            position: absolute;
            top: 0;
            width: 50%;
            height: 100%;
            overflow: hidden;
            background-color: #f7ecd3;
            background-image: 
                radial-gradient(circle at 15% 20%, rgba(168, 124, 72, 0.14) 0%, transparent 45%),
                radial-gradient(circle at 85% 35%, rgba(139, 94, 52, 0.12) 0%, transparent 40%),
                radial-gradient(circle at 25% 75%, rgba(168, 124, 72, 0.13) 0%, transparent 50%),
                radial-gradient(circle at 80% 85%, rgba(120, 75, 40, 0.14) 0%, transparent 45%),
                url('https://www.transparenttextures.com/patterns/aged-paper.png');
            will-change: transform;
            backface-visibility: hidden;
        }
        #split-left {
            left: 0;
            transform-origin: top left;
            box-shadow: 8px 18px 36px rgba(25, 0, 4, 0.45);
        }
        #split-right {
            right: 0;
            transform-origin: top right;
            box-shadow: -8px 18px 36px rgba(25, 0, 4, 0.45);
        }
        .split-inner {
            position: absolute;
            top: 0;
            left: 0;
            pointer-events: none;
        }

        /* Soft shadow fold along the center split seam */
        #split-left::after {
            content: ''; position: absolute; top: 0; right: 0; width: 22px; height: 100%;
            background: linear-gradient(to right, transparent, rgba(74, 59, 50, 0.22));
            pointer-events: none;
        }
        #split-right::after {
            content: ''; position: absolute; top: 0; left: 0; width: 22px; height: 100%;
            background: linear-gradient(to left, transparent, rgba(74, 59, 50, 0.22));
            pointer-events: none;
        }

        /* =========================================================
           PART 2 SECTION (Royal Red Theme — Champagne Gold & Ivory Typography)
           ========================================================= */
        #part2-section {
            display: none;
            position: relative;
            z-index: 12;
            padding: 0 20px;
            color: #fdf5e6;
        }
        #split-scroll-track {
            position: relative;
            width: 100%;
        }
        #couple-sticky-frame {
            position: sticky;
            top: 0;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            opacity: 0;
            visibility: hidden;
            will-change: opacity, transform;
        }
        .couple-details {
            max-width: 780px;
            padding: 20px 10px;
            margin: 0 auto;
        }
        .couple-name-big {
            font-family: 'Alex Brush', cursive;
            font-size: clamp(3rem, 8.8vw, 4.6rem);
            color: #fbe59c;
            line-height: 1.15;
            margin: 4px 0;
            text-shadow: 0 3px 14px rgba(0, 0, 0, 0.45);
        }
        .couple-lineage {
            font-size: 1.3rem;
            color: #f4e2c7;
            margin-bottom: 14px;
            text-shadow: 0 1px 6px rgba(0, 0, 0, 0.35);
        }
        .couple-with {
            font-family: 'Great Vibes', cursive;
            font-size: 2.6rem;
            color: #f5d376;
            margin: 8px 0;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.35);
        }

        /* --- Schedule Table (Same Layout, Restyled for Royal Red Theme) --- */
        .schedule-box {
            max-width: 800px;
            margin: 4vh auto 18vh auto;
            opacity: 0; filter: blur(12px); transform: translateY(50px);
            transition: opacity 1.5s ease-out, filter 1.5s ease-out, transform 1.5s ease-out;
            background: rgba(34, 0, 6, 0.42);
            padding: 30px;
            border-radius: 15px;
            border: 2px dashed rgba(245, 211, 118, 0.65);
            box-shadow: 0 14px 36px rgba(0, 0, 0, 0.32);
            overflow-x: auto;
        }
        table { width: 100%; border-collapse: collapse; min-width: 400px; }
        th, td { padding: 15px; text-align: center; border-bottom: 1px solid rgba(253, 245, 230, 0.22); }
        th { font-family: 'Great Vibes', cursive; font-size: 2rem; color: #f5d376; border-bottom: 2px solid rgba(245, 211, 118, 0.55); }
        td { font-size: 1.15rem; color: #fdf5e6; }
        .venue-sub { font-size: 0.9rem; color: #e6cfb3; }

        /* --- RSVP & Best Compliments (Red Theme) --- */
        .rsvp-box {
            max-width: 720px;
            margin: 0 auto 14vh auto;
            opacity: 0;
            filter: blur(12px);
            transform: translateY(40px);
            transition: opacity 1.5s ease-out, filter 1.5s ease-out, transform 1.5s ease-out;
            line-height: 1.75;
            font-size: 1.25rem;
            color: #f4e2c7;
        }
        .rsvp-heading {
            font-family: 'Great Vibes', cursive;
            font-size: 2.5rem;
            color: #f5d376;
            margin: 18px 0 4px 0;
            text-shadow: 0 2px 8px rgba(0, 0, 0, 0.35);
        }
        .rsvp-detail {
            font-weight: 600;
            color: #fff8ec;
        }

        /* --- Footer (Red Theme) --- */
        .footer-text {
            font-size: 1.55rem;
            opacity: 0; filter: blur(12px); transform: translateY(50px);
            transition: opacity 1.5s ease-out, filter 1.5s ease-out, transform 1.5s ease-out;
            padding-bottom: 100px;
            font-style: italic;
            color: #fbe59c;
            font-weight: bold;
            max-width: 750px;
            margin: 0 auto;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
        }

        /* --- Interactive Trigger Class (for Garden SVGs) --- */
        .interactive-emoji { display: inline-block; cursor: pointer; user-select: none; -webkit-tap-highlight-color: transparent; }
        .pop-anim { animation: clickPop 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; }
        @keyframes clickPop {
            0% { transform: scale(1) rotate(0deg); filter: brightness(1); }
            30% { transform: scale(1.6) rotate(15deg); filter: brightness(1.2); }
            70% { transform: scale(1.6) rotate(-15deg); filter: brightness(1.2); }
            100% { transform: scale(1) rotate(0deg); filter: brightness(1); }
        }

        /* --- Garden Butterfly Wing Flapping --- */
        .bf-flap-anim { animation: bfWing 0.3s infinite alternate ease-in-out; transform-origin: 16px 16px; }
        @keyframes bfWing { 0% { transform: scaleX(1); } 100% { transform: scaleX(0.25); } }

        /* --- Explosion Bird SVG Classes --- */
        .bird-svg { overflow: visible; animation: birdBob 1.2s infinite ease-in-out alternate; }
        .bird-wing { animation: birdFlap 0.5s infinite ease-in-out alternate; }
        @keyframes birdBob { 0% { transform: translateY(0px); } 100% { transform: translateY(12px); } }
        @keyframes birdFlap {
            0%   { d: path("M 5 10 Q 30 15 50 30 Q 70 15 95 10"); }
            100% { d: path("M 5 50 Q 30 35 50 30 Q 70 35 95 50"); }
        }

        .visible-up { opacity: 1 !important; filter: blur(0px) !important; transform: translateY(0) !important; }

        /* =========================================
           MOBILE RESPONSIVENESS
           ========================================= */
        @media (max-width: 768px) {
            .type-fade { font-size: 1.35rem !important; margin-bottom: 14vh; }
            .hadith-trans { font-size: 1.15rem; }
            .sub-header-text { font-size: 1.25rem; }
            .blessings-line { font-size: 1.15rem; }
            .hosts-names { font-size: 1.4rem; }
            .hosts-sub { font-size: 1.05rem; }
            .flower { font-size: 4.5rem; }
            .butterfly { font-size: 2.2rem; }
            .garden-container { gap: 40px; height: 100px; }

            .couple-lineage { font-size: 1.05rem; }
            .couple-with { font-size: 2rem; }

            .scratch-scaler { transform: scale(0.85); }
            .scratch-wrapper { margin: 0 auto 12px auto; }

            .schedule-box { padding: 15px; margin-bottom: 14vh; }
            th { font-size: 1.5rem; padding: 10px; }
            td { font-size: 0.95rem; padding: 10px; }

            .rsvp-box { font-size: 1.1rem; }
            .rsvp-heading { font-size: 2rem; }
            .footer-text { font-size: 1.2rem; }
            .open-btn { font-size: 28px; padding: 14px 36px; }
        }

        @media (max-width: 480px) {
            .type-fade { font-size: 1.2rem !important; }
            .sub-header-text { font-size: 1.12rem; }
            .hosts-names { font-size: 1.25rem; }
            .scratch-scaler { transform: scale(0.75); }
            .garden-container { gap: 20px; }
        }
    </style>
</head>
<body>

    <!-- MASTER SVG DEFINITIONS (Used for Garden & Side Cannons) -->
    <svg width="0" height="0" style="position:absolute; pointer-events: none;">
      <defs>
        <path id="svg-heart" d="M16 28.5C16 28.5 4 20 4 10C4 5.6 7.6 2 12 2C14.4 2 16 3.6 16 3.6C16 3.6 17.6 2 20 2C24.4 2 28 5.6 28 10C28 20 16 28.5 16 28.5Z"/>

        <g id="svg-flower">
            <g stroke="#ffffff" stroke-width="0.5">
                <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" fill="currentColor"/>
                <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(72 16 16)" fill="currentColor"/>
                <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(144 16 16)" fill="currentColor"/>
                <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(216 16 16)" fill="currentColor"/>
                <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(288 16 16)" fill="currentColor"/>
            </g>
            <g fill="#ffffff" opacity="0.4" transform="rotate(36 16 16)">
                <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" />
                <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(72 16 16)" />
                <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(144 16 16)" />
                <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(216 16 16)" />
                <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(288 16 16)" />
            </g>
            <circle cx="16" cy="16" r="3" fill="#ffd700" />
            <circle cx="16" cy="16" r="1.5" fill="#fff" opacity="0.8"/>
        </g>

        <g id="svg-butterfly">
            <g class="bf-flap-anim">
                <path d="M 15 16 C 5 4 0 10 7 16 C 0 22 5 28 15 16 Z" />
                <path d="M 17 16 C 27 4 32 10 25 16 C 32 22 27 28 17 16 Z" />
            </g>
            <rect x="15" y="8" width="2" height="16" rx="1" fill="#4a3b32"/>
        </g>
        <path id="svg-sparkle" d="M16 2 Q16 16 2 16 Q16 16 16 30 Q16 16 30 16 Q16 16 16 2 Z"/>
      </defs>
    </svg>

    <!-- Royal Red Theme Backdrop (Fades in beneath the splitting old-paper curtains) -->
    <div id="red-theme-backdrop"></div>

    <!-- 60fps Pre-Baked Sprite Parallax Canvases (Background & Foreground) -->
    <canvas id="bg-decor-canvas" class="decor-canvas"></canvas>
    <canvas id="fg-decor-canvas" class="decor-canvas"></canvas>

    <!-- Red Glossy Silky Cloth Curtains (Pure Silk, No Yellow Boundary) -->
    <div id="curtain-wrapper">
       <canvas id="curtain-canvas"></canvas>
       <div class="open-btn" onclick="openCurtains()">Open</div>
    </div>

    <!-- Split-Page Curtain Overlay (Pre-warmed when heart is scratched for 0ms start!) -->
    <div id="split-stage">
        <div id="split-left" class="split-half">
            <div id="split-left-inner" class="split-inner"></div>
        </div>
        <div id="split-right" class="split-half">
            <div id="split-right-inner" class="split-inner"></div>
        </div>
    </div>

    <!-- Website Content -->
    <div class="content" id="main-content">

       <!-- PART 1: Upper Page up to Scratched Heart -->
       <div id="part1-wrapper" class="part1-container">
           <!-- Bismillah -->
           <div class="bismillah-wrap">
               <div class="bismillah obs fade-up">بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ</div>
           </div>

           <!-- Type-in Fade-in Translation -->
           <div class="header-text obs type-fade" data-text="&quot;In the name of Allah, the Most Gracious, the Most Merciful&quot;"></div>

           <!-- Hadith -->
           <div class="hadith-box obs fade-up">
               <div class="hadith-arabic">النِّكَاحُ مِنْ سُنَّتِي</div>
               <div class="hadith-trans">"Nikah is my Sunnah" — (Sahih Muslim)</div>
           </div>

           <!-- Ink Spread Hosts & Invitation Request + Blooming Garden -->
           <div class="obs ink-trigger" style="min-height: 360px; margin-bottom: 16vh; display: flex; align-items: center; justify-content: center;">
               <div class="ink-spread-anim">
                   <div class="sub-header-text">
                       <span class="blessings-line">With the blessings of Almighty Allah,</span>
                       <span class="hosts-names">
                           Mrs. Mehnaz Ahmer <span class="hosts-sub">(W/O Late Mr. Ahmer Mukhtar)</span><br>
                           &amp; Mr. Ali Ahmer
                       </span>
                       cordially request the pleasure of your company<br>
                       at the <span class="wedding-word">wedding</span> ceremonies of their beloved daughter &amp; sister
                   </div>

                   <div class="garden-container">
                       <div class="plant">
                           <div class="butterfly">
                               <span class="interactive-emoji">
                                   <svg viewBox="0 0 32 32" width="1em" height="1em" fill="#00bfff"><use href="#svg-butterfly" /></svg>
                               </span>
                           </div>
                           <div class="flower">
                               <span class="interactive-emoji">
                                   <svg viewBox="0 0 32 32" width="1em" height="1em" fill="#ffb6c1" style="overflow: visible;">
                                       <g class="flower-layer-1" stroke="#ffffff" stroke-width="0.5">
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(72 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(144 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(216 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(288 16 16)" fill="currentColor"/>
                                       </g>
                                       <g class="flower-layer-2" fill="#ffffff" opacity="0.4" transform="rotate(36 16 16)">
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(72 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(144 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(216 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(288 16 16)" />
                                       </g>
                                       <g class="flower-layer-3" fill="#ffffff" opacity="0.6">
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(72 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(144 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(216 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(288 16 16)" />
                                       </g>
                                       <g class="flower-center">
                                           <circle cx="16" cy="16" r="3" fill="#ffd700" />
                                           <circle cx="16" cy="16" r="1.5" fill="#fff" opacity="0.8"/>
                                       </g>
                                   </svg>
                               </span>
                           </div>
                       </div>
                       <div class="plant delayed">
                           <div class="butterfly">
                               <span class="interactive-emoji">
                                   <svg viewBox="0 0 32 32" width="1em" height="1em" fill="#ffdab9"><use href="#svg-butterfly" /></svg>
                               </span>
                           </div>
                           <div class="flower">
                               <span class="interactive-emoji">
                                   <svg viewBox="0 0 32 32" width="1em" height="1em" fill="#ff033e" style="overflow: visible;">
                                       <g class="flower-layer-1" stroke="#ffffff" stroke-width="0.5">
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(72 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(144 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(216 16 16)" fill="currentColor"/>
                                           <path d="M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z" transform="rotate(288 16 16)" fill="currentColor"/>
                                       </g>
                                       <g class="flower-layer-2" fill="#ffffff" opacity="0.4" transform="rotate(36 16 16)">
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(72 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(144 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(216 16 16)" />
                                           <path d="M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z" transform="rotate(288 16 16)" />
                                       </g>
                                       <g class="flower-layer-3" fill="#ffffff" opacity="0.6">
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(72 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(144 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(216 16 16)" />
                                           <path d="M 16 16 C 10 14 11 6 16 8 C 21 6 22 14 16 16 Z" transform="rotate(288 16 16)" />
                                       </g>
                                       <g class="flower-center">
                                           <circle cx="16" cy="16" r="3" fill="#ffd700" />
                                           <circle cx="16" cy="16" r="1.5" fill="#fff" opacity="0.8"/>
                                       </g>
                                   </svg>
                               </span>
                           </div>
                       </div>
                   </div>
               </div>
           </div>

           <!-- Scratched Heart (Scroll ends here until scratched!) -->
           <div class="scratch-wrapper obs fade-up">
               <div class="scratch-scaler">
                   <div class="scratch-container">
                       <div class="scratch-bg">
                           <div class="heart-text">
                               Asad <br>
                               <span style="font-size: 1.9rem;">&amp;</span><br>
                               Rimsha
                           </div>
                       </div>
                       <canvas id="scratchCard" width="320" height="320"></canvas>
                   </div>
               </div>
           </div>

           <div id="unlock-hint" class="unlock-hint">
               ↓ Scroll down to reveal ↓
           </div>
       </div>

       <!-- PART 2: Royal Red Theme (Unlocked After Scratching, Revealed Beneath Splitting Part 1) -->
       <div id="part2-section">
           <div id="split-scroll-track">
               <div id="couple-sticky-frame">
                   <div class="couple-details">
                       <div class="couple-name-big">Rimsha Fatima</div>
                       <div class="couple-lineage">D/O Mr. Ahmer Mukhtar (Marhoom)</div>
                       <div class="couple-with">with</div>
                       <div class="couple-name-big">Mr. Asad</div>
                       <div class="couple-lineage">S/O [Groom's Father's Name]</div>
                   </div>
               </div>
           </div>

           <!-- Schedule Table (Same Layout, Restyled for Royal Red Theme) -->
           <div class="schedule-box obs fade-up">
               <table>
                   <tr><th>Event</th><th>Date</th><th>Time</th><th>Location</th></tr>
                   <tr>
                       <td><b>MEHNDI</b></td>
                       <td>Thursday, 24th December 2026</td>
                       <td>07:00 PM onwards</td>
                       <td>Farid Town, Sahiwal</td>
                   </tr>
                   <tr>
                       <td><b>BARAAT</b></td>
                       <td>Friday, 25th December 2026</td>
                       <td>11:00 AM onwards</td>
                       <td>Grand Al-Noor Marriage Hall (JTS)<br><span class="venue-sub">(Near Faridia Park, Tariq Bin Ziad Colony, Sahiwal)</span></td>
                   </tr>
               </table>
           </div>

           <!-- RSVP & Compliments -->
           <div class="rsvp-box obs fade-up">
               <div class="rsvp-heading">RSVP:</div>
               <div class="rsvp-detail">Mr. Ali Ahmer</div>
               <div>[Phone Number]</div>

               <div class="rsvp-heading" style="margin-top: 28px;">With Best Compliments From:</div>
               <div class="rsvp-detail">All Relatives &amp; Friends</div>
           </div>

           <!-- Footer Quote -->
           <div class="footer-text obs fade-up">
               "Your presence and duas are the only gifts we desire."
           </div>
       </div>
    </div>

    <script>
        // ============================================================
        // 1. PER-PIXEL GLOSSY SILK CURTAIN (Overscanned, Pure Red Silk)
        // ============================================================
        const curtainWrapper = document.getElementById('curtain-wrapper');
        const curtainCanvas = document.getElementById('curtain-canvas');

        let cW = 0, cH = 0, cDpr = 1;
        let isCurtainOpening = false;
        let isCurtainDone = false;
        let curtainOpenTime = 0;

        function easeInOutCubic(t) {
            return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
        }
        function clamp01(val) {
            return Math.max(0, Math.min(1, val));
        }

        function computeSilkPoint(side, u, v, timeSec, rawProgress) {
            const waveAmp = (cW < 600 ? 22 : 42);
            const numFolds = cW < 600 ? 6.8 : 9.8;

            const lag = v * 0.22 + (1 - u) * 0.05;
            const t = clamp01((rawProgress - lag) / 0.73);
            const ease = easeInOutCubic(t);

            const outerX = -0.25 * cW - ease * (0.20 * cW);
            const innerX = (0.504 * cW) * (1.0 - ease * 1.12) - ease * (0.06 * cW);

            const seamPin = u * (1.0 - Math.pow(u, 3.0) * (1.0 - ease));
            const breezePhase = v * 3.8 - timeSec * 1.35 + u * 5.0 + (side === 1 ? 1.15 : 0.0);
            const breeze = Math.sin(breezePhase) * (3.5 + 7.5 * v) * seamPin * (1.0 - ease * 0.35);

            const clothWave = Math.sin(v * Math.PI * 2.4 - rawProgress * 7.5 + u * 2.2)
                            * Math.sin(ease * Math.PI)
                            * waveAmp * u * (0.25 + 0.75 * v);

            const yBase = -0.45 * cH + v * (1.48 * cH);
            const dropY = Math.pow(ease, 1.35) * (cH * 0.28) * (0.15 + 0.85 * u);
            const hemScallop = Math.sin(u * numFolds * Math.PI * 2.0) * 3.5 * v * (1.0 - ease);
            const vertRipple = Math.sin(u * Math.PI * 3.0 + rawProgress * 5.0) * Math.sin(ease * Math.PI) * 10.0 * v;

            const xLocal = outerX + u * (innerX - outerX) + clothWave + breeze;
            const x = side === 0 ? xLocal : (cW - xLocal);
            const y = yBase + dropY + hemScallop + vertRipple;

            return { x, y, ease };
        }

        const gl = curtainCanvas.getContext('webgl', { alpha: true, antialias: true })
                || curtainCanvas.getContext('experimental-webgl', { alpha: true, antialias: true });

        let glState = null;
        if (gl) {
            const vsSource = `
                attribute vec2 a_pos;
                attribute vec2 a_uv;
                attribute vec2 a_meta;
                varying vec2 v_uv;
                varying vec2 v_meta;
                void main() {
                    gl_Position = vec4(a_pos, 0.0, 1.0);
                    v_uv = a_uv;
                    v_meta = a_meta;
                }
            `;
            const fsSource = `
                precision mediump float;
                varying vec2 v_uv;
                varying vec2 v_meta;
                uniform float u_time;
                uniform float u_numFolds;
                uniform float u_alpha;

                void main() {
                    float u = clamp(v_uv.x, 0.0, 1.0);
                    float v = clamp(v_uv.y, 0.0, 1.0);
                    float side = v_meta.x;
                    float ease = v_meta.y;

                    float foldPhase = u * u_numFolds * 6.2831853
                                    + sin(v * 3.6 - u_time * 1.35 + side * 1.15) * 0.48
                                    + ease * 2.6 * u;

                    float slope = cos(foldPhase);
                    float ridge = sin(foldPhase);

                    float vScreen = clamp((v - 0.30) / 0.68, 0.0, 1.0);
                    float stageGlow = 0.84 + 0.22 * exp(-pow((vScreen - 0.34) * 1.9, 2.0));
                    float hemShadow = 1.0 - 0.18 * pow(vScreen, 1.8);
                    float vLight = stageGlow * hemShadow;

                    float sharpSpec = pow(max(0.0, slope), 6.5);
                    float broadSheen = pow(max(0.0, slope), 2.0);
                    float rimSheen = pow(1.0 - abs(slope), 3.0) * 0.20;
                    float valleyShadow = pow(max(0.0, -slope), 1.45);
                    float weave = 0.975 + 0.025 * sin(u * 540.0 + v * 65.0) * sin(v * 320.0);

                    vec3 silkCol = vec3(0.49, 0.03, 0.08);
                    silkCol -= valleyShadow * vec3(0.37, 0.028, 0.06);
                    silkCol += broadSheen * vec3(0.30, 0.06, 0.10);
                    silkCol += rimSheen * vec3(0.36, 0.08, 0.14);
                    silkCol += sharpSpec * vec3(0.42, 0.24, 0.27);
                    silkCol += max(0.0, ridge) * 0.04 * vec3(0.3, 0.05, 0.08);

                    vec3 finalCol = silkCol * vLight * weave;
                    gl_FragColor = vec4(clamp(finalCol, 0.0, 1.0), u_alpha);
                }
            `;

            function compileShader(type, src) {
                const s = gl.createShader(type);
                gl.shaderSource(s, src);
                gl.compileShader(s);
                return s;
            }

            const prog = gl.createProgram();
            gl.attachShader(prog, compileShader(gl.VERTEX_SHADER, vsSource));
            gl.attachShader(prog, compileShader(gl.FRAGMENT_SHADER, fsSource));
            gl.linkProgram(prog);
            gl.useProgram(prog);

            const COLS = 48;
            const ROWS = 28;
            const vertsPerSide = (COLS + 1) * (ROWS + 1);
            const totalVerts = vertsPerSide * 2;
            const vertexData = new Float32Array(totalVerts * 6);

            const indices = [];
            for (let s = 0; s < 2; s++) {
                const base = s * vertsPerSide;
                for (let i = 0; i < COLS; i++) {
                    for (let j = 0; j < ROWS; j++) {
                        const v00 = base + i * (ROWS + 1) + j;
                        const v10 = base + (i + 1) * (ROWS + 1) + j;
                        const v01 = v00 + 1;
                        const v11 = v10 + 1;
                        indices.push(v00, v10, v11, v00, v11, v01);
                    }
                }
            }

            const vbo = gl.createBuffer();
            gl.bindBuffer(gl.ARRAY_BUFFER, vbo);
            gl.bufferData(gl.ARRAY_BUFFER, vertexData.byteLength, gl.DYNAMIC_DRAW);

            const ibo = gl.createBuffer();
            gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, ibo);
            gl.bufferData(gl.ELEMENT_ARRAY_BUFFER, new Uint16Array(indices), gl.STATIC_DRAW);

            const aPos = gl.getAttribLocation(prog, 'a_pos');
            const aUv = gl.getAttribLocation(prog, 'a_uv');
            const aMeta = gl.getAttribLocation(prog, 'a_meta');
            gl.enableVertexAttribArray(aPos);
            gl.enableVertexAttribArray(aUv);
            gl.enableVertexAttribArray(aMeta);
            gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 24, 0);
            gl.vertexAttribPointer(aUv, 2, gl.FLOAT, false, 24, 8);
            gl.vertexAttribPointer(aMeta, 2, gl.FLOAT, false, 24, 16);

            gl.enable(gl.BLEND);
            gl.blendFunc(gl.SRC_ALPHA, gl.ONE_MINUS_SRC_ALPHA);

            glState = {
                COLS, ROWS, vertsPerSide, vertexData,
                indexCount: indices.length,
                uTime: gl.getUniformLocation(prog, 'u_time'),
                uNumFolds: gl.getUniformLocation(prog, 'u_numFolds'),
                uAlpha: gl.getUniformLocation(prog, 'u_alpha')
            };
        }

        const cCtxFallback = !glState ? curtainCanvas.getContext('2d') : null;

        function resizeCurtainCanvas() {
            if (isCurtainDone) return;
            cW = window.innerWidth;
            cH = window.innerHeight;
            cDpr = Math.min(window.devicePixelRatio || 1, 2);
            curtainCanvas.width = Math.floor(cW * cDpr);
            curtainCanvas.height = Math.floor(cH * cDpr);
            if (glState) {
                gl.viewport(0, 0, curtainCanvas.width, curtainCanvas.height);
            } else if (cCtxFallback) {
                cCtxFallback.setTransform(cDpr, 0, 0, cDpr, 0, 0);
            }
        }
        resizeCurtainCanvas();
        window.addEventListener('resize', resizeCurtainCanvas);

        function drawSilkFallback2D(timeSec, rawProgress, alpha) {
            const ctx2 = cCtxFallback;
            ctx2.clearRect(0, 0, cW, cH);
            ctx2.globalAlpha = alpha;
            const ROWS = 48;
            const numFolds = cW < 600 ? 6.8 : 9.8;

            for (let side = 0; side < 2; side++) {
                for (let j = 0; j < ROWS; j++) {
                    const v0 = j / ROWS;
                    const v1 = (j + 1) / ROWS;
                    const vMid = (v0 + v1) * 0.5;
                    const pStart = computeSilkPoint(side, 0, vMid, timeSec, rawProgress);
                    const pEnd = computeSilkPoint(side, 1, vMid, timeSec, rawProgress);
                    const p00 = computeSilkPoint(side, 0, v0, timeSec, rawProgress);
                    const p10 = computeSilkPoint(side, 1, v0, timeSec, rawProgress);
                    const p11 = computeSilkPoint(side, 1, v1, timeSec, rawProgress);
                    const p01 = computeSilkPoint(side, 0, v1, timeSec, rawProgress);

                    const grad = ctx2.createLinearGradient(pStart.x, pStart.y, pEnd.x, pEnd.y);
                    const stops = 36;
                    for (let s = 0; s <= stops; s++) {
                        const u = s / stops;
                        const phase = u * numFolds * Math.PI * 2 + Math.sin(vMid * 3.6 - timeSec * 1.35) * 0.45;
                        const cosVal = Math.cos(phase);
                        const spec = cosVal > 0 ? Math.pow(cosVal, 4.0) : 0;
                        const shad = cosVal < 0 ? Math.pow(-cosVal, 1.3) : 0;
                        grad.addColorStop(u, `rgb(${Math.round(130+spec*115-shad*90)},${Math.round(8+spec*65-shad*8)},${Math.round(22+spec*70-shad*16)})`);
                    }
                    ctx2.fillStyle = grad;
                    ctx2.beginPath();
                    ctx2.moveTo(p00.x, p00.y - 0.8);
                    ctx2.lineTo(p10.x, p10.y - 0.8);
                    ctx2.lineTo(p11.x, p11.y + 0.8);
                    ctx2.lineTo(p01.x, p01.y + 0.8);
                    ctx2.closePath();
                    ctx2.fill();
                }
            }
            ctx2.globalAlpha = 1;
        }

        function renderCurtainFrame(now) {
            if (isCurtainDone) return;
            const timeSec = now / 1000;
            let rawProgress = 0;

            if (isCurtainOpening) {
                const elapsed = (now - curtainOpenTime) / 1000;
                rawProgress = clamp01(elapsed / 2.6);
            }

            const alpha = rawProgress > 0.82 ? Math.max(0, 1 - (rawProgress - 0.82) / 0.18) : 1.0;

            if (glState) {
                const { COLS, ROWS, vertexData, indexCount, uTime, uNumFolds, uAlpha } = glState;
                let idx = 0;
                for (let side = 0; side < 2; side++) {
                    for (let i = 0; i <= COLS; i++) {
                        const u = i / COLS;
                        for (let j = 0; j <= ROWS; j++) {
                            const v = j / ROWS;
                            const pt = computeSilkPoint(side, u, v, timeSec, rawProgress);
                            vertexData[idx++] = (pt.x / cW) * 2.0 - 1.0;
                            vertexData[idx++] = 1.0 - (pt.y / cH) * 2.0;
                            vertexData[idx++] = u;
                            vertexData[idx++] = v;
                            vertexData[idx++] = side;
                            vertexData[idx++] = pt.ease;
                        }
                    }
                }
                gl.clearColor(0, 0, 0, 0);
                gl.clear(gl.COLOR_BUFFER_BIT);
                gl.uniform1f(uTime, timeSec);
                gl.uniform1f(uNumFolds, cW < 600 ? 6.8 : 9.8);
                gl.uniform1f(uAlpha, alpha);
                gl.bufferSubData(gl.ARRAY_BUFFER, 0, vertexData);
                gl.drawElements(gl.TRIANGLES, indexCount, gl.UNSIGNED_SHORT, 0);
            } else if (cCtxFallback) {
                drawSilkFallback2D(timeSec, rawProgress, alpha);
            }

            if (rawProgress >= 1) {
                isCurtainDone = true;
                curtainWrapper.style.display = 'none';
                return;
            }
            requestAnimationFrame(renderCurtainFrame);
        }

        requestAnimationFrame(renderCurtainFrame);

        // ============================================================
        // 2. AUTO-FIT BISMILLAH FOR MOBILE SCREENS
        // ============================================================
        function fitBismillah() {
            const el = document.querySelector('.bismillah');
            if (!el) return;
            el.style.fontSize = '';
            const maxWidth = window.innerWidth - 48;
            const naturalWidth = el.scrollWidth;
            if (naturalWidth > maxWidth && naturalWidth > 0) {
                const currentFontSize = parseFloat(window.getComputedStyle(el).fontSize);
                const scaledSize = currentFontSize * (maxWidth / naturalWidth) * 0.94;
                el.style.fontSize = scaledSize + 'px';
            }
        }
        window.addEventListener('load', fitBismillah);
        window.addEventListener('resize', fitBismillah);
        if (document.fonts && document.fonts.ready) {
            document.fonts.ready.then(fitBismillah);
        }

        // ============================================================
        // 3. 60FPS PRE-BAKED SPRITE PARALLAX + BIRD FLOCK + SPLIT CURTAIN ENGINE
        // ============================================================
        const redBackdrop = document.getElementById('red-theme-backdrop');
        const bgDecorCanvas = document.getElementById('bg-decor-canvas');
        const fgDecorCanvas = document.getElementById('fg-decor-canvas');
        const bgCtx = bgDecorCanvas.getContext('2d');
        const fgCtx = fgDecorCanvas.getContext('2d');

        const shapeTypes = ['heart', 'flower', 'butterfly', 'sparkle'];
        const weddingColors = ['#ff033e', '#ffb6c1', '#d4af37', '#e6a8d7', '#ffdab9', '#ffffff', '#ffd700'];

        function generateSvgGraphic(sizeRem, color) {
            let type = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
            return `<svg viewBox="0 0 32 32" width="${sizeRem}rem" height="${sizeRem}rem" fill="${color}" style="pointer-events: none;"><use href="#svg-${type}" /></svg>`;
        }

        function drawVectorShape(ctx, type, color) {
            ctx.save();
            ctx.fillStyle = color;

            if (type === 'heart') {
                const p = new Path2D("M16 28.5C16 28.5 4 20 4 10C4 5.6 7.6 2 12 2C14.4 2 16 3.6 16 3.6C16 3.6 17.6 2 20 2C24.4 2 28 5.6 28 10C28 20 16 28.5 16 28.5Z");
                ctx.fill(p);
            } else if (type === 'sparkle') {
                const p = new Path2D("M16 2 Q16 16 2 16 Q16 16 16 30 Q16 16 30 16 Q16 16 16 2 Z");
                ctx.fill(p);
            } else if (type === 'butterfly') {
                const leftW = new Path2D("M 15 16 C 5 4 0 10 7 16 C 0 22 5 28 15 16 Z");
                const rightW = new Path2D("M 17 16 C 27 4 32 10 25 16 C 32 22 27 28 17 16 Z");
                ctx.fill(leftW);
                ctx.fill(rightW);
                ctx.fillStyle = '#4a3b32';
                ctx.beginPath();
                ctx.roundRect ? ctx.roundRect(15, 8, 2, 16, 1) : ctx.rect(15, 8, 2, 16);
                ctx.fill();
            } else if (type === 'flower') {
                const petal = new Path2D("M 16 16 C 4 10 6 -2 16 2 C 26 -2 28 10 16 16 Z");
                const innerPetal = new Path2D("M 16 16 C 6 12 8 2 16 5 C 24 2 26 12 16 16 Z");

                ctx.strokeStyle = 'rgba(255,255,255,0.85)';
                ctx.lineWidth = 0.5;
                for (let k = 0; k < 5; k++) {
                    ctx.save();
                    ctx.translate(16, 16);
                    ctx.rotate((k * 72 * Math.PI) / 180);
                    ctx.translate(-16, -16);
                    ctx.fill(petal);
                    ctx.stroke(petal);
                    ctx.restore();
                }

                ctx.fillStyle = 'rgba(255,255,255,0.42)';
                for (let k = 0; k < 5; k++) {
                    ctx.save();
                    ctx.translate(16, 16);
                    ctx.rotate(((k * 72 + 36) * Math.PI) / 180);
                    ctx.translate(-16, -16);
                    ctx.fill(innerPetal);
                    ctx.restore();
                }

                ctx.fillStyle = '#ffd700';
                ctx.beginPath();
                ctx.arc(16, 16, 3, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = 'rgba(255,255,255,0.85)';
                ctx.beginPath();
                ctx.arc(16, 16, 1.4, 0, Math.PI * 2);
                ctx.fill();
            }
            ctx.restore();
        }

        const spriteCache = {};
        function getBlurredSprite(type, color, blurPx) {
            const key = `${type}|${color}|${blurPx}`;
            if (spriteCache[key]) return spriteCache[key];

            const size = 112;
            const raw = document.createElement('canvas');
            raw.width = size;
            raw.height = size;
            const rCtx = raw.getContext('2d');
            rCtx.translate(24, 24);
            rCtx.scale(2, 2);
            drawVectorShape(rCtx, type, color);

            const out = document.createElement('canvas');
            out.width = size;
            out.height = size;
            const oCtx = out.getContext('2d');

            if ('filter' in oCtx) {
                oCtx.filter = `blur(${blurPx}px)`;
                oCtx.drawImage(raw, 0, 0);
            } else {
                oCtx.globalAlpha = 0.14;
                const r = blurPx * 1.1;
                for (let a = 0; a < 8; a++) {
                    const ang = (a * Math.PI) / 4;
                    oCtx.drawImage(raw, Math.cos(ang) * r, Math.sin(ang) * r);
                }
                oCtx.globalAlpha = 0.35;
                oCtx.drawImage(raw, 0, 0);
            }

            spriteCache[key] = out;
            return out;
        }

        const isMobile = window.innerWidth <= 768;
        const bgCount = isMobile ? 30 : 60;
        const fgCount = isMobile ? 12 : 25;

        let dW = 0, dH = 0, dDpr = 1;
        function resizeDecorCanvases() {
            dW = window.innerWidth;
            dH = window.innerHeight;
            dDpr = Math.min(window.devicePixelRatio || 1, 2);
            bgDecorCanvas.width = Math.floor(dW * dDpr);
            bgDecorCanvas.height = Math.floor(dH * dDpr);
            fgDecorCanvas.width = Math.floor(dW * dDpr);
            fgDecorCanvas.height = Math.floor(dH * dDpr);
            bgCtx.setTransform(dDpr, 0, 0, dDpr, 0, 0);
            fgCtx.setTransform(dDpr, 0, 0, dDpr, 0, 0);
        }
        resizeDecorCanvases();

        function makeParticle(isFg) {
            const type = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
            const color = weddingColors[Math.floor(Math.random() * weddingColors.length)];
            const sizePx = isFg ? (Math.random() * 32 + 40) : (Math.random() * 24 + 18);
            const blurPx = isFg ? 3.2 : 1.6;
            return {
                type,
                sprite: getBlurredSprite(type, color, blurPx),
                xFrac: Math.random() * 0.94 + 0.03,
                yFrac: Math.random(),
                sizePx,
                alpha: isFg ? 0.65 : 0.55,
                phase: Math.random() * Math.PI * 2,
                floatSpeed: isFg ? 0.78 : 1.05,
                floatAmp: isFg ? 18 : 14,
                swayAmp: isFg ? 10 : 6,
                flapPhase: Math.random() * Math.PI * 2,
                popStart: 0,
                lastX: -999,
                lastY: -999
            };
        }

        const bgParticles = [];
        for (let i = 0; i < bgCount; i++) bgParticles.push(makeParticle(false));

        const fgParticles = [];
        for (let i = 0; i < fgCount; i++) fgParticles.push(makeParticle(true));

        const numFlocks = isMobile ? 3 : 5;
        const birdFlocks = [];
        for (let f = 0; f < numFlocks; f++) {
            const isRight = Math.random() > 0.5;
            const duration = Math.random() * 25 + 30;
            const yBaseFrac = Math.random() * 0.65 + 0.12;
            const birdsInFlock = Math.floor(Math.random() * 3) + 3;
            const birds = [];
            for (let b = 0; b < birdsInFlock; b++) {
                const xOff = isRight ? -(b * 35 + Math.random() * 10) : (b * 35 + Math.random() * 10);
                const yOff = (b % 2 === 0 ? 1 : -1) * (Math.ceil(b / 2) * 20) + (Math.random() * 10 - 5);
                birds.push({
                    xOff,
                    yOff,
                    scale: (Math.random() * 15 + 30) / 52,
                    flapPhase: Math.random() * Math.PI * 2,
                    popStart: 0,
                    lastX: -999,
                    lastY: -999
                });
            }
            birdFlocks.push({
                isRight,
                duration,
                timeOffset: Math.random() * duration,
                yBaseFrac,
                birds
            });
        }

        // --- Scroll-Driven Page Split State (Smooth Damped Lerp + Pre-Warmed GPU!) ---
        const part1Wrapper = document.getElementById('part1-wrapper');
        const part2Section = document.getElementById('part2-section');
        const splitScrollTrack = document.getElementById('split-scroll-track');
        const coupleStickyFrame = document.getElementById('couple-sticky-frame');
        const splitStage = document.getElementById('split-stage');
        const splitLeft = document.getElementById('split-left');
        const splitRight = document.getElementById('split-right');
        const splitLeftInner = document.getElementById('split-left-inner');
        const splitRightInner = document.getElementById('split-right-inner');

        let splitPrepared = false;
        let splitStartY = 0;
        let splitTravel = 700;
        let visualP = 0;
        let redBlend = 0;
        let clonedHintEls = [];

        function syncSplitMetrics() {
            if (!splitPrepared) return;
            const vh = window.innerHeight;
            const cw = document.documentElement.clientWidth;
            splitTravel = Math.round(vh * 0.95);
            splitStartY = Math.max(0, part1Wrapper.offsetHeight - vh);
            part2Section.style.marginTop = `-${vh}px`;
            splitScrollTrack.style.height = `${splitTravel + vh}px`;

            splitLeftInner.style.width = `${cw}px`;
            splitRightInner.style.width = `${cw}px`;
            splitRightInner.style.left = `${-cw / 2}px`;
            splitLeftInner.style.transform = `translate3d(0, ${-splitStartY}px, 0)`;
            splitRightInner.style.transform = `translate3d(0, ${-splitStartY}px, 0)`;
        }

        window.addEventListener('resize', () => {
            resizeDecorCanvases();
            syncSplitMetrics();
        });

        function buildSplitClones() {
            function makeSafeClone() {
                const clone = part1Wrapper.cloneNode(true);
                clone.removeAttribute('id');
                clone.querySelectorAll('[id]').forEach(n => n.removeAttribute('id'));

                // Remove scratch canvas from clone so only revealed "Asad & Rimsha" heart appears
                const c = clone.querySelector('canvas');
                if (c) c.remove();

                // Lock all already-visible Part 1 elements cleanly so nothing restarts or vanishes!
                clone.querySelectorAll('.obs').forEach(el => {
                    el.style.transition = 'none';
                    if (el.classList.contains('fade-up')) el.classList.add('visible-up');
                    if (el.classList.contains('ink-trigger')) el.classList.add('visible-ink');
                    if (el.classList.contains('type-fade')) el.classList.add('visible-fade');
                });

                // Lock ink-spread & garden flowers/butterflies in their bloomed state (no animation restart!)
                const inkAnim = clone.querySelector('.ink-spread-anim');
                if (inkAnim) {
                    inkAnim.style.transition = 'none';
                    inkAnim.style.opacity = '1';
                    inkAnim.style.clipPath = 'none';
                    inkAnim.style.filter = 'none';
                }
                clone.querySelectorAll('.flower-layer-1, .flower-layer-2, .flower-layer-3, .flower-center').forEach(layer => {
                    layer.style.animation = 'none';
                    layer.style.transform = 'scale(1)';
                });
                clone.querySelectorAll('.flower svg').forEach(svg => {
                    svg.style.animation = 'none';
                    svg.style.transform = 'scale(1)';
                });
                clone.querySelectorAll('.butterfly').forEach(bf => {
                    bf.style.transition = 'none';
                    bf.style.animation = 'none';
                    bf.style.bottom = '100px';
                    bf.style.opacity = '1';
                });

                // Keep "Scroll down to reveal" visible in clones so it blurs-out-fades-out smoothly!
                const hint = clone.querySelector('.unlock-hint');
                if (hint) {
                    hint.classList.remove('active');
                    hint.classList.add('clone-unlock-hint');
                }
                return clone;
            }
            splitLeftInner.innerHTML = '';
            splitRightInner.innerHTML = '';
            splitLeftInner.appendChild(makeSafeClone());
            splitRightInner.appendChild(makeSafeClone());
            clonedHintEls = Array.from(splitStage.querySelectorAll('.clone-unlock-hint'));
        }

        function setHintBlurOut(shouldBlurOut) {
            const realHint = document.getElementById('unlock-hint');
            if (shouldBlurOut) {
                if (realHint) realHint.classList.add('blur-out-away');
                clonedHintEls.forEach(el => el.classList.add('blur-out-away'));
            } else {
                if (realHint) realHint.classList.remove('blur-out-away');
                clonedHintEls.forEach(el => el.classList.remove('blur-out-away'));
            }
        }

        function updateSplitCurtains(scrollY) {
            if (!splitPrepared) return;

            const targetP = clamp01((scrollY - splitStartY) / splitTravel);
            visualP += (targetP - visualP) * 0.18;
            if (Math.abs(targetP - visualP) < 0.0005) visualP = targetP;

            if (visualP <= 0.0005 && targetP === 0) {
                visualP = 0;
                redBlend = 0;
                part1Wrapper.style.opacity = '1';
                part1Wrapper.style.visibility = 'visible';
                part1Wrapper.style.pointerEvents = 'auto';

                // Restore "Scroll down to reveal" smoothly if scrolled back to top
                setHintBlurOut(false);

                splitStage.style.zIndex = '19';
                splitStage.style.opacity = '0.001';
                splitLeft.style.transform = 'translate3d(0, 0, 0)';
                splitRight.style.transform = 'translate3d(0, 0, 0)';

                redBackdrop.style.opacity = '0';
                coupleStickyFrame.style.visibility = 'hidden';
                coupleStickyFrame.style.opacity = '0';
                part2Section.style.pointerEvents = 'none';
            } else if (visualP < 0.999) {
                const ease = easeInOutCubic(visualP);

                part1Wrapper.style.opacity = '0';
                part1Wrapper.style.visibility = 'hidden';
                part1Wrapper.style.pointerEvents = 'none';

                // Smoothly blur-out-fade-out "Scroll down to reveal" instead of snapping it off!
                setHintBlurOut(true);

                splitStage.style.zIndex = '25';
                const stageAlpha = visualP > 0.72 ? Math.max(0, 1 - (visualP - 0.72) / 0.28) : 1;
                splitStage.style.opacity = stageAlpha;

                redBlend = clamp01(visualP / 0.16);
                redBackdrop.style.opacity = redBlend;

                part2Section.style.pointerEvents = 'auto';

                const tx = ease * 42;
                const ty = Math.pow(ease, 1.2) * 58;
                const rotZ = ease * 10;
                const sx = 1 - ease * 0.18;

                splitLeft.style.transform = `translate3d(${-tx}vw, ${ty}vh, 0) rotate(${-rotZ}deg) scaleX(${sx})`;
                splitRight.style.transform = `translate3d(${tx}vw, ${ty}vh, 0) rotate(${rotZ}deg) scaleX(${sx})`;

                const cp = clamp01((visualP - 0.04) / 0.50);
                const cEase = easeInOutCubic(cp);
                coupleStickyFrame.style.visibility = 'visible';
                coupleStickyFrame.style.opacity = cEase;
                coupleStickyFrame.style.transform = `scale3d(${(0.92 + 0.08 * cEase).toFixed(3)}, ${(0.92 + 0.08 * cEase).toFixed(3)}, 1)`;
            } else {
                visualP = 1;
                redBlend = 1;
                part1Wrapper.style.opacity = '0';
                part1Wrapper.style.visibility = 'hidden';
                part1Wrapper.style.pointerEvents = 'none';

                setHintBlurOut(true);

                splitStage.style.zIndex = '-1';
                splitStage.style.opacity = '0';

                redBackdrop.style.opacity = '1';
                part2Section.style.pointerEvents = 'auto';
                coupleStickyFrame.style.visibility = 'visible';
                coupleStickyFrame.style.opacity = '1';
                coupleStickyFrame.style.transform = 'none';
            }
        }

        let decorLoopActive = false;
        function renderDecorFrame(now) {
            if (!decorLoopActive) return;
            const timeSec = now / 1000;
            const scrollY = window.scrollY || window.pageYOffset || 0;

            updateSplitCurtains(scrollY);

            bgCtx.clearRect(0, 0, dW, dH);
            fgCtx.clearRect(0, 0, dW, dH);

            // 1. Background Parallax Sprites (0.15x scroll speed)
            const bgWrapH = dH + 180;
            for (let i = 0; i < bgParticles.length; i++) {
                const p = bgParticles[i];
                const rawY = p.yFrac * bgWrapH - scrollY * 0.15;
                const wrappedY = ((rawY % bgWrapH) + bgWrapH) % bgWrapH - 90;
                const y = wrappedY + Math.sin(timeSec * p.floatSpeed + p.phase) * p.floatAmp;
                const x = p.xFrac * dW + Math.cos(timeSec * 0.65 + p.phase) * p.swayAmp;

                let popScale = 1, popRot = 0;
                if (p.popStart > 0) {
                    const pt = (now - p.popStart) / 600;
                    if (pt < 1) {
                        popScale = 1 + Math.sin(pt * Math.PI) * 0.65;
                        popRot = Math.sin(pt * Math.PI * 2) * 0.28;
                    } else {
                        p.popStart = 0;
                    }
                }

                p.lastX = x;
                p.lastY = y;

                const drawSize = (p.sizePx * (112 / 64));
                const flapX = p.type === 'butterfly' ? (0.625 + 0.375 * Math.sin(timeSec * 10.5 + p.flapPhase)) : 1;

                bgCtx.save();
                bgCtx.globalAlpha = p.alpha;
                bgCtx.translate(x, y);
                if (popRot !== 0) bgCtx.rotate(popRot);
                bgCtx.scale(popScale * flapX, popScale);
                bgCtx.drawImage(p.sprite, -drawSize * 0.5, -drawSize * 0.5, drawSize, drawSize);
                bgCtx.restore();
            }

            // 2. V-Formation Pencil Bird Flocks (Smoothly shift to champagne gold on Red Theme!)
            const br = Math.round(74 + redBlend * (245 - 74));
            const bg = Math.round(59 + redBlend * (222 - 59));
            const bb = Math.round(50 + redBlend * (179 - 50));
            const birdColor = `rgb(${br},${bg},${bb})`;

            for (let f = 0; f < birdFlocks.length; f++) {
                const fl = birdFlocks[f];
                const prog = ((timeSec + fl.timeOffset) % fl.duration) / fl.duration;
                const fx = fl.isRight
                    ? (-0.15 * dW + prog * (1.30 * dW))
                    : (1.15 * dW - prog * (1.30 * dW));
                const fy = (fl.yBaseFrac * dH) + (0.15 * dH) - prog * (0.30 * dH);
                const tilt = fl.isRight ? -0.17 : 0.17;

                for (let b = 0; b < fl.birds.length; b++) {
                    const bd = fl.birds[b];
                    const bx = fx + bd.xOff;
                    const by = fy + bd.yOff + Math.sin(timeSec * 2.6 + bd.flapPhase) * 6;

                    let popScale = 1, popRot = 0;
                    if (bd.popStart > 0) {
                        const pt = (now - bd.popStart) / 600;
                        if (pt < 1) {
                            popScale = 1 + Math.sin(pt * Math.PI) * 0.65;
                            popRot = Math.sin(pt * Math.PI * 2) * 0.28;
                        } else {
                            bd.popStart = 0;
                        }
                    }

                    bd.lastX = bx;
                    bd.lastY = by;

                    if (bx < -80 || bx > dW + 80 || by < -80 || by > dH + 80) continue;

                    const flap = Math.sin(timeSec * 6.3 + bd.flapPhase) * 0.5 + 0.5;
                    const tipY = -12 + flap * 26;
                    const ctrlY = -8 + flap * 13;

                    bgCtx.save();
                    bgCtx.globalAlpha = 0.55;
                    bgCtx.translate(bx, by);
                    bgCtx.rotate(tilt + popRot);
                    bgCtx.scale(bd.scale * popScale, bd.scale * popScale);
                    bgCtx.strokeStyle = birdColor;
                    bgCtx.lineWidth = 3.2;
                    bgCtx.lineCap = 'round';
                    bgCtx.lineJoin = 'round';
                    bgCtx.beginPath();
                    bgCtx.moveTo(-26, tipY);
                    bgCtx.quadraticCurveTo(-12, ctrlY, 0, 2);
                    bgCtx.quadraticCurveTo(12, ctrlY, 26, tipY);
                    bgCtx.stroke();
                    bgCtx.restore();
                }
            }

            // 3. Foreground Parallax Sprites (1.40x scroll speed)
            const fgWrapH = dH + 220;
            for (let i = 0; i < fgParticles.length; i++) {
                const p = fgParticles[i];
                const rawY = p.yFrac * fgWrapH - scrollY * 1.40;
                const wrappedY = ((rawY % fgWrapH) + fgWrapH) % fgWrapH - 110;
                const y = wrappedY + Math.sin(timeSec * p.floatSpeed + p.phase) * p.floatAmp;
                const x = p.xFrac * dW + Math.cos(timeSec * 0.55 + p.phase) * p.swayAmp;

                let popScale = 1, popRot = 0;
                if (p.popStart > 0) {
                    const pt = (now - p.popStart) / 600;
                    if (pt < 1) {
                        popScale = 1 + Math.sin(pt * Math.PI) * 0.65;
                        popRot = Math.sin(pt * Math.PI * 2) * 0.28;
                    } else {
                        p.popStart = 0;
                    }
                }

                p.lastX = x;
                p.lastY = y;

                const drawSize = (p.sizePx * (112 / 64));
                const flapX = p.type === 'butterfly' ? (0.625 + 0.375 * Math.sin(timeSec * 10.5 + p.flapPhase)) : 1;

                fgCtx.save();
                fgCtx.globalAlpha = p.alpha;
                fgCtx.translate(x, y);
                if (popRot !== 0) fgCtx.rotate(popRot);
                fgCtx.scale(popScale * flapX, popScale);
                fgCtx.drawImage(p.sprite, -drawSize * 0.5, -drawSize * 0.5, drawSize, drawSize);
                fgCtx.restore();
            }

            requestAnimationFrame(renderDecorFrame);
        }

        // ============================================================
        // 4. SCROLL OBSERVER & 1-SECOND POST-DROP BLUR-IN REVEAL
        // ============================================================
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (entry.target.classList.contains('fade-up')) { entry.target.classList.add('visible-up'); }
                    if (entry.target.classList.contains('ink-trigger')) { entry.target.classList.add('visible-ink'); }
                    if (entry.target.classList.contains('type-fade')) {
                        entry.target.classList.add('visible-fade');
                        typeWriterFadeIn(entry.target);
                    }
                }
            });
        }, { threshold: 0.22 });

        function openCurtains() {
            if (isCurtainOpening) return;
            isCurtainOpening = true;
            curtainOpenTime = performance.now();
            curtainWrapper.classList.add('opened');

            setTimeout(() => {
                fitBismillah();
                const mainContent = document.getElementById('main-content');
                mainContent.classList.add('site-revealed');

                bgDecorCanvas.classList.add('decor-revealed');
                fgDecorCanvas.classList.add('decor-revealed');
                if (!decorLoopActive) {
                    decorLoopActive = true;
                    requestAnimationFrame(renderDecorFrame);
                }

                part1Wrapper.querySelectorAll('.obs').forEach(el => observer.observe(el));

                setTimeout(() => {
                    mainContent.style.filter = 'none';
                    mainContent.style.transform = 'none';
                    bgDecorCanvas.style.filter = 'none';
                    fgDecorCanvas.style.filter = 'none';
                }, 1900);
            }, 1000);
        }

        // ============================================================
        // 5. INTERACTIVE TAP / CLICK HANDLER
        // ============================================================
        document.addEventListener('click', function(e) {
            if (!isCurtainOpening) return;

            const target = e.target.closest('.interactive-emoji');
            if (target) {
                target.classList.remove('pop-anim');
                void target.offsetWidth;
                target.classList.add('pop-anim');
                return;
            }

            if (e.target.closest('#scratchCard')) return;

            const cx = e.clientX;
            const cy = e.clientY;
            const now = performance.now();

            for (let i = fgParticles.length - 1; i >= 0; i--) {
                const p = fgParticles[i];
                const dx = cx - p.lastX, dy = cy - p.lastY;
                const rad = Math.max(24, p.sizePx * 0.65);
                if (dx * dx + dy * dy <= rad * rad) {
                    p.popStart = now;
                    return;
                }
            }
            for (let f = 0; f < birdFlocks.length; f++) {
                const birds = birdFlocks[f].birds;
                for (let b = 0; b < birds.length; b++) {
                    const bd = birds[b];
                    const dx = cx - bd.lastX, dy = cy - bd.lastY;
                    if (dx * dx + dy * dy <= 32 * 32) {
                        bd.popStart = now;
                        return;
                    }
                }
            }
            for (let i = bgParticles.length - 1; i >= 0; i--) {
                const p = bgParticles[i];
                const dx = cx - p.lastX, dy = cy - p.lastY;
                const rad = Math.max(22, p.sizePx * 0.7);
                if (dx * dx + dy * dy <= rad * rad) {
                    p.popStart = now;
                    return;
                }
            }
        });

        // ============================================================
        // 6. TYPEWRITER "FADE-IN" LOGIC
        // ============================================================
        function typeWriterFadeIn(el) {
            if(el.dataset.typed) return;
            el.dataset.typed = true;
            let text = el.getAttribute('data-text');
            el.innerHTML = '';
            let chars = text.split('');
            let spans = [];
            chars.forEach(char => {
                if (char === ' ') {
                    el.appendChild(document.createTextNode(' '));
                } else {
                    let span = document.createElement('span');
                    span.textContent = char;
                    span.style.opacity = '0';
                    span.style.transition = 'opacity 0.5s ease-in-out';
                    el.appendChild(span);
                    spans.push(span);
                }
            });
            let i = 0;
            let timer = setInterval(() => {
                if (i < spans.length) { spans[i].style.opacity = '1'; i++; }
                else { clearInterval(timer); }
            }, 30);
        }

        // ============================================================
        // 7. SCRATCH CARD LOGIC (Unlocks Part 2 + Pre-Warms Split Stage!)
        // ============================================================
        const canvas = document.getElementById('scratchCard');
        const ctx = canvas.getContext('2d');
        let isDrawing = false;
        let isRevealed = false;

        ctx.fillStyle = '#a0a0a0';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        ctx.fillStyle = '#ffffff';
        ctx.font = '30px Playfair Display';
        ctx.textAlign = 'center';
        ctx.fillText('Scratch me', canvas.width/2, canvas.height/2 + 10);

        function getMousePos(e) {
            const rect = canvas.getBoundingClientRect();
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;

            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;

            return {
                x: (clientX - rect.left) * scaleX,
                y: (clientY - rect.top) * scaleY
            };
        }

        function scratch(e) {
            if (!isDrawing || isRevealed) return;
            e.preventDefault();
            const pos = getMousePos(e);
            ctx.globalCompositeOperation = 'destination-out';
            ctx.beginPath();
            ctx.arc(pos.x, pos.y, 25, 0, Math.PI * 2);
            ctx.fill();
            checkReveal();
        }

        canvas.addEventListener('mousedown', () => isDrawing = true);
        canvas.addEventListener('mousemove', scratch);
        canvas.addEventListener('mouseup', () => isDrawing = false);
        canvas.addEventListener('mouseleave', () => isDrawing = false);
        canvas.addEventListener('touchstart', (e) => { isDrawing = true; scratch(e); });
        canvas.addEventListener('touchmove', scratch);
        canvas.addEventListener('touchend', () => isDrawing = false);

        function unlockRestOfInvitation() {
            if (splitPrepared) return;
            buildSplitClones();
            part2Section.style.display = 'block';
            splitPrepared = true;
            syncSplitMetrics();

            // Pre-warm splitStage on GPU immediately so frame 1 of scroll has 0ms stutter!
            splitStage.style.display = 'block';
            splitStage.style.zIndex = '19';
            splitStage.style.opacity = '0.001';

            document.getElementById('unlock-hint').classList.add('active');
            part2Section.querySelectorAll('.obs').forEach(el => observer.observe(el));
        }

        function checkReveal() {
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            let transparentPixels = 0;
            const totalPixels = imageData.data.length / 4;

            for (let i = 3; i < imageData.data.length; i += 40) {
                if (imageData.data[i] === 0) transparentPixels++;
            }

            if (transparentPixels / (totalPixels/10) > 0.30 && !isRevealed) {
                isRevealed = true;
                canvas.style.transition = 'opacity 0.8s ease-out, filter 0.8s ease-out';
                canvas.style.opacity = 0;
                canvas.style.filter = 'blur(10px)';
                setTimeout(() => canvas.style.display = 'none', 800);

                unlockRestOfInvitation();
                fireSideCannon('left');
                fireSideCannon('right');
                spawnExplosionFlock();
            }
        }

        // ============================================================
        // 8. CUSTOM SIDE-CANNONS (Left & Right Bottom Screen)
        // ============================================================
        function fireSideCannon(side) {
            const container = document.createElement('div');
            container.style.position = 'fixed';
            container.style[side] = '-20px';
            container.style.bottom = '10%';
            container.style.zIndex = '1000';
            container.style.pointerEvents = 'none';
            document.body.appendChild(container);

            const particleCount = isMobile ? 40 : 80;

            for (let i = 0; i < particleCount; i++) {
                let p = document.createElement('div');
                p.style.position = 'absolute';

                let randomSize = Math.random() * 1.5 + 1.2;
                let randomColor = weddingColors[Math.floor(Math.random() * weddingColors.length)];
                p.innerHTML = generateSvgGraphic(randomSize, randomColor);

                let angleDeg = side === 'left' ? -(Math.random() * 50 + 20) : -(Math.random() * 50 + 110);
                let angle = angleDeg * (Math.PI / 180);

                let velocity = Math.random() * 1000 + 400;
                let tx = Math.cos(angle) * velocity;
                let ty = Math.sin(angle) * velocity;
                let rot = (Math.random() - 0.5) * 720;
                let delay = Math.random() * 2000;

                p.animate([
                    { transform: `translate(0px, 0px) scale(0) rotate(0deg)`, opacity: 0 },
                    { transform: `translate(0px, 0px) scale(0.5) rotate(0deg)`, opacity: 1, offset: 0.05 },
                    { transform: `translate(${tx * 0.8}px, ${ty * 0.8}px) scale(1) rotate(${rot/2}deg)`, opacity: 1, offset: 0.25 },
                    { transform: `translate(${tx * 1.5}px, ${window.innerHeight + 1000}px) scale(0.6) rotate(${rot}deg)`, opacity: 0 }
                ], {
                    duration: Math.random() * 5000 + 10000,
                    delay: delay,
                    easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
                    fill: 'forwards'
                });

                container.appendChild(p);
            }
            setTimeout(() => container.remove(), 17000);
        }

        // ============================================================
        // 9. SLOW-MOTION CINEMATIC FLOCK OF BIRDS (15-20 Seconds)
        // ============================================================
        function spawnExplosionFlock() {
            const flockContainer = document.createElement('div');
            flockContainer.style.position = 'fixed';
            flockContainer.style.left = '50%';
            flockContainer.style.top = '50%';
            flockContainer.style.transform = 'translate(-50%, -50%)';
            flockContainer.style.zIndex = '1000';
            flockContainer.style.pointerEvents = 'none';
            document.body.appendChild(flockContainer);

            const birdCount = isMobile ? 25 : 45;
            for (let i = 0; i < birdCount; i++) {
                let bird = document.createElement('div');
                bird.style.position = 'absolute';

                let flapDelay = '-' + (Math.random() * 0.5).toFixed(2) + 's';
                bird.innerHTML = `
                    <svg class="bird-svg" viewBox="0 0 100 60" width="${Math.random() * 15 + 30}" height="20">
                        <path class="bird-wing" style="animation-delay: ${flapDelay};" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d="M 5 10 Q 30 15 50 30 Q 70 15 95 10" />
                    </svg>`;

                let tx = (Math.random() - 0.5) * window.innerWidth * 2.5;
                let ty = - (Math.random() * window.innerHeight * 1.5 + 400);
                let rot = (Math.random() - 0.5) * 40;
                let delay = Math.random() * 2000;

                bird.animate([
                    { transform: `translate(0px, 0px) scale(0) rotate(0deg)`, opacity: 0 },
                    { transform: `translate(0px, 0px) scale(0.2) rotate(0deg)`, opacity: 1, offset: 0.05 },
                    { transform: `translate(${tx}px, ${ty}px) scale(1.5) rotate(${rot}deg)`, opacity: 0 }
                ], {
                    duration: Math.random() * 5000 + 15000,
                    delay: delay,
                    easing: 'ease-out',
                    fill: 'forwards'
                });

                flockContainer.appendChild(bird);
            }
            setTimeout(() => flockContainer.remove(), 25000);
        }
    </script>
</body>
</html>
"""

components.html(html_content, scrolling=True)
