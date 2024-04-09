import streamlit as st

st.title("Welcome to West Bengal Joint Entrance Examination Board.")
st.header("Application Form Of JECA 2024")
st.subheader("-design by Soumyamoy Dhara")
name = st.text_input("Enter Your Name : ")
fname = st.text_input("Enter Your Father Name : ")
mname = st.text_input("Enter Your Mother Name : ")
adr = st.text_area("Enter Your Address : ")
qualificationdata = st.selectbox("Last Qualifing Exam :",("BCA","B.Tach","Bsc.CS","IT","Bsc(H)"))
button = st.button("Done")
if button :
    st.markdown(f"""
    Name : {name}
    Father Name : {fname}
    Mother Name : {mname}
    Address : {adr}
    class : {qualificationdata}""")