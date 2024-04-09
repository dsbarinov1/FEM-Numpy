import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def numpy_polynomials():
    st.title('Работа с полиномами в NumPy')

    st.markdown("""
    ## Работа с полиномами
    В пакете NumPy реализован набор специализироваанных функций и методов для работы с полиномами.
    Функция **``poly``** ищет коэффициенты многочлена с заданной последовательностью корней (кратные корни должны быть включены в последовательность столько раз, какова их кратность), возвращая коэффициенты многочлена, старший коэффициент которого равен единице. Также может быть задана квадратная матрица, и в этом случае возвращаются коэффициенты характеристического многочлена матрицы.

    ```python
    roots_1 = [-1,2,2,34]
    poly_1 = np.poly(roots_1)
    poly_1
    ```

    Вывод:

    ```python
    array([   1.,  -37.,  102.,    4., -136.])
    ```
    Полученный массив представляет полином\n
    $$1.0 \cdot x^{4} - 37.0 \cdot x^{3} + 102.0 \cdot x^{2} + 4.0 \cdot x - 136.0$$\n

    Функция **``roots``** ищет корни полинома по заданным коэффициентам.

    ```python
    roots_2 = np.roots(poly_1)
    roots_2
    ```
    Вывод:

    ```python
    array([34.        ,  2.00000004,  1.99999996, -1.        ])
    ```
    Функция **``polyint``** производит интегрирование полинома с заданными коэффициентам.

    Проинтегрируем полином\n
    $$x^5 + x^4 + x^3 + x^2 + x + 1$$

    ```python
    poly_int_1 = np.polyint([1,1,1,1,1,1])
    poly_int_1
    ```
    Вывод:
    ```python
    array([0.16666667, 0.2       , 0.25      , 0.33333333, 0.5       ,
       1.        , 0.        ])
    ```
    Получили полином\n
    $$ \\frac{1}{6}x^6 + \\frac{1}{5}x^5 + \\frac{1}{4}x^4 + \\frac{1}{3}x^3 + \\frac{1}{2}x^2 + x + 1 + 0$$

    Функция **``polyder``** производит дифференцирование полинома с заданными коэффициентам.
    ```python
    poly_diff_1 = np.polyder(poly_int_1)
    poly_diff_1
    ```
    Вывод:
    ```python
    array([1., 1., 1., 1., 1., 1.])
    ```
    Функции **``polyadd``**, **``polysub``**, **``polymul``** и **``polydiv``** позволяют проводить суммирование, вычитание, умножение и деление полиномов, соответственно.
    Функция **``polyval``** подставляет в многочлен заданное значение.

    ```python
    res_1 = np.polyval(poly_1,5)
    res_1
    ```
    Вывод:
    ```python
    -1566.0
    ```
    Функция **``polyfit``** может быть использована для подбора интерполяционного многочлена заданного порядка для некоторого набора данных.

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
    ```
    """
    )
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

    chart_type = st.sidebar.selectbox('Выберите степень полинома', ['2', '3', '4', '5', '6', '7', '8', '9', '10'])
    # Отображение соответствующего графика
    st.set_option('deprecation.showPyplotGlobalUse', False)
    fig = plt.figure(0)
    plt.plot(x, y, '--o')

    if chart_type == '2':
        st.subheader('Приближение полиномом 2 степени.')
        plt.plot(x,y2)
        st.pyplot()
    elif chart_type == '3':
        st.subheader('Приближение полиномом 3 степени.')
        plt.plot(x,y3)
        st.pyplot()
    elif chart_type == '4':
        st.subheader('Приближение полиномом 4 степени.')
        plt.plot(x,y4)
        st.pyplot()
    elif chart_type == '5':
        st.subheader('Приближение полиномом 5 степени.')
        plt.plot(x,y5)
        st.pyplot()
    elif chart_type == '6':
        st.subheader('Приближение полиномом 6 степени.')
        plt.plot(x,y6)
        st.pyplot()
    elif chart_type == '7':
        st.subheader('Приближение полиномом 7 степени.')
        plt.plot(x,y7)
        st.pyplot()
    elif chart_type == '8':
        st.subheader('Приближение полиномом 8 степени.')
        plt.plot(x,y8)
        st.pyplot()
    elif chart_type == '9':
        st.subheader('Приближение полиномом 9 степени.')
        plt.plot(x,y9)
        st.pyplot()
    elif chart_type == '10':
        st.subheader('Приближение полиномом 10 степени.')
        plt.plot(x,y10)
        st.pyplot()


if __name__ == '__main__':
    numpy_polynomials()
