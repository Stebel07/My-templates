from fnmatch import fnmatch

min_col_str = 0
for i in range (1037799, 1936169997, 2023): #Первое число узнается подбором(близжайшее к минимальному числу, подходящему к маске), 
    #второе число - максимально возможное число, подходящее к маске, третье число - число кратности
    if min_col_str == 2: #2 - Необходимое кол-во строк(в заданиях, где нету определенного кол-ва убрать все строки с упоминанием min_col_str)
        break
    if fnmatch(str(i), '1?3616*7'):
        min_col_str += 1
        print(i, i // 2023)