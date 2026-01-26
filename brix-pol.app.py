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

# --- 2. CSS SAKTI: UI/UX OPTIMIZED ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Lexend:wght@400;600;800&family=Montserrat:wght@800&family=Poppins:wght@400;600&display=swap');

    /* Background Setup */
    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Container Glassmorphism */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 30px !important;
        backdrop-filter: blur(20px);
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

    /* SAPAAN GLOWING */
    .sapaan-petugas {{
        text-align: center;
        color: #ffffff;
        font-family: 'Montserrat', sans-serif;
        font-size: 26px;
        font-weight: 800;
        margin: 25px 0;
        text-shadow: 0 0 10px rgba(0, 206, 209, 0.8), 0 0 20px rgba(0, 0, 0, 0.5);
    }}

    /* SUB-MENU UI/UX DESIGN (LEXEND FONT) */
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
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 15px;
        padding: 20px !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
    }}

    /* Hover Effect */
    .stButton > button:hover {{
        transform: translateY(-10px);
        background: linear-gradient(145deg, #004080, #00ced1);
        border: 1px solid #00ced1 !important;
        box-shadow: 0 15px 40px rgba(0, 206, 209, 0.5);
    }}

    /* Ukuran Icon dalam Tombol */
    .stButton > button span {{
        font-size: 45px !important;
        margin-bottom: 5px;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.write("---")
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    selected = option_menu(None, ["Dashboard", "Analisa Tetes"], 
                          icons=["grid-fill", "vial"], 
                          default_index=0)

# --- 4. DASHBOARD UTAMA ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header
    st.markdown(f"""
        <div class="mega-header">
            <div style="flex: 1; text-align: left;">
                <img src="data:image/png;base64,{bin_sgn}" width="150">
            </div>
            <div style="flex: 2; text-align: center;">
                <h1 class="judul-mega">CANE METRIX</h1>
                <p style="font-family:Poppins; letter-spacing:2px; font-weight:600; color:#e0f7fa;">ACCELERATING QA PERFORMANCE</p>
                <div style="border-top: 1px solid rgba(255,255,255,0.2); margin-top:10px; padding-top:5px;">
                    <small><b>{now.strftime('%d %B %Y')}</b> | <b>{now.strftime('%H:%M:%S')}</b></small>
                </div>
            </div>
            <div style="flex: 1; text-align: right;">
                <img src="data:image/png;base64,{bin_lpp}" width="150">
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Sapaan
    st.markdown(f"""<div class="sapaan-petugas">HELLO PLANTERS! OPTIMIZED FOR: <span style="color:#00ced1;">{shift_pilih}</span></div>""", unsafe_allow_html=True)

    # GRID SUB-MENU (Icon Atas, Text Bawah)
    row1_col = st.columns(4)
    with row1_col[0]: st.button("📝\n\nINPUT DATA", key="b1", use_container_width=True)
    with row1_col[1]: st.button("📊\n\nDATABASE HARIAN", key="b2", use_container_width=True)
    with row1_col[2]: st.button("📂\n\nDATABASE BULANAN", key="b3", use_container_width=True)
    with row1_col[3]: st.button("🔄\n\nREKAP STASIUN", key="b4", use_container_width=True)

    row2_col = st.columns(4)
    with row2_col[0]: st.button("🧮\n\nHITUNG ANALISA", key="b5", use_container_width=True)
    with row2_col[1]: st.button("📈\n\nTREND PERFORMANCE", key="b6", use_container_width=True)
    with row2_col[2]: st.button("⚙️\n\nPENGATURAN", key="b7", use_container_width=True)
    with row2_col[3]: st.button("📥\n\nEXPORT/IMPORT", key="b8", use_container_width=True)

    time.sleep(1)
    st.rerun()

elif selected == "Analisa Tetes":
    st.markdown(f"<h2>🧪 Analysis Module - {shift_pilih}</h2>", unsafe_allow_html=True)
