import streamlit as st
from movies.service import MoviesService
import plotly.express as px


def show_home():
    st.title('Estatísticas dos Filmes')

    movie_service = MoviesService()
    movie_stats = movie_service.get_movies_stats()

    # ========================
    # GRÁFICO
    # ========================
    if 'movies_by_genre' in movie_stats and len(movie_stats['movies_by_genre']) > 0:
        st.subheader('Filmes por Gênero')

        fig = px.pie(
            movie_stats['movies_by_genre'],
            names='genre__name',
            values='count',
            title='Filmes por Gênero'
        )

        st.plotly_chart(fig)

    # ========================
    # TOTAL FILMES
    # ========================
    if 'total_movies' in movie_stats:
        st.subheader('Total de Filmes Cadastrados')
        st.write(movie_stats['total_movies'])

    # ========================
    # GÊNEROS (CORRIGIDO AQUI)
    # ========================
    if 'movies_by_genre' in movie_stats:
        st.subheader('Total de Gêneros Cadastrados')

        for genre in movie_stats['movies_by_genre']:
            st.write(f"{genre['genre__name']}: {genre['count']}")

    # ========================
    # TOTAL REVIEWS
    # ========================
    if 'total_reviews' in movie_stats:
        st.subheader('Total de Avaliações Cadastradas')
        st.write(movie_stats['total_reviews'])

    # ========================
    # MÉDIA
    # ========================
    if 'average_stars' in movie_stats:
        st.subheader('Média geral de estrelas nas avaliações')
        st.write(movie_stats['average_stars'])