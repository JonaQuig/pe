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

def spin(image):
        print(GREEN + "Which way would you like to rotate your image?" + RESET)
        while True:
            print("---------------------Options-----------------------")
            print("1. Left to Right / Right to Left")
            print("2. Up to Down / Down to Up")
            print("3. Rotate 90, 180, or 270 degrees")
            SpinChoice = input()

            if SpinChoice == "1":
                return image.transpose(Image.FLIP_LEFT_RIGHT)
            elif SpinChoice == "2":
                return image.transpose(Image.FLIP_TOP_BOTTOM)

def scale(image):
        width, height = image.size
        while True:
            print("What would you like your scale factor to be?")
            scale_factor_input = input()
            if scale_factor_input.isdigit:
                scale_factor = float(scale_factor_input)
                if scale_factor > 0:
                    new_width = int(width * scale_factor)
                    new_height = int(height * scale_factor)
                    scaled_image = image.resize((new_width, new_height))
                    scaled_image.show()
                    return scaled_image
                else:
                    print(RED + "Wrong input. Is the input positive?" + RESET)
            else:
                print(RED + "Invalid input. Please enter a number." + RESET)

while True:
    print("---------------------EDITS-----------------------")
    print("1. Crop")
    print("2. Spin")
    print("3. Enlarge/Shrink")
    EditChoice = input()
    if EditChoice == 'Crop':
        ImageChoice = crop(ImageChoice)
    elif EditChoice == 'Spin':
        ImageChoice = spin(ImageChoice)
    elif EditChoice == 'Enlarge' or EditChoice == 'Shrink':
        ImageChoice = scale(ImageChoice)
    else:
        print(RED + "Invalid choice" + RESET)
    print("Would you like to continue editing?")
    answer = input()
    if answer.lower() == 'yes':
        print(GREEN + "Great!" + RESET)
    else:
        break


# Minimum Requirements:
# 	- method for user to select photo       CHECK
#	- 3 types of edits that could be used   2 of 3 done!
#	- changing file type
#   - manipulate the file at an individual pixel level
#	(i.e. Swap pixel colors, all red becomes green. Or apply a filter like ‘Enhance’)
