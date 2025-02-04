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
            # Method for user to select photo
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

print(RESET + "Now that we have our image, lets make some edits!")
while True:
    print("---------------------EDITS-----------------------")
    print("1. Crop")
    print("2. Spin")
    print("3. Enlarge/Shrink")

    EditChoice = input()

    def crop(image):
        # Give image size to help user choose crop values/coordinates
        width, height = image.size
        print(f"Image Size: {width} * {height} ")
        # Actual value choosing
        while True:
            print("Enter the coordinates for cropping:")
            left = int(input(f"Left (0-{width - 1}): "))
            top = int(input(f"Top (0-{height - 1}): "))
            right = int(input(f"Right (0-{width - 1}): "))
            bottom = int(input(f"Bottom (0-{height - 1}): "))
            if not (0 <= left < right <= width and 0 <= top < bottom <= height):
                print(RED + "Coordinates aren't possible." + RESET)
                continue
            else:
                cropped_image = image.crop((left, top, right, bottom))
                cropped_image.show()
                return cropped_image

    if EditChoice == 'Crop':
        ImageChoice = crop(ImageChoice)
#   if EditChoice == 'Spin':
#       ImageChoice = spin(ImageChoice)
#   if EditChoice == 'Enlarge':
#       ImageChoice = enlarge(ImageChoice)
#   if EditChoice == 'Shrink':
#       ImageChoice = shrink(ImageChoice)
    print("Would you like to continue editing?")
    answer = input()
    if answer == 'yes':
        print(GREEN + "Great!" + RESET)
    elif answer == 'no':
        break

# Minimum Requirements:
# 	- method for user to select photo       CHECK
#	- 3 types of edits that could be used
#	- changing file type
#   - manipulate the file at an individual pixel level
#	(i.e. Swap pixel colors, all red becomes green. Or apply a filter like ‘Enhance’)