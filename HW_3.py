########### Exercise 1 ##############
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

# Part 1: Replace missing values in weight, height, and sessions

for column in [1, 2, 3]:
    valid_values = gym_data[:, column][gym_data[:, column] != 0]
    mean_value = valid_values.mean()

    if column == 3:
        mean_value = round(mean_value)

    gym_data[gym_data[:, column] == 0, column] = mean_value

print("Cleaned Gym Data:")
print(gym_data)

# Part 2: Create a new array with weight, height, and weekly sessions

fitness_data = gym_data[:, 1:4].copy()

print("Fitness Data:")
print(fitness_data)

print("\nFitness Data Shape:")
print(fitness_data.shape)

# Part 3: Calculate BMI and fitness score

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

# Part 4: Find the member with the highest fitness score

best_index = np.argmax(fitness_score)

print("Member with the Highest Fitness Score:")
print(member_names[best_index])

print("Highest Fitness Score:")
print(fitness_score[best_index])

# Part 5: Find the member whose weekly sessions differ most from the mean

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

########### Exercise 2 ##############
# Part 1: Apply Min-Max Scaling to Recipes

recipes = np.array([
    [15, 350, 2, 5],
    [45, 600, 7, 10],
    [10, 200, 0, 3],
    [30, 450, 5, 7],
    [60, 800, 8, 12]
])

recipe_names = ["Salad", "Curry", "Toast", "Pasta", "Stew"]

# Calculate the minimum and maximum values of each feature
recipes_min = np.min(recipes, axis=0)
recipes_max = np.max(recipes, axis=0)

# Apply Min-Max Scaling
recipes_scaled = (recipes - recipes_min) / (recipes_max - recipes_min)

print("\nExercise 2 - Part 1")
print("Minimum values:", recipes_min)
print("Maximum values:", recipes_max)
print("Scaled recipes:")
print(recipes_scaled)

# Part 2: Scale the preferences of three users

users = np.array([
    [10, 250, 1, 4],
    [50, 700, 8, 11],
    [25, 400, 4, 6]
])

# Scale users using the minimum and maximum values of recipes
users_scaled = (users - recipes_min) / (recipes_max - recipes_min)

print("\nExercise 2 - Part 2")
print("Original user preferences:")
print(users)

print("Scaled user preferences:")
print(users_scaled)

# Part 3: Calculate Euclidean distances between users and recipes

# Reshape arrays to enable broadcasting
users_reshaped = users_scaled[:, np.newaxis, :]
recipes_reshaped = recipes_scaled[np.newaxis, :, :]

# Calculate Euclidean distances
distances = np.sqrt(
    np.sum((users_reshaped - recipes_reshaped) ** 2, axis=2)
)

print("\nExercise 2 - Part 3")
print("Distance matrix:")
print(distances)

print("Distance matrix shape:", distances.shape)

# Part 4: Find the closest recipe for each user

closest_recipe_indices = np.argmin(distances, axis=1)

print("\nExercise 2 - Part 4")

for i in range(len(closest_recipe_indices)):
    recipe_index = closest_recipe_indices[i]
    print(f"User {i + 1}: {recipe_names[recipe_index]}")

# Part 5: Rank all recipes from closest to farthest for each user

ranked_recipe_indices = np.argsort(distances, axis=1)

print("\nExercise 2 - Part 5")

for i in range(len(ranked_recipe_indices)):
    print(f"\nUser {i + 1} recipe ranking:")

    for rank, recipe_index in enumerate(ranked_recipe_indices[i], start=1):
        distance = distances[i, recipe_index]
        recipe_name = recipe_names[recipe_index]
        print(f"{rank}. {recipe_name} - Distance: {distance:.4f}")

########### Exercise 3 ##############

# Part 1: Create the weight matrix

scheme_A = np.array([0.5, 0.3, 0.2])
scheme_B = np.array([0.2, 0.3, 0.5])
scheme_C = np.array([0.1, 0.2, 0.7])

weight_matrix = np.array([
    scheme_A,
    scheme_B,
    scheme_C
])

print("\nExercise 3 - Part 1")
print("Weight matrix:")
print(weight_matrix)
print("Weight matrix shape:", weight_matrix.shape)

# Part 2: Calculate final scores using matrix multiplication

scores = np.array([
    [18, 15, 20],
    [12, 14, 16],
    [20, 19, 18],
    [10, 8, 15]
])

final_scores = scores @ weight_matrix.T

print("\nExercise 3 - Part 2")
print("Final scores:")
print(final_scores)
print("Final scores shape:", final_scores.shape)

# Part 3: Find the best weighting scheme for each student

best_scheme_indices = np.argmax(final_scores, axis=1)
scheme_names = ["A", "B", "C"]

print("\nExercise 3 - Part 3")
print("Best scheme indices:", best_scheme_indices)

for i, scheme_index in enumerate(best_scheme_indices, start=1):
    print(f"Student {i}: Scheme {scheme_names[scheme_index]}")

# Part 4: Find the scheme with the highest class average

class_averages = np.mean(final_scores, axis=0)
best_class_scheme_index = np.argmax(class_averages)
scheme_names = ["A", "B", "C"]

print("\nExercise 3 - Part 4")
print("Class averages:", class_averages)
print("Best scheme for the class:", scheme_names[best_class_scheme_index])

# Part 5: Add a fourth weighting scheme

scheme_D = np.array([0.2, 0.4, 0.4])

weight_matrix = np.vstack((weight_matrix, scheme_D))

print("\nExercise 3 - Part 5")
print("Weight matrix with Scheme D:")
print(weight_matrix)
print("Weight matrix shape:", weight_matrix.shape)

########### Exercise 4 ##############

# Part 1: Extract and transpose the second day

weather_data = np.random.randn(2, 8, 4) * 5 + 20

day2 = weather_data[1]
day2_transposed = day2.T

print("\nExercise 4 - Part 1")
print("Original day 2 shape:", day2.shape)
print("Transposed day 2 shape:", day2_transposed.shape)

# Part 2: Flatten all weather data

weather_flat = weather_data.reshape(-1)

print("\nExercise 4 - Part 2")
print("Flattened weather data:")
print(weather_flat)
print("Flattened data shape:", weather_flat.shape)
print("Total number of values:", weather_flat.size)

# Part 3: Compare transpose and flatten

sample_matrix = np.array([
    [1, 2],
    [3, 4]
])

transposed_matrix = sample_matrix.T
flattened_matrix = sample_matrix.flatten()

print("\nExercise 4 - Part 3")
print("Original matrix:")
print(sample_matrix)

print("Transposed matrix:")
print(transposed_matrix)

print("Flattened matrix:")
print(flattened_matrix)

# Part 4: Add a third day

day3 = np.random.randn(8, 4)
day3_expanded = day3[np.newaxis, :, :]

weather_data = np.concatenate((weather_data, day3_expanded), axis=0)

print("\nExercise 4 - Part 4")
print("Third day shape:", day3.shape)
print("Weather data shape after adding day 3:", weather_data.shape)