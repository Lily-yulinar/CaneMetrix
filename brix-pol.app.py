import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS: Background Putih & Sejajarin Logo (Kiri-Kanan)
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1, h2, h3, p, span, label { color: #1c4e80 !important; }
    [data-testid="stMetricValue"] { color: #1c4e80; }
    .st-emotion-cache-12w0qpk { background-color: #f0f2f6; }
    
    /* Paksa kolom sejajar vertikal di tengah */
    [data-testid="column"] {
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* Styling Logo agar konsisten */
    .logo-container img {
        max-height: 80px;
        width: auto;
        object-fit: contain;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🎋 CANE METRIX")
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard", "Analisa Tetes"],
        icons=["house", "vial"],
        menu_icon="cast", default_index=0,
    )
    st.divider()
    st.write("📅 **Kalender Kerja**")
    st.date_input("Pilih Tanggal", label_visibility="collapsed")
    st.caption("Status: 🟢 Production Ready")

# --- 3. HALAMAN DASHBOARD ---
if selected == "Dashboard":
    # Jam WIB (Waktu Indonesia Barat)
    now_wib = datetime.utcnow() + timedelta(hours=7)
    tgl_skrg = now_wib.strftime("%d %B %Y")
    jam_skrg = now_wib.strftime("%H:%M:%S")

    # Header Utama
    with st.container():
        # Kolom: [SGN (Kiri)] - [Judul (Tengah)] - [LPP (Kanan)]
        l, m, r = st.columns([1, 2.5, 1], vertical_alignment="center")
        
        with l:
            # Logo SGN
            try:
                st.image("sgn.png", width=160)
            except:
                st.caption("SGN Logo")
        
        with m:
            st.markdown(f"""
                <div style="text-align:center;">
                    <h1 style="margin:0; font-size: 45px;">🎋 CANE METRIX</h1>
                    <p style="margin:0; font-weight: bold; font-size: 18px;">Accelerating QA Performance</p>
                    <h2 style="font-family: monospace; margin-top:5px; font-size: 30px;">{tgl_skrg} | {jam_skrg}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with r:
            # Logo LPP (Sekarang sendirian di kanan jadi lebih lega)
            try: 
                st.image("lpp.png", width=130)
            except: 
                st.caption("LPP Logo")

    st.divider()

    # --- GRID MENU DASHBOARD ---
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("### 📋 Input Data")
            st.button("Buka", key="b1", use_container_width=True)
    with c2:
        with st.container(border=True):
            st.markdown("### 📊 DB Harian")
            st.button("Lihat", key="b2", use_container_width=True)
    with c3:
        with st.container(border=True):
            st.markdown("### 📂 DB Bulanan")
            st.button("Buka", key="b3", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4:
        with st.container(border=True):
            st.markdown("### 🔄 Rekap Stasiun")
            st.button("Cek", key="b4", use_container_width=True)
    with c5:
        with st.container(border=True):
            st.markdown("### 🧮 Hitung")
            st.button("Mulai", key="b5", use_container_width=True)
    with c6:
        with st.container(border=True):
            st.markdown("### 📈 Trend")
            st.button("Buka", key="b6", use_container_width=True)

    # Footer Status
    st.write("")
    st.info(f"🟢 Server OK | WIB | {jam_skrg}")

    # Real-time Update
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.info("Kalkulator Analisa Lab Otomatis.")
