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
        return {'Authorization': f'Bearer {token}'}

    def get_movies(self):
        response = requests.get(self.__movies_url, headers=self.__get_headers())

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_movie(self, movie):
        response = requests.post(
            self.__movies_url,
            headers=self.__get_headers(),
            data=movie
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao criar filme. status code: {response.status_code}')