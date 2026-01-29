import streamlit as st
from datetime import datetime
import pandas as pd
import time

# --- 1. SETTINGS & STYLING (THE ELEGANT LUXURY UI) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS untuk Efek Glassmorphism, Neon Glow, dan Animasi Pop-up
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');

    .stApp { background-color: #050a10; }
    
    /* Luxury Header */
    .header-panel {
        background: linear-gradient(135deg, rgba(0, 206, 209, 0.2), rgba(0, 128, 128, 0.1));
        backdrop-filter: blur(15px);
        border-radius: 40px;
        padding: 40px;
        border: 1px solid rgba(0, 206, 209, 0.3);
        text-align: center;
        margin-bottom: 40px;
    }

    /* Neon Sidebar */
    [data-testid="stSidebar"] { background-color: #03070a !important; border-right: 1px solid #00ced1; }

    /* Custom Menu Card (Glassmorphism & Pop-up) */
    .menu-card {
        background: rgba(255, 255, 255, 0.03);
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
        transition: all 0.4s ease;
        cursor: pointer;
        height: 180px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .menu-card:hover {
        background: rgba(0, 206, 209, 0.1);
        transform: translateY(-10px) scale(1.05);
        border: 1px solid #00ced1;
        box-shadow: 0 0 20px rgba(0, 206, 209, 0.5), inset 0 0 10px rgba(0, 206, 209, 0.2);
    }

    .menu-icon { font-size: 45px; margin-bottom: 15px; }
    .menu-label { 
        font-family: 'Montserrat', sans-serif; 
        font-weight: 800; 
        font-size: 14px; 
        color: white; 
        letter-spacing: 1px;
    }
    
    /* Real-time Clock Neon */
    .clock-neon {
        font-family: 'Orbitron';
        color: #00ced1;
        text-shadow: 0 0 10px #00ced1;
        font-size: 20px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN (FIXED) ---
def get_koreksi_suhu(temp):
    # Data image_cb7130.png
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16, 31:0.24, 32:0.32}
    t_base = int(temp)
    return tabel.get(t_base, 0.0) + (temp - t_base) * 0.07

def get_bj(brix_p):
    # Data image_cb66ad.png (Brix vs Density d27.5)
    return 1.000 + (brix_p * 0.00388)

# --- 3. SIDEBAR (CLEAN VERSION) ---
with st.sidebar:
    st.markdown("<h1 style='color:#00ced1; font-family:Orbitron; text-align:center;'>CANE METRIX</h1>", unsafe_allow_html=True)
    st.divider()
    shift = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    if st.button("🏠 DASHBOARD UTAMA", use_container_width=True):
        st.session_state.menu_level = "main"
        st.rerun()
    
    # Real-time Clock (Logic JavaScript-like via Streamlit)
    st.markdown(f"""
        <div style='margin-top:280px; text-align:center;'>
            <div class='clock-neon'>{datetime.now().strftime('%H:%M:%S')}</div>
            <small style='color:grey;'>{datetime.now().strftime('%d %B %Y')}</small>
        </div>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
st.markdown(f"""
    <div class="header-panel">
        <h1 style="font-family:Orbitron; font-size:50px; letter-spacing:10px; margin:0; color:#00ced1;">CANE METRIX</h1>
        <p style="font-family:Lexend; letter-spacing:5px; color:white; opacity:0.8;">ACCELERATING QA PERFORMANCE</p>
    </div>
""", unsafe_allow_html=True)

# --- 5. NAVIGASI MENU ---
if 'menu_level' not in st.session_state or st.session_state.menu_level == "main":
    st.markdown(f"<p class='sapaan-text' style='text-align:center; color:#00ced1; font-family:Montserrat; font-size:25px;'>HELLO PLANTERS! OPTIMIZATION MODE: {shift}</p>", unsafe_allow_html=True)
    
    # Grid Menu 1-8 (Urutan Baru)
    cols = st.columns(4)
    menu_data = [
        ("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), 
        ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN"),
        ("🔄", "REKAP STASIUN"), ("📈", "TREND"), 
        ("⚙️", "PENGATURAN"), ("📥", "EXPORT/IMPORT DATA")
    ]

    for i, (icon, label) in enumerate(menu_data):
        with cols[i % 4]:
            if st.button(f"{icon}\n\n{label}", key=f"btn_{i}", use_container_width=True):
                if label == "HITUNG ANALISA":
                    st.session_state.menu_level = "hitung"
                    st.rerun()

elif st.session_state.menu_level == "hitung":
    st.markdown("<h2 style='color:white; font-family:Lexend;'>🧪 Menu Analisa Laboratorium</h2>", unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🍯 ANALISA TETES", "🧪 OPTICAL DENSITY (OD)"])
    
    with tab1:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:25px; border-radius:20px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            b_baca = st.number_input("Brix Baca", value=12.00, step=0.01)
            p_baca = st.number_input("Pol Baca", value=0.00, step=0.01)
            temp = st.number_input("Suhu (°C)", value=28.00, step=0.1)
            
            # Rumus 1 & 2
            brix_persen = b_baca * 10 
            kor = get_koreksi_suhu(temp)
            brix_kor = brix_persen + kor
        
        with c2:
            # Rumus 3
            bj = get_bj(brix_persen)
            pol_persen = (0.286 * (p_baca * 2)) / bj
            # Rumus 4
            hk = (pol_persen / brix_kor * 100) if brix_kor > 0 else 0.0
            
            st.metric("Brix Koreksi", f"{brix_kor:.2f}")
            st.metric("% Pol", f"{pol_persen:.2f}")
            if hk > 100: st.error(f"HK: {hk:.2f}% (DATA TIDAK VALID!)")
            else: st.success(f"### HK (Purity): {hk:.2f}%")
            
            st.caption(f"Info: Faktor 0.286 | Pengenceran 10x | BJ: {bj:.5f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab2:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:25px; border-radius:20px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        st.markdown("### Perhitungan Optical Density")
        abs_val = st.number_input("Absorbance (Abs)", value=0.000, step=0.001, format="%.3f")
        b_asli = st.number_input("Brix Asli (Untuk BJ)", value=12.00, step=0.01)
        
        # Rumus OD [New Request]
        bj_asli = get_bj(b_asli)
        od_result = (abs_val * bj_asli) / 1
        
        st.markdown(f"""
            <div style='background:#0d1b2a; padding:20px; border-radius:15px; border-left:5px solid #00ced1;'>
                <span style='color:#00ced1;'>HASIL OPTICAL DENSITY (OD):</span><br>
                <b style='font-size:35px; color:white;'>{od_result:.4f}</b>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD"):
        st.session_state.menu_level = "main"
        st.rerun()

# Otomatis Refresh Jam (Simple hack)
time.sleep(1)
st.rerun()
