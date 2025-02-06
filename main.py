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


image_modified = False
while True:
    print("---------------------EDITS-----------------------")
    print("1. Crop")
    print("2. Filter")
    print("3. Scale")
    EditChoice = input()
    if EditChoice == 'Crop':
        ImageChoice = crop(ImageChoice)
        image_modified = True
    elif EditChoice == 'Enlarge' or EditChoice == 'Shrink':
        ImageChoice = scale(ImageChoice)
        image_modified = True
    elif EditChoice == 'Filter':
        ImageChoice = filter(ImageChoice)
        image_modified = True
    else:
        print(RED + "Invalid choice" + RESET)
    print("Would you like to continue editing?")
    answer = input()
    if answer.lower() == 'yes':
        print(GREEN + "Great!" + RESET)
    else:
        break
if image_modified:
    print(GREEN + "Image has been modified" + RESET)
else:
    print("No modifications to image")


print("Would you like to save and/or change the image?")
save_change = input()
if save_change == "yes":
    print(GREEN + "Now, lets save and/or change the image!" + RESET)
    while True:
        print("Enter name for new, edited image: " + BLUE + "eg. name.jpg or name.png" + RESET)
        SavedImageName = input()
        if "." not in SavedImageName:
            print(RED + "Invalid Name, name must include \'.\': eg. .jpg or .png" + RESET)
            continue

        file_extension = SavedImageName[SavedImageName.rfind("."):]
        valid_extensions = [".jpg", ".jpeg", ".png", ".gif"]
        if file_extension.lower() not in valid_extensions:
            print(RED + "Invalid file extension. Use .jpg, .jpeg, .png, or .gif" + RESET)
            continue

        if file_extension.lower() == ".jpg" or file_extension.lower() == ".jpeg":
            ImageChoice.save(SavedImageName, "JPEG")
        elif file_extension.lower() == ".png":
            ImageChoice.save(SavedImageName, "PNG")
        saved_image = Image.open(SavedImageName)
        saved_image.show()

        print(GREEN + f"Image has been saved as {SavedImageName}! " + RESET)
        break
else:
    print("Thankyou, for editing an Image!")
