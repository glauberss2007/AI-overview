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
1. Introduction
2. Theory
3. [implementation](fuzzy-logic/restaurant_tip.py)
   - lib install
   
         pip install scikit-fuzzy
    
## Machine learning
1. Introduction to Machine Learning and Data Science
2. Orange installation using the [script](machine_learning/orange_installation_script)
    
        pip install orange3
    
### Classification
1. Example of a risk avaliation database history used for training:
      ![image](https://user-images.githubusercontent.com/22028539/118693090-2028c700-b7e1-11eb-8449-a345da02e4a2.png)

2. Example of a buy probability database history used for training:
      ![image](https://user-images.githubusercontent.com/22028539/118693319-55cdb000-b7e1-11eb-9c23-b4ac14bbbbf9.png) 

3. Example of an image classification:
      ![image](https://user-images.githubusercontent.com/22028539/118693469-73027e80-b7e1-11eb-907c-41c91ec4715d.png) 

4. Naive Bayes algorithyns that is based on a probability table:
      ![image](https://user-images.githubusercontent.com/22028539/118693851-d5f41580-b7e1-11eb-9ee4-b0ecaa966632.png)

5. Naive bayes alg with Orange [zoo-naive-bayes](machine_learning/zoo_orange_naive_bayes.ows)
   - naive bayes on orange:
        ![image](https://user-images.githubusercontent.com/22028539/118696564-caeeb480-b7e4-11eb-920a-55fefff4a19d.png)
   - Zoo dataset > Naive Bayes Alg > Data Table > Test and Score 80% training size > Data Info > Distribution > Confusion MAtrix.
   - Check CA > Save model > Load Model > Select Data set > Prediction
   
6. Decision tree alg with orange [zoo-naive-tree](machine_learning/zoo_orange_tree.ows)
   - Decision tree alg viszual representation:
        ![image](https://user-images.githubusercontent.com/22028539/118697927-35542480-b7e6-11eb-85b3-1f0b893d00ad.png)
   - Tree alg on orange:
        ![image](https://user-images.githubusercontent.com/22028539/118698886-4fdacd80-b7e7-11eb-9f51-7bbdd6eaa085.png)
   
7. Learning by rule alg with orange [zoo-rule-learn](machine_learning/zoo_rule_learn.ows)
   - Rule learning representation:
       ![image](https://user-images.githubusercontent.com/22028539/118699571-0f2f8400-b7e8-11eb-9a3a-8daa3b1700e4.png)
   - rule learn on orange:
       ![image](https://user-images.githubusercontent.com/22028539/118699958-7e0cdd00-b7e8-11eb-93f5-b28f78aba1ba.png)

8. Instance learn - kNN [zoo-knn-learn](machine_learning/zoo_knn_learn.ows)
   -kNN representation:
        ![image](https://user-images.githubusercontent.com/22028539/118700923-89acd380-b7e9-11eb-9ebb-79d48b95e0a9.png)
   -histore base connversion:
        ![image](https://user-images.githubusercontent.com/22028539/118701090-b95bdb80-b7e9-11eb-9e9f-c3af53988dd5.png)
   - kNN on orange:
        ![image](https://user-images.githubusercontent.com/22028539/118701571-3d15c800-b7ea-11eb-9c9c-20d2f3a01805.png)

9. Learn by support vector machine (SVM) [zoo-svm-learn](machine_learning/svm-orange-model.ows)
  -SVM representation (max bord search):
        ![image](https://user-images.githubusercontent.com/22028539/120073538-1cadff00-c06f-11eb-95d5-383e707ead93.png)
  -SVM on orange:
        ![image](https://user-images.githubusercontent.com/22028539/120073632-91813900-c06f-11eb-9716-f27af222b010.png)
10. Logistic Regression [zoo-lr-learn](machine_learning/zoo_orange_lr.ows)
  - LR representation:
        ![image](https://user-images.githubusercontent.com/22028539/120073785-369c1180-c070-11eb-9553-9732a0a419f8.png)
  - LR on Orange:
        ![image](https://user-images.githubusercontent.com/22028539/120073872-95fa2180-c070-11eb-9fd0-d39f820e7466.png)

11. Benchmark comparison for animal success prediction [zoo-benchmark](machine_learning/zoo_benckmark.ows): 
        ![image](https://user-images.githubusercontent.com/22028539/120074329-aca17800-c072-11eb-9fc2-bc368e3576d1.png)

12. K-Fold Cross Validation 
        ![image](https://user-images.githubusercontent.com/22028539/120074526-9f38bd80-c073-11eb-8cf0-9dad7ff2458e.png)

13. Cross validation using an wine database  [zoo-benchmark](machine_learning/wine-cross-validation.ows):
        ![image](https://user-images.githubusercontent.com/22028539/120074940-a234ad80-c075-11eb-9548-3530d1337f2e.png)

14. Image classification:
  - Option > addons > orange image analyzer (restart orange)
  - Site to download imagens dataset:
  - Orange model:
      
### Regression
  Used for number prediction, for example:
  
1. What is regression?
        ![image](https://user-images.githubusercontent.com/22028539/120902487-1c85a480-c617-11eb-8db2-b89b3f29a3ca.png)
2. Linear regression example for anual health plan cost based on age:
        ![image](https://user-images.githubusercontent.com/22028539/120902622-bd745f80-c617-11eb-9eda-71bbcadc66b6.png) 
3. Linear regression using Orange [car-price-prediction](machine_learning/car-price-prediction.ows):
        ![image](https://user-images.githubusercontent.com/22028539/120902866-2ad4c000-c619-11eb-84e7-e04841761882.png)
4. House price prediction [house-price-prediction](machine_learning/house-price-prediction.ows):
        ![image](https://user-images.githubusercontent.com/22028539/120903971-c49f6b80-c61f-11eb-830d-91f798af65e5.png)

### Grouping
   Use examples:
   ![image](https://user-images.githubusercontent.com/22028539/120904081-8eaeb700-c620-11eb-9d37-a7bbfbea6ee7.png)

1. Grouping with K-Means:
    - Centroid AVG check
        ![image](https://user-images.githubusercontent.com/22028539/120904146-f107b780-c620-11eb-97bf-d1eee593f0b2.png)
    - K-Means on origin [iris-kmeans-orange:
        ![image](https://user-images.githubusercontent.com/22028539/121002819-24eaf600-c763-11eb-92f8-81b73ef98787.png)
2. Credit card spend group [credit-card-kmeans-orange](machine-learning/market-association-orange.ows):
    - ![image](https://user-images.githubusercontent.com/22028539/121004525-2d443080-c765-11eb-840d-3b904c6c8374.png)

3. Image Grouping [dogs-cats-association-in-orange](machine_learning/iris-kmeans.ows):
    - ![image](https://user-images.githubusercontent.com/22028539/121012075-b8292900-c76d-11eb-9e96-fa9ecbcc60ba.png)


### Association
   Use examples:
      ![image](https://user-images.githubusercontent.com/22028539/121006965-e277e800-c767-11eb-8c4e-21e7dd810ecc.png)
1. Apriori algorithym:
      - Market layout association:
          ![image](https://user-images.githubusercontent.com/22028539/121007577-7944a480-c768-11eb-8620-dd2c0f233016.png)
      - Apriori in orange [market-association-orange](machine_learning/market-association-orange.ows):
          ![image](https://user-images.githubusercontent.com/22028539/121009263-53200400-c76a-11eb-83eb-3c4a2fe9dcf7.png)
2. Adult econoomic association [market-association-orange](machine_learning/):
   ![image](https://user-images.githubusercontent.com/22028539/121012622-49000480-c76e-11eb-9339-3f3f26be8f9d.png)

### Complementary topics
1. Pre process values and normalization comparison [pre-process-orange.ows](machine_learning/):
    - ![image](https://user-images.githubusercontent.com/22028539/121042219-d7ce4a80-c789-11eb-89a6-e8dde56dde30.png)
2. Pre process discret [pre-processing-orange.ows](machine_learning/):
    - ![image](https://user-images.githubusercontent.com/22028539/121043576-23cdbf00-c78b-11eb-8938-85e268a9087c.png)
    - Atrubits selection[atributs-selection-orange.ows](machine_learning/):
          ![image](https://user-images.githubusercontent.com/22028539/121048371-1f0a0a80-c78d-11eb-92e5-024da7d19a61.png)

3. Dimension reduction with PCA [dimension-reduction.ows](machine_learning/):
    - ![image](https://user-images.githubusercontent.com/22028539/121049190-df8fee00-c78d-11eb-8f93-d50ea4418719.png)

4. PLC grouping [pca-grouping.ows](machine_learning/)
    - ![image](https://user-images.githubusercontent.com/22028539/121049849-78bf0480-c78e-11eb-81bb-b1b0a5f5cfe9.png)

5. Outliers detection [outliers-detection.ows](machine_learning/)
    - ![image](https://user-images.githubusercontent.com/22028539/121050834-4bbf2180-c78f-11eb-816f-f19fa5aff964.png)

6. Temporal [temporal_?.ows](machine_learning/)
    - Documentation link: 
    - ![image](https://user-images.githubusercontent.com/22028539/121053171-73af8480-c791-11eb-8371-3eacdc3d1fe6.png)
    - ![image](https://user-images.githubusercontent.com/22028539/121056298-719af500-c794-11eb-9bb9-4c6fdf51d416.png)
    - Model evaluation: 
        ![image](https://user-images.githubusercontent.com/22028539/121057160-5d0b2c80-c795-11eb-9294-9c21d2c2aa71.png)

### Data visualization and exploration
1. Orange basic graphs[exploring-graph](machine_learning/)
    ![image](https://user-images.githubusercontent.com/22028539/121069664-1f61d000-c7a4-11eb-8d87-cfb577680949.png)

2. Covid exploring data using Orange and Python [covid](machine_learning/)
    - ![image](https://user-images.githubusercontent.com/22028539/121072596-cdbb4480-c7a7-11eb-8a5c-39f77b113220.png)
    - ![image](https://user-images.githubusercontent.com/22028539/121074464-46230500-c7aa-11eb-96b6-2a8a343d5d52.png)
    - ![image](https://user-images.githubusercontent.com/22028539/121075053-16c0c800-c7ab-11eb-91b5-22a9ed25f01d.png)
    - ![image](https://user-images.githubusercontent.com/22028539/121076603-fabe2600-c7ac-11eb-8a2d-121d9cdb7bfa.png)
    - ![image](https://user-images.githubusercontent.com/22028539/121077972-b59af380-c7ae-11eb-9338-75faffdc6ee5.png)

### Reinforcement learning
## Artificial neural networks and deep learning
## Natural language processing
## Computer vision
## Multi-agent systems
## Other areas of Artificial Intelligence
## Final considerations
## Basic Python Programming

## References
>http://www.goal.ufop.br/
 
>https://iaexpert.academy/
