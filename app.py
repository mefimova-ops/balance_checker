import streamlit as st

st.title("Проверка бухгалтерского баланса")

st.subheader("Загрузка файлов")
balance_file = st.file_uploader("Загрузите CSV баланса", type=["csv"])
osv_file = st.file_uploader("Загрузите CSV ОСВ", type=["csv"])

if st.button("Проверить"):
    if balance_file and osv_file:
        st.success("Файлы успешно загружены и готовы к обработке!")
    else:
        st.warning("Пожалуйста, загрузите оба CSV-файла.")
