from tp import AntSystemTSP


if __name__ == "__main__":
    dist = [
        [0, 2, 9, 10, 7],
        [2, 0, 6, 4, 3],
        [9, 6, 0, 8, 5],
        [10, 4, 8, 0, 6],
        [7, 3, 5, 6, 0]
    ]

    aco = AntSystemTSP(dist, iterations=100)
    best_tour, best_cost = aco.run()

    print("Melhor caminho encontrado:", best_tour)
    print("Custo total:", best_cost)
