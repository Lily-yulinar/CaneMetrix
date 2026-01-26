import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS SAKTI: Paksa Tinggi Logo Sama & Sejajar Tengah
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1, h2, h3, p, span, label { color: #1c4e80 !important; }
    [data-testid="stMetricValue"] { color: #1c4e80; }
    .st-emotion-cache-12w0qpk { background-color: #f0f2f6; }
    
    /* CSS biar logo nggak kecil sebelah */
    img {
        max-height: 80px; /* Paksa tinggi maksimal semua logo sama */
        width: auto;      /* Lebar menyesuaikan biar nggak gepeng */
        object-fit: contain;
    }

    /* Paksa kolom sejajar vertikal di tengah */
    [data-testid="column"] {
        display: flex;
        align-items: center;
        justify-content: center;
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

    # Wadah Header
    with st.container():
        # Kolom: [SGN] - [Judul] - [PTPN & LPP]
        l, m, r = st.columns([1, 2.5, 1.2], vertical_alignment="center")
        
        with l:
            try:
                st.image("sgn.png") # Width dilepas biar diatur CSS img di atas
            except:
                st.caption("Logo SGN")
        
        with m:
            st.markdown(f"""
                <div style="text-align:center;">
                    <h1 style="margin:0; font-size: 45px;">🎋 CANE METRIX</h1>
                    <p style="margin:0; font-weight: bold; font-size: 18px;">Accelerating QA Performance</p>
                    <h2 style="font-family: monospace; margin-top:5px; font-size: 30px;">{tgl_skrg} | {jam_skrg}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with r:
            # Sub-kolom buat duo logo kanan
            k1, k2 = st.columns(2, vertical_alignment="center")
            with k1:
                try: 
                    st.image("ptpn.png") # Ini yang tadi kekecilan, sekarang dipaksa CSS
                except: 
                    st.caption("PTPN")
            with k2:
                try: 
                    st.image("lpp.png")
                except: 
                    st.caption("LPP")

    st.divider()

    # --- GRID MENU KOTAK-KOTAK ---
    c1, c2, c3 = st.columns(3)
    with c1:
        with st.container(border=True):
            st.markdown("### 📋 Input Data")
            st.write("Input harian sampel lab.")
            st.button("Buka", key="b1", use_container_width=True)
    with c2:
        with st.container(border=True):
            st.markdown("### 📊 DB Harian")
            st.write("Rekap data per shift.")
            st.button("Lihat", key="b2", use_container_width=True)
    with c3:
        with st.container(border=True):
            st.markdown("### 📂 DB Bulanan")
            st.write("Laporan bulanan QA.")
            st.button("Buka", key="b3", use_container_width=True)

    c4, c5, c6 = st.columns(3)
    with c4:
        with st.container(border=True):
            st.markdown("### 🔄 Rekap Stasiun")
            st.write("Cek performa stasiun.")
            st.button("Cek", key="b4", use_container_width=True)
    with c5:
        with st.container(border=True):
            st.markdown("### 🧮 Hitung")
            st.write("Kalkulator manual.")
            st.button("Mulai", key="b5", use_container_width=True)
    with c6:
        with st.container(border=True):
            st.markdown("### 📈 Trend")
            st.write("Grafik HK harian.")
            st.button("Buka", key="b6", use_container_width=True)

    # Refresh tiap detik biar jam jalan
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.info("Kalkulator otomatis Brix, Pol, dan HK.")
