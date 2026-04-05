import pandas as pd
import streamlit as st
from datetime import datetime
from st_aggrid import AgGrid

from actors.service import ActorService
from genres.service import GenreService
from movies.service import MoviesService


def show_movies():
    movies_service = MoviesService()

    # ========================
    # LISTAGEM
    # ========================
    movies = movies_service.get_movies()

    if movies:
        st.title('Lista de Filmes')
        movies_df = pd.json_normalize(movies)

        # evita erro se colunas não existirem
        columns_to_drop = [col for col in ['actors', 'genre.id'] if col in movies_df.columns]
        movies_df = movies_df.drop(columns=columns_to_drop)

        AgGrid(data=movies_df, reload_data=True, key='movies_grid')
    else:
        st.warning('Nenhum filme encontrado.')

    # ========================
    # FORMULÁRIO
    # ========================
    st.title('Cadastrar Novo Filme')

    title = st.text_input('Título')

    release_date = st.date_input(
        label='Data de lançamento',
        value=datetime.today(),
        min_value=datetime(1600, 1, 1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )

    # ========================
    # GÊNEROS
    # ========================
    genre_service = GenreService()
    genres = genre_service.get_genres()

    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    # ========================
    # ATORES
    # ========================
    actor_service = ActorService()
    actors = actor_service.get_actors()

    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actor_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actor_names]

    # ========================
    # RESUMO
    # ========================
    resume = st.text_area('Resumo')

    # ========================
    # BOTÃO
    # ========================
    if st.button('Cadastrar'):
        try:
            new_movie = movies_service.create_movie(
                title=title,
                release_date=release_date,
                genre=genre_names[selected_genre_name],
                actors=selected_actors_ids,
                resume=resume
            )

            if new_movie:
                st.success('Filme cadastrado com sucesso!')
                st.rerun()

        except Exception as e:
            st.error(f'Erro ao cadastrar o filme: {e}')