import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import time

# --- 1. KONFIGURASI HALAMAN ---
# Kita set layout wide dan temanya nanti bakal ikut settingan browser (default putih)
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# Tambahan CSS buat maksa background jadi putih bersih dan teks gelap
st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }
    h1, h2, h3, p {
        color: #1c4e80 !important;
    }
    [data-testid="stMetricValue"] {
        color: #1c4e80;
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
    # --- HEADER LOGO (Semua ditaruh di atas beb) ---
    # Kita bagi jadi 5 kolom biar rapi (Logo - Logo - Judul - Logo - Logo)
    l1, l2, l3, l4, l5 = st.columns([1, 1, 3, 1, 1])
    
    with l1:
        try:
            st.image("sgn.png", width=100)
        except:
            st.caption("SGN")
            
    with l2:
        try:
            st.image("ptpn.png", width=100)
        except:
            st.caption("PTPN")

    with l3:
        now = datetime.now()
        tgl_skrg = now.strftime("%d %B %Y")
        jam_skrg = now.strftime("%H:%M:%S")
        st.markdown(f"""
            <div style="text-align:center;">
                <h1 style="margin:0; font-size: 40px;">🎋 CANE METRIX</h1>
                <p style="margin:0; font-weight: bold;">Accelerating QA Performance</p>
                <h2 style="font-family: monospace; margin-top:5px;">{tgl_skrg} | {jam_skrg}</h2>
            </div>
        """, unsafe_allow_html=True)

    with l4:
        try:
            st.image("lpp.png", width=100)
        except:
            st.caption("LPP AGRO")
            
    with l5:
        # Cadangan kalau ada logo lain, atau kosongin aja beb
        st.write("")

    st.divider() # Garis pemisah biar rapi
    
    # --- GRID MENU KOTAK-KOTAK (Bento Style) ---
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### 📋 Input Data")
            st.write("Input harian sampel lab.")
            st.button("Buka", key="btn1", use_container_width=True)
            
    with col2:
        with st.container(border=True):
            st.markdown("### 📊 DB Harian")
            st.write("Rekap data per shift.")
            st.button("Lihat", key="btn2", use_container_width=True)
            
    with col3:
        with st.container(border=True):
            st.markdown("### 📂 DB Bulanan")
            st.write("Laporan bulanan QA.")
            st.button("Buka", key="btn3", use_container_width=True)

    # Footer Status
    st.write("")
    st.info(f"🟢 Status Server: OK | Shift I | Terakhir Update: {jam_skrg}")

    # Jam Real-time
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.info("Kalkulator otomatis untuk parameter Brix, Pol, dan HK.")
    # Logika perhitungan lo tetep aman di sini
