import streamlit as st
from api.service import Auth


def login(username, password):
    Auth_service = Auth()
    response = Auth_service.get_token(username, password)

    if response.get('Error'):
        st.error(f'Falha ao realizar login: {response.get("Error")}')
        return

    token = response.get('access')

    if not token:
        st.error("Token não encontrado na resposta da API.")
        st.write(response)  # debug
        return

    st.session_state.token = token
    st.success("Login realizado com sucesso!")
    st.rerun()


def logout():
    st.session_state.token = None
    st.rerun()