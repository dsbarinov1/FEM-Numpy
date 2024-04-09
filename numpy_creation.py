import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np

def create_python_array(size):
    return [i for i in range(size)]

def create_numpy_array(size):
    return np.arange(size)

def compare_creation_time(max_size):
    sizes = list(range(100, max_size+1, max_size//10))
    python_times = []
    numpy_times = []

    for size in sizes:
        start_time = time.time()
        create_python_array(size)
        python_times.append(time.time() - start_time)

        start_time = time.time()
        create_numpy_array(size)
        numpy_times.append(time.time() - start_time)

    return sizes, python_times, numpy_times

def python_creation():
    st.title("Создание массивов в Python")

    st.write("""
    ## Создание одномерных массивов

    ### Используя список
    ```python
    arr1 = [1, 2, 3, 4, 5]
    ```
    """)
    arr1 = [1, 2, 3, 4, 5]
    st.info(f"Output:  \n {arr1}")

    st.write("""
    ### С использованием генератора списка
    ```python
    arr2 = [i for i in range(1, 6)]
    ```
    """)
    arr2 = [i for i in range(1, 6)]
    st.info(f"Output:  \n {arr2}")

    st.write("""
    ## Создание двумерных массивов

    ### С использованием вложенных списков
    ```python
    arr3 = [[1, 2, 3], [4, 5, 6]]
    ```
    """)
    arr3 = [[1, 2, 3], [4, 5, 6]]
    st.info(f"Output:  \n {arr3}")

    st.write("""
    ### С использованием генератора вложенных списков
    ```python
    arr4 = [[i + j for j in range(3)] for i in range(2)]
    ```
    """)
    arr4 = [[i + j for j in range(3)] for i in range(2)]
    st.info(f"Output:  \n {arr4}")

    st.write("""
    ## Создание случайных массивов

    ### Массив случайных (целых) чисел
    ```python)
    import random
    rand_arr = [random.randint(1, 10) for _ in range(5)]
    ```
    """)
    size = st.number_input('Выберите размер массива:', value=5)
    max_int = st.number_input('Укажите ограничение сверху на генерируемые целые числа: ', value=10)
    random_int_array = st.button("Сгенерировать ***случайный*** массив!")

    if random_int_array:
        from scripts.create_array import create_random_int_python_array
        st.info(f"Output:  \n{create_random_int_python_array(max_int, size)}")
    
    st.write("""
    ## Создание случайных многомерных массивов

    ### Многомерный массив случайных (целых) чисел
    ```python
    import random
    rand_arr = [[random.randint(0, max_int) for _ in range(max_size)] for _ in range(max_dim)]
    ```
    """)
    dim = st.number_input('Выберите размерность массива: ', value=2, key=4)
    size2 = st.number_input('Выберите размер подмассива:', value=10, key=2)
    max_int2 = st.number_input('Укажите ограничение сверху на генерируемые целые числа: ', value=10, key=3)
    random_int_multi_array = st.button("Сгенерировать ***случайный*** многомерный массив!")

    if random_int_multi_array:
        from scripts.create_array import create_random_int_python_multi_array
        multi_arr = create_random_int_python_multi_array(max_int2, size2, dim)
        text='['
        for i in range(0, dim):
            text+='['
            for j in range(0, size2):
                text+=str(multi_arr[i][j])
                if j != size2-1:
                    text+=', '
            if i!=dim-1:
                text+=']  \n'
            else:
                text+=']]'
            
        st.info(f"Output:  \n{text}")

    st.write("""
    ## Интерактивное создание массива
    """)

    import random
    dim = st.slider("Выберите размерность массива", min_value=1, max_value=10, value=1)
    size = st.slider("Выберите размер каждого измерения", min_value=1, max_value=10, value=1)
    interactive_arr = [[random.randint(1, 10) for _ in range(size)] for _ in range(dim)]
    st.write(interactive_arr)

def numpy_creation():
    import random
    st.title("Создание массивов в NumPy")

    st.write("""
    ## Создание одномерных массивов

    ### Используя функцию `np.array()`
    ```python
    arr1 = np.array([1, 2, 3, 4, 5])
    ```
    """)
    arr1 = np.array([1, 2, 3, 4, 5])
    st.info(f"Output:  \n {arr1}")

    st.write("""
    ### С использованием функций `np.zeros()` и `np.ones()`
    ```python
    zeros_arr = np.zeros(5)
    ones_arr = np.ones(5)
    ```
    """)
    zeros_arr = np.zeros(5)
    ones_arr = np.ones(5)
    st.info(f"Output:  \n {zeros_arr}  \n {ones_arr}")

    st.write("""
    ### Создание последовательности с использованием функции `np.arange()`
    ```python
    seq_arr = np.arange(1, 6)
    ```
    """)
    seq_arr = np.arange(1, 6)
    st.info(f"Output:  \n {seq_arr}")
    
    st.write("""
    ## Создание двумерных массивов

    ### С использованием функции `np.array()`
    ```python
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    ```
    """)
    arr2 = np.array([[1, 2, 3], [4, 5, 6]])
    st.info(f"Output:  \n {arr2}")

    st.write("""
    ### Массив из нормального распределения
    Три ключевых параметра:
    loc - среднее значение (пик) распределения. По умолчанию - 0.
    scale - стандартное отклонение. По умолчанию - 1.
    size - форма результирующего массива. По умолчанию - 1.
    ```python
    normal_arr = np.random.normal(0, 1, 1)
    ```
    """)
    normal_arr = np.random.normal(0, 1, 1)
    st.info(f"Output:  \n {normal_arr}")
    
    st.write("""
    ## Создание случайных массивов

    ### Массив случайных чисел
    ```python
    rand_arr = np.random.rand(max_dim, max_size)
    ```
    """)
    dim = st.slider("Выберите размерность массива", min_value=1, max_value=10, value=1)
    size = st.slider("Выберите размер каждого измерения", min_value=1, max_value=10, value=1)
    np_random_array = st.button("Сгенерировать ***случайный*** массив!")

    if np_random_array:
        from scripts.create_array import create_random_float_numpy_array
        multi_arr = create_random_float_numpy_array(dim, size)
        text='['
        for i in range(0, size):
            text+='['
            for j in range(0, dim):
                text+=str(multi_arr[i][j])
                if j != dim-1:
                    text+=', '
            if i!=size-1:
                text+=']  \n'
            else:
                text+=']]'
            
        st.info(f"Output:  \n{text}")

    st.write("""
    ### Массив случайных целых чисел
    ```python
    randint_arr = np.random.randint(0, max_int, max_size)
    ```
    """)
    max_int2 = st.number_input('Укажите ограничение сверху на генерируемые целые числа: ', value=10, key=4)
    size3 = st.slider("Выберите размер каждого измерения", min_value=1, max_value=10, value=1, key=5)
    np_random_int_array = st.button("Сгенерировать ***случайный*** целочисленный массив!")

    if np_random_int_array:
        from scripts.create_array import create_random_int_numpy_array
        st.info(f"Output:  \n{create_random_int_numpy_array(max_int2, size3)}")
    

    st.write("""
    ### Интерактивное создание массива
    """)
    
    dim = st.slider("Выберите размерность массива", min_value=1, max_value=10, value=1, key=6)
    size = st.slider("Выберите размер каждого измерения", min_value=1, max_value=10, value=7)
    interactive_arr = np.random.randint(10, size=tuple(size for _ in range(dim)))
    st.write(interactive_arr)


if __name__ == '__main__':
    menu = st.sidebar.radio("Подразделы",
        (   
            ":blue[Pyt]:orange[hon]",
            ":green[NumPy]",
            ":rainbow[Python vs. NumPy]",
        ),
        captions = 
        [
            "Стандартная реализация",
            "NumPy реализация",
            "Сравнение производительности	:timer_clock:"
        ]
    )

    if menu == ":blue[Pyt]:orange[hon]":
        python_creation()

    if menu == ":green[NumPy]":
        numpy_creation()

    if menu == ":rainbow[Python vs. NumPy]":
        st.title("Сравнение создания массивов в Python и NumPy")

        st.write("""
        ## Плюсы и минусы создания массивов в Python и NumPy

        ### Python:
        - **Плюсы:**
            - Простота использования.
            - Широкие возможности работы со списками и генераторами.
            - Возможность работы с различными типами данных в одном массиве (списке)
        - **Минусы:**
            - Медленная производительность для больших массивов.
            - Ограниченные функциональные возможности.

        ### NumPy:
        - **Плюсы:**
            - Быстрые операции над массивами благодаря векторизации.
            - Расширенные возможности работы с массивами (математические функции, индексация и т. д.).
            - Потребляет (в среднем) меньше памяти по сравнению с обычными списками.
        - **Минусы:**
            - Необходимость изучения дополнительной библиотеки.
            - Статическая типизация
        """)

        max_size = st.slider("Выберите максимальный размер массива для сравнения", min_value=100, max_value=100000000, value=50000)
        
        sizes, python_times, numpy_times = compare_creation_time(max_size)

        plt.figure(figsize=(10, 6))
        plt.plot(sizes, python_times, label="Python", marker='o')
        plt.plot(sizes, numpy_times, label="NumPy", marker='o')
        plt.xlabel("Размер массива")
        plt.ylabel("Время создания (сек)")
        plt.title("Сравнение времени создания массивов в Python и NumPy")
        plt.legend()
        st.pyplot(plt)
