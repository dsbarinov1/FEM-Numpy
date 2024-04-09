import streamlit as st

def numpy_broadcasting():
    st.title('Broadcasting в NumPy')

    st.markdown("""
    Broadcasting снимает правило одной размерности и позволяет производить арифметические операции над массивами разных, но всё-таки согласованных размерностей.
    """)

    st.markdown("""
    Простейшим примером является умножение вектора на число:
    """)

    st.code("""
    2 * np.arange(1, 4)
    """, language='python')

    st.markdown("""
    Правило согласования размерностей:
    ```In order to broadcast, the size of the trailing axes for both arrays in an operation must either be the same size or one of them must be one```
    """)

    st.markdown("""
    Пример добавления вектора к каждой строчке матрицы:
    """)

    st.code("""
    np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]]) + np.arange(3)
    """, language='python')

    st.markdown("""
    Пример добавления вектора к каждому столбцу матрицы:
    """)

    st.code("""
    np.arange(4)[:, np.newaxis] + np.array([[0, 0, 0], [10, 10, 10], [20, 20, 20], [30, 30, 30]])
    """, language='python')

if __name__ == '__main__':
    numpy_broadcasting()
