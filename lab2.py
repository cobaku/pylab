import numpy as np
import pandas as pd

matrix = np.random.randint(0, 10, size=(100, 100))
inverted = np.linalg.inv(matrix)

mdf = pd.DataFrame(matrix)
mdf.to_excel("matrix.xlsx")

idf = pd.DataFrame(inverted)
idf.to_excel("inverted.xlsx")

sign, logdet = np.linalg.slogdet(matrix)
ivnsign, logdetinv = np.linalg.slogdet(inverted)

print(np.linalg.det(matrix))
print(np.linalg.det(inverted))

print(np.exp(logdet))
print(np.exp(logdetinv))
