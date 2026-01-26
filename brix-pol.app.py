import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Fungsi Encode Gambar (Tanpa ini background & logo lokal gak bakal muncul)
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

# Load semua aset gambar
bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: LUXURY GLASTING & SHINY ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Background Utama: Fix agar background.jpg muncul */
    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Overlay Glassmorphism kontainer utama */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.7);
        border-radius: 30px;
        padding: 40px !important;
        backdrop-filter: blur(12px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.2);
        margin-top: 30px;
    }}

    /* Header Luxury Blue Muda (Glasting Edition) */
    .glasting-header {{
        background: linear-gradient(135deg, rgba(28, 78, 128, 0.9) 0%, rgba(0, 206, 209, 0.8) 100%);
        padding: 25px;
        border-radius: 25px;
        color: white;
        display: flex;
        justify-content: space-between;
        align-items: center;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 0 20px rgba(0, 206, 209, 0.3);
        margin-bottom: 25px;
    }}

    .judul-wrapper {{
        text-align: center;
        flex: 2;
    }}

    .judul-futuristik {{
        font-family: 'Orbitron', sans-serif;
        font-size: 50px;
        letter-spacing: 6px;
        margin: 0;
        background: linear-gradient(to bottom, #ffffff, #aed9f4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        filter: drop-shadow(0 0 8px rgba(255,255,255,0.5));
    }}

    /* TOMBOL SUB-MENU: Glasting Effect on Hover */
    .stButton > button {{
        height: 180px;
        border-radius: 25px;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 20px;
        color: white !important;
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.8), rgba(0, 51, 102, 0.9));
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        position: relative;
        overflow: hidden;
    }}

    /* Efek Kilatan (Glasting) saat kursor geser */
    .stButton > button::before {{
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.4), transparent);
        transition: 0.5s;
    }}

    .stButton > button:hover::before {{
        left: 100%;
    }}

    .stButton > button:hover {{
        transform: translateY(-12px);
        box-shadow: 0 20px 40px rgba(0, 206, 209, 0.4);
        border: 2px solid #00ced1 !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (Shift di sini saja) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    st.write("⚙️ **Control Panel**")
    shift_pilih = st.selectbox("Shift Tugas:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["grid-fill", "vial"],
        default_index=0,
    )
    st.divider()
    st.info(f"🟢 Petugas: **{shift_pilih}**")

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header Luxury Glasting (Shift dihapus, diganti Logo Cane Metrix di judul)
    st.markdown(f"""
        <div class="glasting-header">
            <div style="flex: 1; text-align: left;">
                <img src="data:image/png;base64,{bin_sgn}" width="150">
            </div>
            <div class="judul-wrapper">
                <div style="font-size: 30px; margin-bottom: -10px;">🎋</div>
                <h1 class="judul-futuristik">CANE METRIX</h1>
                <p style="font-family: 'Poppins'; font-weight: 300; letter-spacing: 2px; margin:0;">ACCELERATING QA PERFORMANCE</p>
                <small style="opacity: 0.8;">{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{bin_lpp}" width="130">
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h4 style='text-align:center; color:#1c4e80; font-family:Poppins;'>Hello, Planters! Optimized for <b>{shift_pilih}</b>.</h4>", unsafe_allow_html=True)

    # Grid Bento Box (Shiny Glasting)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📝\nINPUT DATA", key="b1", use_container_width=True)
    with c2: st.button("📊\nDAILY DB", key="b2", use_container_width=True)
    with c3: st.button("📂\nMONTHLY DB", key="b3", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4: st.button("🔄\nSTATIONS", key="b4", use_container_width=True)
    with c5: st.button("🧮\nCALCULATOR", key="b5", use_container_width=True)
    with c6: st.button("⚙️\nSETTINGS", key="b6", use_container_width=True)

    time.sleep(1)
    st.rerun()

# --- 5. ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.markdown(f"<h2>🧪 Quality Analysis - {shift_pilih}</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        st.write("Ready to process analysis.")
