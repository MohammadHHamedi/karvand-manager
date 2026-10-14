########### Practice 1 ##############
import numpy as np

gym_data = np.array([
    [28, 75, 175, 4],
    [34, 68, 168, 3],
    [45, 82, 180, 2],
    [22, 58, 162, 5],
    [38, 90, 0, 1],
    [29, 65, 170, 0]
])

member_names = np.array([
    "Ali", "Sara", "Reza",
    "Neda", "Hassan", "Maryam"
])

print("Original Gym Data:")
print(gym_data)

print("\nMember Names:")
print(member_names)

# Replace missing values in weight, height, and sessions

for column in [1, 2, 3]:
    valid_values = gym_data[:, column][gym_data[:, column] != 0]
    mean_value = valid_values.mean()

    if column == 3:
        mean_value = round(mean_value)

    gym_data[gym_data[:, column] == 0, column] = mean_value

print("Cleaned Gym Data:")
print(gym_data)

# Create a new array with weight, height, and weekly sessions

fitness_data = gym_data[:, 1:4].copy()

print("Fitness Data:")
print(fitness_data)

print("\nFitness Data Shape:")
print(fitness_data.shape)

# Calculate BMI and fitness score

weight = fitness_data[:, 0]
height = fitness_data[:, 1] / 100
sessions = fitness_data[:, 2]

bmi = weight / (height ** 2)

fitness_score = (bmi * 1) + (sessions * 2)

fitness_data = np.column_stack((
    fitness_data,
    fitness_score
))

print("Fitness Data with Fitness Score:")
print(fitness_data)

print("\nBMI:")
print(bmi)

print("\nFitness Scores:")
print(fitness_score) 

# Find the member with the highest fitness score

best_index = np.argmax(fitness_score)

print("Member with the Highest Fitness Score:")
print(member_names[best_index])

print("Highest Fitness Score:")
print(fitness_score[best_index])

# Find the member whose weekly sessions differ most from the mean

sessions_mean = np.mean(sessions)
sessions_std = np.std(sessions)

deviations = np.abs(sessions - sessions_mean)

most_different_index = np.argmax(deviations)

print("Mean Weekly Sessions:")
print(sessions_mean)

print("\nStandard Deviation:")
print(sessions_std)

print("\nMember with the Most Different Weekly Sessions:")
print(member_names[most_different_index])

print("Weekly Sessions:")
print(sessions[most_different_index])

print("Absolute Deviation from Mean:")
print(deviations[most_different_index])