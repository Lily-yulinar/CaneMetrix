import streamlit as st
from streamlit_option_menu import option_menu

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="CANE METRIX", page_icon="🧪", layout="wide")

# --- 2. DATABASE LENGKAP (Tabel Koreksi Suhu & Tabel I BJ) ---
data_koreksi_brix = {
    25: -0.19, 26: -0.12, 27: -0.05, 28: 0.02, 29: 0.09,
    30: 0.16, 31: 0.24, 32: 0.31, 33: 0.38, 34: 0.46,
    35: 0.54, 36: 0.62, 37: 0.70, 38: 0.78, 39: 0.86,
    40: 0.94, 41: 1.02, 42: 1.10, 43: 1.18, 44: 1.26,
    45: 1.34, 46: 1.42, 47: 1.50, 48: 1.58, 49: 1.66, 50: 1.72
}

# Database BJ dari Tabel I (0.0 - 23.9)
data_bj_brix = {
    0.0: 0.996373, 1.0: 1.000201, 2.0: 1.004058, 3.0: 1.007944, 4.0: 1.011858,
    5.0: 1.015801, 6.0: 1.019772, 7.0: 1.023773, 8.0: 1.027803, 9.0: 1.031862,
    10.0: 1.035950, 11.0: 1.040068, 12.0: 1.044216, 13.0: 1.048394, 14.0: 1.052602,
    15.0: 1.056841, 16.0: 1.061110, 17.0: 1.065410, 18.0: 1.069741, 19.0: 1.074103,
    20.0: 1.078497, 21.0: 1.082923, 22.0: 1.087380, 23.0: 1.091870, 23.9: 1.095939
}

def interpolasi(x, data_dict):
    x_list = sorted(data_dict.keys())
    if x in data_dict: return data_dict[x]
    if x < x_list[0] or x > x_list[-1]: return None
    for i in range(len(x_list) - 1):
        x1, x2 = x_list[i], x_list[i+1]
        y1, y2 = data_dict[x1], data_dict[x2]
        if x1 < x < x2:
            return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return None

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("CANE METRIX")
    selected = option_menu(menu_title=None, options=["Dashboard", "Analisa Tetes"], 
                          icons=["house", "vial"], default_index=1)
    st.divider()
    st.caption("Status: 🟢 Production Ready")

# --- 4. LOGIKA ANALISA TETES ---
if selected == "Analisa Tetes":
    st.header("⚗️ Kalkulator Analisa Tetes")
    st.info("Logika: BJ ditarik dari Brix Asli. Purity dihitung dari Brix Koreksi.")
    
    with st.container(border=True):
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 📊 Data Brix")
            brix_asli = st.number_input("Brix Teramati (Asli)", min_value=0.0, format="%.2f", step=0.1)
            suhu = st.number_input("Suhu Sampel (°C)", min_value=25.0, max_value=50.0, value=28.3, step=0.1)
        with c2:
            st.markdown("### 🧪 Data Pol")
            pol_baca = st.number_input("Pol Teramati", min_value=0.0, format="%.2f", step=0.01)
            st.caption("Faktor: 0.286 | Pengenceran: 10x")

    if brix_asli > 0:
        # 1. Itung Brix Koreksi & Cari BJ (Real-time)
        kor_suhu = interpolasi(suhu, data_koreksi_brix)
        brix_kor = brix_asli + (kor_suhu if kor_suhu else 0)
        bj_brix = interpolasi(brix_asli, data_bj_brix)
        
        st.divider()
        st.subheader("📋 Hasil Analisa")
        res1, res2, res3 = st.columns(3)
        
        # Brix muncul duluan!
        res1.metric("FINAL %BRIX", f"{brix_kor:.3f}")
        res1.caption(f"Koreksi Suhu: {kor_suhu:+.3f}")

        # Pol & HK muncul hanya jika Pol sudah diisi
        if pol_baca > 0:
            if bj_brix:
                pol_persen = ((0.286 * pol_baca) / bj_brix) * 10
                purity = (pol_persen / brix_kor) * 100
                
                res2.metric("FINAL %POL", f"{pol_persen:.2f}")
                res2.caption(f"BJ Brix Asli: {bj_brix:.6f}")
                
                # Cek Validitas Purity
                if purity > 100:
                    res3.metric("PURITY (HK)", f"{purity:.2f}%", delta="⚠️ OVER!", delta_color="inverse")
                    st.error(f"Purity {purity:.2f}% tidak logis! Periksa Pol Teramati.")
                else:
                    res3.metric("PURITY (HK)", f"{purity:.2f}%")
                    st.success("Analisa Berhasil & Logis.")
            else:
                res2.warning("Brix di luar tabel BJ.")
        else:
            res2.info("Input Pol...")
            res3.info("Input Pol...")

elif selected == "Dashboard":
    st.title("🏠 CaneMetrix Dashboard")
    st.success("Aplikasi siap digunakan untuk Shift Lab hari ini!")
