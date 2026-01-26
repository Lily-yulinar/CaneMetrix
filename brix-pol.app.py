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

# Load Aset Gambar
bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: LUXURY GLASTING & MODERN FONTS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Syncopate:wght@700&family=Montserrat:wght@800&family=Poppins:wght@400;600&display=swap');

    /* Background Setup */
    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Glassmorphism Container */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 30px !important;
        backdrop-filter: blur(15px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 15px;
    }}

    /* Balanced Luxury Header */
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

    .judul-mega {{
        font-family: 'Orbitron', sans-serif;
        font-size: 48px;
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
        margin-top: 5px;
    }}

    /* Glow Sapaan Petugas */
    .sapaan-petugas {{
        text-align: center;
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 800;
        margin: 25px 0;
        text-shadow: 0 0 10px rgba(0, 206, 209, 0.8), 0 0 20px rgba(0, 0, 0, 0.5);
        text-transform: uppercase;
    }}

    /* Sub-Menu Eye Catching (Syncopate Font) */
    .stButton > button {{
        height: 140px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-family: 'Syncopate', sans-serif;
        font-weight: 700;
        font-size: 13px;
        color: white !important;
        background: linear-gradient(145deg, rgba(0, 31, 63, 0.9), rgba(0, 60, 60, 0.8));
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    .stButton > button:hover {{
        transform: scale(1.05);
        background: linear-gradient(145deg, #004080, #00ced1);
        border: 1px solid #ffffff !important;
        box-shadow: 0 10px 25px rgba(0, 206, 209, 0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Pilih Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    selected = option_menu(None, ["Dashboard", "Analisa Tetes"], 
                          icons=["grid-fill", "vial"], 
                          default_index=0,
                          styles={
                              "nav-link-selected": {"background-color": "#00ced1"}
                          })
    st.divider()
    st.info(f"🟢 Petugas Aktif: **{shift_pilih}**")

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header Section
    st.markdown(f"""
        <div class="mega-header">
            <div style="flex: 1; text-align: left;">
                <img src="data:image/png;base64,{bin_sgn}" width="150">
            </div>
            <div style="flex: 2; text-align: center;">
                <div style="font-size: 30px; margin-bottom: -10px;">🎋</div>
                <h1 class="judul-mega">CANE METRIX</h1>
                <p class="tagline-mega">Accelerating QA Performance</p>
                <div style="border-top: 1px solid rgba(255,255,255,0.3); margin-top: 10px; padding-top: 5px;">
                    <small><b>{now.strftime('%d %B %Y')}</b> | <b>{now.strftime('%H:%M:%S')}</b></small>
                </div>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{bin_lpp}" width="150">
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Sapaan Petugas (Glowing Montserrat)
    st.markdown(f"""
        <div class="sapaan-petugas">
            HELLO PLANTERS! OPTIMIZATION MODE: <span style="color: #00ced1;">{shift_pilih}</span>
        </div>
    """, unsafe_allow_html=True)

    # GRID SUB-MENU (8 Tombol Eye-Catching)
    # Baris 1
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.button("📝\nINPUT DATA", key="m1", use_container_width=True)
    with m2: st.button("📊\nDATABASE HARIAN", key="m2", use_container_width=True)
    with m3: st.button("📂\nDATABASE BULANAN", key="m3", use_container_width=True)
    with m4: st.button("🔄\nREKAP STASIUN", key="m4", use_container_width=True)

    # Baris 2
    m5, m6, m7, m8 = st.columns(4)
    with m5: st.button("🧮\nHITUNG ANALISA", key="m5", use_container_width=True)
    with m6: st.button("📈\nTREND", key="m6", use_container_width=True)
    with m7: st.button("⚙️\nPENGATURAN", key="m7", use_container_width=True)
    with m8: st.button("📥\nEXPORT/IMPORT", key="m8", use_container_width=True)

    time.sleep(1)
    st.rerun()

# --- 5. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.markdown(f"<h2 style='color:#001f3f; font-family:Montserrat;'>🧪 Analysis Module - {shift_pilih}</h2>", unsafe_allow_html=True)
    st.write("Silakan masukkan parameter lab di bawah ini.")
    # Tambahkan form analisa lo di sini beb...
