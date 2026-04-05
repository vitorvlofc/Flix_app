import streamlit as st
import requests


class ReviewRepository:
    def __init__(self):
        self.__base_url = 'https://vitorvl.pythonanywhere.com/api/v1/'
        self.__reviews_url = f'{self.__base_url}reviews/'

    def __get_headers(self):
        token = st.session_state.get("token")
        if not token:
            return {}
        return {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }

    def get_reviews(self):
        response = requests.get(
            self.__reviews_url,
            headers=self.__get_headers()
        )

        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao obter dados da API: {response.status_code} - {response.text}')

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url,
            headers=self.__get_headers(),
            json=review  # 🔥 CORREÇÃO PRINCIPAL
        )

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.text)

        if response.status_code == 201:
            return response.json()

        if response.status_code == 401:
            st.session_state.token = None
            st.warning("Sessão expirada. Faça login novamente.")
            st.rerun()

        raise Exception(f'Erro ao criar review: {response.status_code} - {response.text}')
    

    