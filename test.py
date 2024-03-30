import streamlit as st

st.header('Aplikasi Penjumlahan Bilangan Numerik', divider='rainbow')
st.title('_AKA_ is :blue[cool] :sunglasses:')
st.write('Hello, *World!* :sunglasses:')

angka_pertama = st.number_input('Masukkan angka pertama')
st.write('angka pertama adalah ', angka_pertama)

angka_kedua = st.number_input('Masukkan angka kedua')
st.write('angka kedua adalah ', angka_kedua)

operasi_matematika=angka_pertama*angka_kedua
st.write(f"Angka pertama {angka_pertama} x Angka kedua {angka_kedua}={operasi_matematika}")
