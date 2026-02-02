import streamlit as st
from datetime import datetime
import pandas as pd
import time

# --- 1. SETTINGS & LUXURY UI ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');

    .stApp { background-color: #050a10; }
    
    /* Luxury Glass Header */
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

    /* Grid Sub-menu Kotak (image_5f7351) */
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

    /* Efek Pop-up Neon & Luxury Glass */
    .stButton > button:hover {
        transform: scale(1.08) translateY(-10px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px #00ced1, inset 0 0 10px rgba(0,206,209,0.5) !important;
        background: rgba(0, 206, 209, 0.1) !important;
    }

    .sapaan {
        font-family: 'Montserrat';
        font-size: 32px;
        color: #00ced1;
        text-align: center;
        margin: 40px 0;
        text-shadow: 0 0 10px rgba(0,206,209,0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA TABEL SUHU (image_cb7130 / image_fbe792) ---
def get_koreksi_fisik(temp):
    # Mapping Data dari Foto Tabel Beb!
    tabel_suhu = {
        25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09, 30: 0.16,
        31: 0.24, 32: 0.315, 33: 0.385, 34: 0.465, 35: 0.54, 36: 0.62,
        37: 0.70, 38: 0.78, 39: 0.86, 40: 0.94, 41: 1.02, 42: 1.10
    }
    t_round = int(temp)
    if t_round in tabel_suhu:
        # Interpolasi halus antar derajat
        val1 = tabel_suhu[t_round]
        val2 = tabel_suhu.get(t_round + 1, val1 + 0.08)
        return val1 + (temp - t_round) * (val2 - val1)
    return 0.0

def get_bj_standard(brix):
    # Logika Berat Jenis (image_cb66ad.png)
    return 1.000 + (brix * 0.00388)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h1 style='color:#00ced1; font-family:Orbitron; text-align:center;'>🎋 CANE METRIX</h1>", unsafe_allow_html=True)
    st.divider()
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    if st.button("🏠 DASHBOARD UTAMA", use_container_width=True):
        st.session_state.menu_level = "main"; st.rerun()

# --- 4. HEADER PANEL (image_5f187d) ---
now = datetime.now()
st.markdown(f"""
    <div class="header-panel">
        <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0;">CANE METRIX</h1>
        <p style="font-family:Lexend; letter-spacing:5px; margin-bottom:15px;">ACCELERATING QA PERFORMANCE</p>
        <div style="border-top:1px solid rgba(255,255,255,0.2); width:50%; margin: 10px auto;"></div>
        <div style="font-family:Orbitron; color:#00ced1; font-size:20px; margin-top:10px;">
            {now.strftime('%d %B %Y')} | <span style="text-shadow: 0 0 10px #00ced1;">{now.strftime('%H:%M:%S')}</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. NAVIGATION ---
if 'menu_level' not in st.session_state: st.session_state.menu_level = "main"

if st.session_state.menu_level == "main":
    st.markdown(f'<div class="sapaan">Hello, Planters! Let\'s optimize {shift_pilih} analysis.</div>', unsafe_allow_html=True)
    
    # Grid 8 Menu Kotak (image_5f7351)
    menu_items = [
        ("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), 
        ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN"),
        ("🔄", "REKAP STASIUN"), ("📈", "TREND"), 
        ("⚙️", "PENGATURAN"), ("📥", "EXPORT/IMPORT DATA")
    ]
    
    cols = st.columns(4)
    for i, (icon, label) in enumerate(menu_items):
        with cols[i % 4]:
            if st.button(f"{icon}\n\n{label}", key=f"m_{i}", use_container_width=True):
                if label == "HITUNG ANALISA":
                    st.session_state.menu_level = "hitung"; st.rerun()

elif st.session_state.menu_level == "hitung":
    st.markdown("<h2 style='color:white; font-family:Lexend;'>🧪 Laboratory Calculation</h2>", unsafe_allow_html=True)
    
    tab_tetes, tab_od = st.tabs(["🍯 ANALISA TETES", "🧪 OPTICAL DENSITY (OD)"])
    
    with tab_tetes:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:30px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            b_baca = st.number_input("Brix Baca", value=12.00, step=0.01)
            p_baca = st.number_input("Pol Baca", value=0.00, step=0.01)
            temp = st.number_input("Suhu Lab (°C)", value=28.00, step=0.1)
            
            # Rumus Request Lo Beb
            brix_persen = b_baca * 10
            kor_val = get_koreksi_fisik(temp)
            brix_kor = brix_persen + kor_val
            
        with c2:
            bj = get_bj_standard(brix_persen)
            # %pol = (0,286 x (pol baca x 2)) / BJ
            pol_persen = (0.286 * (p_baca * 2)) / bj
            hk = (pol_persen / brix_kor * 100) if brix_kor > 0 else 0.0
            
            st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
            st.metric("% POL TETES", f"{pol_persen:.2f}")
            st.success(f"### HK (PURITY): {hk:.2f}%")
            st.caption(f"Koreksi Tabel: {kor_val:+.2f} | BJ ICUMSA: {bj:.5f}")
        st.markdown('</div>', unsafe_allow_html=True)

    with tab_od:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:30px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        abs_val = st.number_input("Absorbance (Abs)", value=0.000, step=0.001, format="%.3f")
        b_asli = st.number_input("Brix Asli (Massa Sampel)", value=12.00)
        
        # OD = Abs x BJ dari %brix asli / 1
        bj_asli = get_bj_standard(b_asli)
        od_final = (abs_val * bj_asli) / 1
        
        st.markdown(f"""
            <div style='background:rgba(0,206,209,0.1); padding:25px; border-radius:15px; border-left:8px solid #00ced1;'>
                <span style='color:#00ced1;'>HASIL OPTICAL DENSITY:</span><br>
                <b style='font-size:45px; color:white; font-family:Orbitron;'>{od_final:.4f}</b>
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD", use_container_width=True):
        st.session_state.menu_level = "main"; st.rerun()

# --- 6. AUTO REFRESH JAM ---
time.sleep(1)
st.rerun()
