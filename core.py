import streamlit as st
from genres.page import show_genre
from movies.page import show_movie
from actors.page import show_actor
from reviews.page import show_review
from login.page import show_login

def main():
    st.markdown(
        """
        <style>
        * {
            user-select: none;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if 'token' not in st.session_state:
        show_login()
    else:
        st.title('Flix App')

        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',
            ['Inicio', 'Gêneros', 'Filmes', 'Atores/Atrizes', 'Avaliações',]
        )

        if menu_option == 'Início':
            st.write('Início')
        
        if menu_option == 'Gêneros':
            show_genre()

        if menu_option == 'Filmes':
            show_movie()
        
        if menu_option == 'Atores/Atrizes':
            show_actor()
        
        if menu_option == 'Avaliações':
            show_review()

if __name__ == '__main__':
    main()