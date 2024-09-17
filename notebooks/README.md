Task 3: Statistical Analysis of Gender Impact on Insurance Claims and Vehicle Types
Overview
This project involves conducting statistical tests to analyze the impact of gender on insurance claims and vehicle type distributions. The goal is to determine if there are significant differences in claims behavior and vehicle preferences between male and female policyholders. The findings will inform business strategy and enhance customer experience.

Objectives
Perform statistical tests (t-tests and chi-squared tests) to evaluate the impact of gender on:
Claims submitted by policyholders.
Distribution of vehicle types owned by policyholders.
Document and interpret the results within the context of their impact on business strategy and customer experience.
Data Requirements
A CSV file containing the following columns:
Gender: Categorical variable indicating the gender of the policyholder (e.g., Male, Female).
Claims: Numerical variable representing the number of claims submitted by the policyholder.
VehicleType: Categorical variable indicating the type of vehicle owned (e.g., Car, Truck, SUV).
Statistical Tests Conducted
T-test for Claims:
Compares the average claims submitted by male and female policyholders.
Null Hypothesis: Gender does not significantly impact claims submitted.
Chi-squared Test for Vehicle Type:
Assesses whether the distribution of vehicle types varies by gender.
Null Hypothesis: Gender does not significantly associate with vehicle type distribution.
Implementation Steps
Load the Dataset:
Use pandas to read the CSV file containing the insurance data.
Data Preparation:
Ensure the relevant columns (Claims, Gender, VehicleType) exist in the dataset.
Statistical Analysis:
Conduct a t-test for claims based on gender.
Conduct a chi-squared test for vehicle type distribution based on gender.
Results Interpretation:
Analyze p-values from the statistical tests to determine if the null hypotheses can be rejected.
Document findings and implications for business strategy and customer experience.
Visualization:
Use seaborn and matplotlib to create visual representations of the claims distribution and vehicle type distribution by gender.
