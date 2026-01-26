# --- HALAMAN DASHBOARD ---
if selected == "Dashboard":
    placeholder = st.empty()
    
    with placeholder.container():
        # Bagian Atas: Logo - Judul - Logo
        # Kita bagi jadi 3 kolom beb
        l1, l2, l3 = st.columns([1, 3, 1])
        
        with l1:
            # Panggil file sgn.png yang lo upload tadi
            st.image("sgn.png", width=80) 
            
        with l2:
            now = datetime.now()
            tgl_skrg = now.strftime("%d %B %Y")
            jam_skrg = now.strftime("%H:%M:%S")
            # Judul Tengah
            st.markdown(f"""
                <div style="text-align:center;">
                    <h1 style="color:#1c4e80; margin:0;">🎋 CANE METRIX</h1>
                    <p style="margin:0; font-weight: bold;">Accelerating QA Performance</p>
                    <h2 style="color:#1c4e80; font-family: monospace; margin-top:5px;">{tgl_skrg} | {jam_skrg}</h2>
                </div>
            """, unsafe_allow_html=True)
            
        with l3:
            # Panggil file ptpn.png yang lo upload tadi
            st.image("ptpn.png", width=80)

    st.write("") # Spasi biar gak dempet
    
    # --- BAGIAN KOTAK-KOTAK MENU ---
    # (Kode kotak-kotak lo tetep di sini beb)
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.container(border=True):
            st.markdown("### 📋 Input Data")
            st.write("Input harian sampel lab.")
            st.button("Buka", key="btn1", use_container_width=True)
    # ... dst sampai col6
    
    # --- BAGIAN FOOTER LOGO LPP ---
    st.divider()
    f1, f2 = st.columns([4, 1])
    with f1:
        st.info(f"🟢 Status Server: OK | Shift I")
    with f2:
        st.image("lpp.png", width=70)

    # Trik refresh jam tetap ada
    time.sleep(1)
    st.rerun()
