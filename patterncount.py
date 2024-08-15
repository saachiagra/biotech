def PatternCount(txt, ptn):
    count = 0
    for i in range(len(txt)+1-len(ptn)):
        # print(txt[i:i+len(ptn)])
        if txt[i:i+len(ptn)] == ptn:
            count += 1
    return count

inFile = open("dataset_30272_6.txt", 'r', encoding="utf-8")
inText = inFile.read()
inText = inText.splitlines()

print(PatternCount(inText[0], inText[1]))