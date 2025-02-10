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
            print(GREEN + "What image would you like to edit? Buffalo, Elephant, or Bird?")
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

def filter(image):
    print(GREEN + "What filter would you like?" + RESET)
    while True:
        print("---------------------FILTERS-----------------------")
        print("1. Invert Colours")
        print("2. FlashBang")
        Image_Filter = input()
        if Image_Filter == 'Invert Colours':
            r, g, b = image.split()
            filtered_image = Image.merge("RGB", (b, g, r))
            filtered_image.show()
            return filtered_image
        elif Image_Filter == 'FlashBang':
            filtered_image = image.point(lambda i: i * 20)
            filtered_image.show()
            return filtered_image
        else:
            print("Pick one of the options correctly!")

while True:
    print("---------------------EDITS-----------------------")
    print("1. Crop")
    print("2. Filter")
    print("3. Scale")
    EditChoice = input()
    if EditChoice == 'Crop':
        ImageChoice = crop(ImageChoice)
    elif EditChoice == "Scale":
        ImageChoice = scale(ImageChoice)
    elif EditChoice == 'Filter':
        ImageChoice = filter(ImageChoice)
    else:
        print(RED + "Invalid choice" + RESET)
    print("Would you like to continue editing?")
    answer = input()
    if answer.lower() == 'yes':   #Continue Editing
        print(GREEN + "Great!" + RESET)
    else:
        print(GREEN + "Now that were done editing..." + RESET)   #Save new changed or unchanged image
        print("What would you like your image to be saved as? " + BLUE + "End with file type such as .png or .jpg: " + RESET + "eg. image_name.jpg")
        SavedName = input()
        ImageChoice.save(SavedName)
        print(f"Your image has been saved as \'{SavedName}\'.")
        break

#possibly add that user could take their own image and edit it based on program.