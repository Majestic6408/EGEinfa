for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = (z <= (not(y <= x))) or w
                if not F:
                    print(w, x, y, z)