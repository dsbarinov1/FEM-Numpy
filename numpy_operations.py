import streamlit as st
import numpy as np

def numpy_operations():
    st.title('Операции и функции в NumPy')

    st.markdown("""
    ## Операции

    ```python
    x = np.arange(40).reshape(5, 2, 4)
    print(x)

    print(x.mean())
    print(np.mean(x))

    a =[[1, 2], [1, 0]]
    b =np.unique(a, axis=0)
    np.sort(a, axis=0)

    a = np.array([1, 2, 3], dtype=np.int_)
    b = np.array([4, 5, 6], dtype=np.int_)
    np.concatenate((a.reshape(len(a), 1), b.reshape(len(b), 1)), axis=1)

    x.mean(axis=0)

    x.mean(axis=1)

    x.mean(axis=2)

    x.mean(axis=(0,2))

    x.mean(axis=(0,1,2))
    ```

    ## Конкатенация многомерных массивов

    Конкатенировать несколько массивом можно с помощью функций **np.concatenate, np.hstack, np.vstack, np.dstack**

    ```python
    x = np.arange(10).reshape(5, 2)
    y = np.arange(100, 120).reshape(5, 4)

    np.hstack((x, y))

    a = np.array([1, 2, 3, 4, 5])
    b = np.zeros(5)
    c = np.vstack((a, b))
    c = c.T
    c.ravel()

    np.insert(a, range(1, len(a)), 0)

    x = np.ones([2, 3])
    y = np.zeros([2, 2])

    # Какой будет результат
    print(np.hstack((x,y)).shape)
    print(np.vstack((x,y)).shape)

    p = np.arange(1).reshape([1, 1, 1, 1])
    p

    print("vstack: ", np.vstack((p, p)).shape)
    print("hstack: ", np.hstack((p, p)).shape)
    print("dstack: ", np.dstack((p, p)).shape)
    print("concatenate: ", np.concatenate((p, p), axis=3).shape)
    ```

    ## Типы

    ```python
    x = [1, 2, 70000]

    np.array(x, dtype=np.float32)

    np.array(x, dtype=np.uint16)

    np.array(x, dtype=np.unicode_)
    ```

    ## Типизация

    ```python
    import numpy.typing as npt

    def as_array(a: npt.ArrayLike) -> npt.NDArray[np.int_]:
        return np.array(a)

    arr = as_array([1,2, 3])
    ```

    ## Функциональное программирование

    ```python
    def f(value):
        return np.sqrt(value)

    print(np.apply_along_axis(f, 0, np.arange(10)))

    vf = np.vectorize(f)

    vf(np.arange(100000))
    ```

    ```python
    np.apply_along_axis(f, 0, np.arange(100000))
    ```

    ```python
    np.array([f(v) for v in np.arange(100000)])
    ```
    """)

if __name__ == '__main__':
    numpy_operations()
