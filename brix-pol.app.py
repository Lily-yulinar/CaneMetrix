import streamlit as st
from streamlit_option_menu import option_menu
from datetime import datetime
import time

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

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
    # Kalender di Sidebar buat pengingat beb
    st.write("📅 **Kalender Kerja**")
    st.date_input("Pilih Tanggal", label_visibility="collapsed")
    st.caption("Status: 🟢 Production Ready")

# --- 3. HALAMAN DASHBOARD ---
if selected == "Dashboard":
    # Logika Waktu Real-time
    now = datetime.now()
    tgl_skrg = now.strftime("%d %B %Y")
    jam_skrg = now.strftime("%H:%M:%S")

    # Header Header ala image_e3fa36.png
    st.markdown(f"""
        <div style="background-color:#1c4e80; padding:20px; border-radius:10px; text-align:center;">
            <h1 style="color:white; margin:0;">🎋 CANE METRIX</h1>
            <p style="color:white; margin:0;">Accelerating QA Performance</p>
            <h3 style="color:white; margin:10px 0 0 0;">{tgl_skrg} | {jam_skrg}</h3>
        </div>
    """, unsafe_allow_html=True)
    
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

    col4, col5, col6 = st.columns(3)
    with col4:
        with st.container(border=True):
            st.markdown("### 🔄 Rekap Stasiun")
            st.write("Cek performa stasiun.")
            st.button("Cek", key="btn4", use_container_width=True)
            
    with col5:
        with st.container(border=True):
            st.markdown("### 🧮 Hitung")
            st.write("Kalkulator manual.")
            st.button("Mulai", key="btn5", use_container_width=True)
            
    with col6:
        with st.container(border=True):
            st.markdown("### 📈 Trend")
            st.write("Grafik HK harian.")
            st.button("Buka", key="btn6", use_container_width=True)

    # Footer
    st.divider()
    f1, f2 = st.columns([3, 1])
    f1.info(f"🟢 Status Server: OK | Terakhir Update: {jam_skrg}")
    f2.markdown("**SHIFT I**")

# --- 4. HALAMAN ANALISA TETES ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.write("Gunakan menu ini untuk kalkulasi otomatis beb.")
    # Kode logika Analisa Tetes lo yang kemarin tetep di sini ya!
