import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("Images/photo.png",width=250)

with col2:
    st.title("Deekshita Moily")
    content = """
              Hi All, I'm a recent  BCA graduate who is really exited about creating apps. 
              With a strong foundation in Python programming, I'm on my way to becoming a proficient Python programmer.
              My goal is to keep growing in theworld of app development.
              """
    st.info(content)
content1 = """
Below you can find some of the apps that I have built in Python.Feel free to contact me!"""
st.info(content1)

#responsive or provide space between the rows!
col3, empty_col,col4 = st.columns([1.5,0.5,1.5])
col3,col4 =st.columns(2)
#resposive or provide space between the rows!

df = pandas.read_csv("data (1).csv",sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")
