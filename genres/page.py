import streamlit as st


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

    st.table(genres)

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do gênero')
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso!')