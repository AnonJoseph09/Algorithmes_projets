def calc(array, n1, n2):
    return sum(array[n1:n2+1])


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n1, n2 = 2, 5
print(calc(array, n1, n2))  