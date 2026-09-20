# 🐜 Solução do Caixeiro Viajante com Colônia de Formigas (ACO)

Este repositório contém uma implementação em **Python** para resolver o **Problema do Caixeiro Viajante (Traveling Salesperson Problem - TSP)** utilizando a meta-heurística de **Otimização por Colônia de Formigas (Ant Colony Optimization - ACO)**.

---

## 📌 Sobre o Problema

O **Problema do Caixeiro Viajante (TSP)** consiste em encontrar a rota de menor custo/distância que passe por um conjunto de cidades (vértices) exatamente uma vez e retorne à cidade de origem. Como é um problema **NP-difícil**, métodos exatos tornam-se inviáveis para instâncias grandes, justificando o uso de meta-heurísticas como o **ACO**.

---

## 🧮 Funcionamento do Algoritmo (ACO)

O algoritmo simula o comportamento de formigas reais em busca de alimento através do uso de **feromônio**:
1. **Construção de Soluções:** Cada formiga explora o grafo e escolhe o próximo vértice com base em probabilidade (influenciada pela quantidade de feromônio e pela distância da aresta).
2. **Atualização de Feromônio:** Rotas mais curtas recebem maior depósito de feromônio.
3. **Evaporação:** O feromônio de todas as arestas evapora gradualmente ao longo do tempo para evitar convergência prematura em mínimos locais.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Conceitos:** Teoria dos Grafos, Algoritmos Probabilísticos / Estocásticos, Meta-heurísticas e Otimização Combinatória.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python 3 instalado em seu ambiente:
```bash
python3 --version
