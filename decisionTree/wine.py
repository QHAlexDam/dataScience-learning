import pandas as pd
import os
from sklearn import *
from pandas import DataFrame

#getting data from csv
filePathRaw = '.\decisionTree\winequality-white.csv'
if os.path.exists(filePathRaw):
    df = pd.read_csv(r'.\decisionTree\winequality-white.csv', sep=';')

#rewrite to csv without separator
filePathClean = '.\decisionTree\winequality-white-clean.csv'
if not os.path.exists(filePathClean): 
    df.to_csv(filePathClean)

