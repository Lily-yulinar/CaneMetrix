import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🎋", layout="wide")

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("🎋 CANE METRIX")
    # Definisikan variabel 'selected' di sini supaya nggak error lagi beb!
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard", "Analisa Tetes"],
        icons=["house", "vial"],
        menu_icon="cast", default_index=0,
    )
    st.divider()
    st.caption("Status: 🟢 Production Ready")

# --- 3. HALAMAN DASHBOARD (KOTAK-KOTAK ALA image_e3fa36.png) ---
if selected == "Dashboard":
    # Header Header ala gambar lo
    st.markdown("""
        <div style="background-color:#1c4e80; padding:20px; border-radius:10px; text-align:center;">
            <h1 style="color:white; margin:0;">🎋 CANE METRIX</h1>
            <p style="color:white; margin:0;">Accelerating QA Performance | 17 NOVEMBER 2025</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("") # Spasi
    
    # Grid Menu Kotak-Kotak
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

    # Footer ala gambar lo
    st.divider()
    f1, f2 = st.columns([3, 1])
    f1.info("🟢 Status Server: OK | Jumlah sampel masuk hari ini: 45")
    f2.markdown("**SHIFT I**")

# --- 4. HALAMAN ANALISA TETES (Kodingan Lama Lo) ---
elif selected == "Analisa Tetes":
    st.header("🎋 Analisa Tetes")
    st.write("Silakan masukkan data analisa di bawah.")
    # (Logika analisa tetes lo tetep aman di sini beb)
