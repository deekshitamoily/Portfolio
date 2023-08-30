import streamlit as st
st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("Images/photo.png")

with col2:
    st.title("Deekshita Moily")
    content = """
              Hi All, I'm a recent  BCA graduate who is really exited about creating apps. 
              With a strong foundation in Python programming, I'm on my way to becoming a proficient Python programmer.
              My goal is to keep growing in theworld of app development.
                """
    st.info(content)
