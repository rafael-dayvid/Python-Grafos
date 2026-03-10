import numpy as np
import random

# -----------------------
# Ant System para TSP
# -----------------------

class AntSystemTSP:
    def __init__(self, distance_matrix, num_ants=None, alpha=1, beta=5,
                 rho=0.5, Q=100, iterations=200):

        self.dist = np.array(distance_matrix)
        self.n = len(self.dist)

        self.num_ants = num_ants if num_ants else self.n
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.Q = Q
        self.iterations = iterations

        # Feromônio inicial
        self.tau = np.ones((self.n, self.n)) * 1e-6
        np.fill_diagonal(self.tau, 0)

        # Heurística η = 1/d
        self.eta = 1 / (self.dist + np.eye(self.n))

    # ---------------------------------------------------------
    # Função de probabilidade da Equação 2 (slide)
    # ---------------------------------------------------------
    def transition_probability(self, i, unvisited):
        tau = self.tau[i, unvisited] ** self.alpha
        eta = self.eta[i, unvisited] ** self.beta
        p = tau * eta
        return p / np.sum(p)

    # ---------------------------------------------------------
    # Construção da solução por uma formiga
    # ---------------------------------------------------------
    def build_solution(self):
        start = random.randint(0, self.n - 1)
        tour = [start]
        unvisited = list(range(self.n))
        unvisited.remove(start)

        current = start
        while unvisited:
            probs = self.transition_probability(current, unvisited)
            next_city = random.choices(unvisited, weights=probs)[0]
            tour.append(next_city)
            unvisited.remove(next_city)
            current = next_city

        return tour

    # ---------------------------------------------------------
    # Cálculo do custo de um percurso
    # ---------------------------------------------------------
    def tour_length(self, tour):
        length = 0
        for i in range(len(tour) - 1):
            length += self.dist[tour[i], tour[i + 1]]
        length += self.dist[tour[-1], tour[0]]
        return length

    # ---------------------------------------------------------
    # Atualização de feromônio (slide)
    # ---------------------------------------------------------
    def update_pheromones(self, tours, lengths):
        self.tau *= (1 - self.rho)  # evaporação

        for k, tour in enumerate(tours):
            Lk = lengths[k]
            for i in range(len(tour) - 1):
                a, b = tour[i], tour[i + 1]
                self.tau[a, b] += self.Q / Lk
                self.tau[b, a] += self.Q / Lk

            # aresta final
            a, b = tour[-1], tour[0]
            self.tau[a, b] += self.Q / Lk
            self.tau[b, a] += self.Q / Lk

    # ---------------------------------------------------------
    # Execução do algoritmo
    # ---------------------------------------------------------
    def run(self):
        best_tour = None
        best_cost = float('inf')

        for it in range(self.iterations):

            tours = []
            lengths = []

            for _ in range(self.num_ants):
                tour = self.build_solution()
                L = self.tour_length(tour)
                tours.append(tour)
                lengths.append(L)

                if L < best_cost:
                    best_cost = L
                    best_tour = tour

            self.update_pheromones(tours, lengths)

            print(f"Iteração {it+1}/{self.iterations} | Melhor custo = {best_cost}")

        return best_tour, best_cost
