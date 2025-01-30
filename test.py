def calculate_n(start, number):
    s = [start]
    v = start
    for i in range(1, number):
        s.append(v := ( v - (4 if i % 2 == 1 else 3) ))

    return s

