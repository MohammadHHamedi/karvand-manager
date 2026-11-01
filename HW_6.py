
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

########### Exercise 2 Part B: KNN Classification ###########

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# Load the Wine dataset
X, y = load_wine(return_X_y=True)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42,
    stratify=y
)

# Standardize the features
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Evaluate KNN with different values of k
k_values = [1, 5, 15]

print("Exercise 2 Part B: KNN Classification")
print("-" * 45)
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

for k in k_values:
    # Create and train the KNN model
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train_scaled, y_train)

    # Predict the classes of the test samples
    y_pred = model.predict(X_test_scaled)

    # Calculate test accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print(f"k = {k:2d} | Test Accuracy: {accuracy:.4f}")