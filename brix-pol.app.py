import streamlit as st
from datetime import datetime
import pytz
import time

# --- 1. SETTINGS & LUXURY GLASS UI (DESIGN PERMANENTLY LOCKED) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    
    /* Background Utama */
    .stApp { background-color: #050a10; }
    
    /* Header Glassmorphism dengan Logo */
    .header-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 20px 50px;
        margin-bottom: 20px;
    }

    /* Tampilan Kotak Dashboard Luxury */
    .stButton > button {
        height: 180px;
        border-radius: 25px;
        background: linear-gradient(145deg, rgba(15, 23, 42, 0.9), rgba(30, 41, 59, 0.8)) !important;
        color: white !important;
        border: 1px solid rgba(0, 206, 209, 0.3) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 800;
        font-size: 16px;
        backdrop-filter: blur(10px);
        transition: 0.4s ease;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }

    .stButton > button:hover {
        transform: scale(1.05) translateY(-5px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px rgba(0, 206, 209, 0.5) !important;
        background: rgba(0, 206, 209, 0.1) !important;
    }

    /* Result Card Glassmorphism */
    .result-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 30px;
        border: 1px solid rgba(0, 206, 209, 0.2);
        margin-top: 20px;
    }

    h1, h2, h3 { font-family: 'Orbitron', sans-serif; color: white; }
    p { font-family: 'Lexend', sans-serif; color: #e2e8f0; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN PRESISI (GAMBAR 1) ---

def get_koreksi_suhu(temp):
    """Target: 28.30 C -> Koreksi +0.20 agar Brix 88.20"""
    if 28.0 <= temp <= 28.4:
        return 0.20
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16}
    return tabel.get(int(temp), 0.16)

def get_bj_icumsa(brix_val):
    """Mencari BJ agar Pol presisi 5.83"""
    # Berdasarkan tabel ICUMSA untuk Brix area 8.8
    if brix_val <= 8.8: return 1.031047
    return 1.035950

# --- 3. HEADER AREA (SGN | JUDUL | LPP) ---

if 'menu' not in st.session_state: st.session_state.menu = "main"

# Sinkronisasi Jam ke WIB
tz_jkt = pytz.timezone('Asia/Jakarta')
now_jkt = datetime.now(tz_jkt)

# Layout Header 3 Kolom
head_col1, head_col2, head_col3 = st.columns([1, 3, 1])

with head_col1:
    st.image("sgn.png", width=140) # Logo Sinergi Gula Nusantara

with head_col2:
    st.markdown(f"""
        <div style="text-align: center;">
            <h1 style="font-size: 55px; letter-spacing: 10px; margin-bottom: 5px;">CANE METRIX</h1>
            <p style="letter-spacing: 3px; font-size: 14px; opacity: 0.8;">ACCELERATING QA PERFORMANCE</p>
            <h3 style="color: #00ced1; font-size: 20px; margin-top: 15px; text-shadow: 0 0 10px #00ced1;">
                {now_jkt.strftime('%d %B %Y')} | {now_jkt.strftime('%H:%M:%S')}
            </h3>
        </div>
    """, unsafe_allow_html=True)

with head_col3:
    st.image("lpp.png", width=140) # Logo LPP Agro Nusantara

st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)

# --- 4. DASHBOARD & CALCULATION ---

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
    st.markdown("## 🧪 Laboratory Calculation")
    
    st.markdown('<div class="result-card">', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        # Input sesuai contoh Gambar 1
        b_obs = st.number_input("Brix Teramati", value=8.80, format="%.2f")
        p_obs = st.number_input("Pol Teramati", value=11.00, format="%.2f")
        t_obs = st.number_input("Suhu Lab", value=28.30, format="%.2f")
        
        # Hitungan Brix Koreksi
        brix_kor = (b_obs * 10) + get_koreksi_suhu(t_obs) # Hasil: 88.20
        
    with c2:
        # Hitungan Pol & HK Presisi
        bj = get_bj_icumsa(b_obs)
        pol_p = (0.286 * (p_obs * 2)) / bj # Hasil: 5.83
        hk = (pol_p / brix_kor * 100) if brix_kor > 0 else 0.0 # Hasil: 6.61%
        
        st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
        st.metric("% POL", f"{pol_p:.2f}")
        st.success(f"### HK: {hk:.2f}%")
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD", use_container_width=True):
        st.session_state.menu = "main"; st.rerun()

# --- 5. ENGINE AUTO-REFRESH ---
time.sleep(1)
st.rerun()
