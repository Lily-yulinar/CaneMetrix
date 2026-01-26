import streamlit as st
from datetime import datetime, timedelta
import base64
import os
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

# --- 2. DATABASE TABEL KOREKSI (Tadi Sore Edition) ---
def get_lab_data(b_obs, temp):
    # Tabel Koreksi Suhu Brix (Brix 10-20-30-dst)
    # Ini data yang kita presisikan tadi sore
    koreksi_suhu = {
        20: 0.00, 21: 0.07, 22: 0.14, 23: 0.21, 24: 0.28,
        25: 0.36, 26: 0.44, 27: 0.52, 28: 0.61, 29: 0.69,
        30: 0.78, 31: 0.88, 32: 0.98, 33: 1.08, 34: 1.18, 35: 1.28
    }
    
    # Faktor BJ Brix (Berdasarkan Tabel BJ Schmitz)
    # Pendekatan Linear Presisi: BJ = 1 + (Brix * 0.00388)
    kor_temp = koreksi_suhu.get(int(temp), 0.0)
    brix_20 = b_obs + kor_temp
    bj_brix = 1.0000 + (brix_20 * 0.00388)
    
    return kor_temp, brix_20, bj_brix

# --- 3. CSS UI/UX PREMIUM ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Lexend:wght@400;600&family=Montserrat:wght@800&display=swap');
    
    .stApp {{ background: url("data:image/jpg;base64,{bin_bg}"); background-size: cover; background-attachment: fixed; }}
    .main .block-container {{ background: rgba(255, 255, 255, 0.75); border-radius: 30px; padding: 30px !important; backdrop-filter: blur(20px); }}
    
    .mega-header {{ 
        background: linear-gradient(135deg, rgba(0, 31, 63, 0.95) 0%, rgba(0, 100, 100, 0.9) 100%); 
        padding: 20px 40px; border-radius: 25px; display: flex; justify-content: space-between; align-items: center; 
        color: white; border: 1px solid rgba(255,255,255,0.3); margin-bottom: 25px;
    }}
    
    .judul-mega {{ font-family: 'Orbitron'; font-size: 45px; background: linear-gradient(to bottom, #fff, #00ced1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin:0; }}
    .sapaan-petugas {{ text-align: center; color: #fff; font-family: 'Montserrat'; font-size: 24px; text-shadow: 0 0 10px #00ced1; margin: 20px 0; }}
    
    .stButton > button {{ 
        height: 150px; border-radius: 22px; font-family: 'Lexend'; font-weight: 600;
        background: linear-gradient(145deg, rgba(10, 25, 41, 0.95), rgba(0, 60, 60, 0.9)); 
        color: white !important; transition: 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    .stButton > button:hover {{ transform: translateY(-8px); border: 1px solid #00ced1 !important; box-shadow: 0 15px 40px rgba(0, 206, 209, 0.6); }}
    
    .card-lab {{ background: rgba(0, 20, 40, 0.92); padding: 30px; border-radius: 25px; border: 2px solid #00ced1; color: white; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. NAVIGASI ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    if st.button("🏠 DASHBOARD UTAMA"): st.session_state.menu_level = "main"; st.rerun()

# --- 5. HEADER ---
now = datetime.utcnow() + timedelta(hours=7)
st.markdown(f"""
    <div class="mega-header">
        <img src="data:image/png;base64,{bin_sgn}" width="130">
        <div style="text-align: center;">
            <h1 class="judul-mega">CANE METRIX</h1>
            <small style="letter-spacing:2px;">{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
        </div>
        <img src="data:image/png;base64,{bin_lpp}" width="130">
    </div>
""", unsafe_allow_html=True)

# --- 6. LOGIKA MENU ---
if st.session_state.menu_level == "main":
    st.markdown(f"<div class='sapaan-petugas'>HELLO PLANTERS! OPTIMIZATION MODE: {shift_pilih}</div>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📝\n\nINPUT DATA", key="b1", use_container_width=True)
    with c2: st.button("📊\n\nDATABASE HARIAN", key="b2", use_container_width=True)
    with c3: st.button("📂\n\nDATABASE BULANAN", key="b3", use_container_width=True)
    with c4: st.button("🔄\n\nREKAP STASIUN", key="b4", use_container_width=True)
    c5, c6, c7, c8 = st.columns(4)
    with c5: 
        if st.button("🧮\n\nHITUNG ANALISA", key="b5", use_container_width=True):
            st.session_state.menu_level = "sub_analisa"; st.rerun()
    with c6: st.button("📈\n\nTREND", key="b6", use_container_width=True)
    with c7: st.button("⚙️\n\nPENGATURAN", key="b7", use_container_width=True)
    with c8: st.button("📥\n\nEXPORT", key="b8", use_container_width=True)

elif st.session_state.menu_level == "sub_analisa":
    st.markdown("<div class='sapaan-petugas'>PILIH KOMPONEN ANALISA</div>", unsafe_allow_html=True)
    a1, a2, a3, a4 = st.columns(4)
    with a1:
        if st.button("🧪\n\nANALISA TETES", key="a1", use_container_width=True):
            st.session_state.menu_level = "form_tetes"; st.rerun()
    with a2: st.button("💎\n\nANALISA GKP", key="a2", use_container_width=True)
    with a3: st.button("🔥\n\nANALISA AIR KETEL", key="a3", use_container_width=True)
    with a4: st.button("🥣\n\nANALISA BAHAN MASAKAN", key="a4", use_container_width=True)

elif st.session_state.menu_level == "form_tetes":
    st.markdown("<div class='sapaan-petugas'>🧪 KALKULATOR TETES (SCHMITZ TABLE)</div>", unsafe_allow_html=True)
    st.markdown('<div class="card-lab">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📥 Input Data Lab")
        b_obs = st.number_input("Brix Terbaca (Obs)", value=0.0, step=0.01)
        p_obs = st.number_input("Pol Terbaca (Obs)", value=0.0, step=0.01)
        temp = st.slider("Suhu Analisa (°C)", 20, 35, 28)

    # --- EKSEKUSI TABEL TADI SORE ---
    kor_temp, brix_20, bj = get_lab_data(b_obs, temp)
    pol_persen = (p_obs * 0.26048) / bj if bj > 0 else 0.0 # Konstanta Schmitz 26.048
    hk = (pol_persen / brix_20 * 100) if brix_20 > 0 else 0.0

    with col2:
        st.subheader("📊 Hasil Perhitungan")
        st.write(f"Koreksi Suhu (Tabel): `+{kor_temp}`")
        st.write(f"BJ Brix (Schmitz): `{bj:.5f}`")
        st.divider()
        st.metric("% BRIX 20°C", f"{brix_20:.2f}")
        st.metric("% POL", f"{pol_persen:.2f}")
        st.markdown(f"""
            <div style='background:linear-gradient(to right, #00ced1, #008080); padding:15px; border-radius:15px; color:#fff; text-align:center;'>
                <h2 style='margin:0;'>HK: {hk:.2f}%</h2>
            </div>
        """, unsafe_allow_html=True)
        if st.button("💾 ARSIPKAN DATA ANALISA", use_container_width=True): st.success("Data Tersimpan!")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ KEMBALI"): st.session_state.menu_level = "sub_analisa"; st.rerun()

time.sleep(1)
st.rerun()
