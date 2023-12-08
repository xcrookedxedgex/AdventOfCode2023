def adventOfCodeDayTwo():
    inputString = read_text_file()
    input_dict = create_directory(inputString)
    print(input_dict)

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
        value.strip()
        key = int(''.join(filter(str.isdigit, key))) #searches for the first appearance of a digit in a string
        input_dict[key] = value
    return input_dict



if __name__ == "__main__":
    adventOfCodeDayTwo()