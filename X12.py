from math import sqrt


def calc(v1, v2, v3, delta):
    if delta < 0:
        return "Não há solução para essa equação quadratica!"
    else:
        X1 = (-(v2) + sqrt(delta)) / (2*v1)
        X2 = (-(v2) - sqrt(delta)) / (2*v1)
        return [X1, X2]
