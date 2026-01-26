import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time
import base64
import os

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Fungsi Sakti buat panggil gambar lokal ke CSS
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return None

# Load Background & Logo
img_bg = get_base64('background.jpg')
img_sgn = get_base64('sgn.png')
img_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: GLOSSY & SHINY EFFECT ---
# Kita pake background-image dari file background.jpg lo beb!
bg_css = f"background-image: url('data:image/jpg;base64,{img_bg}');" if img_bg else "background-color: #1c4e80;"

st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;400;600&display=swap');

    .stApp {{
        {bg_css}
        background-size: cover;
        background-attachment: fixed;
    }}
    
    /* Overlay transparan biar tulisan tetep tajem di depan background */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.7); 
        border-radius: 25px;
        margin-top: 20px;
        padding: 40px !important;
        backdrop-filter: blur(8px); /* Efek kaca buram */
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }}

    /* Header Luxury Blue */
    .header-container {{
        background: linear-gradient(135deg, #1c4e80 0%, #0a2342 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}

    .judul-futuristik {{
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        letter-spacing: 4px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}

    /* TOMBOL MENGKILAP (GLOSSY SHINE) */
    .stButton > button {{
        height: 180px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 20px;
        color: white !important;
        position: relative;
        overflow: hidden;
        transition: 0.4s ease;
    }}

    /* Efek Kilatan Pas Hover ala Luxury Dashboard */
    .stButton > button::after {{
        content: "";
        position: absolute;
        top: -50%;
        left: -100%;
        width: 50%;
        height: 200%;
        background: rgba(255, 255, 255, 0.2);
        transform: rotate(35deg);
        transition: 0.6s;
    }}

    .stButton > button:hover::after {{
        left: 150%;
    }}

    /* Gradasi Biru Mengkilap */
    div[data-testid="column"]:nth-of-type(1) .stButton > button {{ background: linear-gradient(135deg, #72bcd4, #4682b4); }}
    div[data-testid="column"]:nth-of-type(2) .stButton > button {{ background: linear-gradient(135deg, #4682b4, #1c4e80); }}
    div[data-testid="column"]:nth-of-type(3) .stButton > button {{ background: linear-gradient(135deg, #1c4e80, #0a2342); }}

    .stButton > button:hover {{
        transform: scale(1.03) translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.4);
    }}

    .shift-tag {{
        background: #00ced1;
        color: #1c4e80;
        padding: 8px 15px;
        border-radius: 12px;
        font-weight: 800;
        box-shadow: 0 0 15px rgba(0,206,209,0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR & SHIFT SELECTOR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.divider()
    shift_aktif = st.selectbox("Pilih Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["house-heart-fill", "beaker-fill"],
        default_index=0,
    )
    st.info(f"🟢 Petugas: **{shift_aktif}**")

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header Section dengan Logo yang dibalut Base64
    st.markdown(f"""
        <div class="header-container">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="width:150px"> 
                    <img src="data:image/png;base64,{img_sgn if img_sgn else ''}" width="130"> 
                </div>
                <div style="text-align: center;">
                    <h1 class="judul-futuristik">CANE METRIX</h1>
                    <p style="font-family:'Poppins'; opacity:0.8; letter-spacing:1px;">ACCELERATING QA PERFORMANCE</p>
                    <small>{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
                </div>
                <div style="width:150px; text-align:right;"> 
                    <span class="shift-tag">{shift_aktif}</span><br><br>
                    <img src="data:image/png;base64,{img_lpp if img_lpp else ''}" width="110">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h4 style='text-align:center; color:#1c4e80;'>Hello, Planters! Optimization mode active for <b>{shift_aktif}</b>.</h4>", unsafe_allow_html=True)

    # Menu Grid (6 Tombol Mengkilap)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝\nINPUT DATA", key="b1", use_container_width=True)
    with c2: st.button("📊\nDAILY DB", key="b2", use_container_width=True)
    with c3: st.button("📂\nMONTHLY DB", key="b3", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4: st.button("🔄\nSTATIONS", key="b4", use_container_width=True)
    with c5: st.button("🧮\nCALCULATOR", key="b5", use_container_width=True)
    with c6: st.button("👤\nACCOUNT", key="b6", use_container_width=True)

    time.sleep(1)
    st.rerun()

# --- 5. HALAMAN ANALISA (Interpolasi Aman Beb!) ---
elif selected == "Analisa Tetes":
    st.header(f"🧪 Quality Analysis - {shift_aktif}")
    # Logika interpolasi dan hitung QA lo tetep di sini...
    st.info("Form input data lab sedang aktif.")
