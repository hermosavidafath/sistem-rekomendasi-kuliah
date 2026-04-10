import streamlit as st

st.title("🎓 Sistem Rekomendasi Jurusan Kuliah Sederhana")
st.write("Sistem Cerdas berbasis Rule (IF-ELSE)")

# Input
minat = st.selectbox("Pilih Minat Anda:", ["Matematika & Logika", "Seni & Desain", "Biologi & Alam", "Sosial & Komunikasi", "Teknologi & Komputer"])
kemampuan = st.selectbox("Pilih Kemampuan Unggulan:", ["Analitis", "Kreatif", "Hafalan", "Berbicara & Menulis", "Problem Solving"])
nilai_un = st.selectbox("Nilai Rata-rata Rapor:", ["< 70", "70 - 80", "> 80"])

if st.button("Dapatkan Rekomendasi"):
    rekomendasi = ""
    alasan = ""

    # Rule IF-ELSE
    if minat == "Teknologi & Komputer":
        if kemampuan == "Problem Solving" or kemampuan == "Analitis":
            rekomendasi = "Teknik Informatika / Ilmu Komputer"
            alasan = "Minat teknologi dan kemampuan problem solving sangat cocok untuk jurusan ini."
        elif kemampuan == "Kreatif":
            rekomendasi = "Desain Komunikasi Visual (DKV) / Multimedia"
            alasan = "Kombinasi teknologi dan kreativitas cocok untuk jurusan berbasis desain digital."
        else:
            rekomendasi = "Sistem Informasi"
            alasan = "Jurusan ini cocok untuk yang berminat teknologi dengan kemampuan komunikasi dan analisis."

    elif minat == "Matematika & Logika":
        if kemampuan == "Analitis" or kemampuan == "Problem Solving":
            if nilai_un == "> 80":
                rekomendasi = "Matematika / Statistika / Aktuaria"
                alasan = "Nilai tinggi dan kemampuan analitis sangat mendukung jurusan eksakta murni."
            else:
                rekomendasi = "Teknik Industri / Manajemen"
                alasan = "Kemampuan logika dan matematika cocok untuk jurusan teknik atau manajemen bisnis."
        else:
            rekomendasi = "Akuntansi / Ekonomi"
            alasan = "Minat matematika dengan kemampuan lain cocok untuk jurusan bisnis dan keuangan."

    elif minat == "Biologi & Alam":
        if kemampuan == "Hafalan":
            rekomendasi = "Kedokteran / Farmasi / Keperawatan"
            alasan = "Minat biologi dan kemampuan hafalan sangat dibutuhkan di bidang kesehatan."
        elif kemampuan == "Analitis":
            rekomendasi = "Biologi / Kimia / Teknik Lingkungan"
            alasan = "Kemampuan analitis dan minat alam cocok untuk sains murni atau teknik lingkungan."
        else:
            rekomendasi = "Pertanian / Kehutanan / Perikanan"
            alasan = "Minat pada alam cocok untuk jurusan berbasis sumber daya alam."

    elif minat == "Seni & Desain":
        if kemampuan == "Kreatif":
            rekomendasi = "Desain Grafis / Arsitektur / Seni Rupa"
            alasan = "Kreativitas tinggi sangat dibutuhkan di jurusan seni dan desain."
        elif kemampuan == "Berbicara & Menulis":
            rekomendasi = "Sastra / Broadcasting / Periklanan"
            alasan = "Kombinasi seni dan kemampuan komunikasi cocok untuk jurusan media kreatif."
        else:
            rekomendasi = "Pendidikan Seni / Musik"
            alasan = "Minat seni bisa diarahkan ke jurusan pendidikan seni atau musik."

    elif minat == "Sosial & Komunikasi":
        if kemampuan == "Berbicara & Menulis":
            rekomendasi = "Ilmu Komunikasi / Hubungan Internasional / Jurnalistik"
            alasan = "Kemampuan komunikasi yang baik sangat cocok untuk jurusan sosial dan media."
        elif kemampuan == "Analitis":
            rekomendasi = "Hukum / Psikologi / Sosiologi"
            alasan = "Kemampuan analitis dan minat sosial cocok untuk jurusan hukum atau psikologi."
        else:
            rekomendasi = "Administrasi Publik / Ilmu Politik"
            alasan = "Minat sosial cocok untuk jurusan yang berhubungan dengan pemerintahan dan kebijakan."

    # Output
    st.success(f"✅ Rekomendasi Jurusan: **{rekomendasi}**")
    st.info(f"💡 Alasan: {alasan}")
