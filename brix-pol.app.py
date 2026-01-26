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

# --- 2. CSS SAKTI: MEGA HEADER & BOLD TEXT ---
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

    /* MEGA HEADER GLASTING */
    .mega-header {{
        background: linear-gradient(135deg, rgba(0, 48, 96, 0.95) 0%, rgba(0, 160, 176, 0.9) 100%);
        padding: 40px 50px;
        border-radius: 30px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 2px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 15px 35px rgba(0, 160, 176, 0.5);
        margin-bottom: 30px;
        text-align: center;
    }}

    /* Judul Super Besar */
    .judul-mega {{
        font-family: 'Orbitron', sans-serif;
        font-size: 65px; /* GEDE BANGET BEB */
        font-weight: 900;
        letter-spacing: 8px;
        margin: 0;
        line-height: 1;
        background: linear-gradient(to bottom, #ffffff, #a2e3fa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 15px rgba(255,255,255,0.4));
    }}

    /* Tagline Gede */
    .tagline-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 22px; /* GEDEIN DIKIT */
        font-weight: 600;
        letter-spacing: 3px;
        margin-top: 10px;
        color: #e0f7fa;
        text-transform: uppercase;
    }}

    /* Jam & Tanggal Gede */
    .info-mega {{
        font-family: 'Poppins', sans-serif;
        font-size: 20px;
        font-weight: 400;
        margin-top: 15px;
        color: rgba(255,255,255,0.9);
        border-top: 1px solid rgba(255,255,255,0.2);
        padding-top: 10px;
    }}

    /* Sapaan Petugas (BIAR KELIHATAN) */
    .sapaan-petugas {{
        text-align: center;
        color: #003060; /* Biru Tua Bold */
        font-family: 'Poppins', sans-serif;
        font-size: 24px;
        font-weight: 800;
        margin: 20px 0;
    }}

    /* TOMBOL GLASTING SHINY */
    .stButton > button {{
        height: 180px;
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 22px;
        color: white !important;
        background: linear-gradient(135deg, #001f3f, #004b78);
        transition: 0.4s;
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
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
        transition: 0.6s;
    }}

    .stButton > button:hover::before {{ left: 100%; }}
    .stButton > button:hover {{
        transform: translateY(-12px);
        box-shadow: 0 20px 40px rgba(0, 160, 176, 0.6);
        border: 2px solid #00ced1 !important;
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
    
    # MEGA HEADER (LOGO 95px)
    st.markdown(f"""
        <div class="mega-header">
            <div style="flex: 1; text-align: left;">
                <img src="data:image/png;base64,{bin_sgn}" width="110">
            </div>
            <div style="flex: 3; text-align: center;">
                <div style="font-size: 40px; margin-bottom: -15px;">🎋</div>
                <h1 class="judul-mega">CANE METRIX</h1>
                <p class="tagline-mega">Accelerating QA Performance</p>
                <div class="info-mega">
                    <b>{now.strftime('%d %B %Y')}</b> &nbsp; | &nbsp; <b>{now.strftime('%H:%M:%S')}</b>
                </div>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{bin_lpp}" width="110">
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Tulisan Sapaan yang sekarang SANGAT KELIHATAN
    st.markdown(f"""
        <div class="sapaan-petugas">
            Hello, Planters! Let's optimize <span style="color: #00ced1;">{shift_pilih}</span> analysis today.
        </div>
    """, unsafe_allow_html=True)

    # Menu Grid
    m1, m2, m3 = st.columns(3)
    with m1: st.button("📝\nINPUT DATA", key="m1", use_container_width=True)
    with m2: st.button("📊\nDAILY DB", key="m2", use_container_width=True)
    with m3: st.button("📂\nMONTHLY DB", key="m3", use_container_width=True)

    m4, m5, m6 = st.columns(3)
    with m4: st.button("🔄\nSTATIONS", key="m4", use_container_width=True)
    with m5: st.button("🧮\nCALCULATOR", key="m5", use_container_width=True)
    with m6: st.button("👤\nACCOUNT", key="m6", use_container_width=True)

    time.sleep(1)
    st.rerun()

elif selected == "Analisa Tetes":
    st.markdown(f"<h2 style='color:#003060;'>🧪 Analysis - {shift_pilih}</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        st.write("Ready to process data.")
