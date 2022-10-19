# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

def uniq_list(num):
    return [i for i in range(20, num + 1) if i % 20 == 0 or i % 21 == 0]

print(uniq_list(int(input("Enter the number: "))))

