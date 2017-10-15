"""
Vane Plotter
"""

import pandas as pd
import numpy as np
import operator

xl = pd.ExcelFile('data0.xls')
df1 = xl.parse(xl.sheet_names[0])

valueDictionary = dict()
columnCount = df1.shape[1]
rowCount = df1.shape[0]

colIndex = 0
while (colIndex < columnCount):
    rowIndex = 0
    while (rowIndex < rowCount and not pd.isnull(df1.iloc[rowIndex][colIndex])):
        value = df1.iloc[rowIndex][colIndex].split(',')[0]
        if value in valueDictionary:
            valueDictionary[value] += 1
        else:
            valueDictionary[value] = 1
        rowIndex += 1
    colIndex += 1
            
SortedList = sorted(valueDictionary.items(), key=operator.itemgetter(0))
sorted(SortedList, key=operator.itemgetter(1), reverse=True)