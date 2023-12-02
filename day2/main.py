
# Constants
filename = "input.txt"

max_cubes = {"red"   :12,
             "green" :13,
             "blue"  :14
             } # R, G, B cubes


def getRGB(data):
    game = {
    "red"  : 0,
    "green": 0,
    "blue" : 0
    }
    temp = data.split(",")
    for i in temp:
        # print(f"data is: {i}")
        if i.find("red") >= 0:
            game["red"] = int(i.strip(" red"))
        elif i.find("green") >= 0:
            game["green"] = int(i.strip(" green"))
        elif i.find("blue") >= 0:
            game["blue"] = int(i.strip(" blue"))
    # print(game)
    return game

def compareRGB_pt1(data):
    compare1 = max_cubes
    compare2 = data
    inside_limits = True
    for key in compare1.keys():
        if compare2[key] <= compare1[key]:
            inside_limits =  True
        else:
            inside_limits = False
            return inside_limits
    return inside_limits
            
def Part1():
    # Constants
    ans = 0
    game_data = {
        "game_num" : 0,
        "combinations": {
            "red": 0,
            "green": 0,
            "blue": 0,
        },  
    }
    with open(filename) as file:
        for line in file:
            inside_limit = True
            whole_data = line.strip().split(":")
            game_data["game_num"] = whole_data[0]
            print(game_data["game_num"])
            temp = whole_data[1].split(";")
            for i in temp: 
                game_data["combinations"] = getRGB(i)
                print(game_data["combinations"])
                if compareRGB_pt1(game_data["combinations"]):
                    print(f"inside limits for {game_data["game_num"]}")
                    inside_limit = True
                else:
                    print(f"outside limits for {game_data["game_num"]}")
                    inside_limit = False
                    break
            if inside_limit:
                ans = ans + int(game_data["game_num"].strip("Game"))
                print(f"Answer is: {ans}")
                
            # print(game_data)
    print(ans)
    return ans


def compareRGB_pt2(compare1,compare2):
    end_combo = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    for key in compare1.keys():
        if compare2[key] <= compare1[key]:
            end_combo[key] =  compare1[key]
        else:
            end_combo[key] =  compare2[key]
            
    return end_combo

def resetRGB(data,ans):
    for key in data.keys():
        ans = ans * data[key]
        data[key] = 0
    return data,ans 

def Part2():
    # Constants
    ans_per_game = 1
    ans = []
    game_data = {
        "game_num" : 0,
        "combinations": {
            "red": 0,
            "green": 0,
            "blue": 0,
        },
    }
    compare_data = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    
    with open(filename) as file:
        for line in file:
            whole_data = line.strip().split(":")
            game_data["game_num"] = whole_data[0]
            # print(game_data["game_num"])
            temp = whole_data[1].split(";")
            for i in temp:
                compare_data = getRGB(i)
                game_data["combinations"] = compareRGB_pt2(game_data["combinations"],compare_data)
            # print(game_data["combinations"])
            game_data["combinations"], ans_per_game = resetRGB(game_data["combinations"],ans_per_game)
            # print(f"The answer for{game_data['game_num']} is {ans_per_game}")
            ans.append(ans_per_game)
            ans_per_game = 1
        print(f"The final answer is {sum(ans)}")
        return sum(ans)

Part2()