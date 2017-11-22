'''0/1 Knapsack problem solved using Genetic Algorithm. 
   Author : Harini Gowdagere Tulasidas '''
   
from random import choice, randint
import random 
from copy import deepcopy

class knapsack:
    
    def __init__(self ,n, w , v , p ,mx , num):
        self.n = n
        self.weight = deepcopy(w)
        self.values = deepcopy(v)
        self.population_size = p
        self.max_wt = mx
        self.num_iterations = num
        
    
    def initial_population(self):
        '''function to generate the initial population'''
        return [[randint(0, 1) for j in range(self.n)] for i in range(self.population_size)]
    
    def population_with_fitness(self,p):
        ''' function to compute the fitness of every genome in the population. 
        It takes the population as a parameter and returns the population with fitness 
        for every genome'''
        p_fitness = [(self.fitness(gene) , gene) for gene in p]       
        return p_fitness     
    
    def fitness(self,gene):
        ''' fitness function : Computes the total value and total weight for the genome. 
        If the total weight is over the capacity of the knapsack , the value is updated as 0 
        ie the item isn't added to the knapsack else the value is 1 indicating the presence of item in the knapsack'''
        fitness = 0
        sum_weight = 0
        for i in range(len(gene)):
            sum_weight += gene[i] * self.weight[i]
            fitness += gene[i] *self.values[i]
        if sum_weight > self.max_wt:
            return 0  
        else:
            return fitness

    def crossover(self,gene1 , gene2):
        ''' Performs crossover on the 2 genome. The crossover point is chosen in random. The function takes 2 genomes 
        as parameters and returns the child genomes with the respective fitness '''
        pt = randint(0,self.n-1)
        child1 = gene1[:pt] + gene2[pt:]
        child2 = gene1[pt:] + gene2[:pt] 
        return (self.fitness(child1) , child1) , (self.fitness(child2) , child2)

    def mutation(self,gene):
        ''' Performs Mutation on a genome . It changes the value to 1 when the value is 0 and vice versa. The function takes 
        a genome as a parameter and returns the genome with the fitness. '''
        mutPct = randint(0, self.n-1)
        if gene[mutPct] == 0:
            gene[mutPct]=1
        else:
            gene[mutPct]=0
        return (self.fitness(gene) , gene)        

    def main(self):
        '''The main genetic algorithm is implemented here. It generates the initial population and performs the crossover , mutation 
        and fitness evuation in a loop for a specified number of iterations. The ouput will be the best member of the population in the las iteration
        and the fitness value and the weight in the knapsack in that instance.'''
        total_weight = 0
        population = self.population_with_fitness(self.initial_population())
        print '*****************************************'
        print 'Initial population :'
        for x in population:
            print x
        print '*****************************************'
        i = 0
        while i < self.num_iterations:
            gene1 = choice(population)
            gene2 = choice(population)
            son , daughter = self.crossover(gene1[1], gene2[1])
            mutation_probability = random.random()
            if mutation_probability > 0.50:
                population.append(self.mutation(son[1]))
                population.append(daughter)
            else:
                population.append(son)
                population.append(self.mutation(daughter[1]))    
            population.sort(reverse=True)             
            if len(population) > self.population_size:
                population = population[:self.population_size]             
            i+=1  
        print 'Final value :' ,population[0]          
        print 'The  total value/fitness of the Knapsack is : ',population[0][0]
        for a in range(len(population[0][1])):
            total_weight += population[0][1][a]*self.weight[a]
        print 'The total weight in the knapsack is' , total_weight 
             
if __name__ == "__main__" :
    x = raw_input("Enter the number of elements: ")
    n = int(x)
    
    wt_input = raw_input("Enter the weights: ")
    w = wt_input.split()
    w = [int(a) for a in w]
    
    val_input = raw_input("Enter the Values: ")
    v = val_input.split()
    v = [int(a) for a in v]
    
    maxwt = raw_input("Enter the capacity of the Knapsack: ")
    mx = int(maxwt)
    
    p_size = raw_input("Enter population Size: ")
    p = int(p_size)
    
    it_size = raw_input("Enter the number of Iterations: ")
    num = int(it_size)
    knap = knapsack(n, w , v , p , mx , num)
    knap.main()