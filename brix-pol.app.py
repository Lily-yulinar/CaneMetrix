# --- HALAMAN DASHBOARD ---
if selected == "Dashboard":
    # Wadah untuk jam biar bisa update terus
    placeholder = st.empty()
    
    # Loop untuk update jam tiap detik
    # Pakai container agar tampilan kotak-kotak di bawahnya nggak goyang
    with placeholder.container():
        now = datetime.now()
        tgl_skrg = now.strftime("%d %B %Y")
        jam_skrg = now.strftime("%H:%M:%S")

        # Header Header ala image_e3fa36.png
        st.markdown(f"""
            <div style="background-color:#1c4e80; padding:20px; border-radius:10px; text-align:center; border: 2px solid #336699;">
                <h1 style="color:white; margin:0;">🎋 CANE METRIX</h1>
                <p style="color:white; margin:0;">Accelerating QA Performance</p>
                <h2 style="color:#00ffcc; margin:10px 0 0 0; font-family: monospace;">{tgl_skrg} | {jam_skrg}</h2>
            </div>
        """, unsafe_allow_html=True)

    # --- GRID MENU KOTAK-KOTAK (Tetap Sama) ---
    st.write("") 
    col1, col2, col3 = st.columns(3)
    # ... (lanjutkan kodingan kotak-kotak lo yang kemarin di sini) ...

    # Trik rahasia biar jam gerak: refresh halaman tiap 1 detik
    time.sleep(1)
    st.rerun()
