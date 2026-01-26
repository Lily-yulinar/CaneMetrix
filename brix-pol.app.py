import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time
import base64

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Fungsi buat convert gambar lokal ke base64 biar bisa dipake di CSS
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Pastikan file lo namanya background.jpg di folder yang sama ya beb
try:
    bin_str = get_base64('background.jpg')
    bg_css = f"""
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-attachment: fixed;
    }}"""
except:
    bg_css = ".stApp { background-color: #1c4e80; }" # Fallback kalo file ga ada

# --- 2. CSS SAKTI: GLOSSY & SHINY EFFECT ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;400;600&display=swap');

    {bg_css}
    
    /* Overlay transparan buat area utama */
    .main .block-container {{
        background-color: rgba(255, 255, 255, 0.8); 
        border-radius: 25px;
        margin-top: 20px;
        padding: 40px !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(4px);
    }}

    /* Header Box Luxury */
    .header-container {{
        background: linear-gradient(135deg, #1c4e80 0%, #0a2342 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.18);
    }}

    .judul-futuristik {{
        font-family: 'Orbitron', sans-serif;
        font-size: 45px;
        letter-spacing: 4px;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.5);
    }}

    /* EFEK MENGKILAP (SHINY) PADA TOMBOL */
    .stButton > button {{
        height: 180px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 22px;
        color: white !important;
        position: relative;
        overflow: hidden; /* Biar kilatannya ga keluar kotak */
        transition: all 0.4s ease;
    }}

    /* Kilatan Cahaya Pas Hover */
    .stButton > button::after {{
        content: "";
        position: absolute;
        top: -50%;
        left: -60%;
        width: 20%;
        height: 200%;
        background: rgba(255, 255, 255, 0.3);
        transform: rotate(30deg);
        transition: all 0.6s;
    }}

    .stButton > button:hover::after {{
        left: 120%;
    }}

    /* Gradasi Mengkilap Sesuai Urutan */
    div[data-testid="column"]:nth-of-type(1) .stButton > button {{
        background: linear-gradient(135deg, #72bcd4 0%, #4682b4 100%);
    }}
    div[data-testid="column"]:nth-of-type(2) .stButton > button {{
        background: linear-gradient(135deg, #4682b4 0%, #1c4e80 100%);
    }}
    div[data-testid="column"]:nth-of-type(3) .stButton > button {{
        background: linear-gradient(135deg, #1c4e80 0%, #0a2342 100%);
    }}

    .stButton > button:hover {{
        transform: scale(1.05) translateY(-5px);
        box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    }}

    .shift-badge {{
        background: #00ced1;
        color: #1c4e80;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 800;
        box-shadow: 0 0 15px rgba(0,206,209,0.5);
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR SHIFT SELECTOR ---
with st.sidebar:
    st.title("🎋 CANE METRIX")
    st.write("---")
    st.subheader("⚙️ Control Panel")
    shift_aktif = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["house-door-fill", "beaker-fill"],
        default_index=0,
    )
    st.divider()
    st.info(f"🟢 Petugas: **{shift_aktif}**")

# --- 4. DASHBOARD ---
if selected == "Dashboard":
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Header Section
    st.markdown(f"""
        <div class="header-container">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="width:150px"> <img src="data:image/png;base64,{get_base64('sgn.png') if True else ''}" width="130"> </div>
                <div style="text-align: center;">
                    <h1 class="judul-futuristik">CANE METRIX</h1>
                    <p style="font-family:'Poppins'; opacity:0.8; letter-spacing:2px;">ACCELERATING QA PERFORMANCE</p>
                    <small>{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
                </div>
                <div style="width:150px; text-align:right;"> 
                    <div class="shift-badge">{shift_aktif}</div>
                    <img src="data:image/png;base64,{get_base64('lpp.png') if True else ''}" width="100" style="margin-top:10px;">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<h4 style='text-align:center; color:#1c4e80; font-family:Poppins;'>Hello, Planters! Let's optimize <b>{shift_aktif}</b> analysis today.</h4>", unsafe_allow_html=True)
    st.write("")

    # Menu Grid (Shiny Buttons)
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
    st.markdown(f"<h2>🧪 Analysis - {shift_aktif}</h2>", unsafe_allow_html=True)
    with st.container(border=True):
        st.write("Input parameter lab untuk kalkulasi otomatis.")
        # Fungsi-fungsi interpolasi lo tetep aman di sini beb...
        brix = st.number_input("Brix Lab", format="%.2f")
        pol = st.number_input("Pol Lab", format="%.2f")
        if st.button("PROCESS DATA"):
            hk = (pol/brix*100) if brix > 0 else 0
            st.balloons()
            st.metric("Harkat Kemurnian (HK)", f"{round(hk,2)}%")
