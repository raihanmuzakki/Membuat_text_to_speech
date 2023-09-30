import streamlit as st
from gtts import gTTS
from IPython.display import Audio
st.title("Text to Speech (TTS) with Streamlit")
# Input teks dari pengguna
text = st.text_area("Masukkan teks yang ingin diubah menjadi suara:")
# Tombol untuk mengonversi teks menjadi suara
if st.button("Konversi ke Suara"):
    if text:
        # Konversi teks menjadi suara menggunakan gTTS
        tts = gTTS(text)
        
        # Simpan suara dalam berkas sementara
        audio_file = "tts_audio.mp3"
        tts.save(audio_file)
        
        # Tampilkan audio
        st.audio(audio_file, format="audio/mp3")
    else:
        st.warning("Silakan masukkan teks terlebih dahulu.")
    # Tampilkan petunjuk
st.markdown("Catatan: Aplikasi ini menggunakan Google Text-to-Speech (gTTS). Pastikan Anda memiliki koneksi internet saat menggunakan aplikasi ini.")
