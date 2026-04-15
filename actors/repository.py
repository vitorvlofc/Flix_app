import requests
import streamlit as st


class ActorRepository:
    def __init__(self):
        self.__base_url = 'https://vitorvl.pythonanywhere.com/api/v1'
        self.__actors_url = f'{self.__base_url}/actors/'

    def __get_headers(self):
        token = st.session_state.get("token")
        if not token:
            return {}
        return {'Authorization': f'Bearer {token}'}

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__get_headers()
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao obter dados da API: {response.status_code}')

    def create_actor(self, actor):
        response = requests.post(
            self.__actors_url,
            headers=self.__get_headers(),
            json=actor  # corrigido (era data)
        )

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao criar ator/atriz. status code: {response.status_code}')
