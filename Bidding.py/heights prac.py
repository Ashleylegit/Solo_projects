# Given heights of students
students_heights = [156, 178, 165, 171, 187]

# Initialize variables to store total height and number of students
total_height = 0
number_of_students = 0

# Loop through the list of student heights to calculate total height and count the number of students
for height in students_heights:
    total_height += height
    number_of_students += 1

# Calculate the average height
average_height = total_height / number_of_students

# Print the total number of students and the
# Print the total number of students and their average height
print(f"Number of students = {number_of_students}")
print(f"Average height = {average_height}")

# Initialize an empty list to store student heights
students_heights = []

# Ask the user for the number of students
number_of_students = int(input("Enter the number of students: "))

# Use a loop to get heights for each student
for i in range(number_of_students):
    # Get height from the user and convert it to an integer
    height = int(input(f"Enter the height of student {i + 1} in centimeters: "))
    # Add the height to the list of student heights
    students_heights.append(height)