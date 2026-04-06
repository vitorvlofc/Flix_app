import streamlit as st
import requests


class MoviesRepository:
    def __init__(self):
        self.__base_url = 'https://vitorvl.pythonanywhere.com/api/v1/'
        self.__movies_url = f'{self.__base_url}movies/'

    def __get_headers(self):
        token = st.session_state.get("token")
        if not token:
            return {}
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def get_movies(self):
        response = requests.get(
            self.__movies_url,
            headers=self.__get_headers()
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao obter dados da API: {response.status_code} - {response.text}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__get_headers(),
            json=movie  # 🔥 CORREÇÃO PRINCIPAL
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao criar filme: {response.status_code} - {response.text}')
    

def get_movies_stats(self):
    response = requests.get(
        f'{self.__movies_url}stats/',
        headers=self.__get_headers()
    )

    if response.status_code == 200:
        return response.json()

    if response.status_code == 401:
        st.session_state.token = None
        st.warning("Sessão expirada. Faça login novamente.")
        st.rerun()

    raise Exception(f'Erro ao obter estatísticas dos filmes: {response.status_code}')