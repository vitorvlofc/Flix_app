import streamlit as st
from api.service import Auth


def login(username, password):
    Auth_service = Auth()
    response = Auth_service.get_token(username, password)

    if response.get('Error'):
        st.error(f'Falhaa ao realizar login: {response.get("Error")}]')
    else:
        st.session_state.token = response.get('access')
        st.rerun()


def logout():
    for key in st.session_state.keys():
        del st.session_state[key]
    st.rerun()