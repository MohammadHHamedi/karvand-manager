
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

########### Exercise 1.2: Linear Regression with Multiple Features ###########

from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


# Load the California Housing dataset
housing = fetch_california_housing(as_frame=True)
df = housing.frame

# Select multiple features and the target variable
X = df[["MedInc", "HouseAge", "AveRooms"]]
y = df["MedHouseVal"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Calculate the R-squared score
r2 = r2_score(y_test, y_pred)

# Display the results
print("Exercise 1.2: Linear Regression with Multiple Features")
print("-" * 55)
print(f"Features: {list(X.columns)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
print(f"Intercept: {model.intercept_:.4f}")

for feature, coefficient in zip(X.columns, model.coef_):
    print(f"Coefficient for {feature}: {coefficient:.4f}")

print(f"Test R-squared: {r2:.4f}")