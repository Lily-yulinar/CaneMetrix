import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Fungsi Encode Gambar (Penting biar muncul!)
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# Ambil string base64 buat background dan logo
bin_bg = get_base64_of_bin_file('background.jpg')
bin_sgn = get_base64_of_bin_file('sgn.png')
bin_lpp = get_base64_of_bin_file('lpp.png')

# --- 2. CSS CUSTOM: LUXURY & SHINY ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Background Utama */
    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Overlay Kaca (Glassmorphism) */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 40px !important;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 30px;
    }}

    /* Header Midnight Luxury */
    .luxury-header {{
        background: linear-gradient(135deg, #001f3f 0%, #003366 100%);
        padding: 30px;
        border-radius: 20px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 4px solid #00ced1;
        margin-bottom: 20px;
    }}

    .judul-header {{
        font-family: 'Orbitron', sans-serif;
        font-size: 48px;
        letter-spacing: 5px;
        margin: 0;
        text-shadow: 0 0 15px rgba(0,206,209,0.4);
    }}

    /* Tombol Menu Glossy */
    .stButton > button {{
        height: 180px;
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 22px;
        color: white !important;
        background: linear-gradient(135deg, #003366, #001f3f);
        transition: 0.5s;
        overflow: hidden;
    }}

    /* Efek Kilau Pas Hover */
    .stButton > button:hover {{
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        border: 2px solid #00ced1 !important;
    }}

    .shift-label {{
        color: #00ced1;
        font-weight: bold;
        letter-spacing: 2px;
        font-size: 18px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Pilih Shift Tugas:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["grid-fill", "vial"],
        default_index=0,
    )
    st.info(f"🟢 Petugas Aktif: {shift_pilih}")

# --- 4. HALAMAN DASHBOARD ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Custom Header Luxury
    st.markdown(f"""
        <div class="luxury-header">
            <div style="flex: 1;">
                <img src="data:image/png;base64,{bin_sgn}" width="140">
            </div>
            <div style="flex: 2; text-align: center;">
                <h1 class="judul-header">CANE METRIX</h1>
                <p style="font-family: 'Poppins'; opacity: 0.8; margin:0;">ACCELERATING QA PERFORMANCE</p>
                <small>{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
            </div>
            <div style="flex: 1; text-align: right;">
                <div class="shift-label">{shift_pilih}</div>
                <img src="data:image/png;base64,{bin_lpp}" width="120" style="margin-top:10px;">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h4 style='text-align:center; color:#001f3f;'>Welcome, Planters! Let's optimize <b>{shift_pilih}</b> analysis today.</h4>", unsafe_allow_html=True)

    # Grid Bento Box
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝\nINPUT DATA", key="btn1", use_container_width=True)
    with c2: st.button("📊\nDAILY DB", key="btn2", use_container_width=True)
    with c3: st.button("📂\nMONTHLY DB", key="btn3", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4: st.button("🔄\nSTATIONS", key="btn4", use_container_width=True)
    with c5: st.button("🧮\nCALCULATOR", key="btn5", use_container_width=True)
    with c6: st.button("👤\nACCOUNT", key="btn6", use_container_width=True)

    time.sleep(1)
    st.rerun()

# --- 5. HALAMAN ANALISA (Fungsi Asli Tetap Aman) ---
elif selected == "Analisa Tetes":
    st.markdown(f"<h2>🧪 Quality Analysis - {shift_pilih}</h2>", unsafe_allow_html=True)
    # Masukkan fungsi interpolasi & perhitungan lo di sini sayang...
    with st.container(border=True):
        st.write("Ready for QA Measurement.")
