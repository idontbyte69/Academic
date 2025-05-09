import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple
import random
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Queen:
    row: int
    col: int

class ChessBoard:
    def __init__(self, size: int):
        self.size = size
        self.queens: List[Queen] = []
        self.fitness = float('-inf')
        
    def add_queen(self, row: int, col: int):
        self.queens.append(Queen(row, col))
        
    def clear(self):
        self.queens.clear()
        
    def calculate_fitness(self) -> float:
        conflicts = 0
        for i in range(len(self.queens)):
            for j in range(i + 1, len(self.queens)):
                q1, q2 = self.queens[i], self.queens[j]
                if q1.row == q2.row or q1.col == q2.col or abs(q1.row - q2.row) == abs(q1.col - q2.col):
                    conflicts += 1
        self.fitness = -conflicts
        return self.fitness

class GeneticSolver:
    def __init__(self, board_size: int = 8, population_size: int = 100, 
                 max_generations: int = 1000, mutation_rate: float = 0.1,
                 tournament_size: int = 3, elite_size: int = 2):
        self.board_size = board_size
        self.population_size = population_size
        self.max_generations = max_generations
        self.mutation_rate = mutation_rate
        self.tournament_size = tournament_size
        self.elite_size = elite_size
        self.population: List[ChessBoard] = []
        self.best_solution: ChessBoard = None
        self.generation = 0
        self.fitness_history: List[float] = []
        
    def initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            board = ChessBoard(self.board_size)
            positions = list(range(self.board_size))
            random.shuffle(positions)
            for col, row in enumerate(positions):
                board.add_queen(row, col)
            board.calculate_fitness()
            self.population.append(board)
            
    def tournament_selection(self) -> ChessBoard:
        tournament = random.sample(self.population, self.tournament_size)
        return max(tournament, key=lambda x: x.fitness)
    
    def order_crossover(self, parent1: ChessBoard, parent2: ChessBoard) -> ChessBoard:
        child = ChessBoard(self.board_size)
        start, end = sorted(random.sample(range(self.board_size), 2))
        
        # Copy segment from parent1
        for i in range(start, end + 1):
            child.add_queen(parent1.queens[i].row, i)
            
        # Fill remaining positions from parent2
        remaining = [q for q in parent2.queens if q not in child.queens]
        for i in range(self.board_size):
            if i < start or i > end:
                child.add_queen(remaining.pop(0).row, i)
                
        return child
    
    def mutate(self, board: ChessBoard):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.board_size), 2)
            board.queens[i].row, board.queens[j].row = board.queens[j].row, board.queens[i].row
            
    def evolve(self):
        self.initialize_population()
        self.best_solution = max(self.population, key=lambda x: x.fitness)
        
        for generation in range(self.max_generations):
            self.generation = generation
            new_population = []
            
            # Elitism
            sorted_population = sorted(self.population, key=lambda x: x.fitness, reverse=True)
            new_population.extend(sorted_population[:self.elite_size])
            
            # Create rest of the population
            while len(new_population) < self.population_size:
                parent1 = self.tournament_selection()
                parent2 = self.tournament_selection()
                child = self.order_crossover(parent1, parent2)
                self.mutate(child)
                child.calculate_fitness()
                new_population.append(child)
            
            self.population = new_population
            current_best = max(self.population, key=lambda x: x.fitness)
            
            if current_best.fitness > self.best_solution.fitness:
                self.best_solution = deepcopy(current_best)
                
            self.fitness_history.append(self.best_solution.fitness)
            
            if self.best_solution.fitness == 0:
                break
                
        return self.best_solution
    
    def visualize_solution(self):
        if not self.best_solution:
            return
            
        plt.figure(figsize=(8, 8))
        board = np.zeros((self.board_size, self.board_size))
        board[1::2, ::2] = 1
        board[::2, 1::2] = 1
        
        plt.imshow(board, cmap='binary')
        
        for queen in self.best_solution.queens:
            plt.plot(queen.col, queen.row, 'ro', markersize=20)
            
        plt.xticks(range(self.board_size))
        plt.yticks(range(self.board_size))
        plt.grid(True)
        plt.title(f'N-Queens Solution (Fitness: {self.best_solution.fitness})')
        plt.savefig('output/queens_solution.png')
        plt.show()
        
    def plot_fitness_history(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.fitness_history)
        plt.title('Best Fitness Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Fitness')
        plt.grid(True)
        plt.savefig('output/fitness_history.png')
        plt.show()

def main():
    solver = GeneticSolver(board_size=8, population_size=100, max_generations=1000)
    solution = solver.evolve()
    
    print(f"\nSolution found in generation {solver.generation}")
    print(f"Final fitness: {solution.fitness}")
    
    solver.visualize_solution()
    solver.plot_fitness_history()

if __name__ == "__main__":
    main()