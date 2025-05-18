

# seir.py

import sys
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def seir_model(y, t, N, beta, sigma, gamma):
    S, E, I, R = y
    dSdt = -beta * S * I / N
    dEdt = beta * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * I
    return [dSdt, dEdt, dIdt, dRdt]

if __name__ == "__main__":
    if len(sys.argv) != 9:
        print("Użycie: python3 seir.py N S0 E0 I0 R0 beta sigma gamma")
        sys.exit(1)

    N, S0, E0, I0, R0 = map(int, sys.argv[1:6])
    beta, sigma, gamma = map(float, sys.argv[6:9])

    y0 = [S0, E0, I0, R0]
    t = np.linspace(0, 160, 160)  # 160 dni

    ret = odeint(seir_model, y0, t, args=(N, beta, sigma, gamma))
    S, E, I, R = ret.T

    # Wykresy
    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label='S - podatni')
    plt.plot(t, E, label='E - eksponowani')
    plt.plot(t, I, label='I - zainfekowani')
    plt.plot(t, R, label='R - wyzdrowiali')
    plt.xlabel('Czas (dni)')
    plt.ylabel('Liczba osób')
    plt.title('Model SEIR')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


#python zadanie1.py 1000 999 1 0 0 1.34 0.19 0.34
