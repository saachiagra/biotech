import numpy as np
import matplotlib.pyplot as plt
import requests
from minimumskew import *
from frequentwords import *
from FrequentWordsWithMismatches import *

# GET SALMONELLA ENTERICA GENOME DATA FROM WEB PAGE
web = requests.get("https://bioinformaticsalgorithms.com/data/Salmonella_enterica.txt")
text = web.text
text = text[118:].replace("\n", "")

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
# plt.rcParams["figure.autolayout"] = True

# CREATE GC SKEW ARRAY AND FIND MIN VALUE OF SKEW (APPROX LOC OF oriC)
array, min = MinimumSkew(text)
index = []
for x in range(len(array)):
    index.append(x)

# GRAPH STUFF
x = np.array(index)
y = np.array(array)

plt.title("Line graph")
plt.plot(x, y, color="green")

plt.show()

# CREATE WINDOW BASED ON INFERENCED oriC LOCATION
text = text[min[0]:min[0]+500]

# ALGORITHM 1: ALL EXACT OCCURRENCES
array, max = FindClumps2(text, 9)
print("-"*10 + " ALG 1 " + "-"*10)
for x in array:
    print(x, end=" ")
print(max)

# ALGORITHM 2: ALL APPROXIMATE OCCURRENCES
array, max = freqWordsMis(text, 9, 1)
print("-"*10 + " ALG 2 " + "-"*10)
for x in array:
    print(x, end=" ")
print(max)

# ALGORITHM 3: ALL APPROXIMATE OCCURRENCES & REVERSE COMPLIMENTS
array, max = freqWordsMisRev(text, 9, 1)
print("-"*10 + " ALG 3 " + "-"*10)
for x in array:
    print(x, end=" ")
print(max)