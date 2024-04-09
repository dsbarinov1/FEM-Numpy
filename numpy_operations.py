import streamlit as st
import numpy as np
import subprocess
import sys

def print_out(name):
    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/{name}.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")

def numpy_operations():
    st.title('Операции и функции в NumPy')

    st.write("## Размеры массива и количество размерностей")

    #shape and dim
    st.write("Pазмеры массива храниться в поле **shape**, а количество размерностей - в **ndim**")

    st.markdown("""
    ```python
    array = np.ones((2, 3,))
    print('Размерность массива - %s, количество размерностей - %d'%(array.shape, array.ndim))
    print(array)
    ```
    """
    )

    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/shape_ndim.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")

    #reshape
    st.write("Метод **[reshape](https://docs.scipy.org/doc/numpy/reference/generated/numpy.reshape.html)** позволяет преобразовать размеры массива без изменения данных")    


    st.markdown("""
    ```python
    array = np.arange(0, 6, 0.5)
    array = array.reshape((2, 6))
    print(array)
    ```
    """
    )

    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/reshape.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")


    #ravel
    st.write("Для того что бы развернуть многомерный массив в вектор, можно воспользоваться функцией **ravel**")

    st.markdown("""
    ```python
    array = np.ravel(array)
    print(array)
    ```
    """
    )

    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/ravel.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")


    #copy
    st.write("## Копирование")
    st.markdown("""
    Для копирования в numpy есть метод **copy**
    ```python
    array1 = np.array([1,2,3])
    array2 = array1.copy
    print(array2)
    ```
    """
    )
    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/copy.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")


    #операции над массивами одинаковой размерности
    st.markdown("""
    ## Операции над массивами одинаковой размерности
    Арифметические операции в NumPy можно производить непосредственно над массивами одинаковой размерности без использования циклов.\n
    Например, вычисление поэлементного сложения (или разности) между векторами выглядит следующим образом:
    ```python
    vec1 = np.array([1, 1, 1, 1, 1])
    vec2 = np.array([2, 2, 2, 2, 2])
    print(vec1 + vec2)
    ```
    """
    )

    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/simple_op.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")

    st.markdown("""
    Аналогчино для многомерных массивов\n
    **Замечание:** Все арифметические операции над массивами одинаковой размерности производятся поэлементно
                
    
    ## Операции
    Транспонирование производится с помощью **.T**
                
    
    В NumPy реализованно много полезных операций для работы с массивами: **[np.min](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.min.html)**, 
    **[np.max](https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.max.html)**, 
    **[np.sum](https://docs.scipy.org/doc/numpy/reference/generated/numpy.sum.html)**, 
    **[np.mean](https://docs.scipy.org/doc/numpy/reference/generated/numpy.mean.html)** и т.д.\n
    **Замечание:** В каждой из перечисленных функций есть параметр \*\*axis\*\*, который указывает по какому измерению производить данную операцию. По умолчанию операция производится по всем значениям массива
    ```python
    x = np.arange(40).reshape(5, 2, 4)
    print(x)
    ```           
    """
    )

    text = ''
    command = [f"{sys.executable}", "-u", f"scripts/x.py"] # Add '-u' to disable stdout buffering
    process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT, universal_newlines = True)

    while process.poll() is None:
        line = process.stdout.readline()
        if not line:
            continue
        text += line.strip() + '  \n'
    st.info(f"Output:  \n{text}")

    st.markdown("""
    ```python
    print(x.mean(axis=0))
    ```
    """
    )
    print_out("x_mean0")

    st.markdown("""
    ```python
    print(x.mean(axis=1))
    ```
    """
    )
    print_out("x_mean1")

    st.markdown("""
    ```python
    print(x.mean(axis=2))
    ```
    """
    )
    print_out("x_mean2")

    st.markdown("""
    ```python
    print(x.mean(axis=(0, 2)))
    ```
    """
    )
    print_out("x_mean02")

    st.markdown("""
    Также есть операция **[np.unique](https://numpy.org/doc/stable/reference/generated/numpy.unique.html)**, возвращающая уникальные значения элементов массива,
    и операция **[np.sort](https://numpy.org/doc/stable/reference/generated/numpy.sort.html)** возвращающая отсортированный массив
    """
    )
    

    st.markdown("""
    
    ## Конкатенация многомерных массивов

    Конкатенировать несколько массивом можно с помощью функций **np.concatenate, np.hstack, np.vstack, np.dstack**

    ```python
    x = np.arange(10).reshape(5, 2)
    y = np.arange(100, 120).reshape(5, 4)

    print(np.hstack((x, y)))
    ```
    """)

    print_out("hstack")

    st.markdown("""
    ```python
    a = np.array([1, 2, 3, 4, 5])
    b = np.zeros(5)
    c = np.vstack((a, b))
    c = c.T
    print(c.ravel())
    ```
    """)
    print_out("vstack")

if __name__ == '__main__':
    numpy_operations()
