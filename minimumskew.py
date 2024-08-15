def MinimumSkew(txt):
    skew = []
    count = 0
    for i in txt:
        if i == "C":
            count -= 1
        elif i == "G":
            count += 1
        else:
            count += 0
        skew.append(count)
    # print(skew)
    minimum = min(skew)
    # print(minimum)
    minIndex = []
    for index, x in enumerate(skew):
        if x == minimum:
            minIndex.append(index + 1)
    return skew, minIndex
