import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🧪", layout="wide")

# --- 2. DATABASE KOREKSI BRIX (Tabel Fisik Lab) ---
# Data diambil dari tabel koreksi suhu 20°C
data_koreksi_brix = {
    25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09,
    30: 0.16, 31: 0.24, 32: 0.31, 33: 0.38, 34: 0.46,
    35: 0.54, 36: 0.62, 37: 0.70, 38: 0.78, 39: 0.86,
    40: 0.94, 41: 1.02, 42: 1.10, 43: 1.18, 44: 1.26,
    45: 1.34, 46: 1.42, 47: 1.50, 48: 1.58, 49: 1.66, 50: 1.72
}

# Fungsi Interpolasi Linear untuk akurasi desimal
def hitung_interpolasi(suhu):
    suhu_list = sorted(data_koreksi_brix.keys())
    if suhu in data_koreksi_brix:
        return data_koreksi_brix[suhu]
    for i in range(len(suhu_list) - 1):
        x1, x2 = suhu_list[i], suhu_list[i+1]
        y1, y2 = data_koreksi_brix[x1], data_koreksi_brix[x2]
        if x1 < suhu < x2:
            # Rumus Interpolasi: y = y1 + (x - x1) * (y2 - y1) / (x2 - x1)
            return y1 + (suhu - x1) * (y2 - y1) / (x2 - x1)
    return None

# --- 3. SIDEBAR NAVIGATION (Sesuai Desain CANE METRIX) ---
with st.sidebar:
    st.title("CANE METRIX")
    st.write("Accelerating QA Performance")
    st.divider()
    
    selected = option_menu(
        menu_title="Main Menu",
        options=["Dashboard", "Hitung Brix", "Hitung Pol", "Hitung Purity", "Analisa Tetes"],
        icons=["house", "droplet", "activity", "percent", "vial"],
        menu_icon="cast",
        default_index=1,
    )
    
    st.divider()
    st.caption("Status Server: ✅ OK")
    st.caption("Versi: 1.2 (Latest Update)")

# --- 4. LOGIKA HALAMAN ---

if selected == "Dashboard":
    st.title("🏠 Welcome, Planters!")
    st.write("Selamat datang di sistem manajemen analisa laboratorium **CANE METRIX**.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Sampel Masuk", "45", "+2")
    col2.metric("Status Lab", "Akt
