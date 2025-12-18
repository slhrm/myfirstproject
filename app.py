import streamlit as st
st.title("My first project")
name = st.text_input(".....")
age = st.text_input(".....")
if name:
  st.write(f"Hello {name}!")
else if age:
  st.write(f"So you are {age}!")

