# seir_wrapper.py

import argparse
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

def main():
    parser = argparse.ArgumentParser(description='Symulacja modelu SEIR')
    parser.add_argument('-N', type=int, default=1000, help='Rozmiar populacji')
    parser.add_argument('-S0', type=int, default=999, help='Początkowa liczba podatnych')
    parser.add_argument('-E0', type=int, default=1, help='Początkowa liczba eksponowanych')
    parser.add_argument('-I0', type=int, default=0, help='Początkowa liczba zainfekowanych')
    parser.add_argument('-R0', type=int, default=0, help='Początkowa liczba wyzdrowiałych')
    parser.add_argument('-beta', type=float, default=1.34, help='Wskaźnik infekcji')
    parser.add_argument('-sigma', type=float, default=0.19, help='Wskaźnik inkubacji')
    parser.add_argument('-gamma', type=float, default=0.34, help='Wskaźnik wyzdrowień')

    args = parser.parse_args()

    y0 = [args.S0, args.E0, args.I0, args.R0]
    t = np.linspace(0, 160, 160)

    ret = odeint(seir_model, y0, t, args=(args.N, args.beta, args.sigma, args.gamma))
    S, E, I, R = ret.T

    plt.figure(figsize=(10, 6))
    plt.plot(t, S, label='S - podatni')
    plt.plot(t, E, label='E - eksponowani')
    plt.plot(t, I, label='I - zainfekowani')
    plt.plot(t, R, label='R - wyzdrowiali')
    plt.xlabel('Czas (dni)')
    plt.ylabel('Liczba osób')
    plt.title('Model SEIR (wrapper)')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()

#python zadanie2.py -N 2000 -I0 5 -beta 2.0
