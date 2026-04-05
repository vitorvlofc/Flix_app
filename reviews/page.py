import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

from reviews.service import ReviewService
from movies.service import MoviesService


def show_reviews():
    review_service = ReviewService()

    # ========================
    # LISTAGEM DE AVALIAÇÕES
    # ========================
    reviews = review_service.get_reviews()

    if reviews:
        st.title('Lista de Avaliações')

        reviews_df = pd.json_normalize(reviews)

        AgGrid(
            data=reviews_df,
            reload_data=True,
            key='reviews_grid'
        )
    else:
        st.warning('Nenhuma avaliação encontrada.')

    # ========================
    # FORMULÁRIO
    # ========================
    st.title('Cadastrar Nova Avaliação')

    movie_service = MoviesService()
    movies = movie_service.get_movies()

    # 🚨 proteção caso não tenha filmes
    if not movies:
        st.warning('Nenhum filme disponível para avaliar.')
        return

    # 🔥 CORREÇÃO: mapa título → id
    movie_map = {movie['title']: movie['id'] for movie in movies}

    selected_movie = st.selectbox(
        'Filme',
        list(movie_map.keys())
    )

    stars = st.number_input(
        label='Estrelas',
        min_value=1,
        max_value=5,
        step=1
    )

    comment = st.text_area('Comentário')

    # ========================
    # BOTÃO
    # ========================
    if st.button('Enviar Avaliação'):
        try:
            new_review = review_service.create_review(
                movie=movie_map[selected_movie],  #  ID correto
                stars=stars,
                comment=comment
            )

            if new_review:
                st.success('Avaliação cadastrada com sucesso!')
                st.rerun()

        except Exception as e:
            st.error(f'Erro ao cadastrar a avaliação: {e}')