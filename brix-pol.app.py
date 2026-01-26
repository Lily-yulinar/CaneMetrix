import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# --- 2. SIDEBAR NAVIGATION (Variabel 'selected' dibuat di sini beb) ---
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
    # Wadah kosong buat update jam tanpa refresh seluruh kotak menu
    placeholder = st.empty()
    
    with placeholder.container():
        now = datetime.now()
        tgl_skrg = now.strftime("%d %B %Y")
        jam_skrg = now.strftime("%H:%M:%S")

        # Header Biru dengan Jam Real-time
        st.markdown(f"""
            <div style="background-color:#1c4e80; padding:20px; border-radius:10px; text-align:center; border: 2px solid #336699;">
                <h1 style="color:white; margin:0;">🎋 CANE METRIX</h1>
                <p style="color:white; margin:0;">Accelerating QA Performance</p>
                <h2 style="color:#00ffcc; margin:10px 0 0 0; font-family: monospace;">{tgl_skrg} | {jam_skrg}</h2>
            </div>
        """, unsafe_allow_html=True)

    # Grid Menu Kotak-Kotak (Bento Style)
    st.write("") 
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

    # --- TRIK AGAR JAM BERGERAK ---
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.info("Kalkulator Analisa Tetes otomatis.")
    # (Logika perhitungan lo yang kemarin ditaruh di sini)
