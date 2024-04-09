import streamlit as st

def numpy_intro():
    st.title('Введение в NumPy')

    st.markdown("""
    NumPy — это библиотека для работы с многомерными массивами и включает набор математических функций для работы над ними.
    """)

    st.markdown("""
    ### Особенности библиотеки:
    - Поддержка N-мерных массивов с быстрой векторизацией и индексацией.
    - Инструменты численных вычислений: множество математических функций, генераторы случайных чисел, операции линейной алгебры, преобразования Фурье и многое другое.
    - Совместимость с широким спектром вычислительных платформ.
    - Простота использования: для практического применения требуется знать только несколько концептов массивов NumPy.
    """)
    
    st.markdown("""
    ### Возможности библиотеки NumPy:
    - работать с многомерными массивами (включая матрицы)
    - производить быстрое вычисление математических функций на многомерных массивах
    """)

    st.markdown("""
    Ядром пакета NumPy является объект ndarray.
    """)

    st.markdown("""
    ### Важные отличия между NumPy arrays и Python sequences:
    - NumPy array имеет фиксированную длину, которая определяется в момент его создания (в отличие от Python lists, которые могут расти динамически)
    - Элементы в NumPy array должны быть одного типа
    - Можно выполнять операции непосредственно над NumPy arrays
    """)

    st.markdown("""
    ### Сильные стороны NumPy:
    - Vectorization
    - Broadcasting
    """)

    st.markdown("""
    ### Мотивирующий пример
    ![Imgur](https://i.imgur.com/z4GzOX6.png)
    """)

if __name__ == '__main__':
    numpy_intro()
