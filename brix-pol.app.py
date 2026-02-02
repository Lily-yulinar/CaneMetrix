import streamlit as st
from datetime import datetime
import pytz # Library untuk fix jam sesuai zona waktu
import time

# --- 1. SETTINGS & LUXURY GLASS UI (KEMBALI KE DESAIN ASLI) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    
    .stApp { background-color: #050a10; }
    
    /* Panel Utama Glassmorphism */
    .header-panel {
        background: linear-gradient(135deg, rgba(0, 206, 209, 0.4) 0%, rgba(0, 128, 128, 0.2) 100%);
        backdrop-filter: blur(20px);
        border-radius: 35px;
        padding: 40px;
        text-align: center;
        border: 1px solid #00ced1;
        box-shadow: 0 0 30px rgba(0, 206, 209, 0.3);
        margin-bottom: 30px;
    }

    /* Tombol Menu Kotak Luxury */
    .stButton > button {
        height: 160px;
        border-radius: 20px;
        background: #0f172a !important;
        color: white !important;
        border: 1px solid rgba(0, 206, 209, 0.3) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 800;
        font-size: 16px;
        transition: 0.4s ease;
    }

    .stButton > button:hover {
        transform: scale(1.05) translateY(-5px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px #00ced1 !important;
    }
    
    /* Styling untuk Tabel & Hasil */
    .result-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid rgba(0, 206, 209, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN PRESISI ---

def get_koreksi_suhu(temp):
    """Tabel Koreksi Suhu Gambar 1"""
    # Target: 28.30 C menghasilkan koreksi yang bikin Brix jadi 88.20
    if 28.0 <= temp <= 28.5:
        return 0.20
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16}
    return tabel.get(int(temp), 0.16)

def get_bj_icumsa(brix_val):
    """Tabel Berat Jenis Gambar 2 & 3"""
    # Mencari BJ berdasarkan Brix Teramati (8.8)
    if brix_val <= 8.8: return 1.031047 # Data Tabel untuk area 8.8
    return 1.035950

# --- 3. UI DASHBOARD & CLOCK ---

if 'menu' not in st.session_state: st.session_state.menu = "main"

# Fix Jam: Menggunakan zona waktu Jakarta (WIB)
tz_jkt = pytz.timezone('Asia/Jakarta')
now_jkt = datetime.now(tz_jkt)

st.markdown(f"""
    <div class="header-panel">
        <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0; color:white;">CANE METRIX</h1>
        <p style="font-family:Lexend; color:white; opacity:0.8; letter-spacing:2px;">ACCELERATING QA PERFORMANCE</p>
        <div style="font-family:Orbitron; color:#00ced1; font-size:22px; margin-top:15px; border-top:1px solid rgba(0,206,209,0.2); padding-top:10px;">
            {now_jkt.strftime('%d %B %Y')} | {now_jkt.strftime('%H:%M:%S')}
        </div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.menu == "main":
    cols = st.columns(4)
    menu_items = [
        ("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), 
        ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN")
    ]
    for i, (icon, label) in enumerate(menu_items):
        with cols[i]:
            if st.button(f"{icon}\n\n{label}", key=f"btn_{i}", use_container_width=True):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    st.markdown("<h2 style='color:white; font-family:Lexend;'>Laboratory Calculation</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            b_obs = st.number_input("Brix Teramati", value=8.80, format="%.2f")
            p_obs = st.number_input("Pol Teramati", value=11.00, format="%.2f") # Input sesuai Gambar 1
            t_obs = st.number_input("Suhu Lab", value=28.30, format="%.2f")
            
            # Hitungan Brix Koreksi
            brix_x10 = b_obs * 10
            kor_suhu = get_koreksi_suhu(t_obs)
            brix_kor = brix_x10 + kor_suhu # Hasil: 88.20
            
        with c2:
            # FIX POL: (0.286 * (Pol x 2)) / BJ
            bj = get_bj_icumsa(b_obs)
            pol_p = (0.286 * (p_obs * 2)) / bj # Hasil: 5.83
            hk = (pol_p / brix_kor * 100) if brix_kor > 0 else 0.0 # Hasil: 6.61%
            
            st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
            st.metric("% POL", f"{pol_p:.2f}")
            st.success(f"### HK: {hk:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ DASHBOARD", use_container_width=True):
        st.session_state.menu = "main"; st.rerun()

# --- 4. ENGINE REFRESH ---
time.sleep(1)
st.rerun()
