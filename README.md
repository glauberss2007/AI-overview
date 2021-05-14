# Artificial Intelligence
## Introduction
Currently, Artificial Intelligence and Machine Learning (Machine Learning) are being considered the most relevant fields of work in Information Technology, being responsible for the use of intelligent algorithms for the construction of software and hardware that simulate human capacity. The Machine Learning job market in various parts of the world is on the rise and the trend is that this type of professional is increasingly in demand! Even some studies indicate that knowledge of this area will soon be a prerequisite for professionals in Information Technology!

In this repository it is possible to find implementation projects for the following problems:
- Search for routes with better routes on city maps (greedy search and A * search)
- Choosing the cheapest air tickets, in a scenario of buying group tickets and maximizing profits when loading products - optimization algorithms: hill climb, simulated annealing (simulated tempering) and genetic algorithm
- Predicting how much you would tip in a restaurant (fuzzy logic)
- Classification using naïve bayes algorithms, decision tree, rules, k-NN, logistic regression and neural networks
- House price forecast using linear regression
- Grouping of bank data using the k-means algorithm
- Generation of association rules with the a priori algorithm
- Pre-processing, dimensionality reduction and outlier detection in databases
- Stock price forecast with time series
- Visualization and exploration of data in the COVID-19 disease database
- Construction of an agent to control a taxi for passenger transport with reinforcement learning
- Classification of images of cats and dogs with convolutional neural networks
- Classification of images of Homer and Bart, of the Simpsons drawing also using convolutional neural networks
- POS (part-of-speech), stemming, stemming, word cloud (wordcloud) and named entity extraction using natural language processing techniques
- Creation of a classifier of feelings in Portuguese
- Face detection and facial recognition in images
- Video object tracking
- Simulation of a multi-agent system for communication between agents using the FIPA-REQUEST protocol

Each type of problem requires different techniques for its solution, therefore, knowing all the areas of AI you will know which techniques to use in the most varied types of scenarios!

### Overview
  - Required: 
    - Python
      > https://www.python.org/downloads/
    - Orange
    - numpy lib:
            
            sudo apt install python3-pip            
            sudo pip3 install numpy
            
## Search algorithms
1. Introduction
2. Search theory
    - Go from Arad to Bucharest
    - Puzzles of 8
    - Hash
3. Heuristics
    - Cost of "8 puzzle" can be balanced based on the sum of the distances of how close to each element it is.
    - Cost of "Arad to Bucharest" based on the distance value of cities in a straight line.
 4. Ordered vectors
    - Data structure vizualization: 
    > https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
5. Ordered vector - theory
6. Ordered vector - [implementation](search_algotithms/ordered-vector/orderedVector.py)
7. Creating the city map - [implementation](search_algotithms/city-map-greedy/city_map_graph.py) 
8. Greedy search - theory
9. Gluttony search - [implementation](search_algotithms/city-map-greedy/greedy_search.py)
10. Greedy search - debugging step by step
11. Quest A * (The Star) - theory
12. Search A * (A Estrela) - [implementation](search_algotithms/city-map-astar/astar_search.py)
13. Search A * (The Star) - debug step by step
14. PLUS
    TODO: brazil graph image
    TODO: Heuristic table
15. Brazillian cities graph - [implementation](search_algotithms/city-map-brazil)

## Optimization algorithms
1. Introduction to optimization algorithms
2. Flight case study
3. Representation of the problem - [implementation](optimization-algorithms/fly-travel-problem/problem_representation.py) 
3. Printing the solution - [implementation](optimization-algorithms/fly-travel-problem/problem_representation.py)
4. Cost function (fitness) - [implementation](optimization-algorithms/fly-travel-problem/fitness_function.py)
5. Hill climb - theory
6. Hill climb - [implementation](optimization-algorithms/fly-travel-problem/hill_climb.py)
7. Simulated annealing - theory
8. Simulated annealing - [implementation](optimization-algorithms/fly-travel-problem/simulated_annealing.py)
9. Genetic algorithm - theory
10. Genetic algorithm - [implementation](optimization-algorithms/fly-travel-problem/algoritmo_genetico.py)
11. Product transport [implementation](optimization-algorithms/product-transport)
 

## Fuzzy logic
## Machine learning
## Classification
## Regression
## Association
## Complementary topics
## Data visualization and exploration
## Reinforcement learning
## Artificial neural networks and deep learning
## Natural language processing
## Computer vision
## Multi-agent systems
## Other areas of Artificial Intelligence
## Final considerations
## Basic Python Programming

## References
>http://www.goal.ufop.br/
> 
>https://iaexpert.academy/