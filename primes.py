"""
Module nombres premiers.
"""
from math import sqrt


def isprime(p):
    """
    Vérifie si le nombre spécifié est premier.
    """
    if p < 2:
        return False

    if p == 2:
        return True

    premier = True

    i = 2
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            premier = False
            break
        i = i + 1

    return premier

def main():
    """
    Fonction principal.
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
