import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


movies = [
    {
        "id": 1,
        "name": "Os Predadores"
    },
    {
        "id": 2,
        "name": "Titanic"
    },
    {
        "id": 3,
        "name": "Rambo"
    }
]


def show_movies():
    st.title('Lista de Filmes')

    AgGrid(data=pd.DataFrame(movies), reload_data=True, key='movies_grid')