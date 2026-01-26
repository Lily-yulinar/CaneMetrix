import streamlit as st
from datetime import datetime, timedelta
import pandas as pd # Untuk simulasi database
import base64
import os

# --- 1. KOREKSI LAYOUT & LOGO (FIXED) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

if 'menu_level' not in st.session_state:
    st.session_state.menu_level = "main"
if 'db_harian' not in st.session_state:
    st.session_state.db_harian = [] # Database sementara

def get_base64(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bin_bg = get_base64('background.jpg')
bin_sgn = get_base64('sgn.png')
bin_lpp = get_base64('lpp.png')

# --- 2. LOGIKA TABEL (INTERPOLASI PRESISI) ---
def get_kor_temp(t):
    # Data dari image_cb7130 (Interpolasi Linear)
    tabel = {
        28: 0.02, 29: 0.09, 30: 0.16, 31: 0.24, 32: 0.32, 
        33: 0.39, 34: 0.47, 35: 0.54
    }
    t_base = int(t)
    if t_base in tabel and (t_base + 1) in tabel:
        v1, v2 = tabel[t_base], tabel[t_base + 1]
        return v1 + (t - t_base) * (v2 - v1)
    return tabel.get(t_base, 0.0)

def get_bj_presisi(b):
    # Data dari image_cb66ad & image_cb6690
    # Pendekatan Tabel Density d27.5
    return 1.000 + (b * 0.00388) 

# --- 3. UI CSS (PROFESSIONAL DARK MODE) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Lexend:wght@400;600&display=swap');
    .stApp {{ background: url("data:image/jpg;base64,{bin_bg}"); background-size: cover; background-attachment: fixed; }}
    .main .block-container {{ background: rgba(255, 255, 255, 0.75); border-radius: 30px; padding: 30px !important; backdrop-filter: blur(20px); }}
    .mega-header {{ background: linear-gradient(135deg, rgba(0, 31, 63, 0.95), rgba(0, 100, 100, 0.9)); padding: 20px; border-radius: 20px; display: flex; justify-content: space-between; align-items: center; color: white; }}
    .card-lab {{ background: rgba(0, 25, 45, 0.95); padding: 25px; border-radius: 20px; border: 1.5px solid #00ced1; color: white; }}
    .metric-box {{ background: rgba(255,255,255,0.05); padding: 15px; border-radius: 12px; border-left: 4px solid #00ced1; }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. HEADER & SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#00ced1;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    shift_pilih = st.selectbox("Shift Operasional:", ["SHIFT I", "SHIFT II", "SHIFT III"])
    if st.button("🏠 DASHBOARD UTAMA"):
        st.session_state.menu_level = "main"; st.rerun()
    st.markdown(f"<div style='margin-top:250px; background:#00ced1; color:black; padding:10px; border-radius:8px; text-align:center;'><b>Petugas Aktif: {shift_pilih}</b></div>", unsafe_allow_html=True)

now = datetime.utcnow() + timedelta(hours=7)
st.markdown(f"""
    <div class="mega-header">
        <img src="data:image/png;base64,{bin_sgn}" width="120">
        <div style="text-align: center;">
            <h2 style="font-family:Orbitron; letter-spacing:4px; margin:0;">CANE METRIX</h2>
            <small>{now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}</small>
        </div>
        <img src="data:image/png;base64,{bin_lpp}" width="120">
    </div>
""", unsafe_allow_html=True)

# --- 5. LOGIKA MENU ---
if st.session_state.menu_level == "main":
    st.markdown(f"<h3 style='text-align:center; color:white;'>HELLO PLANTERS! OPTIMIZATION MODE: {shift_pilih}</h3>", unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📝\n\nINPUT DATA", use_container_width=True)
    with c2: st.button("📊\n\nDATABASE HARIAN", use_container_width=True)
    with c3: st.button("📂\n\nDATABASE BULANAN", use_container_width=True)
    with c4: st.button("🔄\n\nREKAP STASIUN", use_container_width=True)
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        if st.button("🧮\n\nHITUNG ANALISA", use_container_width=True):
            st.session_state.menu_level = "form_tetes"; st.rerun()
    with c6: st.button("📈\n\nTREND", use_container_width=True)
    with c7: st.button("⚙️\n\nPENGATURAN", use_container_width=True)
    with c8: st.button("📥\n\nEXPORT", use_container_width=True)

elif st.session_state.menu_level == "form_tetes":
    st.markdown("<h3 style='color:#00ced1;'>🧪 Form Analisa Tetes</h3>", unsafe_allow_html=True)
    
    st.markdown('<div class="card-lab">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📥 Data Pengamatan")
        b_obs = st.number_input("Brix Teramati (Brix Obs)", value=12.00, step=0.01, format="%.2f")
        temp = st.number_input("Suhu (°C)", value=29.40, step=0.1, format="%.2f")
        
        # Real-time Output Brix (Poin 2)
        kor = get_kor_temp(temp)
        brix_kor = b_obs + kor
        st.markdown(f"""
            <div class="metric-box">
                <small>Koreksi Tabel: {kor:+.3f}</small><br>
                <span style="font-size:20px;"><b>BRIX KOREKSI: {brix_kor:.2f}</b></span>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        p_obs = st.number_input("Pol Teramati (Pol Obs)", value=0.00, step=0.01, format="%.2f")

    # Kalkulasi Purity
    bj_val = get_bj_presisi(b_obs)
    pol_persen = ((0.286 * p_obs) / bj_val) * 10
    hk = (pol_persen / brix_kor * 100) if brix_kor > 0 else 0.0

    with col2:
        st.markdown("#### 📊 Hasil Analisa")
        # Info Detail (Poin 3 & 4)
        st.info(f"Faktor Pol: 0.286 | Pengenceran: 10x")
        st.info(f"BJ Tabel (Brix {b_obs}): {bj_val:.6f}")
        
        st.metric("% POL", f"{pol_persen:.2f}")
        
        # Validasi Purity (Poin 1)
        if hk > 100:
            st.error(f"⚠️ HK: {hk:.2f}% (OVER 100% - PERIKSA POL/BRIX!)")
        else:
            st.success(f"### HK (Purity): {hk:.2f}%")
        
        if st.button("💾 SIMPAN DATA KE DATABASE", use_container_width=True):
            # Simulasi Simpan ke Database Per Shift
            data_baru = {"Shift": shift_pilih, "Waktu": now.strftime("%H:%M"), "Brix": brix_kor, "Pol": pol_persen, "HK": hk}
            st.session_state.db_harian.append(data_baru)
            st.toast(f"Data Shift {shift_pilih} Berhasil Diarsipkan!", icon="✅")
    
    st.markdown('</div>', unsafe_allow_html=True)
    if st.button("⬅️ KEMBALI"): st.session_state.menu_level = "main"; st.rerun()
