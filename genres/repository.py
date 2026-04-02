import streamlit as st
import requests


class GenreRepository:
    def __init__(self):
        self.__base_url = 'https://vitorvl.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'

    def __get_headers(self):
        token = st.session_state.get("token")
        if not token:
            return {}
        return {'Authorization': f'Bearer {token}'}

    def get_genres(self):
        response = requests.get(self.__genres_url, headers=self.__get_headers())

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__get_headers(),
            data=genre
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao criar gênero. status code: {response.status_code}')