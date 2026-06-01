# Titanic Survival Prediction – Data Cleaning Project

## Overview

This project focuses on cleaning and preprocessing the Titanic dataset to prepare it for machine learning applications. The dataset contains information about Titanic passengers, including demographic details, ticket information, and survival status.

The project demonstrates essential data preprocessing techniques such as handling missing values, encoding categorical variables, visualizing data distributions, and exporting a cleaned dataset.

---

## Objectives

* Load and explore the Titanic dataset using Pandas.
* Handle missing values using appropriate imputation techniques.
* Encode categorical features for machine learning compatibility.
* Visualize passenger age distribution.
* Export the cleaned dataset to a new CSV file.

---

## Dataset

**Source:** Titanic Dataset (Kaggle)

The dataset includes passenger details such as:

* PassengerId
* Survived
* Pclass
* Name
* Sex
* Age
* SibSp
* Parch
* Ticket
* Fare
* Cabin
* Embarked

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Data Preprocessing Steps

### 1. Loading the Dataset

The dataset is loaded using Pandas:

```python
import pandas as pd
df = pd.read_csv("Titanic-Dataset.csv")
```

### 2. Handling Missing Values

Missing values are handled as follows:

* **Age** → Replaced with Median
* **Fare** → Replaced with Mean
* **Embarked** → Replaced with Mode
* **Cabin** → Removed due to a large number of missing values

### 3. Encoding Categorical Variables

#### Label Encoding

The `Sex` column is converted into numerical values:

| Original | Encoded |
| -------- | ------- |
| Female   | 0       |
| Male     | 1       |

#### One-Hot Encoding

The `Embarked` column is transformed into binary columns:

* Embarked_Q
* Embarked_S

### 4. Data Visualization

A histogram with KDE is created to analyze the age distribution of Titanic passengers using Seaborn and Matplotlib.

### 5. Exporting Cleaned Data

The cleaned dataset is saved as:

```text
Titanic_Cleaned.csv
```

---

## Project Structure

```text
Assignment 1/
│
├── Titanic Survival Prediction.py
├── Titanic-Dataset.csv
├── Titanic_Cleaned.csv
└── README.md
```

---

## Results

* Successfully cleaned missing data.
* Encoded categorical variables.
* Visualized age distribution.
* Generated a machine-learning-ready dataset.
* Exported cleaned data to a CSV file.

---

## Learning Outcomes

Through this project, the following concepts were learned:

* Data loading and exploration with Pandas
* Missing value treatment
* Label Encoding and One-Hot Encoding
* Data visualization using Matplotlib and Seaborn
* Dataset preprocessing for machine learning workflows

---

## Author

**Bharat Kumar Gope**  
B.Tech CSE Student  
Ramgarh Engineering College

---

## Future Improvements

* Feature scaling and normalization
* Outlier detection and removal
* Feature engineering
* Building a Titanic Survival Prediction Machine Learning Model
* Model evaluation and performance comparison
