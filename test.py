import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0

st.write(f"Counter value: {st.session_state.counter}")
if st.button('Increment Counter'):
    st.session_state.counter += 1