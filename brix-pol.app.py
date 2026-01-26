# --- Tambahkan Font Baru di Bagian CSS ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syncopate:wght@700&family=Montserrat:wght@800&family=Poppins:wght@400;600&display=swap');

    /* ... (CSS Background & Header tetap sama) ... */

    /* STYLE SUB-MENU EYE-CATCHING */
    .stButton > button {{
        height: 140px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        font-family: 'Syncopate', sans-serif; /* Font baru biar keren */
        font-weight: 700;
        font-size: 14px; /* Ukuran pas biar teks panjang muat */
        color: #ffffff !important;
        background: linear-gradient(145deg, rgba(0, 31, 63, 0.9), rgba(0, 80, 80, 0.8));
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}

    .stButton > button:hover {{
        transform: scale(1.05);
        background: linear-gradient(145deg, #004080, #00ced1);
        border: 1px solid #ffffff !important;
        box-shadow: 0 10px 25px rgba(0, 206, 209, 0.4);
        color: #ffffff !important;
    }}
    
    /* Efek teks dalam tombol */
    .stButton > button p {{
        margin-top: 10px;
        line-height: 1.2;
    }}
    </style>
    """, unsafe_allow_html=True)

# --- 4. DASHBOARD UTAMA (Bagian Grid Menu) ---
if selected == "Dashboard":
    # ... (Bagian Header & Sapaan tetap sama) ...
    
    # GRID MENU: 8 Tombol Sesuai Request Lo
    # Baris 1
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.button("📝\nINPUT DATA", key="m1", use_container_width=True)
    with m2: st.button("📊\nDATABASE HARIAN", key="m2", use_container_width=True)
    with m3: st.button("📂\nDATABASE BULANAN", key="m3", use_container_width=True)
    with m4: st.button("🔄\nREKAP STASIUN", key="m4", use_container_width=True)

    # Baris 2
    m5, m6, m7, m8 = st.columns(4)
    with m5: st.button("🧮\nHITUNG ANALISA", key="m5", use_container_width=True)
    with m6: st.button("📈\nTREND", key="m6", use_container_width=True)
    with m7: st.button("⚙️\nPENGATURAN", key="m7", use_container_width=True)
    with m8: st.button("📥\nEXPORT/IMPORT", key="m8", use_container_width=True)

    time.sleep(1)
    st.rerun()
