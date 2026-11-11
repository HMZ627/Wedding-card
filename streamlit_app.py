import streamlit as st
import streamlit.components.v1 as components

# Configure the page setting
st.set_page_config(
    page_title="Wedding Invitation - Asad & Rimsha",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit's native header, footer and padding for a seamless full-screen app
st.markdown(
    """
    <style>
        .block-container { padding: 0rem !important; }
        header { visibility: hidden !important; }
        footer { visibility: hidden !important; }
        #MainMenu { visibility: hidden !important; }
        iframe {
            height: 100vh !important;
            width: 100vw !important;
            border: none !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# HTML, CSS, JS payload with all animations, scratch card, curtain logic & interactive elements
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Invitation</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <style>
        /* --- Base & Background --- */
        body {
            margin: 0; padding: 0;
            font-family: 'Playfair Display', serif;
            background-color: #f7ecd3; 
            background-image: url('https://www.transparenttextures.com/patterns/aged-paper.png'); 
            color: #4a3b32;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* --- Silky Curtain Animation --- */
        #curtain-wrapper {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: 9999; display: flex; 
        }
        .curtain {
            width: 50%; height: 100%;
            background: linear-gradient(to right, #500000 0%, #800000 20%, #b30000 50%, #800000 80%, #500000 100%);
            box-shadow: 0 0 20px rgba(0,0,0,0.7);
            /* Complex bezier curve to mimic pulling and gathering of heavy cloth */
            transition: transform 2.5s cubic-bezier(0.64, 0.04, 0.35, 1), 
                        border-radius 2.5s ease-in-out, 
                        box-shadow 2.5s ease;
            position: relative;
            will-change: transform, border-radius;
        }
        .curtain-left { border-right: 4px solid #d4af37; transform-origin: top left; }
        .curtain-right { border-left: 4px solid #d4af37; transform-origin: top right; }
        
        .open-btn {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: #f4f1ea; color: #800000;
            padding: 20px 50px; font-size: 35px; cursor: pointer;
            border-radius: 10px; border: 2px solid #d4af37;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            z-index: 10000; font-family: 'Great Vibes', cursive;
            transition: opacity 0.5s, transform 0.3s;
            -webkit-tap-highlight-color: transparent;
        }
        .open-btn:hover { transform: translate(-50%, -50%) scale(1.1); }
        
        /* The Silky Drop & Gather geometry triggered on click */
        #curtain-wrapper.opened {
            opacity: 0;
            pointer-events: none;
            transition: opacity 1s ease 1.8s; /* Fade whole layer smoothly out at the end */
        }
        #curtain-wrapper.opened .open-btn { opacity: 0; pointer-events: none; transform: translate(-50%, -50%) scale(0.5); }
        
        #curtain-wrapper.opened .curtain-left { 
            /* Shrinks dramatically to side, drops down 15%, swings out -5deg */
            transform: scaleX(0.12) translateY(15%) rotateZ(-5deg); 
            border-bottom-right-radius: 80% 50%; /* Rounds the gathered corner */
            box-shadow: inset -50px 0 50px rgba(0,0,0,0.8); /* Deep shadow simulates folds */
        }
        #curtain-wrapper.opened .curtain-right { 
            transform: scaleX(0.12) translateY(15%) rotateZ(5deg); 
            border-bottom-left-radius: 80% 50%;
            box-shadow: inset 50px 0 50px rgba(0,0,0,0.8);
        }

        /* --- Main Content --- */
        .content { min-height: 100vh; padding: 10vh 20px; text-align: center; overflow-x: hidden; position: relative; z-index: 10; }
        
        /* Bismillah Dynamic Auto-Scaler */
        .bismillah { 
            font-family: 'Amiri', serif; 
            /* Clamp prevents it from ever being larger than the screen */
            font-size: clamp(2rem, 15vw, 4.5rem); 
            margin-bottom: 20vh; 
            opacity: 0; 
            transform: translateY(30px); 
            transition: all 1.5s ease-out; 
            line-height: 1.2;
            white-space: nowrap; 
        }
        
        /* Type-in Fade-in */
        .type-fade { 
            font-size: 2.2rem; 
            margin: 0 auto 20vh auto; 
            max-width: 800px; 
            padding: 0 15px;
            line-height: 1.5;
            opacity: 0; 
            transition: opacity 1.5s ease-in; 
            min-height: 80px;
        }
        
        /* --- Ink Spread Section --- */
        .ink-spread-anim { 
            clip-path: circle(0% at center); 
            filter: blur(20px); 
            opacity: 0; 
            transition: clip-path 2.5s cubic-bezier(0.25, 1, 0.5, 1), filter 2.5s ease-out, opacity 1.5s ease-in; 
            padding: 20px 0;
            will-change: clip-path, filter;
        }
        .sub-header-text { font-size: 2rem; position: relative; }
        
        .invite-word { font-size: 6rem; display: block; text-align: center; font-family: 'Great Vibes', cursive; margin: 20px 0; color: #4a3b32; line-height: 1; }
        .wedding-word { color: #ff033e; font-weight: bold; font-style: italic; }
        
        /* --- Detailed Blooming Garden Sequence --- */
        .garden-container { display: flex; justify-content: center; gap: 100px; margin-top: 30px; height: 130px; }
        .plant { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .flower { font-size: 6rem; display: flex; align-items: center; justify-content: center; }
        .butterfly { font-size: 3rem; position: absolute; bottom: 20px; opacity: 0; transition: all 1.5s ease-in-out; z-index: 10; will-change: transform; }

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
        .scratch-wrapper { margin: 0 auto 20vh auto; display: flex; justify-content: center; opacity: 0; transform: translateY(30px); transition: all 1.5s ease-out; }
        .scratch-scaler { transform: scale(1); transition: transform 0.3s; }
        .scratch-container {
            position: relative; width: 320px; height: 320px;
            clip-path: path("M 160,90 C 160,90 110,0 20,50 C -50,120 160,300 160,300 C 160,300 370,120 300,50 C 210,0 160,90 160,90 Z");
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }
        .scratch-bg { width: 100%; height: 100%; background: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        .heart-text { font-family: 'Great Vibes', cursive; color: #b30000; font-size: 2.6rem; line-height: 1.1; text-align: center; margin-top: 25px; }
        canvas { position: absolute; top: 0; left: 0; z-index: 10; cursor: pointer; touch-action: none; }

        /* --- Schedule Table --- */
        .schedule-box { max-width: 800px; margin: 0 auto 20vh auto; opacity: 0; transform: translateY(50px); transition: all 1.5s; background: rgba(255,255,255,0.4); padding: 30px; border-radius: 15px; border: 2px dashed #bba171; overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; min-width: 400px; }
        th, td { padding: 15px; text-align: center; border-bottom: 1px solid #d8ccb8; }
        th { font-family: 'Great Vibes', cursive; font-size: 2rem; color: #800000; border-bottom: 2px solid #bba171; }
        td { font-size: 1.2rem; }

        /* --- Footer --- */
        .footer-text { font-size: 1.5rem; opacity: 0; transform: translateY(50px); transition: all 1.5s; padding-bottom: 100px; font-style: italic; color: #800000; font-weight: bold;}

        /* --- Interactive Trigger Class --- */
        .interactive-emoji { display: inline-block; cursor: pointer; user-select: none; -webkit-tap-highlight-color: transparent; will-change: transform; }
        .pop-anim { animation: clickPop 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; }
        @keyframes clickPop {
            0% { transform: scale(1) rotate(0deg); filter: brightness(1); }
            30% { transform: scale(1.6) rotate(15deg); filter: brightness(1.2); }
            70% { transform: scale(1.6) rotate(-15deg); filter: brightness(1.2); }
            100% { transform: scale(1) rotate(0deg); filter: brightness(1); }
        }

        /* --- Custom Graphic Animations (Butterflies Flapping) --- */
        .bf-flap-anim { animation: bfWing 0.3s infinite alternate ease-in-out; transform-origin: 16px 16px; will-change: transform; }
        @keyframes bfWing { 0% { transform: scaleX(1); } 100% { transform: scaleX(0.25); } }

        /* --- Parallax & Float Elements --- */
        .bg-deco { animation: floatDeco 6s infinite ease-in-out alternate; will-change: transform; }
        .fg-deco { animation: floatDeco 8s infinite ease-in-out alternate-reverse; will-change: transform; }
        @keyframes floatDeco { 0% { transform: translateY(0px); } 100% { transform: translateY(-25px); } }
        
        /* --- Drawn Pencil Birds in Flocks --- */
        .bird-flock { position: fixed; z-index: 1; pointer-events: none; opacity: 0.55; will-change: transform; }
        .bird-flock .interactive-emoji { pointer-events: auto; }
        .bird-svg { overflow: visible; animation: birdBob 1.2s infinite ease-in-out alternate; }
        .bird-wing { animation: birdFlap 0.5s infinite ease-in-out alternate; } 
        @keyframes birdBob { 0% { transform: translateY(0px); } 100% { transform: translateY(12px); } }
        @keyframes birdFlap {
            0%   { d: path("M 5 10 Q 30 15 50 30 Q 70 15 95 10"); } 
            100% { d: path("M 5 50 Q 30 35 50 30 Q 70 35 95 50"); } 
        }
        @keyframes flyRight { 0% { transform: translateX(-15vw) translateY(15vh); } 100% { transform: translateX(115vw) translateY(-15vh); } }
        @keyframes flyLeft { 0% { transform: translateX(115vw) translateY(15vh); } 100% { transform: translateX(-15vw) translateY(-15vh); } }

        .visible-up { opacity: 1 !important; transform: translateY(0) !important; }
        .visible-fade { opacity: 1 !important; }

        /* =========================================
           MOBILE RESPONSIVENESS
           ========================================= */
        @media (max-width: 768px) {
            .type-fade { font-size: 1.5rem !important; margin-bottom: 15vh; }
            .sub-header-text { font-size: 1.5rem; }
            .invite-word { font-size: 4rem; margin: 15px 0; }
            .flower { font-size: 4.5rem; }
            .butterfly { font-size: 2.2rem; }
            .garden-container { gap: 40px; height: 100px; }
            
            /* Scaling down the entire Scratch mechanism natively */
            .scratch-scaler { transform: scale(0.85); }
            .scratch-wrapper { margin: 0 auto 15vh auto; }
            
            /* Table Adjustments */
            .schedule-box { padding: 15px; margin-bottom: 15vh; }
            th { font-size: 1.5rem; padding: 10px; }
            td { font-size: 1rem; padding: 10px; }
            
            .footer-text { font-size: 1.2rem; }
            .open-btn { font-size: 26px; padding: 15px 35px; }
        }

        @media (max-width: 480px) {
            .type-fade { font-size: 1.3rem !important; }
            .invite-word { font-size: 3.5rem; }
            .scratch-scaler { transform: scale(0.75); } 
            .garden-container { gap: 20px; }
        }
    </style>
</head>
<body>

    <!-- MASTER SVG DEFINITIONS -->
    <svg width="0" height="0" style="position:absolute; pointer-events: none;">
      <defs>
        <path id="svg-heart" d="M16 28.5C16 28.5 4 20 4 10C4 5.6 7.6 2 12 2C14.4 2 16 3.6 16 3.6C16 3.6 17.6 2 20 2C24.4 2 28 5.6 28 10C28 20 16 28.5 16 28.5Z"/>
        
        <!-- Highly Detailed 3-Layer Botanical Flower -->
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

    <!-- Red Curtains -->
    <div id="curtain-wrapper">
       <div class="curtain curtain-left"></div>
       <div class="curtain curtain-right"></div>
       <div class="open-btn" onclick="openCurtains()">Open</div>
    </div>

    <!-- Website Content -->
    <div class="content" id="main-content">
       
       <div class="bismillah obs fade-up">﷽</div>

       <div class="header-text obs type-fade" data-text="Starting with the name of Allah, The most Beneficial and The most Merciful."></div>

       <div class="obs ink-trigger" style="min-height: 300px; margin-bottom: 15vh; display: flex; align-items: center; justify-content: center;">
           <div class="ink-spread-anim">
               <div class="sub-header-text">
                   We are pleased to
                   <span class="invite-word">Invite</span>
                   you to the <span class="wedding-word">Wedding</span> ceremony
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

       <!-- Wrapped Container for Mobile Scaling -->
       <div class="scratch-wrapper obs fade-up">
           <div class="scratch-scaler">
               <div class="scratch-container">
                   <div class="scratch-bg">
                       <div class="heart-text">
                           Asad <br>
                           <span style="font-size: 1.8rem;">&</span><br>
                           Rimsha
                       </div>
                   </div>
                   <canvas id="scratchCard" width="320" height="320"></canvas>
               </div>
           </div>
       </div>

       <div class="header-text obs type-fade" data-text="Show your kind love by participating in the event"></div>

       <div class="schedule-box obs fade-up">
           <table>
               <tr><th>Event</th><th>Date</th><th>Time</th><th>Location</th></tr>
               <tr>
                   <td><b>MEHNDI</b></td>
                   <td>24-12-2026</td>
                   <td>6:00 PM</td>
                   <td>Farid Town Sahiwal</td>
               </tr>
               <tr>
                   <td><b>BARAAT</b></td>
                   <td>25-12-2026</td>
                   <td>10:00 AM</td>
                   <td>Grand Al-Noor Marraige Hall (JTS)<br><span style="font-size: 0.9rem; color: #666;">(Near Faridia Park, Tariq Bin Ziad colony)</span></td>
               </tr>
           </table>
       </div>

       <div class="footer-text obs fade-up">
           May Allah Bless you and your family with Rehmaat and Barakaat
       </div>
    </div>

    <script>
        // 1. Curtain Drop Animation
        function openCurtains() {
            const wrapper = document.getElementById('curtain-wrapper');
            wrapper.classList.add('opened');
            setTimeout(() => { wrapper.style.display = 'none'; }, 3000);
        }

        const content = document.getElementById('main-content');
        const shapeTypes = ['heart', 'flower', 'butterfly', 'sparkle'];
        const weddingColors = ['#ff033e', '#ffb6c1', '#d4af37', '#e6a8d7', '#ffdab9', '#ffffff', '#ffd700'];
        
        function generateSvgGraphic(sizeRem, color) {
            let type = shapeTypes[Math.floor(Math.random() * shapeTypes.length)];
            return `<svg viewBox="0 0 32 32" width="${sizeRem}rem" height="${sizeRem}rem" fill="${color}" style="pointer-events: none;"><use href="#svg-${type}" /></svg>`;
        }

        // Detect Mobile for slight performance density scaling
        const isMobile = window.innerWidth <= 768;
        const bgCount = isMobile ? 30 : 60;
        const fgCount = isMobile ? 12 : 25;

        // A) Parallax Background SVG Decor
        for(let i=0; i<bgCount; i++) {
            let wrapper = document.createElement('div');
            wrapper.className = 'parallax-bg-wrapper';
            wrapper.style.position = 'absolute';
            wrapper.style.left = Math.random() * 95 + 'vw';
            wrapper.style.top = Math.random() * 100 + '%'; 
            wrapper.style.zIndex = '0'; 

            let el = document.createElement('div');
            el.className = 'bg-deco';
            el.style.animationDelay = (Math.random() * 3) + 's';
            
            let inner = document.createElement('span');
            inner.className = 'interactive-emoji';
            let randomSize = Math.random() * 1.5 + 1; 
            let randomColor = weddingColors[Math.floor(Math.random() * weddingColors.length)];
            
            inner.innerHTML = generateSvgGraphic(randomSize, randomColor);
            
            // Reduced Blur
            inner.style.filter = 'blur(1.5px)'; 
            inner.style.opacity = '0.55';
            
            el.appendChild(inner);
            wrapper.appendChild(el);
            content.appendChild(wrapper);
        }

        // B) Parallax Foreground SVG Decor
        for(let i=0; i<fgCount; i++) {
            let wrapper = document.createElement('div');
            wrapper.className = 'parallax-fg-wrapper';
            wrapper.style.position = 'absolute';
            wrapper.style.left = Math.random() * 95 + 'vw';
            wrapper.style.top = Math.random() * 100 + '%';
            wrapper.style.zIndex = '50'; 
            wrapper.style.pointerEvents = 'none'; 

            let el = document.createElement('div');
            el.className = 'fg-deco';
            el.style.animationDelay = (Math.random() * 3) + 's';
            
            let inner = document.createElement('span');
            inner.className = 'interactive-emoji';
            let randomSize = Math.random() * 2 + 2.5; 
            let randomColor = weddingColors[Math.floor(Math.random() * weddingColors.length)];
            
            inner.innerHTML = generateSvgGraphic(randomSize, randomColor);
            
            inner.style.filter = 'blur(3px)'; 
            inner.style.opacity = '0.65';
            inner.style.pointerEvents = 'auto'; 
            
            el.appendChild(inner);
            wrapper.appendChild(el);
            content.appendChild(wrapper);
        }

        // C) Organized Bird Flocks with V-formation geometry
        const numFlocks = isMobile ? 3 : 5;
        for(let f = 0; f < numFlocks; f++) {
            let flockWrapper = document.createElement('div');
            flockWrapper.className = 'bird-flock';
            
            let isRight = Math.random() > 0.5;
            let animName = isRight ? 'flyRight' : 'flyLeft';
            let animDuration = Math.random() * 25 + 30; 
            
            flockWrapper.style.animation = `${animName} ${animDuration}s linear infinite`;
            flockWrapper.style.animationDelay = '-' + (Math.random() * 25) + 's';
            flockWrapper.style.top = (Math.random() * 65 + 10) + 'vh'; 
            
            let birdsInFlock = Math.floor(Math.random() * 3) + 3; 
            
            for(let b = 0; b < birdsInFlock; b++) {
                let birdNode = document.createElement('div');
                birdNode.style.position = 'absolute';
                
                let xOffset = isRight ? -(b * 35 + Math.random()*10) : (b * 35 + Math.random()*10);
                let yOffset = (b % 2 === 0 ? 1 : -1) * (Math.ceil(b/2) * 20) + (Math.random()*10 - 5);
                
                birdNode.style.left = xOffset + 'px';
                birdNode.style.top = yOffset + 'px';
                
                let inner = document.createElement('div');
                inner.className = 'interactive-emoji';
                let tilt = isRight ? 'rotate(-10deg)' : 'rotate(10deg)';
                inner.style.transform = tilt;
                
                let flapDelay = '-' + (Math.random() * 0.5).toFixed(2) + 's';
                
                inner.innerHTML = `
                <svg class="bird-svg" viewBox="0 0 100 60" width="${Math.random() * 15 + 30}" height="25" style="pointer-events:none;">
                    <path class="bird-wing" style="animation-delay: ${flapDelay};" fill="none" stroke="#4a3b32" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" d="M 5 10 Q 30 15 50 30 Q 70 15 95 10" />
                </svg>`;
                
                birdNode.appendChild(inner);
                flockWrapper.appendChild(birdNode);
            }
            document.body.appendChild(flockWrapper);
        }

        // 3. Parallax Scroll Math Integration
        window.addEventListener('scroll', () => {
            const scrollY = window.scrollY;
            
            document.querySelectorAll('.parallax-bg-wrapper').forEach(el => {
                el.style.transform = `translateY(${scrollY * 0.85}px)`; 
            });
            document.querySelectorAll('.parallax-fg-wrapper').forEach(el => {
                el.style.transform = `translateY(${-scrollY * 0.4}px)`; 
            });
        });

        // 4. Interactive Click/Tap Event Listener
        document.addEventListener('click', function(e) {
            const target = e.target.closest('.interactive-emoji');
            if(target) {
                target.classList.remove('pop-anim');
                void target.offsetWidth; 
                target.classList.add('pop-anim');
            }
        });

        // 5. Scroll Interactions
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if(entry.target.classList.contains('fade-up')) { entry.target.classList.add('visible-up'); }
                    if(entry.target.classList.contains('ink-trigger')) { entry.target.classList.add('visible-ink'); }
                    if(entry.target.classList.contains('type-fade')) {
                        entry.target.classList.add('visible-fade');
                        typeWriterFadeIn(entry.target);
                    }
                }
            });
        }, { threshold: 0.25 });
        document.querySelectorAll('.obs').forEach(el => observer.observe(el));

        // 6. Typewriter "Fade-In" Logic
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

        // 7. Scratch Card Logic (Threshold 30% + Mobile Scaler Fix)
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
            // Critical math: accounts for mobile CSS transform: scale() shrinking the element
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
        // Mobile touch events natively mapped
        canvas.addEventListener('touchstart', (e) => { isDrawing = true; scratch(e); });
        canvas.addEventListener('touchmove', scratch);
        canvas.addEventListener('touchend', () => isDrawing = false);

        function checkReveal() {
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            let transparentPixels = 0;
            const totalPixels = imageData.data.length / 4;
            
            for (let i = 3; i < imageData.data.length; i += 40) {
                if (imageData.data[i] === 0) transparentPixels++;
            }
            
            if (transparentPixels / (totalPixels/10) > 0.30 && !isRevealed) {
                isRevealed = true;
                canvas.style.transition = 'opacity 0.8s';
                canvas.style.opacity = 0;
                setTimeout(() => canvas.style.display = 'none', 800);
                
                // Trigger 15-20s Cinematic Explosion!
                fireSideCannon('left');
                fireSideCannon('right');
                spawnExplosionFlock();
            }
        }

        // 8. Custom Side-Cannons (Fires dynamically from Left/Right bottom screen)
        function fireSideCannon(side) {
            const container = document.createElement('div');
            container.style.position = 'fixed';
            // True side anchors
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
                
                // Calculates shooting arc: Right cannons shoot left-up, Left cannons shoot right-up
                let angleDeg = side === 'left' ? -(Math.random() * 50 + 20) : -(Math.random() * 50 + 110);
                let angle = angleDeg * (Math.PI / 180);
                
                let velocity = Math.random() * 1000 + 400; 
                let tx = Math.cos(angle) * velocity;
                let ty = Math.sin(angle) * velocity; 
                let rot = (Math.random() - 0.5) * 720; 

                // Micro-delays stream the particles gracefully over 2 seconds
                let delay = Math.random() * 2000; 

                p.animate([
                    { transform: `translate(0px, 0px) scale(0) rotate(0deg)`, opacity: 0 },
                    { transform: `translate(0px, 0px) scale(0.5) rotate(0deg)`, opacity: 1, offset: 0.05 },
                    { transform: `translate(${tx * 0.8}px, ${ty * 0.8}px) scale(1) rotate(${rot/2}deg)`, opacity: 1, offset: 0.25 }, 
                    { transform: `translate(${tx * 1.5}px, ${window.innerHeight + 1000}px) scale(0.6) rotate(${rot}deg)`, opacity: 0 } // Very Long Fall
                ], {
                    duration: Math.random() * 5000 + 10000, // 10 to 15 seconds duration
                    delay: delay,
                    easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
                    fill: 'forwards'
                });

                container.appendChild(p);
            }
            setTimeout(() => container.remove(), 17000); 
        }

        // 9. Slow-Motion Cinematic Flock of Birds (15-20 Seconds)
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
                
                // Long, slow, epic flight path
                let tx = (Math.random() - 0.5) * window.innerWidth * 2.5;
                let ty = - (Math.random() * window.innerHeight * 1.5 + 400); 
                let rot = (Math.random() - 0.5) * 40; 
                let delay = Math.random() * 2000; 

                bird.animate([
                    { transform: `translate(0px, 0px) scale(0) rotate(0deg)`, opacity: 0 },
                    { transform: `translate(0px, 0px) scale(0.2) rotate(0deg)`, opacity: 1, offset: 0.05 },
                    { transform: `translate(${tx}px, ${ty}px) scale(1.5) rotate(${rot}deg)`, opacity: 0 }
                ], {
                    // INCREASED DURATION TO 15 TO 20 SECONDS!
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
