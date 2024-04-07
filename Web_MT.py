import streamlit as st
import pandas


st.header('MT ACESSORIA DE MARKETING')
st.image('images/mtcapa.jpg')

col1, col2 = st.columns(2)

df = pandas.read_csv("data.csv")

with col1:
    for index, row in df[:3].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Veja nosso Projeto]({row['url']})")


with col2:
    for index, row in df[3:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Veja nosso Projeto]({row['url']})")