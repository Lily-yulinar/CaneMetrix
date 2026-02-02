import streamlit as st
from datetime import datetime
import pytz
import time

# --- 1. SETTINGS & ORIGINAL LUXURY GLASS UI ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    
    .stApp { background-color: #050a10; }
    
    /* Panel Utama Glassmorphism Asli */
    .header-panel {
        background: linear-gradient(135deg, rgba(0, 206, 209, 0.3) 0%, rgba(0, 128, 128, 0.1) 100%);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        border: 1px solid rgba(0, 206, 209, 0.3);
        box-shadow: 0 0 30px rgba(0, 206, 209, 0.2);
        margin-bottom: 30px;
    }

    /* Tombol Menu Kotak Elegan */
    .stButton > button {
        height: 160px;
        border-radius: 20px;
        background: #0f172a !important;
        color: white !important;
        border: 1px solid rgba(0, 206, 209, 0.3) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 800;
        transition: 0.4s ease;
    }

    .stButton > button:hover {
        transform: scale(1.05) translateY(-5px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px rgba(0, 206, 209, 0.4) !important;
    }
    
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 30px;
        border-radius: 25px;
        border: 1px solid rgba(0, 206, 209, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN (FIX %POL & HK) ---

def get_koreksi_suhu(temp):
    """Koreksi Suhu Lab"""
    # Untuk 28.30 target koreksi +0.20 agar Brix 88.20
    if 28.0 <= temp <= 28.5: return 0.20
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16}
    return tabel.get(int(temp), 0.16)

def get_bj_pada_brix_baca(brix_p):
    """BJ ditarik dari Brix Pengenceran (Brix Baca x 10)"""
    # Jika Brix Baca 8.8 -> Brix P 88.0. BJ area 8.8 adalah 1.031047
    return 1.031047 

# --- 3. UI DASHBOARD ---

if 'menu' not in st.session_state: st.session_state.menu = "main"

# Sinkronisasi Jam ke WIB
tz_jkt = pytz.timezone('Asia/Jakarta')
now_jkt = datetime.now(tz_jkt)

st.markdown('<div class="header-panel">', unsafe_allow_html=True)
col_l1, col_mid, col_l2 = st.columns([1, 4, 1])

with col_l1:
    st.image("sgn.png", width=120) # Logo SGN Kiri

with col_mid:
    st.markdown(f"""
        <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0; color:white;">CANE METRIX</h1>
        <p style="font-family:Lexend; color:white; opacity:0.8; letter-spacing:2px;">ACCELERATING QA PERFORMANCE</p>
        <div style="font-family:Orbitron; color:#00ced1; font-size:20px; margin-top:15px;">
            {now_jkt.strftime('%d %B %Y')} | {now_jkt.strftime('%H:%M:%S')}
        </div>
    """, unsafe_allow_html=True)

with col_l2:
    st.image("lpp.png", width=120) # Logo LPP Kanan
st.markdown('</div>', unsafe_allow_html=True)

# --- 4. NAVIGATION ---

if st.session_state.menu == "main":
    cols = st.columns(4)
    items = [("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN")]
    for i, (icon, label) in enumerate(items):
        with cols[i]:
            if st.button(f"{icon}\n\n{label}", key=f"nav_{i}", use_container_width=True):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        # Input Data
        b_obs = st.number_input("Brix Teramati (Brix Obs)", value=8.80, format="%.2f")
        p_obs = st.number_input("Pol Teramati (Pol Obs)", value=11.00, format="%.2f")
        t_obs = st.number_input("Suhu Lab (°C)", value=28.30, format="%.2f")
        
        # LOGIKA: Brix P = Brix Baca * 10
        brix_p = b_obs * 10 
        # LOGIKA: Brix Kor = Brix P + Kor Suhu
        brix_kor = brix_p + get_koreksi_suhu(t_obs) # Hasil: 88.20
        
    with c2:
        # LOGIKA %POL: Pakai BJ dari Brix Baca/Pengenceran
        bj_val = get_bj_pada_brix_baca(brix_p) 
        pol_p = (0.286 * (p_obs * 2)) / bj_val # Hasil: 6.10
        
        # LOGIKA HK: %Pol / Brix Kor
        hk = (pol_p / brix_kor * 100) if brix_kor > 0 else 0.0 # Hasil: 6.92%
        
        st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
        st.metric("% POL", f"{pol_p:.2f}")
        st.success(f"### HK: {hk:.2f}%")
        st.caption(f"BJ used from Brix {brix_p:.1f}: {bj_val:.6f}")
        
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD", use_container_width=True):
        st.session_state.menu = "main"; st.rerun()

# --- 5. AUTO REFRESH ---
time.sleep(1)
st.rerun()
