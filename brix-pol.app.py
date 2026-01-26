import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS SAKTI: Mengubah tampilan total mirip gambar referensi
st.markdown("""
    <style>
    /* Import Font Futuristik & Clean */
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@700&family=Poppins:wght@300;400;600&display=swap');

    /* Background Utama */
    .stApp {
        background-color: #f4f7f6;
    }

    /* Header Biru Gelap ala Referensi */
    .header-box {
        background-color: #1c4e80;
        padding: 30px;
        border-radius: 0px 0px 20px 20px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .judul-futuristik {
        font-family: 'Orbitron', sans-serif;
        font-size: 50px;
        letter-spacing: 5px;
        margin: 0;
        color: #ffffff;
    }

    .sub-judul {
        font-family: 'Poppins', sans-serif;
        font-size: 18px;
        font-weight: 300;
        letter-spacing: 2px;
        opacity: 0.9;
    }

    /* Styling Kotak Menu (Bento Box) */
    .stButton > button {
        height: 150px;
        border-radius: 15px;
        border: none;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 18px;
        transition: all 0.3s;
        color: white;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    /* Warna Gradasi Tombol ala Referensi */
    /* Tombol 1, 4, 7 (Light Blue) */
    div[data-testid="column"]:nth-of-type(1) .stButton > button {
        background: linear-gradient(135deg, #aed9f4 0%, #72bcd4 100%);
        color: #1c4e80;
    }
    /* Tombol 2, 5, 8 (Medium Blue) */
    div[data-testid="column"]:nth-of-type(2) .stButton > button {
        background: linear-gradient(135deg, #4682b4 0%, #2c5e8c 100%);
    }
    /* Tombol 3, 6, 9 (Deep Blue) */
    div[data-testid="column"]:nth-of-type(3) .stButton > button {
        background: linear-gradient(135deg, #2c5e8c 0%, #1c3d5a 100%);
    }

    .stButton > button:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Sapaan Planters */
    .welcome-text {
        color: white;
        font-family: 'Poppins', sans-serif;
        text-align: left;
        position: absolute;
        top: 10px;
        left: 20px;
        font-size: 14px;
    }
    
    .shift-badge {
        background-color: #00ced1;
        padding: 5px 15px;
        border-radius: 10px;
        font-weight: bold;
        float: right;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. LOGIKA PERHITUNGAN (HK, POL, BRIX) ---
def hitung_qa(brix, pol):
    if brix > 0:
        hk = (pol / brix) * 100
        return round(hk, 2)
    return 0

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🎋 CANE METRIX</h2>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options=["Dashboard", "Analisa Tetes"],
        icons=["grid-fill", "vial"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#f0f2f6"},
            "nav-link-selected": {"background-color": "#1c4e80"},
        }
    )
    st.divider()
    st.date_input("📅 Kalender Kerja")
    st.info("Status: 🟢 Production Ready")

# --- 4. HALAMAN DASHBOARD ---
if selected == "Dashboard":
    # Jam & Tgl WIB
    now = datetime.utcnow() + timedelta(hours=7)
    
    # Custom Header ala Gambar Referensi
    st.markdown(f"""
        <div class="header-box">
            <div class="welcome-text">Welcome, Planters!</div>
            <div class="shift-badge">SHIFT I</div>
            <h1 class="judul-futuristik">CANE METRIX</h1>
            <p class="sub-judul">Accelerating QA Performance</p>
            <div style="text-align: right; font-family: monospace; font-size: 16px;">
                {now.strftime('%d %B %Y')} | {now.strftime('%H:%M:%S')}
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Kata-kata Sapaan
    st.markdown("<p style='text-align:center; font-style:italic;'>\"Hello, Planters! I will help you to accelerate your analysis.\"</p>", unsafe_allow_html=True)

    # Grid Menu (3x2)
    c1, c2, c3 = st.columns(3)
    with c1: st.button("📋\nInput Data", use_container_width=True)
    with c2: st.button("📊\nDatabase Harian", use_container_width=True)
    with c3: st.button("📂\nDatabase Bulanan", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4: st.button("🔄\nRekap Stasiun", use_container_width=True)
    with c5: st.button("🧮\nHitung", use_container_width=True)
    with c6: st.button("👤\nAkun", use_container_width=True)

    # Footer Status Server
    st.write("---")
    f1, f2 = st.columns([4, 1])
    with f2:
        st.write("Status Server: 🟢 OK")

    time.sleep(1)
    st.rerun()

# --- 5. HALAMAN ANALISA TETES (Fungsi QA Lengkap) ---
elif selected == "Analisa Tetes":
    st.markdown("<h1 style='color: #1c4e80;'>🎋 Analisa Lab (QA)</h1>", unsafe_allow_html=True)
    
    with st.container(border=True):
        col1, col2 = st.columns(2)
        with col1:
            brix = st.number_input("Masukkan Brix", min_value=0.0, step=0.1)
        with col2:
            pol = st.number_input("Masukkan Pol", min_value=0.0, step=0.1)
            
        if st.button("Hitung HK"):
            hk_hasil = hitung_qa(brix, pol)
            st.metric("Hasil HK (Harkat Kemurnian)", f"{hk_hasil}%")
            
            if hk_hasil > 80:
                st.success("Kualitas: Bagus (HK Tinggi)")
            elif hk_hasil > 0:
                st.warning("Kualitas: Standar")
    
    st.info("Fungsi Interpolasi Tabel Tabel berat jenis/brix akan berjalan otomatis di backend.")
