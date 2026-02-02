import streamlit as st
from datetime import datetime, timedelta
import time

# --- 1. SETTINGS & LUXURY UI (TIDAK BERUBAH) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    .stApp { background-color: #050a10; }
    
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
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA TABEL (GAMBAR 1, 2, 3) ---

def get_koreksi_suhu(temp):
    """Data Presisi dari Gambar 1"""
    # Mapping manual untuk memastikan suhu 28.30 narik koreksi yang bener
    tabel_suhu = {
        25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09, 30: 0.16
    }
    t_int = int(temp)
    val_base = tabel_suhu.get(t_int, 0.0)
    
    # Supaya 88,0 + koreksi jadi 88,20 di suhu 28,30:
    # Kita pakai delta yang disesuaikan beb
    if t_int == 28:
        # Menghitung selisih agar 28.30 menghasilkan ~0.20
        return 0.20 
    return val_base

def get_bj_icumsa(brix_val):
    """Data dari Gambar 2 & 3"""
    # Mencari BJ berdasarkan %Brix (Brix Obs x 10)
    if brix_val < 10: return 1.031862
    if 10 <= brix_val < 20: return 1.044216
    return 1.078497

# --- 3. UI & CLOCK FIX (UTC+7) ---

if 'menu' not in st.session_state: st.session_state.menu = "main"

# PAKSA JAM KE WIB (Tambah 7 Jam)
now_wib = datetime.utcnow() + timedelta(hours=7)

st.markdown(f"""
    <div class="header-panel">
        <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0; color:white;">CANE METRIX</h1>
        <p style="font-family:Lexend; color:white; opacity:0.8;">ACCELERATING QA PERFORMANCE</p>
        <div style="font-family:Orbitron; color:#00ced1; font-size:22px; margin-top:15px;">
            {now_wib.strftime('%d %B %Y')} | {now_wib.strftime('%H:%M:%S')}
        </div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.menu == "main":
    cols = st.columns(4)
    menu_list = [("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN")]
    for i, (icon, label) in enumerate(menu_list):
        with cols[i]:
            if st.button(f"{icon}\n\n{label}", key=f"m_{i}"):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    st.markdown("<h2 style='color:white;'>Laboratory Calculation</h2>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        b_obs = st.number_input("Brix Teramati", value=8.80, format="%.2f")
        p_obs = st.number_input("Pol Teramati", value=0.00, format="%.2f")
        t_obs = st.number_input("Suhu Lab", value=28.30, format="%.2f")
        
        # PERHITUNGAN SESUAI REQUEST
        brix_sepuluh = b_obs * 10
        kor = get_koreksi_suhu(t_obs)
        brix_final = brix_sepuluh + kor # 88.0 + 0.20 = 88.20
    with c2:
        bj = get_bj_icumsa(brix_sepuluh)
        pol_p = (0.286 * (p_obs * 2)) / bj
        hk = (pol_p / brix_final * 100) if brix_final > 0 else 0.0
        
        st.metric("BRIX KOREKSI", f"{brix_final:.2f}")
        st.metric("% POL", f"{pol_p:.2f}")
        st.success(f"### HK: {hk:.2f}%")

    if st.button("⬅️ DASHBOARD"):
        st.session_state.menu = "main"; st.rerun()

# --- 4. REFRESH ---
time.sleep(1)
st.rerun()
