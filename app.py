import streamlit as st
import random

# Sayfa Ayarları (Tarayıcı sekmesinde görünecek kısım)
st.set_page_config(page_title="Mix & Match Mutfağı", page_icon="🍲", layout="centered")

# === MALZEME LİSTELERİ ===
proteinler = ["Füme Somon", "Tavuk Haşlama", "Haşlanmış Yumurta","Ton Balığı", "Karides", "Izgara Tavuk", "Köfte", "Nohut", "Mantar", "Somon", "Tofu"]
tabanlar = ["Kinoa", "Karabuğday", "Pirinç Pilavı", "Bulgur Pilavı", "Patates Kızartma", "Fırın Patates", "Tatlı Patates", "Patates Püresi", "Makarna"]
sebzeler = ["Ispanak", "Taze Fasulye", "Pazı", "Enginar", "Kereviz", "Brokoli", "Brüksel Lahanası", "Tatlı Patates", "Karnabahar", "Kabak", "Patlıcan", "Avokado"]
soslar = ["Kornişonlu Sos", "Kapari", "Hardal", "Sirke", "Zeytinyağı", "Tahinli Yoğurt","Yoğurt / Labne" "Pesto", "Acılı Sriracha", "Limonlu Zeytinyağı", "Soya-Sarımsak"]
crunch_katmani = ["Kabak Çekirdeği", "Ay Çekirdeği", "Ceviz", "Susam", "Kavrulmuş Badem", "Taze Nane", "Çörek Otu", "Parmesan"]



# Web sitesi yenilendiğinde malzemelerin kaybolmaması için hafıza (Session State) oluşturuyoruz
if "taban" not in st.session_state:
    st.session_state.taban = random.choice(tabanlar)
    st.session_state.protein = random.choice(proteinler)
    st.session_state.sebze = random.choice(sebzeler)
    st.session_state.sos = random.choice(soslar)
    st.session_state.crunch = random.choice(crunch_katmani)

# Fonksiyonlar: Malzemeleri değiştirmek için
def hepsini_degistir():
    st.session_state.taban = random.choice(tabanlar)
    st.session_state.protein = random.choice(proteinler)
    st.session_state.sebze = random.choice(sebzeler)
    st.session_state.sos = random.choice(soslar)
    st.session_state.crunch = random.choice(crunch_katmani)

# === WEB ARAYÜZÜ TASARIMI ===
st.title("🍲 Gökada'nın kaseleri")
st.subheader("5 katmanlı kase jeneratörü.")
st.write("---")

# Menüyü Kartlar Halinde Gösterelim
st.markdown(f"### ✨ GÜNÜN KASESİ ✨")
st.info(f"🔹 **Taban / Tahıl:** {st.session_state.taban}")
st.info(f"🔹 **Protein:** {st.session_state.protein}")
st.info(f"🔹 **Çıtır & Taze Sebze:** {st.session_state.sebze}")
st.info(f"🔹 **Sos Kavanozu:** {st.session_state.sos}")
st.info(f"🔹 **Serpilecek Crunch:** {st.session_state.crunch}")

st.write("---")

# Butonlar ve Kontroller
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Kombini Beğenmedim, Hepsini Değiştir!", use_container_width=True):
        hepsini_degistir()
        st.rerun()

with col2:
    puan = st.select_slider("Tabağa Puan Ver:", options=["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    if st.button("💾 Kombini Onayla ve Puanla", use_container_width=True):
        st.success(f"Harika! Bu tabak {puan} ile şefin favorilerine eklendi. Afiyet olsun! 🎉")

# Tekil Katman Değiştirme Alanı
st.write("#### 🎯 Sadece Tek Bir Katmanı Değiştir")
katman_secimi = Skinner_box = st.selectbox(
    "Beğenmediğin katmanı seç ve altındaki butona bas:",
    ["Taban / Tahıl", "Protein", "Çıtır & Taze Sebze", "Sos Kavanozu", "Serpilecek Crunch"]
)

if st.button("🎲 Sadece Bu Katmanı Zar At"):
    if katman_secimi == "Taban / Tahıl":
        st.session_state.taban = random.choice(tabanlar)
    elif katman_secimi == "Protein":
        st.session_state.protein = random.choice(proteinler)
    elif katman_secimi == "Çıtır & Taze Sebze":
        st.session_state.sebze = random.choice(sebzeler)
    elif katman_secimi == "Sos Kavanozu":
        st.session_state.sos = random.choice(soslar)
    elif katman_secimi == "Serpilecek Crunch":
        st.session_state.crunch = random.choice(crunch_katmani)
    st.rerun()
