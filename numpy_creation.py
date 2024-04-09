import streamlit as st

def numpy_creation():
    st.title('Создание массивов в NumPy')

    st.markdown("""
    ### Способы создания Numpy arrays
    - Конвертация из Python structures
    - Генерация с помощью встроенных функций
    - Чтение с диска
    """)

    st.markdown("""
    #### Конвертация из Python structures
    """)
    
    st.code("""
    import numpy as np

    np.array([1, 2, 3, 4, 5])
    """, language='python')

    st.markdown("""
    При конвертации можно задавать тип данных с помощью аргумента dtype.
    """)

    st.code("""
    np.array([1, 2, 3, 4, 5], dtype=np.float32)
    """, language='python')

    st.markdown("""
    #### Генерация Numpy arrays
    - arange
    - linspace
    - logspace
    - zeros
    - ones
    - empty
    """)

    st.code("""
    np.arange(0, 5, 0.5)
    """, language='python')

    # Остальные примеры создания массивов можно добавить аналогичным образом

if __name__ == '__main__':
    numpy_creation()
