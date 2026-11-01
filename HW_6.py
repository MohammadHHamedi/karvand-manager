
################ MohammadHHamedi##################

# ########### Exercise 1.1: Linear Regression with One Feature ###########

# import matplotlib.pyplot as plt

# from sklearn.datasets import fetch_california_housing
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split


# # Load the California Housing dataset
# housing = fetch_california_housing(as_frame=True)

# # Extract the dataset
# df = housing.frame

# # Select one feature and the target variable
# X = df[["MedInc"]]
# y = df["MedHouseVal"]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.30,
#     random_state=42
# )

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Calculate the R-squared score
# r2 = r2_score(y_test, y_pred)

# # Print the model parameters and evaluation score
# print("Exercise 1.1: Linear Regression with One Feature")
# print("-" * 50)
# print(f"Training samples: {len(X_train)}")
# print(f"Testing samples: {len(X_test)}")
# print(f"Slope: {model.coef_[0]:.4f}")
# print(f"Intercept: {model.intercept_:.4f}")
# print(f"Test R-squared: {r2:.4f}")

# # Plot the data and the regression line
# plt.figure(figsize=(10, 6))

# plt.scatter(
#     X_test["MedInc"],
#     y_test,
#     alpha=0.4,
#     label="Actual Values"
# )

# plt.scatter(
#     X_test["MedInc"],
#     y_pred,
#     alpha=0.4,
#     label="Predicted Values"
# )

# plt.xlabel("Median Income")
# plt.ylabel("Median House Value")
# plt.title("Linear Regression: Median Income vs. House Value")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# ########### Exercise 1.2: Linear Regression with Multiple Features ###########

# from sklearn.datasets import fetch_california_housing
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import r2_score
# from sklearn.model_selection import train_test_split


# # Load the California Housing dataset
# housing = fetch_california_housing(as_frame=True)
# df = housing.frame

# # Select multiple features and the target variable
# X = df[["MedInc", "HouseAge", "AveRooms"]]
# y = df["MedHouseVal"]

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.30,
#     random_state=42
# )

# # Create and train the linear regression model
# model = LinearRegression()
# model.fit(X_train, y_train)

# # Make predictions on the test set
# y_pred = model.predict(X_test)

# # Calculate the R-squared score
# r2 = r2_score(y_test, y_pred)

# # Display the results
# print("Exercise 1.2: Linear Regression with Multiple Features")
# print("-" * 55)
# print(f"Features: {list(X.columns)}")
# print(f"Training samples: {len(X_train)}")
# print(f"Testing samples: {len(X_test)}")
# print(f"Intercept: {model.intercept_:.4f}")

# for feature, coefficient in zip(X.columns, model.coef_):
#     print(f"Coefficient for {feature}: {coefficient:.4f}")

# print(f"Test R-squared: {r2:.4f}")



# ########### Exercise 2 Part A: Bayes Rule ###########

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import norm


# # Define prior probabilities
# p_healthy = 0.92
# p_defective = 0.08

# # Define normal distribution parameters
# healthy_mean = 1000
# healthy_std = 15

# defective_mean = 940
# defective_std = 25

# # Generate weight values for plotting
# weights = np.linspace(850, 1050, 1000)

# # Calculate probability density functions
# healthy_density = norm.pdf(
#     weights,
#     loc=healthy_mean,
#     scale=healthy_std
# )

# defective_density = norm.pdf(
#     weights,
#     loc=defective_mean,
#     scale=defective_std
# )

# # Plot the probability density functions
# plt.figure(figsize=(10, 6))

# plt.plot(
#     weights,
#     healthy_density,
#     label="Healthy Bags",
#     linewidth=2
# )

# plt.plot(
#     weights,
#     defective_density,
#     label="Defective Bags",
#     linewidth=2
# )

# plt.xlabel("Bag Weight")
# plt.ylabel("Probability Density")
# plt.title("Weight Distributions of Healthy and Defective Bags")
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()

# # Calculate weighted densities at weight 970
# observed_weight = 970

# healthy_score = p_healthy * norm.pdf(
#     observed_weight,
#     loc=healthy_mean,
#     scale=healthy_std
# )

# defective_score = p_defective * norm.pdf(
#     observed_weight,
#     loc=defective_mean,
#     scale=defective_std
# )

# # Calculate posterior probabilities
# total_score = healthy_score + defective_score

# p_healthy_given_weight = healthy_score / total_score
# p_defective_given_weight = defective_score / total_score

# # Display the results
# print("Exercise 2 Part A: Bayes Rule")
# print("-" * 40)
# print(f"Observed weight: {observed_weight}")
# print(f"Weighted density for Healthy: {healthy_score:.8f}")
# print(f"Weighted density for Defective: {defective_score:.8f}")
# print(f"Posterior probability of Healthy: {p_healthy_given_weight:.4%}")
# print(f"Posterior probability of Defective: {p_defective_given_weight:.4%}")

# if healthy_score > defective_score:
#     print("Classification: Healthy")
# else:
#     print("Classification: Defective")



# ########### Exercise 2 Part B: KNN Classification ###########

# from sklearn.datasets import load_wine
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.metrics import accuracy_score


# # Load the Wine dataset
# X, y = load_wine(return_X_y=True)

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.30,
#     random_state=42,
#     stratify=y
# )

# # Standardize the features
# scaler = StandardScaler()

# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Evaluate KNN with different values of k
# k_values = [1, 5, 15]

# print("Exercise 2 Part B: KNN Classification")
# print("-" * 45)
# print(f"Training samples: {len(X_train)}")
# print(f"Testing samples: {len(X_test)}")

# for k in k_values:
#     # Create and train the KNN model
#     model = KNeighborsClassifier(n_neighbors=k)
#     model.fit(X_train_scaled, y_train)

#     # Predict the classes of the test samples
#     y_pred = model.predict(X_test_scaled)

#     # Calculate test accuracy
#     accuracy = accuracy_score(y_test, y_pred)

#     print(f"k = {k:2d} | Test Accuracy: {accuracy:.4f}")




# ########### Exercise 3: Logistic Regression with Titanic Dataset ###########

# import numpy as np
# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, confusion_matrix


# # Load the Titanic dataset
# df = pd.read_csv("titanic.csv")

# # Select the required columns
# required_columns = ["Pclass", "Sex", "Age", "Fare", "Survived"]

# missing_columns = [
#     column for column in required_columns
#     if column not in df.columns
# ]

# if missing_columns:
#     raise ValueError(
#         f"Missing required columns: {missing_columns}"
#     )

# df = df[required_columns].copy()

# # Remove rows with missing target values
# df = df.dropna(subset=["Survived"])

# # Fill missing Age values with the mean age
# df["Age"] = df["Age"].fillna(df["Age"].mean())

# # Separate features and target
# X = df[["Pclass", "Sex", "Age", "Fare"]]
# y = df["Survived"].astype(int)

# # Convert categorical Sex values into numeric columns
# X = pd.get_dummies(
#     X,
#     columns=["Sex"],
#     drop_first=True,
#     dtype=int
# )

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.30,
#     random_state=42,
#     stratify=y
# )

# # Standardize the features
# scaler = StandardScaler()

# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# # Create and train the Logistic Regression model
# model = LogisticRegression(max_iter=1000)
# model.fit(X_train_scaled, y_train)

# # Predict survival on the test set
# y_pred = model.predict(X_test_scaled)

# # Calculate test accuracy
# accuracy = accuracy_score(y_test, y_pred)

# # Calculate the confusion matrix
# cm = confusion_matrix(
#     y_test,
#     y_pred,
#     labels=[0, 1]
# )

# # Display the main results
# print("Exercise 3: Logistic Regression")
# print("-" * 45)
# print(f"Total samples: {len(df)}")
# print(f"Training samples: {len(X_train)}")
# print(f"Testing samples: {len(X_test)}")
# print(f"Features: {list(X.columns)}")
# print(f"Test Accuracy: {accuracy:.4f}")

# print("\nConfusion Matrix:")
# print(cm)

# tn, fp, fn, tp = cm.ravel()

# print("\nConfusion Matrix Interpretation:")
# print(f"True Negatives: {tn}")
# print(f"False Positives: {fp}")
# print(f"False Negatives: {fn}")
# print(f"True Positives: {tp}")

# # Display incorrectly classified passengers
# results = X_test.copy()
# results["Actual"] = y_test
# results["Predicted"] = y_pred

# errors = results[
#     results["Actual"] != results["Predicted"]
# ]

# print("\nMisclassified Passengers:")
# if errors.empty:
#     print("No misclassified passengers.")
# else:
#     print(errors.to_string())

# # Display model coefficients
# print("\nModel Coefficients:")
# for feature, coefficient in zip(X.columns, model.coef_[0]):
#     print(f"{feature}: {coefficient:.4f}")

# print(f"Intercept: {model.intercept_[0]:.4f}")

# # Calculate cross-entropy loss for one correct prediction
# # and one incorrect prediction
# probabilities = model.predict_proba(X_test_scaled)
# actual_values = y_test.to_numpy()

# correct_positions = np.where(y_pred == actual_values)[0]
# wrong_positions = np.where(y_pred != actual_values)[0]


# def calculate_cross_entropy(position):
#     actual_class = actual_values[position]
#     actual_class_probability = probabilities[
#         position, actual_class
#     ]

#     actual_class_probability = np.clip(
#         actual_class_probability,
#         1e-15,
#         1 - 1e-15
#     )

#     return -np.log(actual_class_probability)


# print("\nCross-Entropy Loss Examples:")

# if len(correct_positions) > 0:
#     correct_position = correct_positions[0]
#     correct_loss = calculate_cross_entropy(correct_position)

#     print(
#         f"Correct prediction: "
#         f"Actual={actual_values[correct_position]}, "
#         f"Predicted={y_pred[correct_position]}, "
#         f"Loss={correct_loss:.4f}"
#     )
# else:
#     print("No correct prediction was found.")

# if len(wrong_positions) > 0:
#     wrong_position = wrong_positions[0]
#     wrong_loss = calculate_cross_entropy(wrong_position)

#     print(
#         f"Incorrect prediction: "

# f"Actual={actual_values[wrong_position]}, "
#         f"Predicted={y_pred[wrong_position]}, "
#         f"Loss={wrong_loss:.4f}"
#     )
# else:
#     print("No incorrect prediction was found.")


# ########### Exercise 4.1: Gini and Entropy ###########

# import numpy as np


# # Define the class counts
# root = [240, 60]
# left = [180, 10]
# right = [60, 50]


# # Calculate Gini impurity
# def calculate_gini(counts):
#     probabilities = np.array(counts, dtype=float) / sum(counts)
#     return 1 - np.sum(probabilities ** 2)


# # Calculate Entropy
# def calculate_entropy(counts):
#     probabilities = np.array(counts, dtype=float) / sum(counts)
#     probabilities = probabilities[probabilities > 0]

#     return -np.sum(probabilities * np.log2(probabilities))


# # Calculate Gini values
# gini_root = calculate_gini(root)
# gini_left = calculate_gini(left)
# gini_right = calculate_gini(right)

# # Calculate weighted child Gini
# total_samples = sum(root)

# weighted_gini = (
#     sum(left) / total_samples * gini_left
#     + sum(right) / total_samples * gini_right
# )

# # Calculate Gini-based gain
# gini_gain = gini_root - weighted_gini


# # Calculate Entropy values
# entropy_root = calculate_entropy(root)
# entropy_left = calculate_entropy(left)
# entropy_right = calculate_entropy(right)

# # Calculate weighted child Entropy
# weighted_entropy = (
#     sum(left) / total_samples * entropy_left
#     + sum(right) / total_samples * entropy_right
# )

# # Calculate Information Gain
# information_gain = entropy_root - weighted_entropy


# # Display the results
# print("Exercise 4.1: Gini and Entropy")
# print("-" * 45)

# print(f"Root Gini: {gini_root:.4f}")
# print(f"Left Gini: {gini_left:.4f}")
# print(f"Right Gini: {gini_right:.4f}")
# print(f"Weighted Child Gini: {weighted_gini:.4f}")
# print(f"Gini Gain: {gini_gain:.4f}")

# print()

# print(f"Root Entropy: {entropy_root:.4f}")
# print(f"Left Entropy: {entropy_left:.4f}")
# print(f"Right Entropy: {entropy_right:.4f}")
# print(f"Weighted Child Entropy: {weighted_entropy:.4f}")
# print(f"Information Gain: {information_gain:.4f}")


# Exercise 4.2: XOR Problem

# The XOR problem cannot be correctly solved by Logistic Regression
# because Logistic Regression uses a linear decision boundary to separate classes.

# In the XOR dataset, the points belonging to the same class are located at opposite corners. 
# Therefore, no single straight line can separate the two classes correctly.

# However, a Decision Tree can solve the XOR problem because it uses multiple sequential splits based on feature values. 
# It can first split the data using X1 and then use X2 to determine the final class.

# Conclusion: Logistic Regression is limited to a linear decision boundary, 
# while Decision Trees can create more flexible decision boundaries using multiple splits.


########### Exercise 4.3: Decision Tree vs Logistic Regression ###########

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

# Select the required columns
required_columns = ["Pclass", "Sex", "Age", "Fare", "Survived"]
df = df[required_columns].copy()

# Remove rows with missing target values
df = df.dropna(subset=["Survived"])

# Fill missing Age values with the mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Separate features and target
X = df[["Pclass", "Sex", "Age", "Fare"]]
y = df["Survived"].astype(int)

# Convert categorical features into numeric values
X = pd.get_dummies(
    X,
    columns=["Sex"],
    drop_first=True,
    dtype=int
)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Standardize the features for Logistic Regression
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# Train the Logistic Regression model
logistic_model = LogisticRegression(max_iter=1000)

logistic_model.fit(X_train_scaled, y_train)

logistic_predictions = logistic_model.predict(X_test_scaled)

logistic_accuracy = accuracy_score(
    y_test,
    logistic_predictions
)


# Train the Decision Tree model
tree_model = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

tree_model.fit(X_train, y_train)

tree_predictions = tree_model.predict(X_test)

tree_accuracy = accuracy_score(
    y_test,
    tree_predictions
)


# Display accuracy comparison
print("Exercise 4.3: Decision Tree vs Logistic Regression")
print("-" * 55)

print(f"Logistic Regression Accuracy: {logistic_accuracy:.4f}")
print(f"Decision Tree Accuracy: {tree_accuracy:.4f}")


# Display Decision Tree feature importances
print("\nDecision Tree Feature Importances:")
for feature, importance in zip(
    X.columns,
    tree_model.feature_importances_
):
    print(f"{feature}: {importance:.4f}")


# Display Logistic Regression coefficients
print("\nLogistic Regression Coefficients:")
for feature, coefficient in zip(
    X.columns,
    logistic_model.coef_[0]
):
    print(f"{feature}: {coefficient:.4f}")


# Compare the two models
print("\nModel Comparison:")

if tree_accuracy > logistic_accuracy:
    print("Decision Tree performed better.")
elif logistic_accuracy > tree_accuracy:
    print("Logistic Regression performed better.")
else:
    print("Both models achieved the same accuracy.")