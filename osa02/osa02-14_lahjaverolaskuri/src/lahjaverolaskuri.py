hinta = int(input("Lahjan suurruus? "))

if hinta < 5000:
    print("Ei veroa!")

elif hinta >= 5000 and hinta < 25000:
    print(f"Vero: {100+(hinta-5000) * 0.08}")

elif hinta >= 25000 and hinta < 55000:
    print(f"Vero: {1700+(hinta-25000) * 0.10}")

elif hinta >= 55000 and hinta < 200000:
    print(f"Vero: {4700+(hinta-55000) * 0.12}")

elif hinta >= 200000 and hinta < 1000000:
    print(f"Vero: {22100+(hinta-200000) * 0.15}")

elif hinta >= 1000000:
    print(f"Vero: {142100+(hinta-1000000) * 0.17}")

