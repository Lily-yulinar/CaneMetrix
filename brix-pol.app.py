import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: EYE-CATCHING & BALANCED ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@700;800&family=Poppins:wght@400;600;800&display=swap');

    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 30px !important;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 15px;
    }}

    /* HEADER BALANCED (Lebih Kecil & Rapi) */
    .mega-header {{
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.95) 0%, rgba(0, 100, 100, 0.9) 100%);
        padding: 25px 50px;
        border-radius: 25px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 10px 30px rgba(0, 100, 100, 0.4);
        margin-bottom: 25px;
    }}

    .glow-zone {{
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, transparent 70%);
        padding: 10px;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .judul-mega {{
        font-family: 'Orbitron', sans-serif;
        font-size: 48px; /* Dikecilkan dikit biar compact */
        font-weight: 900;
        letter-spacing: 6px;
        margin: 0;
        background: linear-gradient(to bottom, #ffffff, #00ced1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }}

    .tagline-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        font-weight: 600;
        letter-spacing: 2px;
        color: #e0f7fa;
        text-transform: uppercase;
    }}

    .info-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        margin-top: 10px;
        color: #ffffff;
        border-top: 1px solid rgba(255,255,255,0.3);
        padding-top: 8px;
    }}

    /* SAPAAN DENGAN EFEK TERANG */
    .sapaan-petugas {{
        text-align: center;
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 800;
        margin: 20px 0;
        text-shadow: 0 0 10px rgba(0, 206, 209, 0.8), 0 0 20px rgba(0, 0, 0, 0.5);
    }}

    /* SUB-MENU: EYE CATCHING FONT */
    .stButton > button {{
        height: 150px;
        border-radius: 20px;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        font-family: 'Montserrat', sans-serif; /* Ganti font lebih keren */
        font-weight: 800;
        font-size: 20px;
        color: white !important;
        background: linear-gradient(135deg, #001f3f, #006666);
        transition: 0.4s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}

    .stButton > button:hover {{
        transform: translateY(-8px);
        box-shadow: 0 15px 30px rgba(0, 206, 209, 0.5);
        background: linear-gradient(135deg, #003366, #00ced1);
        border: 2px solid #ffffff !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    selected = option_menu(None, ["Dashboard", "Analisa Tetes"], icons=["grid-fill", "vial"], default_index=0)

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # HEADER DENGAN LOGO BALANCE
    st.markdown(f"""
        <div class="mega-header">
            <div class="glow-zone">
                <img src="data:image/png;base64,{bin_sgn}" width="160">
            </div>
            <div style="flex: 2; text-align: center;">
                <h1 class="judul-mega">CANE METRIX</h1>
                <p class="tagline-mega">Accelerating QA Performance</p>
                <div class="info-mega">
                    <b>{now.strftime('%d %B %Y')}</b> &nbsp; | &nbsp; <b>{now.strftime('%H:%M:%S')}</b>
                </div>
            </div>
            <div class="glow-zone">
                <img src="data:image/png;base64,{bin_lpp}" width="160">
            </div>
        </div>
    """, unsafe_allow_html=True)

    # SAPAAN YANG MUDAH DIBACA
    st.markdown(f"""
        <div class="sapaan-petugas">
            HELLO PLANTERS! OPTIMIZATION MODE: <span style="color: #00ced1;">{shift_pilih}</span>
        </div>
    """, unsafe_allow_html=True)

    # Menu Grid Eye-Catching
    m1, m2, m3 = st.columns(3)
    with m1: st.button("📝\nINPUT DATA", key="btn1", use_container_width=True)
    with m2: st.button("📊\nDAILY DB", key="btn2", use_container_width=True)
    with m3: st.button("📂\nMONTHLY DB", key="btn3", use_container_width=True)

    m4, m5, m6 = st.columns(3)
    with m4: st.button("🔄\nSTATIONS", key="btn4", use_container_width=True)
    with m5: st.button("🧮\nCALCULATOR", key="btn5", use_container_width=True)
    with m6: st.button("👤\nACCOUNT", key="btn6", use_container_width=True)

    time.sleep(1)
    st.rerun()
