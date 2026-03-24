import pandas as pd
import streamlit as st
from st_aggrid import AgGrid


reviews = [
    {
        "id": 1,
        "stars": 3
    },
    {
        "id": 2,
        "stars": 4
    },
    {
        "id": 3,
        "stars": 5
    }
]


def show_reviews():
    st.title('Lista de Avaliações')

    AgGrid(data=pd.DataFrame(reviews), reload_data=True, key='reviews_grid')