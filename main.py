from PIL import Image

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

im = Image.open("Buffalo.jpg")
im1 = Image.open("Elephant.jpg")
im2 = Image.open("Bird.jpg")

ImageChoice = ''

x = 100
print(BLUE + "Enter \'start\' to begin")
start = input()
while x == 100:
    if start == 'start':
        PE_Start = 0
        while PE_Start == 0:
            print(GREEN + "What image would you like to edit? Buffalo, Elephant, or Bird")
            IMAGE = input()
            if IMAGE == 'Buffalo' or IMAGE == 'Elephant' or IMAGE == 'Bird':
                print("Good choice!")
                if IMAGE == 'Buffalo':
                    ImageChoice = im
                elif IMAGE == 'Elephant':
                    ImageChoice = im1
                elif IMAGE == 'Bird':
                    ImageChoice = im2
                PE_Start = 1
            elif IMAGE != 'Buffalo' and 'Elephant' and 'Bird':
                print("You can't do that")
        if x == 100:
            x += 1

ImageChoice.show()
