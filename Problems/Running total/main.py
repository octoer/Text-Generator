num = [int(x) for x in input()]
print([sum(num[0:x]) for x in range(1, len(num)+1)])