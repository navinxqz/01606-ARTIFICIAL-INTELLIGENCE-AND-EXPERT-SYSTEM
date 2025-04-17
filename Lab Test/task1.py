def matching(words):
    count = 0
    for i in words:
        if len(i) >= 2 and i[0] == i[-1]:
            count += 1
    return count

n = ['abc', 'xyz', 'aba', '1221']
result = matching(n)
print("Result:", result)
