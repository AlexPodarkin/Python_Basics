# подробнее о list comprehensions

arr = [(i, j)
       for i in range(3) if i % 2 != 0
       for j in range(4) if i % 2 != 0]
print(arr)


arr = [f"{i} * {j} = {i * j}"
       for i in range(3)
       for j in range(4)
       ]
print(arr)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
arr = [x
       for row in matrix
       for x in row]
print(matrix)
# из двухмерного массива в одномерный
print(arr)

# использовать 2 генератора списка для получения 2-х мерного массива
m, n = 4, 4
matrix = [[row for row in range(m)] for col in range(n)]
print(matrix)

# если нам надо возвести 2-х мерный массив в квадрат
matrix_2 = [[row ** 2 for row in col] for col in matrix]
print(matrix_2)

row = [x for v in matrix_2
       for x in v
       ]
print(row)
