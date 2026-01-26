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

# --- 2. CSS SAKTI: GLOW ZONE & GIANT LOGO ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Poppins:wght@400;600;800&display=swap');

    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background: rgba(255, 255, 255, 0.8);
        border-radius: 30px;
        padding: 40px !important;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 20px;
    }}

    /* MEGA HEADER DENGAN GLOW ZONE */
    .mega-header {{
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.95) 0%, rgba(0, 128, 128, 0.9) 100%);
        padding: 50px;
        border-radius: 35px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 20px 40px rgba(0, 128, 128, 0.4);
        margin-bottom: 35px;
    }}

    /* GRADASI TERANG (GLOW) DI BELAKANG LOGO */
    .glow-zone {{
        background: radial-gradient(circle, rgba(255,255,255,0.4) 0%, transparent 70%);
        padding: 20px;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .judul-mega {{
        font-family: 'Orbitron', sans-serif;
        font-size: 75px; /* MAKIN GEDE BEB */
        font-weight: 900;
        letter-spacing: 10px;
        margin: 0;
        line-height: 1;
        background: linear-gradient(to bottom, #ffffff, #00ced1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 20px rgba(255,255,255,0.5));
    }}

    .tagline-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 26px;
        font-weight: 700;
        letter-spacing: 4px;
        margin-top: 15px;
        color: #e0f7fa;
        text-transform: uppercase;
    }}

    .info-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 22px;
        margin-top: 20px;
        color: white;
        border-top: 2px solid rgba(255,255,255,0.3);
        padding-top: 15px;
    }}

    .sapaan-petugas {{
        text-align: center;
        color: #001f3f;
        font-family: 'Poppins', sans-serif;
        font-size: 28px;
        font-weight: 800;
        margin: 30px 0;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8);
    }}

    /* TOMBOL GLASTING MEGA SHINY */
    .stButton > button {{
        height: 190px;
        border-radius: 30px;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        font-size: 24px;
        color: white !important;
        background: linear-gradient(135deg, #001f3f, #008080);
        transition: 0.5s;
        position: relative;
        overflow: hidden;
    }}

    .stButton > button::before {{
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: 0.7s;
    }}

    .stButton > button:hover::before {{ left: 100%; }}
    .stButton > button:hover {{
        transform: translateY(-15px) scale(1.02);
        box-shadow: 0 25px 50px rgba(0, 128, 128, 0.6);
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
    st.info(f"🟢 Petugas: **{shift_pilih}**")

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # MEGA HEADER DENGAN LOGO RAKSASA (250px)
    st.markdown(f"""
        <div class="mega-header">
            <div class="glow-zone">
                <img src="data:image/png;base64,{bin_sgn}" width="250" style="filter: drop-shadow(0 0 15px white);">
            </div>
            <div style="flex: 2; text-align: center;">
                <div style="font-size: 50px; margin-bottom: -10px;">🎋</div>
                <h1 class="judul-mega">CANE METRIX</h1>
                <p class="tagline-mega">Accelerating QA Performance</p>
                <div class="info-mega">
                    <b>{now.strftime('%d %B %Y')}</b> &nbsp; | &nbsp; <b>{now.strftime('%H:%M:%S')}</b>
                </div>
            </div>
            <div class="glow-zone">
                <img src="data:image/png;base64,{bin_lpp}" width="250" style="filter: drop-shadow(0 0 15px white);">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="sapaan-petugas">
            Hello, Planters! Optimization mode active for <span style="color: #008080;">{shift_pilih}</span>.
        </div>
    """, unsafe_allow_html=True)

    # Menu Grid Glasting
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

elif selected == "Analisa Tetes":
    st.markdown(f"<h2 style='color:#001f3f;'>🧪 Analysis - {shift_pilih}</h2>", unsafe_allow_html=True)
