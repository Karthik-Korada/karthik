import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Cats")

col1, col2 = st.columns(2)
with col1:
  st.subheader("2 Cat")
  st.image("./2.jpg", caption="2 Cat", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("7 Cat")
  st.image("./7.jpg", caption="7 Cat", width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
