import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


genres = [
    {
        "id": 1,
        "name": "Ficção"
    },
    {
        "id": 2,
        "name": "Comédia"
    },
    {
        "id": 3,
        "name": "Terror"
    }
]

def show_genres():
    st.title('Lista de Gêneros')

    AgGrid(data=pd.DataFrame(genres), reload_data=True, key='genres_grid')

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')