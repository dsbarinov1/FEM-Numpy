import streamlit as st
from numpy_intro import numpy_intro
from numpy_creation import numpy_creation
from numpy_indexing import numpy_indexing
from numpy_broadcasting import numpy_broadcasting
from numpy_operations import numpy_operations
from numpy_polynomials import numpy_polynomials
from numpy_linear_algebra import numpy_linear_algebra

def main():
    st.set_page_config(layout="wide")

    page = st.sidebar.selectbox("Выберите страницу", ["Введение в NumPy", "Создание массивов в NumPy", 
                                                      "Индексация в NumPy", "Broadcasting в NumPy",
                                                      "Операции в NumPy", "Линейная алгебра в NumPy", 
                                                      "Полиномы в NumPy"])
    
    if page == "Введение в NumPy":
        numpy_intro()
    elif page == "Создание массивов в NumPy":
        numpy_creation()
    elif page == "Индексация в NumPy":
        numpy_indexing()
    elif page == "Broadcasting в NumPy":
        numpy_broadcasting()
    elif page == "Операции в NumPy":
        numpy_operations()
    elif page == "Линейная алгебра в NumPy":
        numpy_linear_algebra()
    elif page == "Полиномы в NumPy":
        numpy_polynomials()

if __name__ == "__main__":
    main()
