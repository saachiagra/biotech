def immediateNeighbors(pattern, d):
    neighborhood = [pattern]
    for i in range(len(pattern)):
        symbol = pattern[i]
        nucleotide = ["A", "C", "G", "T"]
        for x in nucleotide:
            if x == symbol:
                x = x
            else:
                neighbor = pattern[:i] + x + pattern[i+1:]
                neighborhood.append(neighbor)
    return neighborhood

def HammingDistance(txt1, txt2):
    l = len(txt1)
    count = 0
    for i in range(l):
        if txt1[i] != txt2[i]:
            count += 1
    return count

def MaxMap(dict):
    max = 0
    for x in dict:
        if dict[x] > max:
            max = dict[x]
    return max

def reverse(dna):
    compStrand = ""
    for i in dna:
        match i:
            case "A":
                compStrand += "T"
            case "T":
                compStrand += "A"
            case "C":
                compStrand += "G"
            case "G":
                compStrand += "C"
    compStrand = compStrand[::-1]
    return compStrand

def neighbors(pattern, d):
    if int(d) == 0:
        return [pattern]
    if len(pattern) == 1:
        return ["A", "C", "G", "T"]
    neighborhood = []
    nucleotides = ["A", "C", "G", "T"]
    suffixNeighbors = neighbors(pattern[1:], d)
    for text in suffixNeighbors:
        if HammingDistance(pattern[1:], text) < int(d):
            for x in nucleotides:
                neighborhood.append(x + text)
        else:
            neighborhood.append(pattern[0] + text)
    return(neighborhood)

def freqWordsMis(txt, k, d):
    patterns = []
    freqMap = {}
    n = len(txt)
    k = int(k)
    for i in range(n-k+1):
        pattern = txt[i:i+k]
        neighborhood = neighbors(pattern, d)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            try:
                freqMap[neighbor] += 1
            except KeyError:
                freqMap[neighbor] = 1
    m = MaxMap(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            patterns.append(key)
    return patterns, m

def freqWordsMisRev(txt, k, d):
    patterns = []
    freqMap = {}
    n = len(txt)
    k = int(k)
    for i in range(n-k+1):
        pattern = txt[i:i+k]
        neighborhood = neighbors(pattern, d)
        pattern = reverse(pattern)
        neighborhood.extend(neighbors(pattern, d))
        # print(neighborhood)
        for j in range(len(neighborhood)):
            neighbor = neighborhood[j]
            try:
                freqMap[neighbor] += 1
            except KeyError:
                freqMap[neighbor] = 1
    m = MaxMap(freqMap)
    # print(freqMap)
    for key in freqMap:
        if freqMap[key] == m:
            patterns.append(key)
    # for i in patterns:
    #     for j in patterns:
    #         if HammingDistance(i, j) <= d and i != j:
    #             try:
    #                 patterns.remove(i)
    #             except ValueError:
    #                 i = i
    return patterns, m


# inFile = open("dataset_30278_10 (1).txt", 'r', encoding="utf-8")
# inText = inFile.read()
# inText = inText.split()
# # print(inText)

# strand = "ATTATACGAACGTAGGGAC"
# print(reverse(strand))
# quit()