# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 18:38:19 2019

@author: EKREMBÜLBÜL
"""

import random

def makeMatrix(matrixSize = 13, baitCount = 5):
    
    matrix = [[0 for j in range(matrixSize)] for i in range(matrixSize)]
    
    for i in range(matrixSize):
        for j in range(matrixSize):
            if i == 0 or j == 0 or i == matrixSize - 1 or j == matrixSize -1:
                matrix[i][j] = -1
    
    randList = []
    flag = False
    tmpCount = baitCount
    
    while tmpCount > 0:
        
        i = random.randint(1, matrixSize - 2)
        j = random.randint(1, matrixSize - 2)
        
        for each in randList:
            if each == [i, j]:
                flag == True
                
        if flag == False:
            randList.append([i, j])
            tmpCount -= 1
            
    for each in randList:
        matrix[each[0]][each[1]] = 5
        
    return matrix


def makeIndividual(individualSize = 40, individualCount = 4):

    individual = [[random.randint(1, 4) for j in range(individualSize)]\
                  for i in range(individualCount)]
    
    return individual


def eatBait(matrix, individual):
    
    halfMatrixSize = int((len(matrix) - 1) / 2)
    i = halfMatrixSize
    j = halfMatrixSize
    eatedBait = 0
    
    if matrix[i][j] == 5:
        eatedBait += 1
    
    
    














