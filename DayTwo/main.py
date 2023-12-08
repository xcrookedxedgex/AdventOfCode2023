import constants as const

def adventOfCodeDayTwo():
    inputString = read_text_file()
    input_dict = create_directory(inputString)
    for key in input_dict.keys():
        if check_games(input_dict[key]):
            const.SUM += key
    print("RESULT Puzzle 1: ", const.SUM)
    print("POWER:", const.SUM_POWER)

def read_text_file():
    inputLines = ""
    #reads a .txt file and returns the content as list
    with open('input.txt') as f:
        inputLines = f.readlines()
    return inputLines

def create_directory(games):
    input_dict = {}
    for game in games:
        key, value = game.split(":")
        key = key.strip()
        value = value.strip()
        key = int(''.join(filter(str.isdigit, key))) #searches for the first appearance of a digit in a string
        input_dict[key] = value
    return input_dict

def check_games(game):
    valid = True #We asume, that every game is valid
    draw_dict = {}
    rounds_list = game.split(";")
    
    min_red = 0
    min_green = 0
    min_blue = 0

    for round in rounds_list:
        round = round.strip()
        draws = round.split(",")
        for draw in draws:
            draw = draw.strip()
            value, key = draw.split(" ")
            draw_dict[key] = value      
            valid &= check_draw(draw_dict) #We check every round, if one round is invalid, the whole game gets invalid
            min_red, min_blue, min_green = calculate_power(draw_dict, min_red, min_green, min_blue)

    const.SUM_POWER += (min_blue * min_red * min_green)
    return valid

def check_draw(draw_dict):
    for key in draw_dict.keys():
        if(key == "red"):
            if(int(draw_dict[key]) > const.RED):
                return False
        if(key == "green"):
            if(int(draw_dict[key]) > const.GREEN):
                return False
        if(key == "blue"):
            if(int(draw_dict[key]) > const.BLUE):
                return False
    return True

def calculate_power(draw_dict, min_red, min_green, min_blue):
    if("red" in draw_dict):
        red_balls = int(draw_dict["red"])
        if(red_balls > min_red):
            min_red = red_balls
    
    if("blue" in draw_dict):
        blue_balls = int(draw_dict["blue"])
        if(blue_balls > min_blue):
            min_blue = blue_balls
    
    if("green" in draw_dict):
        green_balls = int(draw_dict["green"])
        if(green_balls) > min_green:
            min_green = green_balls
    
    return min_red, min_blue, min_green

    
if __name__ == "__main__":
    adventOfCodeDayTwo()