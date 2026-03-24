import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


actors = [
    {
        "id": 1,
        "name": "leonardo dicaprio"
    },
    {
        "id": 2,
        "name": "brad pitt"
    },
    {
        "id": 3,
        "name": "morgan freeman"
    }
]


def show_actors():
    st.title('Lista de Ator/Atriz')

    AgGrid(data=pd.DataFrame(actors), reload_data=True, key='actors_grid')

    st.title('Cadastrar novo(a) Ator/Atriz')
    name = st.text_input('Nome do ator/atriz')
    if st.button('Cadastrar'):
        st.success(f'Ator/Atriz "{name}" cadastrado(a) com sucesso!')