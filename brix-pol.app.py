import streamlit as st
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Inisialisasi Session State biar gak mental pas ganti menu
if 'menu_level' not in st.session_state:
    st.session_state.menu_level = "main"

# Fungsi panggil aset gambar (Ganti path sesuai file lo ya beb)
def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. CSS SAKTI: UI/UX PREMIUM (Sesuai Dashboard Lo) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Lexend:wght@400;600;800&family=Montserrat:wght@800&family=Poppins:wght@400;600&display=swap');

    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Container Utama */
    .main .block-container {{
        background: rgba(255, 255, 255, 0.75);
        border-radius: 30px;
        padding: 30px !important;
        backdrop-filter: blur(20px);
        box-shadow: 0 10px 50px rgba(0,0,0,0.3);
        margin-top: 15px;
    }}

    /* Mega Header Sesuai Gambar */
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

    /* Tombol Dashboard 8 Kotak */
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

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background: rgba(10, 25, 41, 0.95) !important;
        border-right: 1px solid #00ced1;
    }}

    .card-lab {{
        background: rgba(0, 25, 50, 0.9);
        padding: 30px;
        border-radius: 25px;
        border: 2px solid #00ced1;
        color: white;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (LOGIKA BALIK KE DASHBOARD) ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#00ced1; font-family:Orbitron;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.divider()
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    # Navigasi Sidebar
    if st.button("🏠 DASHBOARD UTAMA", key="side_dash"):
        st.session_state.menu_level = "main"
        st.rerun()
    
    st.divider()
    st.markdown(f"""<div style='background:#00ced1; padding:10px; border-radius:10px; color:#000; text-align:center;'><b>Petugas: {shift_pilih}</b></div>""", unsafe_allow_html=True)

# --- 4. HEADER (LOGO SGN & LPP) ---
now = datetime.utcnow() + timedelta(hours=7)
st.markdown(f"""
    <div class="mega-header">
        <div style="flex: 1; text-align: left;"><img src="data:image/png;base64,{bin_sgn}" width="150"></div>
        <div style="flex: 2; text-align: center;">
            <h1 class="judul-mega">CANE METRIX</h1>
            <p style="font-family:Poppins; letter-spacing:2px; font-weight:600; color:#e0f7fa; margin:0;">ACCELERATING QA PERFORMANCE</p>
            <div style="border-top: 1px solid rgba(255,255,255,0.2); margin-top:10px; padding-top:5px;">
                <small><b>{now.strftime('%d %B %Y')}</b> | <b>{now.strftime('%H:%M:%S')}</b></small>
            </div>
        </div>
        <div style="flex: 1; text-align: right;"><img src="data:image/png;base64,{bin_lpp}" width="150"></div>
    </div>
""", unsafe_allow_html=True)

# --- 5. LOGIKA NAVIGASI MENU ---

# A. DASHBOARD UTAMA (SESUAI GAMBAR ASLI)
if st.session_state.menu_level == "main":
    st.markdown(f"""<div class="sapaan-petugas">HELLO PLANTERS! OPTIMIZATION MODE: <span style="color:#00ced1;">{shift_pilih}</span></div>""", unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📝\n\nINPUT DATA", key="b1", use_container_width=True)
    with c2: st.button("📊\n\nDATABASE HARIAN", key="b2", use_container_width=True)
    with c3: st.button("📂\n\nDATABASE BULANAN", key="b3", use_container_width=True)
    with c4: st.button("🔄\n\nREKAP STASIUN", key="b4", use_container_width=True)

    c5, c6, c7, c8 = st.columns(4)
    with c5: 
        if st.button("🧮\n\nHITUNG ANALISA", key="b5", use_container_width=True):
            st.session_state.menu_level = "sub_analisa"
            st.rerun()
    with c6: st.button("📈\n\nTREND PERFORMANCE", key="b6", use_container_width=True)
    with c7: st.button("⚙️\n\nPENGATURAN", key="b7", use_container_width=True)
    with c8: st.button("📥\n\nEXPORT/IMPORT", key="b8", use_container_width=True)

# B. SUB-MENU HITUNG ANALISA (Sesuai Permintaan)
elif st.session_state.menu_level == "sub_analisa":
    st.markdown(f"""<div class="sapaan-petugas">PILIH KOMPONEN ANALISA</div>""", unsafe_allow_html=True)
    
    a1, a2, a3, a4 = st.columns(4)
    with a1: 
        if st.button("🧪\n\nANALISA TETES", key="a1", use_container_width=True):
            st.session_state.menu_level = "form_tetes"
            st.rerun()
    with a2: st.button("💎\n\nANALISA GKP", key="a2", use_container_width=True)
    with a3: st.button("🔥\n\nANALISA AIR KETEL", key="a3", use_container_width=True)
    with a4: st.button("🥣\n\nANALISA BAHAN MASAKAN", key="a4", use_container_width=True)
    
    if st.button("⬅️ KEMBALI KE DASHBOARD", key="back_to_main"):
        st.session_state.menu_level = "main"
        st.rerun()

# C. FORM ANALISA TETES (LOGIKA INTERPOLASI SESUAI GAMBAR TABEL)
elif st.session_state.menu_level == "form_tetes":
    st.markdown(f"""<div class="sapaan-petugas">🧪 ANALISA TETES: SCHMITZ & TEMPERATURE CORRECTION</div>""", unsafe_allow_html=True)
    
    st.markdown('<div class="card-lab">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Data Pengamatan")
        b_obs = st.number_input("Brix Teramati (Brix Obs)", value=12.00, step=0.01)
        p_obs = st.number_input("Pol Teramati (Pol Obs)", value=0.00, step=0.01)
        temp = st.number_input("Suhu (°C)", value=28.3, step=0.1)
    
    # --- LOGIKA INTERPOLASI TABEL GAMBAR 1 (Koreksi Suhu) ---
    def get_kor_temp(t):
        tabel = {27: -0.05, 28: 0.02, 29: 0.09, 30: 0.16} # dst sesuai gambar image_cb7130
        t_base = int(t)
        return tabel.get(t_base, 0.0) + (t - t_base) * (tabel.get(t_base+1, 0.2) - tabel.get(t_base, 0.0))

    # --- LOGIKA BJ DARI BRIX OBS (Gambar 2 & 3) ---
    def get_bj(b):
        return 1.000 + (b * 0.00388) # Pendekatan tabel image_cb66ad

    kor = get_kor_temp(temp)
    brix_kor = b_obs + kor
    bj_val = get_bj(b_obs)
    pol_persen = ((0.286 * p_obs) / bj_val) * 10
    hk = (pol_persen / brix_kor * 100) if brix_kor > 0 else 0.0

    with col2:
        st.subheader("📊 Hasil")
        st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
        st.metric("% POL", f"{pol_persen:.2f}")
        st.success(f"### HK: {hk:.2f}%")
        if st.button("💾 SIMPAN"): st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI"):
        st.session_state.menu_level = "sub_analisa"
        st.rerun()

time.sleep(1)
st.rerun()
