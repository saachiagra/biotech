# input: genome, some number representing length of sequence
# output: dictionary with all sequence patterns and the number of occurrences for each one
def FrequencyTable(txt, k):
    k = int(k)
    freqMap = {}
    n = len(txt)
    for i in range(n - k + 1):
        ptn = txt[i:i+k]
        try:
            freqMap[ptn] += 1
        except KeyError:
            freqMap[ptn] = 1
    return freqMap

def MaxMap(dict):
    max = 0
    for x in dict:
        if dict[x] > max:
            max = dict[x]
    return max

# input: genome, length of sequence
# output: array containing the sequence(s) most repeated in the genome
def BetterFrequentWords(txt, k):
    FrequentPatterns = []
    freqMap = FrequencyTable(txt,k)
    max = MaxMap(freqMap)
    for x in freqMap:
        if freqMap[x] == max:
            FrequentPatterns.append(x)
    return FrequentPatterns

# inputs: genome, length of sequence to-be-found, length of genome window to examine, minimum num of occurrences
# output: list of sequences within window that satisfy occurrence requirement
def FindClumps(txt, k, l, t):
    patterns = []
    n = len(txt)
    t = int(t)
    k = int(k)
    l = int(l)
    for i in range(n - l + 1):
        window = txt[i:i+l]
        freqMap = FrequencyTable(window, k)
        for key in freqMap:
            if freqMap[key] >= t:
               patterns.append(key) 
    patterns = list(set(patterns))
    return patterns

def FindClumps2(txt, k):
    patterns = []
    n = len(txt)
    k = int(k)
    freqMap = FrequencyTable(txt, k)
    m = MaxMap(freqMap)
    # print(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            patterns.append(key) 
    patterns = list(set(patterns))
    return patterns, m


# inFile = open("input_1.txt", 'r', encoding="utf-8")
# inText = inFile.read()
# inText = inText.splitlines()
# nums = inText[1].split()

# array = BetterFrequentWords(inText[0], inText[1])
# for x in array:
#     print(x, end=" ")