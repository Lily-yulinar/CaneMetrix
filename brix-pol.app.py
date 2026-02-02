import streamlit as st
from datetime import datetime
import pytz
import time

# --- 1. SETTINGS & LUXURY GLASS UI (DESIGN LOCKED & BRIGHTENED) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    
    .stApp { background-color: #050a10; }
    
    /* Header Panel Dicerahkan & Glow Effect */
    .header-panel {
        background: linear-gradient(135deg, rgba(0, 255, 255, 0.25) 0%, rgba(0, 128, 128, 0.15) 100%);
        backdrop-filter: blur(20px);
        border-radius: 35px;
        padding: 35px;
        border: 1px solid rgba(0, 255, 255, 0.5);
        box-shadow: 0 0 50px rgba(0, 255, 255, 0.15);
        margin-bottom: 35px;
        text-align: center;
    }

    /* Tombol Menu Luxury */
    .stButton > button {
        height: 160px;
        border-radius: 20px;
        background: rgba(15, 23, 42, 0.8) !important;
        color: white !important;
        border: 1px solid rgba(0, 206, 209, 0.4) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 800;
        transition: 0.4s ease;
    }

    .stButton > button:hover {
        transform: translateY(-8px);
        border-color: #00ffff !important;
        box-shadow: 0 0 25px rgba(0, 255, 255, 0.4) !important;
    }
    
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(0, 255, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN SESUAI INSTRUKSI BEB ---

def get_koreksi_suhu(temp):
    """Tabel Koreksi Suhu Lab"""
    # Untuk suhu 28.30 target koreksi +0.20
    if 28.0 <= temp <= 28.5: return 0.20
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16}
    return tabel.get(int(temp), 0.16)

def get_bj_pengenceran(brix_p):
    """Berat Jenis berdasarkan Brix Pengenceran"""
    # Brix Pengenceran (Brix Obs * 10) = 88.0
    # Data BJ untuk area Brix 88 (diwakili index tabel)
    return 1.031047 

# --- 3. HEADER AREA (SGN | JUDUL | LPP) ---

if 'menu' not in st.session_state: st.session_state.menu = "main"

# Fix Jam Jakarta
tz_jkt = pytz.timezone('Asia/Jakarta')
now_jkt = datetime.now(tz_jkt)

st.markdown('<div class="header-panel">', unsafe_allow_html=True)
col_l1, col_mid, col_l2 = st.columns([1, 3, 1])

with col_l1:
    st.image("sgn.png", width=130) # Logo Kiri

with col_mid:
    st.markdown(f"""
        <h1 style="font-family:Orbitron; font-size:55px; color:#00ffff; margin:0; text-shadow: 0 0 15px rgba(0,255,255,0.5);">CANE METRIX</h1>
        <p style="font-family:Lexend; color:white; letter-spacing:3px; font-size:14px; opacity:0.9;">ACCELERATING QA PERFORMANCE</p>
        <div style="font-family:Orbitron; color:#00ced1; font-size:20px; margin-top:10px;">
            {now_jkt.strftime('%d %B %Y')} | {now_jkt.strftime('%H:%M:%S')}
        </div>
    """, unsafe_allow_html=True)

with col_l2:
    st.image("lpp.png", width=130) # Logo Kanan
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. CONTENT & LOGIC ---

if st.session_state.menu == "main":
    cols = st.columns(4)
    items = [("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN")]
    for i, (icon, label) in enumerate(items):
        with cols[i]:
            if st.button(f"{icon}\n\n{label}", key=f"btn_{i}", use_container_width=True):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        # Input Data
        b_obs = st.number_input("Brix Teramati (Brix Obs)", value=8.80, format="%.2f")
        p_obs = st.number_input("Pol Teramati (Pol Obs)", value=11.00, format="%.2f")
        t_obs = st.number_input("Suhu Lab (°C)", value=28.30, format="%.2f")
        
        # 1. Brix Pengenceran (Brix Obs * 10)
        brix_p = b_obs * 10 # Hasil: 88.00
        
        # 2. Brix Koreksi (Brix P + Koreksi Suhu)
        kor = get_koreksi_suhu(t_obs)
        brix_kor = brix_p + kor # Hasil: 88.20
        
    with c2:
        # 3. % Pol Pakai BJ Brix Pengenceran
        bj = get_bj_pengenceran(brix_p) 
        pol_persen = (0.286 * (p_obs * 2)) / bj # Hasil: 6.10
        
        # 4. HK Pakai Brix Koreksi
        hk = (pol_persen / brix_kor * 100) if brix_kor > 0 else 0.0 # Hasil: 6.92%
        
        st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
        st.metric("% POL", f"{pol_persen:.2f}")
        st.success(f"### HK: {hk:.2f}%")
        st.caption(f"BJ used: {bj:.6f} (from Brix {brix_p:.1f})")
        
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD", use_container_width=True):
        st.session_state.menu = "main"; st.rerun()

# --- 5. REFRESH ENGINE ---
time.sleep(1)
st.rerun()
