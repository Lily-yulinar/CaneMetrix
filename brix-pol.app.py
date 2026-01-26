import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Inisialisasi Session State untuk Navigasi Menu
if 'menu_level' not in st.session_state:
    st.session_state.menu_level = "main"

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: UI/UX PREMIUM ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Lexend:wght@400;600;800&family=Montserrat:wght@800&family=Poppins:wght@400;600&display=swap');

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
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 15px;
    }}

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

    .sapaan-petugas {{
        text-align: center;
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 800;
        margin: 25px 0;
        text-shadow: 0 0 10px rgba(0, 206, 209, 0.8), 0 0 20px rgba(0, 0, 0, 0.5);
    }}

    /* TOMBOL UI/UX (Lexend + Vertical Layout) */
    .stButton > button {{
        height: 160px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 600;
        font-size: 14px;
        color: white !important;
        background: linear-gradient(145deg, rgba(10, 25, 41, 0.9), rgba(0, 60, 60, 0.8));
        transition: all 0.3s ease-in-out;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }}

    .stButton > button:hover {{
        transform: translateY(-10px);
        background: linear-gradient(145deg, #004080, #00ced1);
        border: 1px solid #00ced1 !important;
        box-shadow: 0 15px 40px rgba(0, 206, 209, 0.5);
    }}

    .btn-back > button {{
        height: 50px !important;
        background: #ff4b4b !important;
        font-size: 16px !important;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    if st.button("🏠 Kembali ke Dashboard"):
        st.session_state.menu_level = "main"
    st.divider()
    st.info(f"Petugas: **{shift_pilih}**")

# --- 4. HEADER & SAPAAN (Tetap Muncul) ---
now = datetime.utcnow() + timedelta(hours=7)
st.markdown(f"""
    <div class="mega-header">
        <div style="flex: 1; text-align: left;"><img src="data:image/png;base64,{bin_sgn}" width="150"></div>
        <div style="flex: 2; text-align: center;">
            <h1 class="judul-mega">CANE METRIX</h1>
            <p style="font-family:Poppins; letter-spacing:2px; font-weight:600; color:#e0f7fa;">ACCELERATING QA PERFORMANCE</p>
            <div style="border-top: 1px solid rgba(255,255,255,0.2); margin-top:10px; padding-top:5px;">
                <small><b>{now.strftime('%d %B %Y')}</b> | <b>{now.strftime('%H:%M:%S')}</b></small>
            </div>
        </div>
        <div style="flex: 1; text-align: right;"><img src="data:image/png;base64,{bin_lpp}" width="150"></div>
    </div>
""", unsafe_allow_html=True)

st.markdown(f"""<div class="sapaan-petugas">OPTIMIZATION MODE: <span style="color:#00ced1;">{shift_pilih}</span></div>""", unsafe_allow_html=True)

# --- 5. LOGIKA NAVIGASI MENU ---

# A. DASHBOARD UTAMA
if st.session_state.menu_level == "main":
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📝\n\nINPUT DATA", key="b1", use_container_width=True)
    with c2: st.button("📊\n\nDATABASE HARIAN", key="b2", use_container_width=True)
    with c3: st.button("📂\n\nDATABASE BULANAN", key="b3", use_container_width=True)
    with c4: st.button("🔄\n\nREKAP STASIUN", key="b4", use_container_width=True)

    c5, c6, c7, c8 = st.columns(4)
    with c5: 
        if st.button("🧮\n\nHITUNG ANALISA", key="b5", use_container_width=True):
            st.session_state.menu_level = "hitung_analisa"
            st.rerun()
    with c6: st.button("📈\n\nTREND PERFORMANCE", key="b6", use_container_width=True)
    with c7: st.button("⚙️\n\nPENGATURAN", key="b7", use_container_width=True)
    with c8: st.button("📥\n\nEXPORT/IMPORT", key="b8", use_container_width=True)

# B. SUB-MENU HITUNG ANALISA
elif st.session_state.menu_level == "hitung_analisa":
    st.markdown("<h3 style='text-align:center; color:#001f3f; font-family:Lexend;'>PILIH JENIS ANALISA</h3>", unsafe_allow_html=True)
    
    a1, a2, a3, a4 = st.columns(4)
    with a1: 
        if st.button("🧪\n\nANALISA TETES", key="a1", use_container_width=True):
            st.session_state.menu_level = "form_tetes"
            st.rerun()
    with a2: st.button("💎\n\nANALISA GKP", key="a2", use_container_width=True)
    with a3: st.button("🔥\n\nANALISA AIR KETEL", key="a3", use_container_width=True)
    with a4: st.button("🥣\n\nANALISA BAHAN MASAKAN", key="a4", use_container_width=True)
    
    st.markdown('<div class="btn-back">', unsafe_allow_html=True)
    if st.button("⬅️ KEMBALI KE DASHBOARD", key="back_to_main"):
        st.session_state.menu_level = "main"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# C. FORM ANALISA TETES (Kodingan yang lo cari!)
elif st.session_state.menu_level == "form_tetes":
    st.markdown("<h2 style='color:#001f3f; font-family:Montserrat;'>🧪 Form Analisa Tetes</h2>", unsafe_allow_html=True)
    
    with st.form("form_tetes_lab"):
        col1, col2 = st.columns(2)
        with col1:
            pb_tetes = st.number_input("Pb Tetes (%)", min_value=0.0, step=0.1)
            hk_tetes = st.number_input("HK Tetes (%)", min_value=0.0, step=0.1)
        with col2:
            ts_tetes = st.number_input("Total Sugar (%)", min_value=0.0, step=0.1)
            brix_tetes = st.number_input("Brix Tetes (%)", min_value=0.0, step=0.1)
            
        submitted = st.form_submit_button("SIMPAN DATA ANALISA")
        if submitted:
            st.success("Data Analisa Tetes Berhasil Disimpan! ✨")
            
    if st.button("⬅️ KEMBALI KE MENU ANALISA"):
        st.session_state.menu_level = "hitung_analisa"
        st.rerun()

# Auto Refresh untuk Jam
time.sleep(1)
st.rerun()
