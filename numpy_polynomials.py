import streamlit as st
import numpy as np

def numpy_polynomials():
    st.title('Работа с полиномами в NumPy')

    st.markdown("""
    ## Работа с полиномами

    ```python
    roots_1 = [-1,2,2,34]
    poly_1 = np.poly(roots_1)
    poly_1
    ```

    ```python
    roots_2 = np.roots(poly_1)
    roots_2
    ```

    ```python
    poly_int_1 = np.polyint([1,1,1,1,1,1])
    poly_int_1
    ```

    ```python
    poly_diff_1 = np.polyder(poly_int_1)
    poly_diff_1
    ```

    ```python
    res_1 = np.polyval(poly_1,5)
    res_1
    ```

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 100, 10)
    y = 10 * np.random.random(10)
    pol2 = np.polyfit(x, y, 2)
    pol3 = np.polyfit(x, y, 3)
    pol4 = np.polyfit(x, y, 4)
    pol5 = np.polyfit(x, y, 5)
    pol6 = np.polyfit(x, y, 6)
    pol7 = np.polyfit(x, y, 7)
    pol8 = np.polyfit(x, y, 8)
    pol9 = np.polyfit(x, y, 9)
    pol10 = np.polyfit(x, y, 10)
    y2 = np.polyval(pol2,x)
    y3 = np.polyval(pol3,x)
    y4 = np.polyval(pol4,x)
    y5 = np.polyval(pol5,x)
    y6 = np.polyval(pol6,x)
    y7 = np.polyval(pol7,x)
    y8 = np.polyval(pol8,x)
    y9 = np.polyval(pol9,x)
    y10 = np.polyval(pol10,x)

    fig = plt.figure(0)
    plt.plot(x, y, '--o')
    ```

    ## Линейная алгебра

    SVD, решение линейных уравнений, нахождение собственных значений, все отсюда:
    https://numpy.org/doc/stable/reference/routines.linalg.html
    ```
    ```

    ```python
    dot(a, b[, out])

    linalg.multi_dot(arrays, *[, out])

    vdot(a, b, /)

    outer(a, b[, out])

    matmul(x1, x2, /[, out, casting, order, ...])

    tensordot(a, b[, axes])

    einsum(subscripts, *operands[, out, dtype, ...])

    einsum_path(subscripts, *operands[, optimize])

    linalg.matrix_power(a, n)

    kron(a, b)

    linalg.cholesky(a)

    linalg.qr(a[, mode])

    linalg.svd(a[, full_matrices, compute_uv, ...])
    ```

    ```python
    ## Собственные значения

    linalg.eig(a)

    linalg.eigh(a[, UPLO])

    linalg.eigvals(a)

    linalg.eigvalsh(a[, UPLO])
    ```

    ```python
    ## Нормы

    linalg.norm(x[, ord, axis, keepdims])

    linalg.cond(x[, p])

    linalg.det(a)

    linalg.matrix_rank(A[, tol, hermitian])

    linalg.slogdet(a)

    trace(a[, offset, axis1, axis2, dtype, out])
    ```

    ```python
    ## Решение линейных уравнений

    linalg.solve(a, b)

    linalg.tensorsolve(a, b[, axes])

    linalg.lstsq(a, b[, rcond])

    linalg.inv(a)

    linalg.pinv(a[, rcond, hermitian])

    linalg.tensorinv(a[, ind])
    ```

    ## Работа с полиномами

    roots_1 = [-1,2,2,34]
    poly_1 = np.poly(roots_1)
    poly_1
    Полученный массив представляет полином
    $$
    1.0 \cdot x^{4} - 37.0 \cdot x^{3} + 102.0 \cdot x^{2} + 4.0 \cdot x - 136.0
    $$

    Функция **``roots``** ищет корни полинома по заданным коэффициентам.

    roots_2 = np.roots(poly_1)
    roots_2

    Функция **``polyint``** производит интегрирование полинома с заданными коэффициентам.

    Проинтегрируем полином
    $$
    x^5 + x^4 + x^3 + x^2 + x + 1
    $$

    poly_int_1 = np.polyint([1,1,1,1,1,1])
    poly_int_1

    Получили полином
    $$
    \frac{1}{6}x^6 + \frac{1}{5}x^5 + \frac{1}{4}x^4 + \frac{1}{3}x^3 + \frac{1}{2}x^2 + x + 1 + 0
    $$

    Функция **``polyder``** производит дифференцирование полинома с заданными коэффициентам.

    poly_diff_1 = np.polyder(poly_int_1)
    poly_diff_1

    Функции **``polyadd``**, **``polysub``**, **``polymul``** и **``polydiv``** позволяют проводить суммирование, вычитание, умножение и деление полиномов, соответственно. Функция **``polyval``** подставляет в многочлен заданное значение.

    res_1 = np.polyval(poly_1,5)
    res_1

    Функция **``polyfit``** может быть использована для подбора интерполяционного многочлена заданного порядка для некоторого набора данных.

    ```python
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 100, 10)
    y =10*np.random.random(10)
    print ("x = ",x)
    print ("y = ",y)
    pol2 = np.polyfit(x, y, 2)
    pol3 = np.polyfit(x, y, 3)
    pol4 = np.polyfit(x, y, 4)
    pol5 = np.polyfit(x, y, 5)
    pol6 = np.polyfit(x, y, 6)
    pol7 = np.polyfit(x, y, 7)
    pol8 = np.polyfit(x, y, 8)
    pol9 = np.polyfit(x, y, 9)
    pol10 = np.polyfit(x, y, 10)
    y2 = np.polyval(pol2,x)
    y3 = np.polyval(pol3,x)
    y4 = np.polyval(pol4,x)
    y5 = np.polyval(pol5,x)
    y6 = np.polyval(pol6,x)
    y7 = np.polyval(pol7,x)
    y8 = np.polyval(pol8,x)
    y9 = np.polyval(pol9,x)
    y10 = np.polyval(pol10,x)
    fig = plt.figure(0)
    plt.plot(x,y,'--o')
    ```
    """)

if __name__ == '__main__':
    numpy_polynomials()
