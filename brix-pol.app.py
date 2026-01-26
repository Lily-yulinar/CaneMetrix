# --- HALAMAN DASHBOARD (VERSI KOTAK-KOTAK) ---
if selected == "Dashboard":
    st.title("🎋 CANE METRIX")
    st.write("Welcome, Planters! Silakan pilih modul analisa di bawah ini:")
    
    # Grid Kotak-Kotak (Bento Style)
    # Row 1
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.subheader("📋 Input Data")
            st.write("Input harian sampel lab.")
            if st.button("Buka Analisa Tetes", use_container_width=True):
                st.info("Pilih 'Analisa Tetes' di menu samping beb!")
                
    with col2:
        with st.container(border=True):
            st.subheader("📊 Database Harian")
            st.write("Rekap data per shift.")
            st.button("Lihat Data", key="db_harian", use_container_width=True)
            
    with col3:
        with st.container(border=True):
            st.subheader("📂 Database Bulanan")
            st.write("Laporan bulanan QA.")
            st.button("Lihat Data", key="db_bulan", use_container_width=True)

    # Row 2
    col4, col5, col6 = st.columns(3)
    with col4:
        with st.container(border=True):
            st.subheader("🔄 Rekap Stasiun")
            st.write("Cek performa tiap stasiun.")
            st.button("Cek Rekap", key="rekap", use_container_width=True)
            
    with col5:
        with st.container(border=True):
            st.subheader("🧮 Hitung Pol")
            st.write("Kalkulator Pol manual.")
            st.button("Mulai Hitung", key="hit_pol", use_container_width=True)
            
    with col6:
        with st.container(border=True):
            st.subheader("📈 Trend")
            st.write("Grafik HK harian.")
            st.button("Buka Grafik", key="trend", use_container_width=True)

    # Row 3 (Status)
    st.divider()
    s1, s2 = st.columns([2, 1])
    with s1:
        st.success("🟢 Status Server: OK | Jumlah sampel masuk hari ini: 45")
    with s2:
        st.caption("17 NOVEMBER 2025 | SHIFT I")
