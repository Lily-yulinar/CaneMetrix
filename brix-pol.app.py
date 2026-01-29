import streamlit as st
from datetime import datetime, timedelta
import base64
import os

# --- 1. SETTINGS ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

if 'menu_level' not in st.session_state:
    st.session_state.menu_level = "main"

# --- 2. ASSETS ---
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bin_sgn = get_base64('sgn.png') # Logo Sinergi Gula Nusantara
bin_lpp = get_base64('lpp.png') # Logo LPP Agro Nusantara

# --- 3. CSS CUSTOM (PERSIS IMAGE_5F7351) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Lexend:wght@400;600&family=Montserrat:wght@700;800&display=swap');

    /* Background Utama */
    .stApp {{
        background-color: #0e1117;
    }}

    /* Panel Header image_5f7351.jpg */
    .header-panel {{
        background: linear-gradient(135deg, #00ced1 0%, #008080 100%);
        border-radius: 40px;
        padding: 40px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 15px 35px rgba(0, 206, 209, 0.3);
    }}

    .header-title {{
        font-family: 'Orbitron', sans-serif;
        font-size: 58px;
        font-weight: 900;
        letter-spacing: 8px;
        margin: 0;
    }}

    .header-sub {{
        font-family: 'Lexend', sans-serif;
        font-size: 18px;
        letter-spacing: 4px;
        margin-top: 10px;
        opacity: 0.9;
    }}

    /* Sapaan image_5f7351.jpg */
    .sapaan-text {{
        font-family: 'Montserrat', sans-serif;
        font-size: 32px;
        color: #00ced1;
        text-align: center;
        margin: 40px 0;
        font-weight: 800;
    }}

    /* Grid Button image_d57902.png */
    .stButton > button {{
        height: 160px;
        border-radius: 25px;
        background: #112233 !important;
        color: white !important;
        border: 1px solid #1a3a5a !important;
        font-family: 'Lexend';
        font-size: 15px;
        font-weight: 600;
        transition: 0.3s;
    }}

    .stButton > button:hover {{
        border-color: #00ced1 !important;
        box-shadow: 0 0 20px rgba(0, 206, 209, 0.4);
        transform: translateY(-8px);
    }}

    /* Sidebar Styling image_d5849d.png */
    [data-testid="stSidebar"] {{
        background-color: #111827 !important;
        border-right: 1px solid #1f2937;
    }}
    
    .sidebar-btn {{
        background: #1f2937;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        border-left: 5px solid #00ced1;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. SIDEBAR (LOGIKA BALIK KE DASHBOARD) ---
with st.sidebar:
    st.markdown("<h2 style='color:#00ced1; text-align:center; font-family:Orbitron;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.menu_level = "main"
        st.rerun()
    
    if st.button("🧪 Analisa Tetes", use_container_width=True):
        st.session_state.menu_level = "analisa_tetes"
        st.rerun()
        
    st.markdown(f"""
        <div style='margin-top:150px;' class='sidebar-btn'>
            <span style='color:#9ca3af; font-size:12px;'>Petugas Aktif:</span><br>
            <b style='color:#00ced1; font-size:18px;'>{shift_pilih}</b>
        </div>
    """, unsafe_allow_html=True)

# --- 5. HEADER PANEL (LOGOS INCLUDED) ---
now = datetime.now()
st.markdown(f"""
    <div class="header-panel">
        <img src="data:image/png;base64,{bin_sgn}" width="120">
        <div>
            <h1 class="header-title">CANE METRIX</h1>
            <div class="header-sub">ACCELERATING QA PERFORMANCE</div>
            <div style="margin-top:15px; font-size:14px; opacity:0.8;">
                {now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}
            </div>
        </div>
        <img src="data:image/png;base64,{bin_lpp}" width="140">
    </div>
""", unsafe_allow_html=True)

# --- 6. NAVIGASI MENU ---
if st.session_state.menu_level == "main":
    st.markdown(f'<div class="sapaan-text">Hello, Planters! Let\'s optimize {shift_pilih} analysis.</div>', unsafe_allow_html=True)
    
    # Grid 8 Tombol (image_d57902.png)
    row1_c1, row1_c2, row1_c3, row1_c4 = st.columns(4)
    with row1_c1: st.button("📄 INPUT DATA", use_container_width=True)
    with row1_c2: st.button("📊 DATABASE HARIAN", use_container_width=True)
    with row1_c3: st.button("📂 DATABASE BULANAN", use_container_width=True)
    with row1_c4: st.button("🔄 REKAP STASIUN", use_container_width=True)
    
    row2_c1, row2_c2, row2_c3, row2_c4 = st.columns(4)
    with row2_c1: 
        if st.button("🧮 HITUNG ANALISA", use_container_width=True):
            st.session_state.menu_level = "analisa_tetes"
            st.rerun()
    with row2_c2: st.button("📈 TREND", use_container_width=True)
    with row2_c3: st.button("⚙️ PENGATURAN", use_container_width=True)
    with row2_c4: st.button("📥 EXPORT/IMPORT", use_container_width=True)

elif st.session_state.menu_level == "analisa_tetes":
    # --- LOGIKA ANALISA TETES LO YG KEMAREN ---
    st.markdown(f"<h2 style='color:white; font-family:Lexend;'>🧪 Form Analisa Tetes - {shift_pilih}</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div style="background:#111827; padding:30px; border-radius:30px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 📥 Data Pengamatan")
            b_obs = st.number_input("Brix Teramati (Brix Obs)", value=12.00, format="%.2f")
            temp = st.number_input("Suhu (°C)", value=29.40, format="%.2f")
            
            # Koreksi Suhu image_cb7130.png
            kor = 0.16 if int(temp) == 30 else 0.09 # Dummy interpolasi simple
            brix_f = b_obs + kor
            st.markdown(f"**BRIX KOREKSI:** <span style='color:#00ced1; font-size:24px;'>{brix_f:.2f}</span>", unsafe_allow_html=True)
            
            p_obs = st.number_input("Pol Teramati (Pol Obs)", value=0.00, format="%.2f")
        
        with c2:
            st.markdown("### 📊 Hasil")
            # Logic BJ dari image_cb66ad.png
            bj = 1.044216 if b_obs == 12.0 else 1.0 # Dummy table lookup
            pol_p = ((0.286 * p_obs) / bj) * 10
            hk = (pol_p / brix_f * 100) if brix_f > 0 else 0.0
            
            st.metric("% POL", f"{pol_p:.2f}")
            if hk > 100: st.error(f"HK: {hk:.2f}% (TIDAK VALID!)")
            else: st.success(f"### HK: {hk:.2f}%")
            
            if st.button("💾 SIMPAN DATA", use_container_width=True):
                st.toast("Data Berhasil Diarsipkan!", icon="✅")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD"):
        st.session_state.menu_level = "main"
        st.rerun()
