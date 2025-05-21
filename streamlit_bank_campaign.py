import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.markdown("""
    <h1 style='text-align: center; color: #996515;;'>
        💰 Prediksi Deposito 💰
    </h1>
    <h1 style='text-align: center; color: #996515;;'>
            Nasabah Bank
    </h1>
    <p style='text-align: center; font-size: 16px;'>
        Isi form di sidebar untuk memprediksi apakah nasabah akan melakukan deposito.
    </p>
""", unsafe_allow_html=True)

st.sidebar.header("📝 Input Data Nasabah")

def input_user():
    with st.sidebar.form("input_form"):
        age = st.number_input("Umur", min_value=18, max_value=95, value=39)
        job = st.selectbox("Pekerjaan", ['admin.', 'self-employed', 'services', 'housemaid', 'technician', 
                                         'management', 'student', 'blue-collar', 'entrepreneur', 'retired', 
                                         'unemployed', 'unknown'])
        balance = st.number_input("Saldo", min_value=-1900, max_value=15000, value=537)
        housing = st.radio("Memiliki Pinjaman Rumah?", ["yes", "no"])
        loan = st.radio("Memiliki Pinjaman Pribadi?", ["yes", "no"])
        contact = st.selectbox("Jenis Kontak", ['cellular', 'telephone', 'unknown'])
        month = st.selectbox("Bulan Kontak Terakhir", ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                                                       'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])
        campaign = st.number_input("Jumlah Kontak dalam Kampanye Ini", min_value=1, max_value=30, value=2)
        pdays = st.number_input("Hari Sejak Kontak Terakhir (sebelumnya)", min_value=-1, max_value=595, value=-1)
        poutcome = st.selectbox("Hasil Kampanye Sebelumnya", ['unknown', 'other', 'failure', 'success'])
        
        submitted = st.form_submit_button("Prediksi")

    df = pd.DataFrame({
        "age": [age],
        "job": [job],
        "balance": [balance],
        "housing": [housing],
        "loan": [loan],
        "contact": [contact],
        "month": [month],
        "campaign": [campaign],
        "pdays": [pdays],
        "poutcome": [poutcome]
    })
    return df, submitted

df_employee, submitted = input_user()

if submitted:
    st.subheader("📊 Data yang Dimasukkan")
    st.write(df_employee)

    # Load model
    with open("C:/purwadhika/Capstone_Modul_3/model_bank_marketing_campaign.sav", "rb") as file:
        model_loaded = pickle.load(file)

    # Prediksi probabilitas
    y_proba = model_loaded.predict_proba(df_employee)[:, 1]
    kelas = np.where(y_proba > 0.4, 1, 0)

    st.subheader("📈 Hasil Prediksi")
    if kelas == 1:
        st.success("✅ **Nasabah DIPREDIKSI AKAN melakukan deposit.**")
    else:
        st.error("❌ **Nasabah DIPREDIKSI TIDAK akan melakukan deposit.**")

    st.markdown(f"**🎯 Probabilitas Deposit:** `{y_proba[0]:.2%}`")
