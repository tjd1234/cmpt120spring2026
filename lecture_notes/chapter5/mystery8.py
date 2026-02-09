# mystery7.py

def mystery(n):
    if n < 1:
        return
    else:
        print(f"calling mystery({n}) ...")
        mystery(n - 1)


print("mystery7.py: calling mystery(5) ...")
mystery(5)
