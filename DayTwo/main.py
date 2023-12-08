import constants as const

def adventOfCodeDayTwo():
    inputString = read_text_file()
    input_dict = create_directory(inputString)
    for key in input_dict.keys():
        if check_games(input_dict[key]):
            const.SUM += key
    print("SUM FOR VALID GAMES: ", const.SUM)

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
    game_dict = {}
    rounds_list = game.split(";")
    for round in rounds_list:
        round = round.strip()
        draws = round.split(",")
        for draw in draws:
            draw = draw.strip()
            value, key = draw.split(" ")
            game_dict[key] = value
    print(game_dict)       
    check_game_dict(game_dict) 
    return True


if __name__ == "__main__":
    adventOfCodeDayTwo()