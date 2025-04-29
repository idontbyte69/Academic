# Genetic Algorithm Implementation (CLP 3)

This project implements a genetic algorithm to solve a specific optimization problem where we need to find a combination of numbers whose sum equals a target value.

## Problem Statement
The algorithm aims to find a solution where the sum of the first two genes in an individual equals a target value (t). The solution is found through an evolutionary process using genetic algorithms.

## Features
- Population-based genetic algorithm
- Fitness-based selection
- Crossover operation for breeding
- Mutation operation for genetic diversity
- Generational evolution until solution is found

## How to Run
1. Run the `CLP.py` file
2. Enter the target sum (t) when prompted
3. Enter the gene length (g) when prompted
4. The program will display the evolution process and the final solution

## Input Format
- First input: Target sum (t) - The desired sum of the first two genes
- Second input: Gene length (g) - The number of genes in each individual

## Output
The program displays:
- The generation number and current best sum in each generation
- The final solution when found, including:
  - Generation number where solution was found
  - Sum of the first two genes
  - Complete gene sequence of the solution

## Implementation Details
- Population size is fixed at 10 individuals
- Each gene is a random number between 0 and 9
- Fitness is calculated based on how close the sum of first two genes is to the target
- Crossover is performed at a random point
- Mutation randomly changes one gene in the individual

## Example
```
Input:
t = 15
g = 5

Output:
Generation: 0 Fittest sum: 12
Generation: 1 Fittest sum: 13
...
Solution found in generation X
Sum of first two genes: 15
Genes: 7 8 3 2 1
```

## Requirements
- Python 3.x
- No external dependencies required 