import streamlit as st

def numpy_indexing():
    st.title('Индексация в NumPy')

    st.markdown("""
    В NumPy работает привычная индексация Python, включая использование отрицательных индексов и срезов.
    """)

    st.code("""
    array = np.arange(10)
    print(array)
    print(array[0])
    print(array[-1])
    print(array[1:-1])
    print(array[1:-1:2])
    print(array[::-1])
    """, language='python')

    st.markdown("""
    В качестве индексов можно использовать массивы:
    """)

    st.code("""
    array[[0, 2, 4, 6, 8, 10]]
    """, language='python')

    st.code("""
    array[[True, False, True, False, True, False, True, False, True, False, True, False]]
    """, language='python')

    st.markdown("""
    ### Пример работы с многомерными массивами:
    """)

    st.code("""
    matrix = np.array([[np.nan,  1,  2,  3], [4, np.nan,  5, np.nan]])

    nans = np.argwhere(np.isnan(matrix))
    mean = np.nanmean(matrix)
    np.nan_to_num(matrix, nan=mean)
    """, language='python')

if __name__ == '__main__':
    numpy_indexing()
