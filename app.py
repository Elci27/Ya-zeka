import streamlit as st
import lyricsgenius

# Genius API
genius = lyricsgenius.Genius("VEcy-gqfMEZ23a7KAfs3mhYtOozIHgAS9HeZ3NnLwRVLs5BnhCO7lB0jvYLd1xlI")
genius.skip_non_songs = True
genius.excluded_terms = ["(Remix)", "(Live)"]
genius.remove_section_headers = True

st.set_page_config(page_title="🎵 Şarkı Sözleri Uygulaması", layout="centered")
st.title("🎼 Şarkı Sözleri Bulucu")

sanatci = st.text_input("Sanatçı adı")
sarki = st.text_input("Şarkı adı")

if st.button("🔍 Sözleri Getir"):
    if sanatci and sarki:
        try:
            song = genius.search_song(sarki, sanatci)
            if song:
                st.success("✅ Şarkı bulundu!")
                st.text_area("🎤 Sözler", song.lyrics, height=400)
            else:
                st.warning("Şarkı bulunamadı.")
        except Exception as e:
            st.error(f"⚠️ Hata: {e}")
    else:
        st.info("Lütfen sanatçı ve şarkı adı girin.")

if st.button("⭐ Önerilen Şarkılar"):
    if sanatci:
        try:
            artist = genius.search_artist(sanatci, max_songs=3, sort="popularity")
            st.markdown(f"🎤 **{sanatci}** için popüler şarkılar:")
            for song in artist.songs:
                st.write(f"- {song.title}")
        except Exception as e:
            st.error(f"⚠️ Öneri alınamadı: {e}")
    else:
        st.info("Lütfen önce sanatçı adını girin.")
