import streamlit as st
from movies.repository import MoviesRepository


class MoviesService:
    def __init__(self):
        self.movies_repository = MoviesRepository()

    def get_movies(self):
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movies_repository.get_movies()
        st.session_state.movies = movies
        return movies   

    def create_movie(self, title, release_date, genre, actors, resume):
        movie = {
            'title': title,
            'release_date': release_date.strftime('%Y-%m-%d'),  # 🔥 CORREÇÃO DATA
            'genre': genre,
            'actors': actors,
            'resume': resume
        }

        new_movie = self.movies_repository.create_movie(movie)
        st.session_state.movies.append(new_movie)
        return new_movie
    
    def get_movies_stats(self):
        return self.movies_repository.get_movies_stats()