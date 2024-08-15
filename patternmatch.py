def findPatterns(ptn, genome):
    index = []
    x = 0
    while x < len(genome):
        try:
            index.append(genome.index(ptn, x))
            x = genome.index(ptn, x) + 1
        except ValueError:
            x = len(genome)
    return index

inFile = open("Vibrio_cholerae.txt", 'r', encoding="utf-8")
inText = inFile.read()
# inText = inText.splitlines()

array = findPatterns("CTTGATCAT", inText)
for x in array:
    print(x, end=" ")


