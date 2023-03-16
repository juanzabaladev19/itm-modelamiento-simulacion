import numpy as np
import pandas as pd
df = pd.read_csv("/Users/juanestebanzabaladaza/Desktop/ITM/repos/itm-modelamiento-simulacion/2023-03-13/datasets/movies.csv", sep=';')
dataResult =df.loc[0]
print(dataResult)
print(dataResult['star_wars'])
