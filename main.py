import matplotlib.pyplot as plt

# Read input.txt file
with open("input.txt", "r") as input_file:
    input_lines = input_file.readlines()

# Create a list to store student averages
student_averages = []

# Calculate average for each student
for line in input_lines:
    # Split line into student name and scores
    parts = line.split()
    student_name = parts[0]
    scores = parts[1:]

    # Convert scores to integers
    scores = [int(float(score)) for score in scores]

    # Calculate average
    average = sum(scores) / len(scores)

    # Add student name and average to list
    student_averages.append((student_name, average))

# Write student name and average to output.txt file
with open("output.txt", "w") as output_file:
    for student, average in student_averages:
        output_file.write(student + " " + str(average) + "\n")

# Calculate overall average
overall_average = sum(average for student,average in student_averages) / len(student_averages)

# write overall average to the output file
with open("output.txt", "a") as output_file:
    output_file.write("Average " + str(overall_average) + "\n")

# Create a list to store scores in 4 different intervals
scores_interval = [[] for i in range(4)]

# Iterate through student averages and categorize them in different intervals
for student, average in student_averages:
    if 15 <= average <= 20:
        scores_interval[0].append(average)
    elif 10 <= average < 15:
        scores_interval[1].append(average)
    elif 5 <= average < 10:
        scores_interval[2].append(average)
    elif 0 <= average < 5:
        scores_interval[3].append(average)

# Plot histogram for each interval
plt.hist(scores_interval, bins = [0, 5, 10, 15, 20], rwidth = 0.8,
         label = ['A', 'B', 'C', 'D'])

# Add labels and title to the histogram
plt.xlabel("Interval")
plt.ylabel("Frequency")
plt.title("Frequency of Scores in each Interval")

# Show legend
plt.legend()

# Show the plot
plt.show()