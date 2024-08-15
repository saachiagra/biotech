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

inFile = open("dataset_30273_2.txt", 'r', encoding="utf-8")
inText = inFile.read()

print(reverse(inText))