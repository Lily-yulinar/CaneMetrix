import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# --- 2. SIDEBAR NAVIGATION (Dibuat di awal supaya gak error! beb) ---
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
        # Kolom Header: Logo Kiri - Judul - Logo Kanan
        h1, h2, h3 = st.columns([1, 4, 1])
        
        with h1:
            st.image("sgn.png", width=100) # Pastikan file sgn.png ada di GitHub
        
        with h2:
            now = datetime.now()
            tgl_skrg = now.strftime("%d %B %Y")
            jam_skrg = now.strftime("%H:%M:%S")
            st.markdown(f"""
                <div style="text-align:center;">
                    <h1 style="color:#1c4e80; margin:0;">🎋 CANE METRIX</h1>
                    <p style="margin:0; font-weight: bold;">Accelerating QA Performance</p>
                    <h2 style="color:#1c4e80; font-family: monospace;">{tgl_skrg} | {jam_skrg}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with h3:
            st.image("ptpn.png", width=100) # Pastikan file ptpn.png ada di GitHub

    st.write("") 
    
    # Grid Menu Kotak-Kotak (Bento Style)
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

    # Footer dengan Logo LPP
    st.divider()
    f1, f2 = st.columns([5, 1])
    f1.info(f"🟢 Status Server: OK | Terakhir Update: {jam_skrg}")
    f2.image("lpp.png", width=80)

    # Jam Real-time
    time.sleep(1)
    st.rerun()

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.write("Masukkan data untuk kalkulasi otomatis.")
    # Kode perhitungan brix-pol lo taruh di bawah sini beb
