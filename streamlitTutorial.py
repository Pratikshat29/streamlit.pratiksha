import streamlit as st
import pandas as pd
import numpy as np
st.title("hello gpt")
name = st.text_input("ask your question")

st.write("This is your stramlit app")
st.text ("let's get started")
name=st.text_input("Enter your name")
if st.button("Great"):
    st.success (f"hello,{name}")


upload_file = st.file_uploader("Upload CSV", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

st.header("This is header")
st.subheader("This is subheader")
st.markdown("link(https://streamlit.io)")
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=10)
st.slider("choose a range",0,100)
st.selectbox("select a fruit",["apple", "banana", "mango"])
st.multiselect("select language",["Java", "Python", "C", "C++"])
st.radio("pick one",["option A","option A"])
st.checkbox("I agree tarmd and conditions")

if st.checkbox("show details"):
   st.info("here vare more details")

   with st.form("login form"):
        username = st.text_input("username") 
        password = st.text_input("password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            st.success(f"Welcome {username}")

df =pd.DataFrame(np.random.randn(20,3), columns=["A","B","C"])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

st.video ("https://www.youtube.com/watch?v=itgeO50_kvg&list=RDitgeO50_kvg&start_radio=1&t=1537s")
st.image ("https://res.cloudinary.com/dtz0urit6/image/upload/q_auto:best,f_jpg/cloudinary-tools-uploads/db6uqfe1wxuybf8rcmqk",caption ="sample image")
