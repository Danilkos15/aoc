def load_data():
    data = []
    with open("data.txt") as file:
        for num in file:
            data.append(int(num))
    return data

def diff(data):
    ret = []
    for i in range(len(data)-1):
        ret.append(data[i+1] - data[i])
    return ret

def slide(data):
    ret = []
    for i in range(len(data)-2):
        ret.append(data[i] + data[i+1] + data[i+2])
    return ret

count = 0
a = diff(slide(load_data()))
for b in a:
    count += 1 if b > 0 else 0

print(count)
