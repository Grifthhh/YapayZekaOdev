# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:38:19 2019

@author: EKREMBÜLBÜL
"""

import time
import random
import copy
import numpy.random as choice
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class GeneticAlgo:
    
    # gerekli degiskenler
    matrix = []
    individuals = []
    individualsWeight = []
    baitCount = 5
    indResultList = []
    xList = []
    yList = []
    plotPathLists = []
    plotBaitList = []
    matrixSize = 13
    individualCount = 4
    iterationCount = 0
        
    # matrix olusturulur
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
            
    # ilk bireyler olusturulur
    def makeIndividuals(self, individualSize = 50, individualCount = None):
        
        if individualCount == None:
            individualCount = self.individualCount
        else:
            self.individualCount = individualCount
    
        self.individuals = [[random.randint(1, 4)\
                          for j in range(individualSize)]\
                          for i in range(individualCount)]
            
    # her birey icin matris gexilir
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
    
    # population icin matris gezilir yani 4 birey icin
    def iteration(self, visitMatrix, drawPlot):
        
        halfMatrixSize = int((len(self.matrix) - 1) / 2)
        i = halfMatrixSize
        j = halfMatrixSize
        self.indResultList = []
            
        for each in self.individuals:
            self.indResultList.append(visitMatrix(each, i, j))
            self.plotPathLists.append([self.xList, self.yList])
            self.xList = []
            self.yList = []
        
        for each in self.plotPathLists:
            drawPlot(each)
        
        self.plotPathLists = []
            
        self.iterationCount += 1
        
    # basari orani hesaplanir
    def rateCalculaion(self):
        
        tmpList = []
        tmpRateList = []
        
        for each in self.indResultList:
            tmpList.append((each[1] + 0.2) / self.baitCount)
        
        summ = 0
        
        for each in tmpList:
            summ += each
            
        for each in tmpList:
            tmpRateList.append(each / summ)
            
        self.individualsWeight = tmpRateList
        
    # yenibireyler secilir
    def selection(self):
        
        tmpIndividuals = random.choices(self.individuals,\
                                        self.individualsWeight, k = 4)
        
        self.individuals = tmpIndividuals
        
    # cross-over yapilir, bireyler caprazlanir
    def crossOver(self):
        
        tmpIndList = self.individuals
        self.individuals = []
        
        size = len(tmpIndList[0])
        halfSize = int(size / 2)
        
        for k in range(2):
        
            n = 2 * k
            
            tmpList = []
            tmpList2 = []
            
            for each in tmpIndList[n][0:halfSize]:
                tmpList.append(each)
                
            for each in tmpIndList[n + 1][25:size]:
                tmpList.append(each)
            
            for each in tmpIndList[n + 1][0:halfSize]:
                tmpList2.append(each)
                
            for each in tmpIndList[n][halfSize:size]:
                tmpList2.append(each)
                
            self.individuals.append(tmpList)
            self.individuals.append(tmpList2)
            
    #bireyler mutasyona ugratilir
    def mutation(self):
        
        tmpList = self.individuals
        indSize = len(self.individuals[0])
        self.individuals = []
        
        for k in range(4):
            for each in tmpList:
                rand = random.randint(1, indSize - 1)
                each[rand] = random.randint(1, 4)
    
        self.individuals = tmpList
    
    # bireylerin matris uzerinde gezmesi cizilir.
    def drawPlot(self, each):
        
        plt.figure()
        plt.scatter(self.plotBaitList[0], self.plotBaitList[1], c = 'red')
        plt.plot(each[0], each[1])
        plt.axis([0, self.matrixSize - 1, 0, self.matrixSize - 1])
                
        red_patch = mpatches.Patch(color='red', label=self.iterationCount)
        plt.legend(handles=[red_patch])
        plt.pause(0.1)
            
         
##############################################################################

x = GeneticAlgo()
x.makeMatrix()
x.makeIndividuals()


x.iteration(x.visitMatrix, x.drawPlot)

bait = x.baitCount
tmpBait = 0

for each in x.indResultList:
    if tmpBait < each[1]:
        tmpBait = each[1]

count = x.iterationCount

# tum yiyecekler yenene veya iterasyon sayisi 1000'i gecene kadar doner
while tmpBait < bait and count < 3:
    x.rateCalculaion()
    x.selection()
    x.crossOver()
    x.mutation()
    x.iteration(x.visitMatrix, x.drawPlot)
    
    for each in x.indResultList:
        if tmpBait < each[1]:
            tmpBait = each[1]
            
    count = x.iterationCount

x.iterationCount
matrix = x.matrix
individuals = x.individuals
indResultList = x.indResultList
path = x.plotPathLists
individualsWeight = x.individualsWeight   
        
        
        
        
        
        
        
        
        
        
    