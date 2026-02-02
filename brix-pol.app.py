import streamlit as st
from datetime import datetime
import time

# --- 1. SETTINGS & LUXURY GLASS UI (DILOCK TOTAL) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS Tetap Mewah & Kotak-kotak (image_d57902)
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

    .stButton > button:hover {
        transform: scale(1.08) translateY(-10px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px #00ced1, inset 0 0 10px rgba(0,206,209,0.5) !important;
        background: rgba(0, 206, 209, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA TABEL (FIXED SESUAI GAMBAR) ---
def get_koreksi_suhu(temp):
    # Data sesuai tabel image_cb7130.png
    tabel = {25:-0.19, 26:-0.12, 27:-0.05, 28:0.02, 29:0.09, 30:0.16, 31:0.24, 32:0.315, 33:0.385, 34:0.465, 35:0.54}
    t_int = int(temp)
    return tabel.get(t_int, 0.0)

def get_bj_icumsa(brix_val):
    # Data sesuai image_cb66ad.png & image_cb6690.png
    bj_map = {0.0: 0.996373, 10.0: 1.035950, 12.0: 1.044216, 15.0: 1.056841, 20.0: 1.078497}
    keys = sorted(bj_map.keys())
    for i in range(len(keys)-1):
        if keys[i] <= brix_val <= keys[i+1]:
            b1, b2 = keys[i], keys[i+1]
            v1, v2 = bj_map[b1], bj_map[b2]
            return v1 + (brix_val - b1) * (v2 - v1) / (b2 - b1)
    return 1.044216

# --- 3. UI COMPONENTS ---
if 'menu' not in st.session_state: st.session_state.menu = "main"

# HEADER DENGAN FIX REAL-TIME CLOCK
now = datetime.now()
st.markdown(f"""
    <div class="header-panel">
        <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0; color:white;">CANE METRIX</h1>
        <p style="font-family:Lexend; color:white; opacity:0.8;">ACCELERATING QA PERFORMANCE</p>
        <div style="font-family:Orbitron; color:#00ced1; font-size:20px; margin-top:15px; border-top:1px solid rgba(0,206,209,0.3); padding-top:10px;">
            {now.strftime('%d %B %Y')} | <span style="text-shadow: 0 0 10px #00ced1;">{now.strftime('%H:%M:%S')}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

if st.session_state.menu == "main":
    cols = st.columns(4)
    menu_list = [
        ("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), 
        ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN"),
        ("🔄", "REKAP STASIUN"), ("📈", "TREND"), 
        ("⚙️", "PENGATURAN"), ("📥", "EXPORT/IMPORT")
    ]
    for i, (icon, label) in enumerate(menu_list):
        with cols[i % 4]:
            if st.button(f"{icon}\n\n{label}", key=f"btn_{i}", use_container_width=True):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    tab1, tab2 = st.tabs(["🍯 ANALISA TETES", "🧪 OPTICAL DENSITY (OD)"])
    with tab1:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:35px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            b_baca = st.number_input("Brix Baca Alat", value=1.20, format="%.2f")
            p_baca = st.number_input("Pol Baca Alat", value=0.00, format="%.2f")
            temp = st.number_input("Suhu Lab (°C)", value=30.00, format="%.2f")
            brix_p = b_baca * 10
            kor = get_koreksi_suhu(temp)
            brix_kor = brix_p + kor
        with c2:
            bj = get_bj_icumsa(brix_p)
            pol_p = (0.286 * (p_baca * 2)) / bj
            hk = (pol_p / brix_kor * 100) if brix_kor > 0 else 0.0
            st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
            st.metric("% POL", f"{pol_p:.2f}")
            st.success(f"### HK: {hk:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:35px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        abs_v = st.number_input("Absorbance (Abs)", value=0.000, format="%.3f")
        b_od = st.number_input("Brix untuk OD (x10)", value=12.00)
        bj_od = get_bj_icumsa(b_od)
        od_total = (abs_v * bj_od * 500) / 1
        st.markdown(f"### HASIL OD TETES: {od_total:.4f}")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ DASHBOARD"):
        st.session_state.menu = "main"; st.rerun()

# --- 4. AUTO-REFRESH SETIAP 1 DETIK ---
# Ini yang bikin jam di laptop lo sinkron beb!
time.sleep(1)
st.rerun()
