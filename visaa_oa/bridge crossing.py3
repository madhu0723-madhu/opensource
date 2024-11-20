X, Y, Z = map(int, input().split())
max_load = Z - Y
if max_load <= 0:
    print(0)
else:
    max_mangoes = max_load // X  
    print(max_mangoes)
