# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 17:12:13 2014

@author: tmold_000
"""
import numpy as np
import matplotlib.pyplot as plt


class evolution: 
    target = [];
    population = [];
    mutationRate = 0; "probability that a gene will mutate"
    maxPopSize = 0; "number of individual allowed in the population at once"
    initSize = 0;
    growthRate = 0; "number of children per couple"
    maxIterations = 0;
    fidelityConstant = 2; "mulitplied by population size to determine expected number of unique partners each individual will have in a generation"
    averageFitness = [];
    

    def __init__(self, target, mutationRate, growthRate, maxPopSize, initSize, fidelityConstant, maxIterations):
      self.target = target;
      self.mutationRate = mutationRate;
      self.maxPopSize = maxPopSize
      self.initSize = initSize
      self.maxIterations = maxIterations;
      self.growthRate = growthRate
      self.fidelityConstant = fidelityConstant;

    def start(self):
        length = len(self.target);
        for i in range(self.initSize):
            individual = [];
            for j in range(length):
                individual.append(np.random.randint(0,2));
            self.population.append(individual);

    
    def evolve(self):
        ("Generation", 0)
        self.start(); "begins with the first population of organisms"
        for n in range(self.maxIterations):
            print("Generation", n);
            popFit = self.popFitness()
            avg = np.mean(popFit);
            print(popFit);
            print(avg);
            self.averageFitness.append(avg);
            self.killStep();
            self.breedStep();
           
    def fitness(self, individual):
        sum = 0;
        for n in range(len(individual)):
            if individual[n] == self.target[n]:
                sum = sum + 1;
        return sum;
        
    def mutate(self,individual):
        for n in range(len(individual)):
            if np.random.rand()<self.mutationRate:
                individual[n] = abs(individual[n] - 1)
        
    def breedStep(self):
        population = self.population;
        newPop = []
        for n in range(int(self.fidelityConstant*len(population))):
            #print('new parents')
            parent1 = population[np.random.randint(0,len(population))];
            parent2 = population[np.random.randint(0,len(population))];
            for i in range(self.growthRate):
                child = self.crossover(parent1, parent2);
                self.mutate(child);
                newPop.append(child);   
        self.population = newPop
            

    def crossover(self, parent1, parent2):
        child = []
        for n in range(len(parent1)):
            parent = np.random.randint(0,2); "0 is assigned to first parent, 1 to second"
            if parent == 0:
                child.append(parent1[n]);
            elif parent == 1:
                child.append(parent2[n]);
        #print(child);
        return child;       
        
    
    def killStep(self):
        self.population = sorted(self.population, key = self.fitness);
        self.population = self.population[(len(self.population) - self.maxPopSize):]
        
    def popFitness(self):
        fitnessArr = [];
        for n in range(len(self.population)):
            fitnessArr.append(self.fitness(self.population[n]));
        return fitnessArr;


target = [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1];
mutationRate = 0;
growthRate = 3;
maxPopSize = 6
initSize = 2
fidelityConstant = 1;
maxIterations = 50; 
      
    

e = evolution(target, mutationRate, growthRate, maxPopSize, initSize, fidelityConstant, maxIterations)
e.evolve();
avgs = e.averageFitness;
plt.plot(range(len(avgs)), avgs);


