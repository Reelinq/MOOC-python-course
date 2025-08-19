def alkuluvut():
    luku = 2
    while True:
        onko_alku = True
        for i in range(2, luku):
            if luku % i == 0:
                onko_alku = False
                break
        if onko_alku:
            yield luku
        luku += 1