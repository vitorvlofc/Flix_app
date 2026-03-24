import streamlit as st
from genres.page import show_genres


def main():
    st.title('Flix App')

    menu_options = st.sidebar.selectbox('Selecione uma opção', ['Início', 'Gêneros', 'Atores/Atrizes', 'Avaliações'])

    if menu_options == 'Início':
        st.write('  início')

    if menu_options == 'Gêneros':
        show_genres()

    if menu_options == 'Atores/Atrizes':
        st.write('  Lista de Atores/Atrizes')

    if menu_options == 'Filmes':
        st.write('  Lista de Filmes')

    if menu_options == 'Avaliações':
        st.write('  Lista de Avaliações')
        

if __name__ == '__main__':
    main()