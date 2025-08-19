def pisin(merkkijono: list):
    pidempi = ""
    for i in merkkijono:
        if len(i) > len(pidempi):
            pidempi = i
    return pidempi

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))