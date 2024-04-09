import streamlit as st
import numpy as np
from st_pages import Page, show_pages, add_page_title
from numpy_intro import numpy_intro
from numpy_creation import numpy_creation
from numpy_operations import numpy_operations
from numpy_polynomials import numpy_polynomials
from numpy_linear_algebra import numpy_linear_algebra


def main():
    st.set_page_config(layout="wide")
    st.sidebar.title("NumPy")

    show_pages(
        [
           Page("app.py", "Введение", "🏠"),
           Page("numpy_intro.py", "Немного о NumPy", ":flag-np:"),
           Page("numpy_creation.py", "Создание массивов", ":one:"),
           Page("numpy_operations.py", "Операции в NumPy", ":two:"),
           Page("numpy_linear_algebra.py", "Линейная алгебра", ":three:"),
           Page("numpy_polynomials.py", "Работа с полиномами", ":four:"), 
        ]
    )
    style = "<style>h2 {text-align: center;}</style>"

    st.title("NumPy - универсальная библиотека для научных вычислений на Python")

    st.markdown(style, unsafe_allow_html=True)
    c1, c2 = st.columns((1,1))

    with c1:
        st.image("https://kbfblog.com/wp-content/uploads/2021/10/article-03440000002019214749270.jpg", output_format='png')

    with c2:
        st.image("https://i.ytimg.com/vi/sihkRZV1wCY/maxresdefault.jpg?7857057827")

    # Generate Three equal columns
    c1, c2 = st.columns((1, 1))

    with c1:
        st.subheader("**Работу выполнили студенты МГУ Саров из группы ВМ-123    :**")
    
    with c2:
        st.subheader("Бабенко Михаил, Баринов Даниил, Гайсин Роберт, Кислер Роман")

if __name__ == "__main__":
    main()
