import streamlit as st
from datetime import datetime
import time

# --- 1. SETTINGS & LUXURY UI (TIDAK BERUBAH) ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700;900&family=Montserrat:wght@800&family=Lexend:wght@600&display=swap');
    .stApp { background-color: #050a10; }
    
    .header-panel {
        background: linear-gradient(135deg, rgba(0, 206, 209, 0.4) 0%, rgba(0, 128, 128, 0.2) 100%);
        backdrop-filter: blur(20px);
        border-radius: 35px;
        padding: 40px;
        text-align: center;
        border: 1px solid #00ced1;
        box-shadow: 0 0 30px rgba(0, 206, 209, 0.3);
        margin-bottom: 30px;
    }

    .stButton > button {
        height: 160px;
        border-radius: 20px;
        background: #0f172a !important;
        color: white !important;
        border: 1px solid rgba(0, 206, 209, 0.3) !important;
        font-family: 'Lexend', sans-serif;
        font-weight: 800;
        font-size: 16px;
        transition: 0.4s ease;
    }

    .stButton > button:hover {
        transform: scale(1.08) translateY(-10px);
        border-color: #00ced1 !important;
        box-shadow: 0 0 25px #00ced1, inset 0 0 10px rgba(0,206,209,0.5) !important;
        background: rgba(0, 206, 209, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA TABEL BARU (GAMBAR 1, 2, 3) ---

def get_koreksi_suhu(temp):
    """Update Data dari Gambar 1"""
    tabel_suhu = {
        25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09, 30: 0.16,
        31: 0.24, 32: 0.315, 33: 0.385, 34: 0.465, 35: 0.54, 36: 0.62,
        37: 0.70, 38: 0.78, 39: 0.86, 40: 0.94
    }
    t_round = int(temp)
    val = tabel_suhu.get(t_round, 0.0)
    if t_round + 1 in tabel_suhu:
        next_val = tabel_suhu[t_round + 1]
        val += (temp - t_round) * (next_val - val)
    return val

def get_bj_icumsa(brix_val):
    """Update Data dari Gambar 2 & 3"""
    # Database BJ ICUMSA 0.0 - 23.9
    bj_db = {
        0.0: 0.996373, 1.0: 1.000201, 2.0: 1.004058, 3.0: 1.007944, 4.0: 1.011858,
        5.0: 1.015801, 6.0: 1.019772, 7.0: 1.023773, 8.0: 1.027803, 9.0: 1.031862,
        10.0: 1.035950, 11.0: 1.040068, 12.0: 1.044216, 13.0: 1.048394, 14.0: 1.052602,
        15.0: 1.056841, 16.0: 1.061110, 17.0: 1.065410, 18.0: 1.069741, 19.0: 1.074103,
        20.0: 1.078497, 21.0: 1.082923, 22.0: 1.087380, 23.0: 1.091870, 23.9: 1.095939
    }
    keys = sorted(bj_db.keys())
    # Logika Pencarian
    for i in range(len(keys)-1):
        if keys[i] <= brix_val <= keys[i+1]:
            b1, b2 = keys[i], keys[i+1]
            v1, v2 = bj_db[b1], bj_db[b2]
            return v1 + (brix_val - b1) * (v2 - v1) / (b2 - b1)
    return 1.044216 # fallback ke BJ 12.0

# --- 3. UI ---
if 'menu' not in st.session_state: st.session_state.menu = "main"

# PEMAKSA JAM REAL-TIME (image_5f187d)
placeholder = st.empty()
with placeholder.container():
    now = datetime.now()
    st.markdown(f"""
        <div class="header-panel">
            <h1 style="font-family:Orbitron; font-size:55px; letter-spacing:8px; margin:0; color:white;">CANE METRIX</h1>
            <p style="font-family:Lexend; color:white; opacity:0.8;">ACCELERATING QA PERFORMANCE</p>
            <div style="font-family:Orbitron; color:#00ced1; font-size:22px; margin-top:15px; text-shadow: 0 0 10px #00ced1;">
                {now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}
            </div>
        </div>
    """, unsafe_allow_html=True)

if st.session_state.menu == "main":
    cols = st.columns(4)
    menu_items = [("📄", "INPUT DATA"), ("🧮", "HITUNG ANALISA"), ("📊", "DATABASE HARIAN"), ("📂", "DATABASE BULANAN"),
                  ("🔄", "REKAP STASIUN"), ("📈", "TREND"), ("⚙️", "PENGATURAN"), ("📥", "EXPORT/IMPORT")]
    for i, (icon, label) in enumerate(menu_items):
        with cols[i % 4]:
            if st.button(f"{icon}\n\n{label}", key=f"m_{i}", use_container_width=True):
                if label == "HITUNG ANALISA": st.session_state.menu = "calc"; st.rerun()

elif st.session_state.menu == "calc":
    st.markdown("<h2 style='color:white; font-family:Lexend;'>🧪 Laboratory Calculation</h2>", unsafe_allow_html=True)
    tab1, tab2 = st.tabs(["🍯 ANALISA TETES", "🧪 OPTICAL DENSITY (OD)"])
    with tab1:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:30px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            b_baca = st.number_input("Brix Teramati (Brix Obs)", value=1.20, format="%.2f", key="b_obs")
            p_baca = st.number_input("Pol Teramati (Pol Obs)", value=0.00, format="%.2f", key="p_obs")
            temp = st.number_input("Suhu (°C)", value=29.40, format="%.2f", key="t_obs")
            
            # Hitungan Baru
            brix_p = b_baca * 10
            kor_suhu = get_koreksi_suhu(temp) #
            brix_kor = brix_p + kor_suhu
        with c2:
            bj_val = get_bj_icumsa(brix_p) #
            pol_p = (0.286 * (p_baca * 2)) / bj_val
            hk = (pol_p / brix_kor * 100) if brix_kor > 0 else 0.0
            st.metric("BRIX KOREKSI", f"{brix_kor:.2f}")
            st.metric("% POL", f"{pol_p:.2f}")
            st.success(f"### HK: {hk:.2f}%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with tab2:
        st.markdown('<div style="background:rgba(255,255,255,0.05); padding:30px; border-radius:25px; border:1px solid #00ced1;">', unsafe_allow_html=True)
        abs_val = st.number_input("Absorbance (Abs)", value=0.000, format="%.3f")
        b_od = st.number_input("Brix Sampel", value=12.00)
        bj_od = get_bj_icumsa(b_od)
        od_res = (abs_val * bj_od * 500) / 1
        st.markdown(f"### HASIL OD TETES: {od_res:.4f}")
        st.markdown('</div>', unsafe_allow_html=True)

    if st.button("⬅️ KEMBALI KE DASHBOARD", use_container_width=True):
        st.session_state.menu = "main"; st.rerun()

# --- 4. ENGINE AUTO-REFRESH (PENTING!) ---
time.sleep(1)
st.rerun()
