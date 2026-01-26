import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🧪", layout="wide")

# --- 2. DATABASE KOREKSI BRIX ---
data_koreksi_brix = {
    25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09,
    30: 0.16, 31: 0.24, 32: 0.31, 33: 0.38, 34: 0.46,
    35: 0.54, 36: 0.62, 37: 0.70, 38: 0.78, 39: 0.86,
    40: 0.94, 41: 1.02, 42: 1.10, 43: 1.18, 44: 1.26,
    45: 1.34, 46: 1.42, 47: 1.50, 48: 1.58, 49: 1.66, 50: 1.72
}

def hitung_interpolasi(suhu):
    suhu_list = sorted(data_koreksi_brix.keys())
    if suhu in data_koreksi_brix:
        return data_koreksi_brix[suhu]
    for i in range(len(suhu_list) - 1):
        x1, x2 = suhu_list[i], suhu_list[i+1]
        y1, y2 = data_koreksi_brix[x1], data_koreksi_brix[x2]
        if x1 < suhu < x2:
            return y1 + (suhu - x1) * (y2 - y1) / (x2 - x1)
    return None

# --- 3. SIDEBAR NAVIGATION ---
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

# --- 4. LOGIKA HALAMAN ---

if selected == "Dashboard":
    st.title("🏠 Welcome, Planters!")
    st.write("Selamat datang di pusat kendali mutu **CANE METRIX**.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Sampel Masuk", "45")
    c2.metric("Status Lab", "Aktif")
    c3.metric("Shift", "Shift I")
    
    st.info("Pilih menu di samping untuk mulai melakukan analisa laboratorium.")

elif selected == "Hitung Brix":
    st.header("📊 Perhitungan Brix Koreksi")
    st.write("Gunakan form ini untuk menghitung Brix yang telah dikoreksi suhu (20°C).")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        brix_baca = st.number_input("Brix Teramati (Alat)", min_value=0.0, format="%.2f", step=0.1)
    with col2:
        suhu_in = st.number_input("Suhu Sampel (°C)", min_value=25.0, max_value=50.0, value=28.3, step=0.1)

    if brix_baca > 0:
        kor = hitung_interpolasi(suhu_in)
        if kor is not None:
            brix_akhir = brix_baca + kor
            st.divider()
            st.subheader("Hasil Analisa")
            res1, res2, res3 = st.columns(3)
            res1.metric("Brix Asli", f"{brix_baca}")
            res2.metric("Koreksi Suhu", f"{kor:+.3f}")
            res3.metric("Brix Koreksi", f"{round(brix_akhir, 3)}")
            st.success(f"Analisa selesai untuk suhu {suhu_in}°C")

elif selected == "Hitung Pol":
    st.header("🧪 Perhitungan Pol")
    st.info("Modul ini akan segera aktif setelah rumus Pol diinput.")

elif selected == "Hitung Purity":
    st.header("📈 Perhitungan Purity (HK)")
    st.info("Modul HK otomatis (Pol/Brix * 100).")

elif selected == "Analisa Tetes":
    st.header("⚗️ Analisa Tetes")
    st.write("Modul integrasi analisa tetes tebu.")
