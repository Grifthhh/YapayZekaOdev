# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:38:19 2019

@author: EKREMBÜLBÜL
"""

import random
import copy
import matplotlib.pyplot as plt

class GeneticAlgo:
    
    matrix = []
    individuals = []
    baitCount = 5
    indResultList = []
    xList = []
    yList = []
    plotPathLists = []
    plotBaitList = []
    matrixSize = 13
        

    def makeMatrix(self, matrixSize = None, baitCount = None):
        
        if baitCount == None:
            baitCount = self.baitCount
        else:
            self.baitCount = baitCount
            
        if matrixSize == None:
            matrixSize = self.matrixSize
        else:
            self.matrixSize = matrixSize
        
        self.matrix = [[0 for j in range(matrixSize)]\
                      for i in range(matrixSize)]
        
        for i in range(matrixSize):
            for j in range(matrixSize):
                if i == 0 or j == 0 or i == matrixSize - 1 or\
                        j == matrixSize -1:
                    self.matrix[i][j] = -1
        
        randList = []
        tmpCount = baitCount
        
        while tmpCount > 0:
            
            i = random.randint(1, matrixSize - 2)
            j = random.randint(1, matrixSize - 2)
            flag = False
            
            for each in randList:
                if each == [i, j]:
                    flag = True
                    
            if flag == False:
                randList.append([i, j])
                tmpCount -= 1
                
        for each in randList:
            self.matrix[each[0]][each[1]] = 5
            
        self.plotBaitList = randList
        
        tmpList = copy.deepcopy(self.plotBaitList)
        self.plotBaitList = []
        xList = []
        yList = []
        
        for k in tmpList:
            xList.append(k[0])
            yList.append(k[1])
        
        self.plotBaitList = [xList, yList]
            
    
    def makeIndividuals(self, individualSize = 50, individualCount = 4):
    
        self.individuals = [[random.randint(1, 4)\
                          for j in range(individualSize)]\
                          for i in range(individualCount)]
            
    def visitMatrix(self, individual, i, j):
        
        eatedBait = 0
        pathLength = 0
        tmpMatrix = copy.deepcopy(self.matrix)
        
        for each in individual:
            
            self.xList.append(j)
            self.yList.append(i)
            
            if tmpMatrix[i][j] == -1:
                return -1, eatedBait, pathLength
            elif tmpMatrix[i][j] == 5:
                eatedBait += 1
                tmpMatrix[i][j] = 0
            
            if eatedBait == self.baitCount:
                return 1, eatedBait, pathLength
            
            if each == 1:
                j -= 1
            elif each == 2:
                i -= 1
            elif each == 3:
                j += 1
            elif each == 4:
                i += 1
            
            pathLength += 1
                
        return 0, eatedBait, pathLength
    
    
    def iteration(self, visitMatrix):
        
        halfMatrixSize = int((len(self.matrix) - 1) / 2)
        i = halfMatrixSize
        j = halfMatrixSize
        self.indResultList = []
            
        for each in self.individuals:
            self.indResultList.append(visitMatrix(each, i, j))
            self.plotPathLists.append([self.xList, self.yList])
            self.xList = []
            self.yList = []
            
            
#    def selection(self):
#        
#        self.indResultList
        
    
    def drawPlot(self):
        
        for each in self.plotPathLists:
        
            plt.figure()
            plt.scatter(self.plotBaitList[0], self.plotBaitList[1], c = 'red')
            plt.plot(each[0], each[1])
            plt.axis([0, self.matrixSize - 1, 0, self.matrixSize - 1])
            
            
         
###############################################################################


x = GeneticAlgo()
x.makeMatrix()
x.makeIndividuals()
x.iteration(x.visitMatrix)
x.drawPlot()
    
matrix = x.matrix
individuals = x.individuals
indResultList = x.indResultList
path = x.plotPathLists
bait = x.plotBaitList
        
        
        
        
        
        
        
        
        
        
        
    