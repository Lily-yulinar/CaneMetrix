import streamlit as st
from datetime import datetime, timedelta
import base64
import os
import time

# --- 1. KONFIGURASI & SESSION STATE ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

if 'menu_level' not in st.session_state:
    st.session_state.menu_level = "main"

# --- 2. DATABASE LOGIK LAB (TADI SORE EDITION) ---

def get_koreksi_suhu(temp):
    """Interpolasi Linear untuk Tabel Koreksi Suhu Brix"""
    # Data dari image_cb7130 (Suhu: Koreksi)
    tabel = {
        27: -0.05, 28: 0.02, 29: 0.09, 30: 0.16, 31: 0.24,
        32: 0.32, 33: 0.39, 34: 0.47, 35: 0.54
    }
    s_bawah = int(temp)
    s_atas = s_bawah + 1
    
    if s_bawah in tabel and s_atas in tabel:
        v_bawah = tabel[s_bawah]
        v_atas = tabel[s_atas]
        # Rumus Interpolasi: y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
        return v_bawah + (temp - s_bawah) * (v_atas - v_bawah)
    return tabel.get(s_bawah, 0.0)

def get_bj_tabel(brix_obs):
    """Interpolasi Linear untuk Tabel BJ (Density d27.5)"""
    # Sampling Data dari image_cb66ad & image_cb6690
    # Format {Brix: BJ}
    tabel_bj = {
        10.0: 1.035950, 10.1: 1.036361, 10.2: 1.036771, 10.3: 1.037182,
        11.0: 1.040068, 12.0: 1.044216, 13.0: 1.048394, 14.0: 1.052602,
        15.0: 1.056841, 16.0: 1.061110, 17.0: 1.065410, 18.0: 1.069741
    }
    # Cari range brix untuk interpolasi
    keys = sorted(tabel_bj.keys())
    if brix_obs <= keys[0]: return tabel_bj[keys[0]]
    if brix_obs >= keys[-1]: return tabel_bj[keys[-1]]
    
    for i in range(len(keys)-1):
        if keys[i] <= brix_obs <= keys[i+1]:
            b1, b2 = keys[i], keys[i+1]
            v1, v2 = tabel_bj[b1], tabel_bj[b2]
            return v1 + (brix_obs - b1) * (v2 - v1) / (b2 - b1)
    return 1.000

# --- 3. CSS (TETAP KONSISTEN) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@900&family=Lexend:wght@400;600&family=Montserrat:wght@800&display=swap');
    .stApp { background: #0e1117; color: white; }
    .mega-header { background: linear-gradient(135deg, #001f3f, #006464); padding: 20px; border-radius: 20px; text-align: center; border: 1px solid #00ced1; }
    .stButton > button { height: 150px; border-radius: 20px; font-family: 'Lexend'; background: #1a1c24; color: white !important; border: 1px solid #333; }
    .stButton > button:hover { border-color: #00ced1 !important; transform: translateY(-5px); }
    .card-lab { background: #111; padding: 25px; border-radius: 20px; border: 2px solid #00ced1; }
    </style>
    """, unsafe_allow_html=True)

# --- 4. LOGIKA MENU ---
if st.session_state.menu_level == "main":
    # Dashboard Utama (Tidak Berubah)
    st.markdown("<div class='mega-header'><h1 style='font-family:Orbitron; color:#00ced1;'>CANE METRIX</h1></div>", unsafe_allow_html=True)
    st.write("")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.button("📝\n\nINPUT DATA", use_container_width=True)
    with c2: st.button("📊\n\nDATABASE HARIAN", use_container_width=True)
    with c3: st.button("📂\n\nDATABASE BULANAN", use_container_width=True)
    with c4: st.button("🔄\n\nREKAP STASIUN", use_container_width=True)
    
    c5, c6, c7, c8 = st.columns(4)
    with c5:
        if st.button("🧮\n\nHITUNG ANALISA", use_container_width=True):
            st.session_state.menu_level = "sub_analisa"; st.rerun()
    with c6: st.button("📈\n\nTREND", use_container_width=True)
    with c7: st.button("⚙️\n\nPENGATURAN", use_container_width=True)
    with c8: st.button("📥\n\nEXPORT", use_container_width=True)

elif st.session_state.menu_level == "sub_analisa":
    if st.button("🧪 ANALISA TETES", use_container_width=True):
        st.session_state.menu_level = "form_tetes"; st.rerun()
    if st.button("⬅️ KEMBALI"): st.session_state.menu_level = "main"; st.rerun()

elif st.session_state.menu_level == "form_tetes":
    st.markdown("<h2 style='font-family:Lexend; color:#00ced1;'>🧪 Analisa Tetes - Pro Calculation</h2>", unsafe_allow_html=True)
    
    with st.container():
        st.markdown('<div class="card-lab">', unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📥 Data Pengamatan")
            b_obs = st.number_input("Brix Teramati (Brix Obs)", value=10.00, step=0.01, format="%.2f")
            p_obs = st.number_input("Pol Teramati (Pol Obs)", value=0.00, step=0.01, format="%.2f")
            temp = st.number_input("Suhu Analisa (°C)", value=28.3, step=0.1, format="%.1f")
        
        # --- EKSEKUSI RUMUS SESUAI PERMINTAAN BEB ---
        # 1. Brix Koreksi Suhu (Tabel 1 + Interpolasi)
        koreksi = get_koreksi_suhu(temp)
        brix_koreksi = b_obs + koreksi
        
        # 2. BJ Brix (Dari Brix Obs - Tabel 2 & 3)
        bj = get_bj_tabel(b_obs)
        
        # 3. %Pol (Rumus: (0.286 * p_obs) / BJ * 10) [Faktor 10x Pengenceran]
        # Catatan: 0.286 adalah faktor standar pol tetes
        pol_persen = ((0.286 * p_obs) / bj) * 10
        
        # 4. Purity (HK) = Pol / Brix_Koreksi
        hk = (pol_persen / brix_koreksi * 100) if brix_koreksi > 0 else 0.0

        with col2:
            st.subheader("📊 Hasil Kalkulasi")
            st.write(f"Interpolasi Koreksi Suhu: `{koreksi:+.3f}`")
            st.write(f"BJ Brix (Tabel d27.5): `{bj:.6f}`")
            st.divider()
            st.metric("BRIX KOREKSI", f"{brix_koreksi:.2f}")
            st.metric("% POL TETES", f"{pol_persen:.2f}")
            st.success(f"### HK (PURITY): {hk:.2f}%")
        
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE MENU"): 
        st.session_state.menu_level = "sub_analisa"; st.rerun()
