import re

# Constants
filename = "input.txt"
Coordinates = []
i = 0

ans = 0
tags = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def Part1():
# Constants
    Coordinates = []
    i = 0
    ans = 0

    with open(filename) as file:
        for line in file:
            calib_data = line.strip()
            i = re.sub(r'[^0-9]','', calib_data)
            Coordinates.append(int(i[0]+i[-1]))
            # print(Coordinates)

    ans = sum(Coordinates)
    print(ans)


def find_all_instances(string,param,result):
    iter = string.count(str(param))
    i = -1
    temp = 0
    while i < iter:
        i = i+1
        temp = string.find(str(param), temp +1)
        if temp >= 0:
            result[0].append(temp)
            result[1].append(param)
    return result

def Part2():
    count = 0
    with open(filename) as file:
        for line in file:
            count = count + 1
            #print(f"the count is {count}")
            contains = [[],[]]
            calib_data = line.strip()
            for i in tags:
                contains = find_all_instances(calib_data, i, contains)
                
            for j in range(0,10):
                contains = find_all_instances(calib_data, j, contains)
            #print (contains)
            minmax = [contains[1][contains[0].index(min(contains[0]))], contains[1][contains[0].index(max(contains[0]))]]
            
            for tag in tags:
                i = minmax.count(tag)
                iter = 0
                place = -1
                while iter < i:
                    iter = iter +1
                    place = minmax.index(tag, place + 1)
                    temp = minmax[place].replace(tag,str(tags.index(tag)+1))
                    minmax[minmax.index(tag)] = temp
            
            #print(minmax)
            Coordinates.append(int(str(minmax[0])+ str(minmax[-1])))
            # print(Coordinates)

    ans = sum(Coordinates)
    print(ans)


print(Part1())

print(Part2())