test = ['40,40,40', '40,40,40']

result = []
for item in test:
    result.append(tuple(map(int, item.split(','))))

print(result)