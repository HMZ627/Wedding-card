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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Invitation</title>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Great+Vibes&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.9.2/dist/confetti.browser.min.js"></script>
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
        
        #curtain-wrapper.opened .curtain-left { transform: translateX(-100%); }
        #curtain-wrapper.opened .curtain-right { transform: translateX(100%); }
        #curtain-wrapper.opened .open-btn { opacity: 0; pointer-events: none; }

        /* --- Main Content --- */
        .content { min-height: 100vh; padding: 100px 20px; text-align: center; overflow-x: hidden; position: relative; z-index: 10; }
        
        /* Bismillah */
        .bismillah { font-family: 'Amiri', serif; font-size: 4.5rem; margin-bottom: 25vh; opacity: 0; transform: translateY(30px); transition: all 1.5s ease-out; }
        
        /* Type-in Fade-in */
        .type-fade { 
            font-size: 2.2rem; 
            margin: 0 auto 25vh auto; 
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
        }
        .sub-header-text { font-size: 2rem; position: relative; }
        
        .invite-word { font-size: 6rem; display: block; text-align: center; font-family: 'Great Vibes', cursive; margin: 30px 0; color: #4a3b32; }
        .wedding-word { color: #ff033e; font-weight: bold; font-style: italic; }
        
        /* 2 Blooming Flowers & Hovering Butterflies */
        .garden-container { display: flex; justify-content: center; gap: 100px; margin-top: 40px; height: 120px; }
        .plant { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; }
        .flower { font-size: 4.5rem; transform: scale(0); transition: transform 1.5s cubic-bezier(0.68, -0.55, 0.27, 1.55); }
        .butterfly { font-size: 2.5rem; position: absolute; bottom: 20px; opacity: 0; transition: all 1.5s ease-in-out; }

        .visible-ink .ink-spread-anim { opacity: 1; clip-path: circle(150% at center); filter: blur(0px); }
        .visible-ink .flower { transform: scale(1); animation: continuousBloom 3s infinite alternate ease-in-out 1.5s; }
        .visible-ink .butterfly { bottom: 90px; opacity: 1; transition-delay: 1.2s; animation: hoverfly 2.5s infinite ease-in-out alternate 2.7s; }
        .plant.delayed .flower { transition-delay: 0.4s; }
        .plant.delayed .butterfly { transition-delay: 1.6s; animation-delay: 3.1s; }

        @keyframes continuousBloom { 0% { transform: scale(1) rotate(-5deg); } 100% { transform: scale(1.15) rotate(5deg); } }
        @keyframes hoverfly { 0% { transform: translateY(0) translateX(0) rotate(-10deg); } 100% { transform: translateY(-15px) translateX(15px) rotate(15deg); } }

        /* --- Scratch Card --- */
        .scratch-wrapper { margin: 0 auto 25vh auto; display: flex; justify-content: center; opacity: 0; transform: translateY(30px); transition: all 1.5s ease-out; }
        .scratch-container {
            position: relative; width: 320px; height: 320px;
            clip-path: path("M 160,90 C 160,90 110,0 20,50 C -50,120 160,300 160,300 C 160,300 370,120 300,50 C 210,0 160,90 160,90 Z");
            box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        }
        .scratch-bg { width: 100%; height: 100%; background: #fff; display: flex; flex-direction: column; align-items: center; justify-content: center; }
        .heart-text { font-family: 'Great Vibes', cursive; color: #b30000; font-size: 2.6rem; line-height: 1.1; text-align: center; margin-top: 25px; }
        canvas { position: absolute; top: 0; left: 0; z-index: 10; cursor: pointer; touch-action: none; }

        /* --- Schedule Table --- */
        .schedule-box { max-width: 800px; margin: 0 auto 25vh auto; opacity: 0; transform: translateY(50px); transition: all 1.5s; background: rgba(255,255,255,0.4); padding: 30px; border-radius: 15px; border: 2px dashed #bba171; overflow-x: auto; }
        table { width: 100%; border-collapse: collapse; }
        th, td { padding: 15px; text-align: center; border-bottom: 1px solid #d8ccb8; }
        th { font-family: 'Great Vibes', cursive; font-size: 2rem; color: #800000; border-bottom: 2px solid #bba171; }
        td { font-size: 1.2rem; }

        /* --- Footer --- */
        .footer-text { font-size: 1.5rem; opacity: 0; transform: translateY(50px); transition: all 1.5s; padding-bottom: 100px; font-style: italic; color: #800000; font-weight: bold;}

        /* --- Interactive Trigger Class --- */
        .interactive-emoji { display: inline-block; cursor: pointer; user-select: none; -webkit-tap-highlight-color: transparent; }
        .pop-anim { animation: clickPop 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important; }
        @keyframes clickPop {
            0% { transform: scale(1) rotate(0deg); filter: brightness(1); }
            30% { transform: scale(1.6) rotate(15deg); filter: brightness(1.2); }
            70% { transform: scale(1.6) rotate(-15deg); filter: brightness(1.2); }
            100% { transform: scale(1) rotate(0deg); filter: brightness(1); }
        }

        /* --- Parallax & Float Elements --- */
        .bg-deco { opacity: 0.4; animation: floatDeco 6s infinite ease-in-out alternate; }
        .fg-deco { animation: floatDeco 8s infinite ease-in-out alternate-reverse; }
        @keyframes floatDeco { 0% { transform: translateY(0px); } 100% { transform: translateY(-25px); } }
        
        /* --- NEW: Drawn Pencil Birds in Flocks with Wingtip-Flapping --- */
        .bird-flock { position: fixed; z-index: 1; pointer-events: none; opacity: 0.55; }
        .bird-flock .interactive-emoji { pointer-events: auto; }

        .bird-svg { overflow: visible; animation: birdBob 1.2s infinite ease-in-out alternate; }
        .bird-wing { animation: birdFlap 0.5s infinite ease-in-out alternate; } 

        @keyframes birdBob { 0% { transform: translateY(0px); } 100% { transform: translateY(12px); } }
        
        /* NEW PATHS: The center (50 30) stays put, while the tips (5, 95) flap vastly up and down! */
        @keyframes birdFlap {
            0%   { d: path("M 5 10 Q 30 15 50 30 Q 70 15 95 10"); } /* Tips high up */
            100% { d: path("M 5 50 Q 30 35 50 30 Q 70 35 95 50"); } /* Tips swooped down */
        }

        @keyframes flyRight { 0% { transform: translateX(-15vw) translateY(15vh); } 100% { transform: translateX(115vw) translateY(-15vh); } }
        @keyframes flyLeft { 0% { transform: translateX(115vw) translateY(15vh); } 100% { transform: translateX(-15vw) translateY(-15vh); } }

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
       
       <div class="bismillah obs fade-up">﷽</div>

       <div class="header-text obs type-fade" data-text="Starting with the name of Allah, The most Beneficial and The most Merciful."></div>

       <div class="obs ink-trigger" style="min-height: 400px; margin-bottom: 15vh; display: flex; align-items: center; justify-content: center;">
           <div class="ink-spread-anim">
               <div class="sub-header-text">
                   We are pleased to
                   <span class="invite-word">Invite</span>
                   you to the <span class="wedding-word">Wedding</span> ceremony
               </div>
               
               <div class="garden-container">
                   <div class="plant">
                       <div class="butterfly"><span class="interactive-emoji">🦋</span></div>
                       <div class="flower"><span class="interactive-emoji">🌸</span></div>
                   </div>
                   <div class="plant delayed">
                       <div class="butterfly"><span class="interactive-emoji">🦋</span></div>
                       <div class="flower"><span class="interactive-emoji">🌺</span></div>
                   </div>
               </div>
           </div>
       </div>

       <div class="scratch-wrapper obs fade-up">
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
            setTimeout(() => { wrapper.style.display = 'none'; }, 2500);
        }

        // 2. Element Generators (Background Floaties, Foreground Floaties, Bird Flocks)
        const content = document.getElementById('main-content');
        const floaties = ['🌸', '❤️', '🌺', '💖', '✨'];
        
        // A) Parallax Background Emoji Decor
        for(let i=0; i<25; i++) {
            let wrapper = document.createElement('div');
            wrapper.className = 'parallax-bg-wrapper';
            wrapper.style.position = 'absolute';
            wrapper.style.left = Math.random() * 90 + 'vw';
            wrapper.style.top = Math.random() * 100 + '%'; 
            wrapper.style.zIndex = '0'; 

            let el = document.createElement('div');
            el.className = 'bg-deco';
            el.style.animationDelay = (Math.random() * 3) + 's';
            
            let inner = document.createElement('span');
            inner.className = 'interactive-emoji';
            inner.innerHTML = floaties[Math.floor(Math.random() * floaties.length)];
            inner.style.fontSize = (Math.random() * 1.5 + 1) + 'rem';
            
            el.appendChild(inner);
            wrapper.appendChild(el);
            content.appendChild(wrapper);
        }

        // B) Parallax Foreground Decor
        for(let i=0; i<12; i++) {
            let wrapper = document.createElement('div');
            wrapper.className = 'parallax-fg-wrapper';
            wrapper.style.position = 'absolute';
            wrapper.style.left = Math.random() * 90 + 'vw';
            wrapper.style.top = Math.random() * 100 + '%';
            wrapper.style.zIndex = '50'; 
            wrapper.style.pointerEvents = 'none'; 

            let el = document.createElement('div');
            el.className = 'fg-deco';
            el.style.animationDelay = (Math.random() * 3) + 's';
            
            let inner = document.createElement('span');
            inner.className = 'interactive-emoji';
            inner.innerHTML = floaties[Math.floor(Math.random() * floaties.length)];
            inner.style.fontSize = (Math.random() * 2 + 2) + 'rem'; 
            inner.style.filter = 'blur(3px)';
            inner.style.opacity = '0.7';
            inner.style.pointerEvents = 'auto'; 
            
            el.appendChild(inner);
            wrapper.appendChild(el);
            content.appendChild(wrapper);
        }

        // C) NEW: Organized Bird Flocks with V-formation geometry
        const numFlocks = 5;
        for(let f = 0; f < numFlocks; f++) {
            let flockWrapper = document.createElement('div');
            flockWrapper.className = 'bird-flock';
            
            let isRight = Math.random() > 0.5;
            let animName = isRight ? 'flyRight' : 'flyLeft';
            let animDuration = Math.random() * 25 + 30; // 30-55s slow sky drift
            
            flockWrapper.style.animation = `${animName} ${animDuration}s linear infinite`;
            flockWrapper.style.animationDelay = '-' + (Math.random() * 25) + 's';
            flockWrapper.style.top = (Math.random() * 65 + 10) + 'vh'; 
            
            let birdsInFlock = Math.floor(Math.random() * 3) + 3; // 3 to 5 birds per flock
            
            for(let b = 0; b < birdsInFlock; b++) {
                let birdNode = document.createElement('div');
                birdNode.style.position = 'absolute';
                
                // Mathematically calculate a loose V-Formation trailing behind the leader
                // If flying right, birds offset to the left (negative X). Vice versa.
                let xOffset = isRight ? -(b * 35 + Math.random()*10) : (b * 35 + Math.random()*10);
                // Alternate placing birds above and below the leader's Y axis
                let yOffset = (b % 2 === 0 ? 1 : -1) * (Math.ceil(b/2) * 20) + (Math.random()*10 - 5);
                
                birdNode.style.left = xOffset + 'px';
                birdNode.style.top = yOffset + 'px';
                
                let inner = document.createElement('div');
                inner.className = 'interactive-emoji';
                let tilt = isRight ? 'rotate(-10deg)' : 'rotate(10deg)';
                inner.style.transform = tilt;
                
                // Stagger flap animation so they don't look robotic
                let flapDelay = '-' + (Math.random() * 0.5).toFixed(2) + 's';
                
                inner.innerHTML = `
                <svg class="bird-svg" viewBox="0 0 100 60" width="${Math.random() * 15 + 35}" height="25">
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
            
            // Push DOWN as you scroll down -> Result: they move UP slower on the screen
            document.querySelectorAll('.parallax-bg-wrapper').forEach(el => {
                el.style.transform = `translateY(${scrollY * 0.5}px)`; 
            });
            // Pull UP as you scroll down -> Result: they move UP faster on the screen
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

        // 7. Scratch Card Logic (Threshold adjusted to 30%)
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
            
            // INCREASED SENSITIVITY: Pops when only 30% is scratched
            if (transparentPixels / (totalPixels/10) > 0.30 && !isRevealed) {
                isRevealed = true;
                canvas.style.transition = 'opacity 0.8s';
                canvas.style.opacity = 0;
                setTimeout(() => canvas.style.display = 'none', 800);
                triggerPopping();
            }
        }

        // 8. Confetti & Flock of Birds Burst Animation!
        function triggerPopping() {
            const duration = 3000;
            const end = Date.now() + duration;

            // Heart and Flower Confetti
            const heartShape = confetti.shapeFromText({ text: '❤️', scalar: 2.5 });
            const flowerShape = confetti.shapeFromText({ text: '🌸', scalar: 2.5 });
            const butterflyShape = confetti.shapeFromText({ text: '🦋', scalar: 2.5 });

            (function frame() {
                confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0, y: 0.6 }, shapes: [heartShape, flowerShape, butterflyShape], zIndex: 100 });
                confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1, y: 0.6 }, shapes: [heartShape, flowerShape, butterflyShape], zIndex: 100 });
                if (Date.now() < end) requestAnimationFrame(frame);
            }());
            
            // EXPLODING FLOCK OF BIRDS
            spawnExplosionFlock();
        }

        function spawnExplosionFlock() {
            const flockContainer = document.createElement('div');
            flockContainer.style.position = 'fixed';
            flockContainer.style.left = '50%';
            flockContainer.style.top = '50%';
            flockContainer.style.transform = 'translate(-50%, -50%)';
            flockContainer.style.zIndex = '1000';
            flockContainer.style.pointerEvents = 'none';
            document.body.appendChild(flockContainer);

            for (let i = 0; i < 20; i++) { 
                let bird = document.createElement('div');
                bird.style.position = 'absolute';
                
                let flapDelay = '-' + (Math.random() * 0.5).toFixed(2) + 's';
                // Utilizing the exact same new Wingtip flapping CSS
                bird.innerHTML = `
                    <svg class="bird-svg" viewBox="0 0 100 60" width="${Math.random() * 15 + 25}" height="20">
                        <path class="bird-wing" style="animation-delay: ${flapDelay};" fill="none" stroke="#4a3b32" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" d="M 5 10 Q 30 15 50 30 Q 70 15 95 10" />
                    </svg>`;
                
                // Random explosion trajectory outward and upward
                let tx = (Math.random() - 0.5) * window.innerWidth;
                let ty = - (Math.random() * window.innerHeight/2 + 200); 
                let rot = (Math.random() - 0.5) * 60; 

                // Dynamic API Javascript animation
                bird.animate([
                    { transform: `translate(0px, 0px) scale(0.2) rotate(0deg)`, opacity: 1 },
                    { transform: `translate(${tx}px, ${ty}px) scale(1.5) rotate(${rot}deg)`, opacity: 0 }
                ], {
                    duration: Math.random() * 1500 + 2000,
                    easing: 'cubic-bezier(0.25, 1, 0.5, 1)',
                    fill: 'forwards'
                });

                flockContainer.appendChild(bird);
            }
            
            // Clean up flock node after finishing animation
            setTimeout(() => flockContainer.remove(), 4000);
        }
    </script>
</body>
</html>
"""

components.html(html_content, scrolling=True)
