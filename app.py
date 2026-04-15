import streamlit as st
from actors.page import show_actors
from genres.page import show_genres
from login.page import show_login
from reviews.page import show_reviews
from movies.page import show_movies
from home.home import show_home


def main():
    # Garante que o token sempre exista
    if "token" not in st.session_state:
        st.session_state.token = None

    # Controle de autenticação
    if not st.session_state.token:
        show_login()
        return

    st.title('Flix App')

    menu_options = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']
    )

    if menu_options == 'Início':
        show_home()

    elif menu_options == 'Gêneros':
        show_genres()

    elif menu_options == 'Atores/Atrizes':
        show_actors()

    elif menu_options == 'Filmes':
        show_movies()

    elif menu_options == 'Avaliações':
        show_reviews()


if __name__ == '__main__':
    main()
