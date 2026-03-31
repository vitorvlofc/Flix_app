import streamlit as st
import requests
from login.service import logout


class GenreRepository:
    def __init__(self):
        self.__base_url = 'https://vitorvl.pythonanywhere.com/api/v1/'
        self.__genres_url = f'{self.__base_url}genres/'
        self.__headers = {'Authorization': f'bearer {st.session_state.token}'}


    def get_genres(self):
        response = requests.get(self.__genres_url, headers=self.__headers)
        if response.status_code == 200:
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(f'Error ao obter dados da API: {response.status_code}')