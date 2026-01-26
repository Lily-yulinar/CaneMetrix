import streamlit as st

st.set_page_config(page_title="Lab Analyzer", page_icon="🧪")

st.title("🧪 Sugar Lab Dashboard")
st.write("Aplikasi otomatisasi perhitungan Brix, Pol, dan HK.")

# Input Area
st.sidebar.header("Input Data")
brix = st.sidebar.number_input("Brix Teramati", min_value=0.0, value=0.0, step=0.1)
pol = st.sidebar.number_input("Pol Bacaan", min_value=0.0, value=0.0, step=0.1)

# Kalkulasi
if brix > 0:
    hk = (pol / brix) * 100
    
    # Dashboard Tampilan Utama
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Nilai HK (Purity)", value=f"{round(hk, 2)}%")
    with col2:
        status = "AMAN" if hk >= 75 else "CEK KEMBALI"
        st.metric(label="Status", value=status)
        
    st.info(f"Hasil analisa menunjukkan nilai kemurnian sebesar {round(hk, 2)}%.")
else:
    st.warning("Silahkan masukkan nilai Brix terlebih dahulu.")
