print('How to make a better break box!')
lg = int(input('Please enter the Length: ')) # Gather Length information
wd = int(input('Please enter the Width: ')) # Gather Width information
ht = int(input('Please enter the Height: ')) # Gather Height information

# Build Function to calculate the Area 
def area(length, width):
    return ((length) * (width))

# Build Function to calculate the Perimeter 
def perimeter(length, width):
    return ((length * 2) + (width * 2))

# Build Function to calculate the Volume 
def volume(length, width, height):
    return (length) * (width) * (height)

# Build Function to calculate the Surface Area                                
def surf_area(length, width, height):
    return ((length * width) + (length * height) + (width * height)) * 2

# Function call to calculate the Area 
user_area = area(lg, wd)
print('The Area is: ' + str(user_area))

# Function call to calculate the perimeter
user_perimeter = perimeter(lg, wd)
print('The Perimeter is: ' + str(user_perimeter))

# Function call to calculate the volume
user_volume = volume(lg, wd, ht)
print('The Volume is ' + str(user_volume))

# Function call to calculate the Surface Area
user_surf_area = surf_area(lg, wd, ht)
print('The Surface Area is ' + str(user_surf_area))
