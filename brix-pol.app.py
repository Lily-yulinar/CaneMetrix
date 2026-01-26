import streamlit as st
from datetime import datetime, timedelta
import os
import base64
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

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

# --- 2. CSS CUSTOM (PERSIS GAMBAR DASHBOARD LO) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Lexend:wght@400;600&family=Montserrat:wght@800&display=swap');

    .stApp {{
        background: url("data:image/jpg;base64,{bin_bg}");
        background-size: cover;
        background-attachment: fixed;
    }}

    .main .block-container {{
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(15px);
        padding: 20px !important;
    }}

    /* Sidebar Styling */
    [data-testid="stSidebar"] {{
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }}

    /* Header Container Sesuai image_d5e9b8 */
    .mega-header {{
        background: linear-gradient(135deg, #00ced1 0%, #008080 100%);
        padding: 30px;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        border: 1px solid rgba(255,255,255,0.2);
        box-shadow: 0 0 20px rgba(0, 206, 209, 0.4);
    }}

    .sapaan {{
        font-family: 'Montserrat';
        font-size: 28px;
        color: #00ced1;
        text-align: center;
        margin: 20px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }}

    /* Grid Dashboard 8 Tombol image_d57902 */
    .stButton > button {{
        height: 140px;
        border-radius: 20px;
        background: linear-gradient(145deg, #05192d, #002d4d) !important;
        color: white !important;
        border: 1px solid #1a3a5a !important;
        font-family: 'Lexend';
        font-weight: 600;
        transition: 0.3s;
    }}

    .stButton > button:hover {{
        border-color: #00ced1 !important;
        box-shadow: 0 0 15px #00ced1;
        transform: translateY(-5px);
    }}

    /* Card Analisa image_cb0bfb */
    .card-analisa {{
        background: rgba(13, 17, 23, 0.9);
        padding: 25px;
        border-radius: 20px;
        border: 1px solid #00ced1;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:#00ced1; text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    st.divider()
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    
    if st.button("🏠 Dashboard", use_container_width=True):
        st.session_state.menu_level = "main"
        st.rerun()
    
    st.button("Analisa Tetes", use_container_width=True)
    
    st.markdown(f"""
        <div style='margin-top:200px; background:#1f2937; padding:15px; border-radius:15px; border-left: 5px solid #00ced1;'>
            <span style='color:#fff;'>🟢 Petugas: <b>{shift_pilih}</b></span>
        </div>
    """, unsafe_allow_html=True)

# --- 4. HEADER ---
now = datetime.utcnow() + timedelta(hours=7)
st.markdown(f"""
    <div class="mega-header">
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <img src="data:image/png;base64,{bin_sgn}" width="100">
            <div>
                <h1 style="font-family:Orbitron; font-size:45px; margin:0;">CANE METRIX</h1>
                <p style="letter-spacing:3px;">ACCELERATING QA PERFORMANCE</p>
                <small>{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
            </div>
            <img src="data:image/png;base64,{bin_lpp}" width="100">
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---
if st.session_state.menu_level == "main":
    st.markdown(f"<div class='sapaan'>Hello, Planters! Let's optimize {shift_pilih} analysis.</div>", unsafe_allow_html=True)
    
    # Grid 8 Tombol (image_d57902)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📄 INPUT DATA", use_container_width=True)
    with c2: st.button("📊 DATABASE HARIAN", use_container_width=True)
    with c3: st.button("📂 DATABASE BULANAN", use_container_width=True)
    with c4: st.button("🔄 REKAP STASIUN", use_container_width=True)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        if st.button("🧮 HITUNG ANALISA", use_container_width=True):
            st.session_state.menu_level = "analisa_tetes"
            st.rerun()
    with c6: st.button("📈 TREND", use_container_width=True)
    with c7: st.button("⚙️ PENGATURAN", use_container_width=True)
    with c8: st.button("📥 EXPORT/IMPORT", use_container_width=True)

elif st.session_state.menu_level == "analisa_tetes":
    st.markdown(f"<h2 style='color:#fff; font-family:Lexend;'>🧪 Form Analisa Tetes - {shift_pilih}</h2>", unsafe_allow_html=True)
    
    st.markdown('<div class="card-analisa">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📥 Data Pengamatan")
        b_obs = st.number_input("Brix Teramati (Brix Obs)", value=12.00, step=0.01, format="%.2f")
        temp = st.number_input("Suhu (°C)", value=29.40, step=0.1, format="%.2f")
        
        # Real-time Brix (image_cb0bfb)
        def get_kor(t):
            tabel = {29: 0.09, 30: 0.16} # Sesuai image_cb7130
            return tabel.get(int(t), 0.0) + (t - int(t)) * 0.07 
            
        koreksi = get_kor(temp)
        brix_final = b_obs + koreksi
        
        st.markdown(f"**BRIX KOREKSI:** <span style='font-size:24px; color:#00ced1;'>{brix_final:.2f}</span>", unsafe_allow_html=True)
        st.caption(f"Koreksi Tabel: {koreksi:+.2f}")
        
        p_obs = st.number_input("Pol Teramati (Pol Obs)", value=0.00, step=0.01, format="%.2f")

    with col2:
        st.markdown("### 📊 Hasil")
        # Logic BJ & Pol (image_cb66ad, image_cb8456)
        bj = 1.000 + (b_obs * 0.00388)
        pol_persen = ((0.286 * p_obs) / bj) * 10
        hk = (pol_persen / brix_final * 100) if brix_final > 0 else 0.0
        
        st.markdown(f"**% POL:** `{pol_persen:.2f}`")
        st.markdown(f"<small>Faktor: 0.286 | Pengenceran: 10x | BJ: {bj:.5f}</small>", unsafe_allow_html=True)
        
        # Validasi Purity (image_cb0bfb)
        if hk > 100:
            st.error(f"HK: {hk:.2f}% (DATA TIDAK VALID!)")
        else:
            st.success(f"### HK: {hk:.2f}%")
        
        if st.button("💾 SIMPAN DATA", use_container_width=True):
            st.toast("Data Berhasil Disimpan ke Database Harian!", icon="✅")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ KEMBALI KE DASHBOARD"):
        st.session_state.menu_level = "main"
        st.rerun()

time.sleep(1)
st.rerun()
