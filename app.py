import streamlit as st


st.title("Welcome to Arsh Web")
st.header("""First
          Ramadan mubarak💝 to all of U
          """)
st.write("What is Your name????")
name = st.text_input("Enter your name: ")
if st.button("Confrim"):
    st.write(f"Welcome Miss/Sir {name} to Arsh Streamlit🥳")

agree = st.checkbox("Agree")
if agree:
    st.write("Great!😀")

st.title("Counter😶‍🌫️")
st.header("welcome to Counter")
if "count" not in st.session_state:
    # st.session_state["count"] = 0
    st.session_state.count = 0

count = 0
st.header(st.session_state.count)

col1, col2 = st.columns(2)
print("count>>>",st.session_state.count)
with col1:
    if st.button("increment"):
        st.session_state.count = st.session_state.count + 1

with col2:
    if st.button("decrement"):
        st.session_state.count = st.session_state.count - 1

st.title("Arsh GitHub")
st.write("U want to open Arsh's GitHub")
if st.button("Yes"):
    st.write("https://github.com/ArshAliAzam")
elif st.button("No"):
    st.write("Thanks for visiting🥰")