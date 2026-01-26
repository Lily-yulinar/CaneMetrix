import streamlit as st
import numpy as np

# --- 1. DATA TABEL (Sesuai Foto Lo) ---
# Format: {Suhu: Nilai Koreksi}
data_koreksi = {
    25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09,
    30: 0.16, 31: 0.24, 32: 0.31, 33: 0.38, 34: 0.46,
    35: 0.54, 36: 0.62, 37: 0.70, 38: 0.78, 39: 0.86,
    40: 0.94, 41: 1.02, 42: 1.10, 43: 1.18, 44: 1.26,
    45: 1.34, 46: 1.42, 47: 1.50, 48: 1.58, 49: 1.66, 50: 1.72
}

# --- 2. FUNGSI INTERPOLASI ---
def dapatkan_koreksi(suhu_input):
    suhu_list = sorted(data_koreksi.keys())
    # Jika suhu pas ada di tabel
    if suhu_input in data_koreksi:
        return data_koreksi[suhu_input]
    # Jika di luar range tabel
    if suhu_input < suhu_list[0] or suhu_input > suhu_list[-1]:
        return None
    # Logika Interpolasi
    for i in range(len(suhu_list) - 1):
        x1, x2 = suhu_list[i], suhu_list[i+1]
        y1, y2 = data_koreksi[x1], data_koreksi[x2]
        if x1 < suhu_input < x2:
            return y1 + (suhu_input - x1) * (y2 - y1) / (x2 - x1)

# --- 3. TAMPILAN UI (CANE METRIX STYLE) ---
st.set_page_config(page_title="Cane Metrix - Hitung Brix", layout="centered")

st.title("📊 Perhitungan Brix Koreksi")
st.markdown("---")

# Input Section
col1, col2 = st.columns(2)
with col1:
    brix_baca = st.number_input("Brix Teramati", min_value=0.0, step=0.1, format="%.2f")
with col2:
    suhu_input = st.number_input("Suhu Sampel (°C)", min_value=25.0, max_value=50.0, step=0.1, format="%.1f")

# Proses Hitung
if brix_baca > 0:
    koreksi = dapatkan_koreksi(suhu_input)
    
    if koreksi is not None:
        brix_akhir = brix_baca + koreksi
        
        # Tampilan Dashboard Hasil
        st.write("### Hasil Analisa")
        c1, c2, c3 = st.columns(3)
        c1.metric("Brix Asli", f"{brix_baca}")
        c2.metric("Koreksi Suhu", f"{koreksi:+.3f}")
        c3.metric("Brix Koreksi", f"{round(brix_akhir, 3)}")
        
        st.success(f"Brix Koreksi untuk suhu {suhu_input}°C adalah **{round(brix_akhir, 3)}**")
    else:
        st.error("Suhu di luar jangkauan tabel (25-50°C)")

st.sidebar.info("CANE METRIX - Versi 1.0 (Brix Module)")
