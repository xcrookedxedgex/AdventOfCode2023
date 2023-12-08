def adventOfCodeDayTwo():
    inputString = read_text_file()
    print(inputString)

def read_text_file():
    inputLines = ""
    #reads a .txt file and returns the content as list
    with open('input.txt') as f:
        inputLines = f.readlines()
    return inputLines


if __name__ == "__main__":
    adventOfCodeDayTwo()