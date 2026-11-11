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

# HTML, CSS, JS payload with all animations, scratch card & curtain logic
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invitation</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
    <style>
        /* --- Base & Background --- */
        body {
            margin: 0; padding: 0;
            font-family: 'Playfair Display', serif;
            background-color: #f7ecd3; /* Off-white */
            background-image: url('https://www.transparenttextures.com/patterns/aged-paper.png'); /* Brown marks old paper */
            color: #4a3b32;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        /* --- Curtain Animation --- */
        #curtain-wrapper {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: 9999; display: flex; transition: opacity 2s ease;
        }
        .curtain {
            width: 50%; height: 100%;
            background: linear-gradient(to right, #500000 0%, #800000 20%, #b30000 50%, #800000 80%, #500000 100%);
            box-shadow: 0 0 20px rgba(0,0,0,0.7);
            transition: transform 2.5s cubic-bezier(0.8, 0, 0.2, 1);
            position: relative;
        }
        .curtain-left { border-right: 4px solid #d4af37; }
        .curtain-right { border-left: 4px solid #d4af37; }
        
        .open-btn {
            position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
            background: #f4f1ea; color: #800000;
            padding: 20px 50px; font-size: 35px; cursor: pointer;
            border-radius: 10px; border: 2px solid #d4af37;
            box-shadow: 0 5px 15px rgba(0,0,0,0.5);
            z-index: 10000; font-family: 'Great Vibes', cursive;
            transition: opacity 0.5s, transform 0.3s;
        }
        .open-btn:hover { transform: translate(-50%, -50%) scale(1.1); }
        
        /* Triggered Classes for Curtains */
        #curtain-wrapper.opened .curtain-left { transform: translateX(-100%); }
        #curtain-wrapper.opened .curtain-right { transform: translateX(100%); }
        #curtain-wrapper.opened .open-btn { opacity: 0; pointer-events: none; }

        /* --- Main Content --- */
        .content { min-height: 100vh; padding: 100px 20px; text-align: center; overflow-x: hidden; position: relative; }
        
        /* Bismillah */
        .bismillah { font-family: 'Amiri', serif; font-size: 4.5rem; margin-bottom: 25vh; opacity: 0; transform: translateY(30px); transition: all 1.5s ease-out; }
        
        /* Type-in Fade-in */
        .type-fade { font-size: 2rem; margin: 0 auto 25vh auto; max-width: 800px; opacity: 0; transition: opacity 1.5s ease-in; min-height: 80px;}
        
        /* --- UPDATED: Ink Spread & Invitation Section --- */
        .ink-spread-anim { 
            margin-bottom: 25vh; 
            clip-path: circle(0% at center); 
            filter: blur(20px); 
            opacity: 0; 
            transition: clip-path 2.5s cubic-bezier(0.25, 1, 0.5, 1), filter 2.5s ease-out, opacity 1.5s ease-in; 
        }
        .sub-header-text { font-size: 2rem; position: relative; }
        
        /* Isolated, Large Invite Word */
        .invite-word { 
            font-size: 6rem; /* Very Large */
            display: block; 
            text-align: center;
            font-family: 'Great Vibes', cursive; 
            margin: 30px 0; 
            color: #4a3b32; 
        }
        
        /* Rose-Red Wedding Word */
        .wedding-word { color: #ff033e; font-weight: bold; font-style: italic; }
        
        /* 2 Blooming Flowers & Hovering Butterflies */
        .garden-container { display: flex; justify-content: center; gap: 100px; margin-top: 40px; height: 120px; }
        .plant { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        
        .flower { 
            font-size: 4.5rem; 
            transform: scale(0); /* Starts hidden */
            transition: transform 1.5s cubic-bezier(0.68, -0.55, 0.27, 1.55); 
        }
        .butterfly { 
            font-size: 2.5rem; 
            position: absolute; 
            bottom: 20px; /* Starts inside flower */
            opacity: 0; 
            transition: all 1.5s ease-in-out; 
        }

        /* Triggered animations when ink spread appears */
        .visible-ink { opacity: 1 !important; clip-path: circle(150% at center) !important; filter: blur(0px) !important; }
        
        /* 1st Bloom the flowers */
        .visible-ink .flower { 
            transform: scale(1); 
            animation: continuousBloom 3s infinite alternate ease-in-out 1.5s; /* Wait for scale transition, then continuous */
        }
        
        /* 2nd Fly the butterflies up out of the flowers */
        .visible-ink .butterfly { 
            bottom: 90px; /* Fly up above flower */
            opacity: 1; 
            transition-delay: 1.2s; /* Wait for flower to bloom first */
            animation: hoverfly 2.5s infinite ease-in-out alternate 2.7s; /* Start hovering after fly-up */
        }
        
        /* Asynchronous delay for right plant so they don't look robotic */
        .plant.delayed .flower { transition-delay: 0.4s; }
        .plant.delayed .butterfly { transition-delay: 1.6s; animation-delay: 3.1s; }

        @keyframes continuousBloom { 
            0% { transform: scale(1) rotate(-5deg); } 
            100% { transform: scale(1.15) rotate(5deg); } 
        }
        @keyframes hoverfly { 
            0% { transform: translateY(0) translateX(0) rotate(-10deg); } 
            100% { transform: translateY(-15px) translateX(15px) rotate(15deg); } 
        }

        /* --- Scratch Card --- */
        .scratch-wrapper { margin: 0 auto 25vh auto; display: flex; justify-content: center; opacity: 0; transform: translateY(30px); transition: all 1.5s ease-out; }
        .scratch-container {
            position: relative; width: 320px; height: 320px;
            clip-path: path("M 160,90 C 160,90 110,0 20,50 C -50,120 160,300 160,300 C 160,300 370,120 300,50 C 210,0 160,90 160,90 Z");
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }
        .scratch-bg { width: 100%; height: 100%; background: #fff; display: flex; flex-direction: column; justify-content: center; align-items: center; font-family: 'Great Vibes', cursive; font-size: 3.5rem; color: #b30000; }
        canvas { position: absolute; top: 0; left: 0; z-index: 10; cursor: pointer; touch-action: none; }

        /* --- Schedule Table --- */
        .schedule-box { max-width: 800px; margin: 0 auto 25vh auto; opacity: 0; transform: translateY(50px); transition: all 1.5s; background: rgba(255,255,255,0.4); padding: 30px; border-radius: 15px; border: 2px dashed #bba171; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 15px; text-align: center; border-bottom: 1px solid #d8ccb8; }
        th { font-family: 'Great Vibes', cursive; font-size: 2rem; color: #800000; border-bottom: 2px solid #bba171; }
        td { font-size: 1.2rem; }

        /* --- Footer --- */
        .footer-text { font-size: 1.5rem; opacity: 0; transform: translateY(50px); transition: all 1.5s; padding-bottom: 100px; font-style: italic; color: #800000; font-weight: bold;}

        /* --- Background Decorations --- */
        .bg-deco { position: absolute; opacity: 0.3; z-index: -1; animation: floatDeco 6s infinite ease-in-out alternate; }
        @keyframes floatDeco { 0% { transform: translateY(0); } 100% { transform: translateY(-20px); } }

        /* Animation Triggers */
        .visible-up { opacity: 1 !important; transform: translateY(0) !important; }
        .visible-fade { opacity: 1 !important; }
    </style>
</head>
<body>

    <!-- Red Curtains -->
    <div id="curtain-wrapper">
       <div class="curtain curtain-left"></div>
       <div class="curtain curtain-right"></div>
       <div class="open-btn" onclick="openCurtains()">Open</div>
    </div>

    <!-- Website Content -->
    <div class="content" id="main-content">
       
       <!-- Calligraphy -->
       <div class="bismillah obs fade-up">﷽</div>

       <!-- Typewriter Header -->
       <div class="header-text obs type-fade" data-text="Starting with the name of Allah, The most Beneficial and The most Merciful."></div>

       <!-- UPDATED: Ink Spread Sub-header with blooming garden -->
       <div class="ink-spread-anim obs ink-trigger">
           <div class="sub-header-text">
               We are pleased to
               <span class="invite-word">Invite</span>
               you to the <span class="wedding-word">Wedding</span> ceremony
           </div>
           
           <!-- The 2 blooming flowers with butterflies -->
           <div class="garden-container">
               <div class="plant">
                   <div class="butterfly">🦋</div>
                   <div class="flower">🌸</div>
               </div>
               <div class="plant delayed">
                   <div class="butterfly">🦋</div>
                   <div class="flower">🌺</div>
               </div>
           </div>
       </div>

       <!-- Scratchable Heart Space -->
       <div class="scratch-wrapper obs fade-up">
           <div class="scratch-container">
               <div class="scratch-bg">
                   Asad <br><span style="font-size: 2rem;">&</span><br> Rimsha
               </div>
               <canvas id="scratchCard" width="320" height="320"></canvas>
           </div>
       </div>

       <!-- Sub-header Typewriter -->
       <div class="header-text obs type-fade" data-text="Show your kind love by participating in the event"></div>

       <!-- Schedule Table -->
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

       <!-- Footer -->
       <div class="footer-text obs fade-up">
           May Allah Bless you and your family with Rehmaat and Barakaat
       </div>
    </div>

    <script>
        // 1. Curtain Drop Animation
        function openCurtains() {
            const wrapper = document.getElementById('curtain-wrapper');
            wrapper.classList.add('opened');
            setTimeout(() => { wrapper.style.display = 'none'; }, 2500);
        }

        // 2. Generate Random Decor (Hearts, Butterflies, Flowers) for Background
        const decorElements = ['🌸', '❤️', '🦋', '🌺', '💖'];
        const content = document.getElementById('main-content');
        for(let i=0; i<15; i++) {
            let el = document.createElement('div');
            el.className = 'bg-deco';
            el.innerHTML = decorElements[Math.floor(Math.random() * decorElements.length)];
            el.style.left = Math.random() * 90 + 'vw';
            el.style.top = Math.random() * 90 + '%';
            el.style.fontSize = (Math.random() * 1.5 + 1) + 'rem';
            el.style.animationDelay = (Math.random() * 3) + 's';
            content.appendChild(el);
        }

        // 3. Scroll Interactions (Intersection Observer)
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    // Fade-Up Trigger
                    if(entry.target.classList.contains('fade-up')) {
                        entry.target.classList.add('visible-up');
                    }
                    // Ink Spread Trigger
                    if(entry.target.classList.contains('ink-trigger')) {
                        entry.target.classList.add('visible-ink');
                    }
                    // Typewriter Trigger
                    if(entry.target.classList.contains('type-fade')) {
                        entry.target.classList.add('visible-fade');
                        typeWriter(entry.target);
                    }
                }
            });
        }, { threshold: 0.25 });

        document.querySelectorAll('.obs').forEach(el => observer.observe(el));

        // 4. Typewriter Logic
        function typeWriter(el) {
            if(el.dataset.typed) return; 
            el.dataset.typed = true;
            let text = el.getAttribute('data-text');
            el.innerHTML = '';
            let i = 0;
            let timer = setInterval(() => {
                if (i < text.length) {
                    el.innerHTML += text.charAt(i);
                    i++;
                } else {
                    clearInterval(timer);
                }
            }, 60);
        }

        // 5. Scratch Card Logic
        const canvas = document.getElementById('scratchCard');
        const ctx = canvas.getContext('2d');
        let isDrawing = false;
        let isRevealed = false;

        // Draw Scratch Material
        ctx.fillStyle = '#a0a0a0';
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        
        // Add Scratch me text
        ctx.fillStyle = '#ffffff';
        ctx.font = '30px Playfair Display';
        ctx.textAlign = 'center';
        ctx.fillText('Scratch me', canvas.width/2, canvas.height/2 + 10);

        function getMousePos(e) {
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            return { x: clientX - rect.left, y: clientY - rect.top };
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

        function checkReveal() {
            const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            let transparentPixels = 0;
            const totalPixels = imageData.data.length / 4;
            
            for (let i = 3; i < imageData.data.length; i += 40) {
                if (imageData.data[i] === 0) transparentPixels++;
            }
            
            if (transparentPixels / (totalPixels/10) > 0.45 && !isRevealed) {
                isRevealed = true;
                canvas.style.transition = 'opacity 0.8s';
                canvas.style.opacity = 0;
                setTimeout(() => canvas.style.display = 'none', 800);
                triggerPopping();
            }
        }

        // 6. Confetti & Heart Bubbles Animation on Reveal
        function triggerPopping() {
            const duration = 3000;
            const end = Date.now() + duration;

            const heartShape = confetti.shapeFromText({ text: '❤️', scalar: 2.5 });
            const flowerShape = confetti.shapeFromText({ text: '🌸', scalar: 2.5 });
            const butterflyShape = confetti.shapeFromText({ text: '🦋', scalar: 2.5 });

            (function frame() {
                confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0, y: 0.6 }, shapes: [heartShape, flowerShape, butterflyShape], zIndex: 100 });
                confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1, y: 0.6 }, shapes: [heartShape, flowerShape, butterflyShape], zIndex: 100 });
                if (Date.now() < end) requestAnimationFrame(frame);
            }());
        }
    </script>
</body>
</html>
"""

components.html(html_content, scrolling=True)
