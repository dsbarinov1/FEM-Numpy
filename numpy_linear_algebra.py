import streamlit as st
import numpy as np
#import subprocess
def numpy_linear_algebra():



    st.title("Линейная алгебра в NumPy")
    st.write("Функции numpy.linalg опираются на библиотеки BLAS и LAPACK для обеспечения эффективной низкоуровневой реализации стандартных алгоритмов линейной алгебры.")
    st.header("Скалярное произведение (numpy.linalg.dot)")
    st.markdown("Пример использования:")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    code = """
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    dot_product = np.dot(a, b)
    """
    st.code(code, language="python")
    dot_product = np.dot(a, b)
    st.info(f"Output:  \n{dot_product}")
    st.write("---")

    st.header("Матричное произведение (numpy.linalg.matmul)")
    st.markdown("Пример использования:")
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    code = """
    matrix1 = np.array([[1, 2], [3, 4]])
    matrix2 = np.array([[5, 6], [7, 8]])
    matrix_product = np.matmul(matrix1, matrix2)
    """
    st.code(code, language="python")
    matrix_product = np.matmul(matrix1, matrix2)
    st.info(f"Output:  \n{matrix_product[0]}  \n{matrix_product[1]}")
    st.write("---")

    st.header("Внешнее произведение (numpy.linalg.outer)")
    st.markdown("Пример использования:")
    outer_product = np.outer(a, b)
    code = """
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    outer_product = np.outer(a, b)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{outer_product[0]}  \n{outer_product[1]}  \n{outer_product[2]}")
    st.write("---")

    st.header("Сингулярное разложение (numpy.linalg.svd)")
    st.markdown("Пример использования:")
    code = """
    X = np.random.randn(3, 3)
    print(X)
    """
    X = np.random.randn(3, 3)
    U, S, V = np.linalg.svd(X)
    st.code(code, language="python")
    st.info(f"Output:  \n{X[0]}  \n{X[1]}  \n{X[2]}")
    code = """
    U, S, V = np.linalg.svd(X)
    print(U)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{U[0]}  \n{U[1]}  \n{U[2]}")
    code = """
    print(S)    
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{S}")
    code = """
    print(V)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{V[0]}  \n{V[1]}  \n{V[2]}")
    st.write("---")

    st.header("Собственные значения и собственные векторы(numpy.linalg.eig)")
    st.write("Позволяет вычислить собственные значения и правые собственные векторы квадратной матрицы")
    st.markdown("Пример использования:")
    A = np.array([[1, -2], [2, -3]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    code = """
    A = np.array([[1, -2], [2, -3]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    eigenvalues, eigenvectors
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{eigenvalues}  \n  \n{eigenvectors[0]}  \n{eigenvectors[1]}")
    st.write("---")

    st.header("QR Разложение (numpy.linalg.qr)")
    st.markdown("Пример использования:")
    Q, R = np.linalg.qr(matrix1)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    Q, R = np.linalg.qr(matrix)
    Q, R
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{Q[0]}  \n  {Q[1]}  \n  \n{R[0]}  \n{R[1]}")
    st.write("---")

    st.header("Обратная матрица (numpy.linalg.inv)")
    st.markdown("Пример использования:")
    inverse_matrix = np.linalg.inv(matrix1)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    inverse_matrix = np.linalg.inv(matrix)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{inverse_matrix[0]}  \n  {inverse_matrix[1]}")
    st.write("---")

    st.header("Определитель матрицы (numpy.linalg.det)")
    st.markdown("Пример использования:")
    determinant = np.linalg.det(matrix1)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    determinant = np.linalg.det(matrix)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{determinant}")
    st.write("---")

    st.header("Ранг матрицы (numpy.linalg.matrix_rank)")
    st.markdown("Пример использования:")
    rank = np.linalg.matrix_rank(matrix1)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    rank = np.linalg.matrix_rank(matrix)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{rank}")
    st.write("---")

    st.header("Возведение матрицы в степень (numpy.linalg.matrix_power)")
    st.markdown("Пример использования:")
    power = 3
    powered_matrix = np.linalg.matrix_power(matrix1, power)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    power = 3
    powered_matrix = np.linalg.matrix_power(matrix, power)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{powered_matrix[0]}  \n{powered_matrix[1]}")
    st.write("---")

    st.header("След матрицы (numpy.linalg.trace)  \nВозвращает сумму по указанным диагоналям матрицы (или 'стэка' матриц)  \nПри указании параметра offset=0 вернется сумма по главной диагонали  \n     При offset>0 - выше главной диагонали  \n     При offset<0 - ниже главной диагонали  \n     По умолчанию: offset=0")
    st.markdown("Пример использования:")
    trace = np.trace(matrix1)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    trace = np.trace(matrix)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{trace}")
    st.write("---")



    st.header("Норма вектора или матрицы (numpy.linalg.norm)")
    st.write("Позволяет вычислять одну из восьми матричных норм и одну из бесконечного числа векторных норм")
    st.markdown("Пример использования:")
    matrix = np.array([[1, 2], [3, 4]])
    np.linalg.norm(matrix)
    code = """
    matrix = np.array([[1, 2], [3, 4]])
    np.linalg.norm(matrix, ord='fro')  # норма Фробениуса
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{np.linalg.norm(matrix, ord='fro')}")
    st.write("---")

    st.header("Число обусловленности(numpy.linalg.cond)")
    st.write("Позволяет вычислить число обусловленности матрицы по одной из семи матричных норм")
    st.markdown("Пример использования:")
    a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
    np.linalg.cond(a) 
    code = """
    a = np.array([[1, 0, -1], [0, 1, 0], [1, 0, 1]])
    np.linalg.cond(a) #2-норма
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{np.linalg.cond(a)}")
    code = """
    np.linalg.cond(a, 'fro') #норма фробениуса
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{np.linalg.cond(a, 'fro')}")
    st.write("---")


    st.header("Решение систем линейных уравнений (numpy.linalg.solve)")
    st.markdown("Пример использования:")
    st.write("Решить систему:  \nx + 2 * y = 1  \n3 * x + 5 * y = 2")
    a = np.array([[1, 2], [3, 5]])
    b = np.array([1, 2])
    x = np.linalg.solve(a, b)
    code = """
    a = np.array([[1, 2], [3, 5]])
    b = np.array([1, 2])
    x = np.linalg.solve(a, b)
    """
    st.code(code, language="python")
    st.info(f"Output:  \n{x}")
    st.write("---")


if __name__ == "__main__":
    numpy_linear_algebra()
