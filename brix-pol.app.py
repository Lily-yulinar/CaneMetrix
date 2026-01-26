import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Fungsi Encode Gambar Lokal ke Base64
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# Load Aset
bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: LUXURY GLASTING ---
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

    /* Kontainer Utama (Glassmorphism) */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 40px !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.2);
        margin-top: 30px;
    }}

    /* Header Glasting Biru Luxury */
    .luxury-header {{
        background: linear-gradient(135deg, rgba(0, 150, 199, 0.9) 0%, rgba(0, 206, 209, 0.8) 100%);
        padding: 25px 45px;
        border-radius: 25px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.5);
        box-shadow: 0 8px 32px rgba(0, 206, 209, 0.4);
        margin-bottom: 25px;
    }}

    .judul-futuristik {{
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        letter-spacing: 5px;
        margin: 0;
        background: linear-gradient(to bottom, #ffffff, #e0f7fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 10px rgba(255,255,255,0.6));
    }}

    /* TOMBOL MENU GLASTING SHINY */
    .stButton > button {{
        height: 180px;
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 20px;
        color: white !important;
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.85), rgba(0, 75, 120, 0.9));
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
    }}

    /* Kilatan Cahaya pas Cursor Geser */
    .stButton > button::before {{
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: 0.6s;
    }}

    .stButton > button:hover::before {{
        left: 100%;
    }}

    .stButton > button:hover {{
        transform: translateY(-10px);
        box-shadow: 0 15px 35px rgba(0, 206, 209, 0.4);
        border: 2px solid #00ced1 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["grid-fill", "vial"],
        default_index=0,
    )
    st.info(f"🟢 Petugas: **{shift_pilih}**")

# --- 4. DASHBOARD ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header Section (Logo Ukuran Pas & Simetris)
    st.markdown(f"""
        <div class="luxury-header">
            <div style="flex: 1; text-align: left;">
                <img src="data:image/png;base64,{bin_sgn}" width="95">
            </div>
            <div style="flex: 2; text-align: center;">
                <div style="font-size: 28px; margin-bottom: -10px;">🎋</div>
                <h1 class="judul-futuristik">CANE METRIX</h1>
                <p style="font-family: 'Poppins'; font-weight: 300; letter-spacing: 1px; margin:0; font-size: 14px;">ACCELERATING QA PERFORMANCE</p>
                <small style="opacity: 0.9;">{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{bin_lpp}" width="95">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h4 style='text-align:center; color:#001f3f; font-family:Poppins;'>Hello, Planters! Let's optimize <b>{shift_pilih}</b> analysis.</h4>", unsafe_allow_html=True)

    # Menu Grid Shiny
    m1, m2, m3 = st.columns(3)
    with m1: st.button("📝\nINPUT DATA", key="b1", use_container_width=True)
    with m2: st.button("📊\nDAILY DB", key="b2", use_container_width=True)
    with m3: st.button("📂\nMONTHLY DB", key="b3", use_container_width=True)

    m4, m5, m6 = st.columns(3)
    with m4: st.button("🔄\nSTATIONS", key="b4", use_container_width=True)
    with m5: st.button("🧮\nCALCULATOR", key="b5", use_container_width=True)
    with m6: st.button("👤\nACCOUNT", key="b6", use_container_width=True)

    time.sleep(1)
    st.rerun()

# --- 5. ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.markdown(f"<h2>🧪 Quality Analysis - {shift_pilih}</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        st.write("Form input data lab aktif.")
