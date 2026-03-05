import streamlit as st

st.title("My First Dashboard")
st.sidebar.write("time series figures dashboard")

st.button("Hit me")
#st.data_editor("Edit data", data)
st.checkbox("check yes no")
st.radio('Pick one:', ["nose", "ear"])
st.selectbox("select", [1,2,3])
st.multiselect("Multiselect", [1,2,3])
st.slider("slider me", min_value=0, max_value=10)
st.select_slider("slide to select", options = [1,"2"])
st.text_input("Enter some text")
st.number_input("enter a number")
st.text_area("Area for textual entry")
st.date_input("date, input")
st.text_input("TIme entry")
