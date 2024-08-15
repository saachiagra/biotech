def HammingDistance(txt1, txt2):
    l = len(txt1)
    count = 0
    for i in range(l):
        if txt1[i] != txt2[i]:
            count += 1
    return count

def ApproximatePattern(seq, gen, error):
    index = []
    for i in range(len(gen) - len(seq) + 1):
        comp = gen[i:i+len(seq)]
        if (HammingDistance(comp, seq) <= int(error)):
            index.append(i)
    return index

inFile = open("dataset_30278_6.txt", 'r', encoding="utf-8")
inText = inFile.read()
inText = inText.splitlines()

x = ApproximatePattern(inText[0], inText[1], inText[2])

# for i in x:
#     print(i, end=" ")
# print(len(x))