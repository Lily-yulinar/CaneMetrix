import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime, timedelta
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# CSS Maksa Background Putih & Teks Biru Gelap
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1, h2, h3, p, span, label { color: #1c4e80 !important; }
    [data-testid="stMetricValue"] { color: #1c4e80; }
    .st-emotion-cache-12w0qpk { background-color: #f0f2f6; }
    /* Biar logo & judul sejajar vertikal */
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
    placeholder = st.empty()
    
    with placeholder.container():
        # Kolom Header: [SGN (Kiri)] - [JUDUL (Tengah)] - [PTPN & LPP (Kanan)]
        l1, l2, l3 = st.columns([1, 3, 1.2])
        
        with l1:
            try:
                st.image("sgn.png", width=130)
            except:
                st.caption("Logo SGN")
            
        with l2:
            # FIX JAM: Tambah 7 jam biar jadi WIB (Waktu Indonesia Barat)
            now_wib = datetime.utcnow() + timedelta(hours=7)
            tgl_skrg = now_wib.strftime("%d %B %Y")
            jam_skrg = now_wib.strftime("%H:%M:%S")
            
            st.markdown(f"""
                <div style="text-align:center;">
                    <h1 style="margin:0; font-size: 45px;">🎋 CANE METRIX</h1>
                    <p style="margin:0; font-weight: bold; font-size: 18px;">Accelerating QA Performance</p>
                    <h2 style="font-family: monospace; margin-top:5px;">{tgl_skrg} | {jam_skrg}</h2>
                </div>
            """, unsafe_allow_html=True)

        with l3:
            # Dua logo di kanan disejajarkan sampingan
            col_kanan1, col_kanan2 = st.columns(2)
            with col_kanan1:
                try: st.image("ptpn.png", width=85)
                except: st.caption("PTPN")
            with col_kanan2:
                try: st.image("lpp.png", width=85)
                except: st.caption("LPP")

    st.divider()
    
    # Grid Kotak-Kotak (Bento Style)
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

    # Footer Status
    st.write("")
    st.info(f"🟢 Status Server: OK | Shift I | WIB (Waktu Indonesia Barat)")

    # Jam Real-time
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.info("Kalkulator otomatis untuk parameter Brix, Pol, dan HK.")
