# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

# n = int(input('введите день недели: '))
# if n > 0 and n < 6:
#     print('Это рабочий день.')
# elif n == 6 or n == 7:
#     print('Это выходной день. Урааааа!!!')
# else: print("Такого дня недели не существует.")



# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.i

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not(x or y or z) == (not x and not y and not z):
#                 print(x,y,z)



# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('введите координату х: '))
y = int(input('введите координату y: '))
if x > 0 and y > 0:
    print(f'точка с координатами ({x};{y}) расположена в I четверти координатной плоскости')
elif x < 0 and y > 0:
    print(f'точка с координатами ({x};{y}) расположена во II четверти координатной плоскости')
elif x < 0 and y < 0:
    print(f'точка с координатами ({x};{y}) расположена в III четверти координатной плоскости')
elif x > 0 and y < 0:
    print(f'точка с координатами ({x};{y}) расположена в IV четверти координатной плоскости')
elif x == 0: 
    print(f'точка с координатами ({x};{y}) расположена на оси координат X')
elif y == 0: 
    print(f'точка с координатами ({x};{y}) расположена на оси координат Y')