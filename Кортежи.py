immutable_var = 1, 10, 'apple', 2,5
print(immutable_var)
immutable_var [1] = 'snake' # кортеж не поддерживает обращение по элементам поэтому внести изменение не позволит
print(immutable_var)

muttable_list =( [2,'mother'], 50, 'cat', 1, 55)
muttable_list [0][0] = 100
print(muttable_list)
