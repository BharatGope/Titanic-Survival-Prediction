# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

print("Original Dataset Shape:", df.shape)

# -----------------------------
# Handle Missing Values
# -----------------------------

# Age -> Median
df["Age"] = df["Age"].fillna(df["Age"].median())


# Fare -> Mean
df["Fare"] = df["Fare"].fillna(df["Fare"].mean())

# Embarked -> Mode
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cabin has too many missing values
df.drop("Cabin", axis=1, inplace=True)

# -----------------------------
# Encode Categorical Variables
# -----------------------------

# Label Encoding for Sex
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])

# One Hot Encoding for Embarked
df = pd.get_dummies(df,
                    columns=["Embarked"],
                    drop_first=True)

# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(8,5))
sns.histplot(df["Age"],
             bins=30,
             kde=True,
             color="skyblue")

plt.title("Age Distribution of Titanic Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# -----------------------------
# Save Cleaned Dataset
# -----------------------------

df.to_csv("Titanic_Cleaned.csv",
          index=False)

print("Cleaned dataset saved successfully!")

print("\nFinal Dataset Shape:", df.shape)
print(df.head())