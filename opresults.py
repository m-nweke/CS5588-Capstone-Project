# -*- coding: utf-8 -*-
"""OPresults.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/113PGuwTX-jCogT6imjFTdB89oiIVF0OZ
"""

#kneeling confusion
from sklearn.metrics import confusion_matrix
import pandas as pd

# Sample data (replace with your model predictions and actual values)
# y_pred: Model predicted values (0 for kneeling, 1 for not kneeling)
# y_actual: Actual values (0 for kneeling, 1 for not kneeling)
y_pred = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
y_actual = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_actual, y_pred)

# Print confusion matrix
print('Confusion Matrix:')
print(conf_matrix)

# Labels
labels = ['Kneeling', 'Not Kneeling']
conf_matrix_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
print(conf_matrix_df)

# Interpretation:
# - conf_matrix[0, 0] is True Negative (TN): Model predicts "kneeling" and the actual value is "kneeling".
# - conf_matrix[0, 1] is False Positive (FP): Model predicts "not kneeling" but the actual value is "kneeling".
# - conf_matrix[1, 0] is False Negative (FN): Model predicts "kneeling" but the actual value is "not kneeling".
# - conf_matrix[1, 1] is True Positive (TP): Model predicts "not kneeling" and the actual value is "not kneeling".

# Calculate True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN)
TP = conf_matrix[1][1]
TN = conf_matrix[0][0]
FP = conf_matrix[0][1]
FN = conf_matrix[1][0]

# Precision: Percentage of true positives among all positive predictions
precision = TP / (TP + FP)

# Recall (Sensitivity): Percentage of true positives among all actual positives
recall = TP / (TP + FN)

# Specificity: Percentage of true negatives among all actual negatives
specificity = TN / (TN + FP)

# Sensitivity: Same as recall, percentage of true positives among all actual positives
sensitivity = recall

# Print the calculated metrics
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Sensitivity: {sensitivity:.2f}')

#kneeling percent correct
def calculate_percentage(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate percentage
    percentage = (num_correct / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage, 2)

    return percentage_rounded

# Example usage
numkneelingcorrect = 18  # Number of correct kneeling answers
totalkneeling = 20  # Total number of kneeling questions

# Calculate the percentage of kneeling correct
percentkneelingcorrect = calculate_percentage(numkneelingcorrect, totalkneeling)

# Print the calculated percentage
print(f"Percentage Kneeling correct: {percentkneelingcorrect}%")

#kneeling percent incorrect:

def calculate_percentage_incorrect(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate the number of incorrect answers
    num_incorrect = total - num_correct

    # Calculate percentage of incorrect answers
    percentage_incorrect = (num_incorrect / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage_incorrect, 2)

    return percentage_rounded

# Example usage
numkneelingcorrect = 18
totalkneeling = 20

# Calculate the percentage of incorrect answers for kneeling
percentkneelingincorrect = calculate_percentage_incorrect(numkneelingcorrect, totalkneeling)
print(f"Percentage Kneeling incorrect: {percentkneelingincorrect}%")

#back confusion
from sklearn.metrics import confusion_matrix
import pandas as pd

# Sample data (replace with your model predictions and actual values)
# y_pred: Model predicted values (1 for straight, 0 for hunched/reclined)
# y_actual: Actual values (1 for straight, 0 for hunched/reclined)
y_pred = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1]
y_actual = [0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0 , 0, 1, 1, 1]

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_actual, y_pred)

# Print confusion matrix
print('Confusion Matrix:')
print(conf_matrix)

# Optionally, label the confusion matrix for clarity
labels = ['Hunched/Reclined', 'Straight']
conf_matrix_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
print(conf_matrix_df)

# Interpretation:
# - conf_matrix[0, 0] is True Negative (TN): Model predicts "hunched" or "reclined" and the actual value is "hunched" or "reclined".
# - conf_matrix[0, 1] is False Positive (FP): Model predicts "straight" but the actual value is "hunched" or "reclined".
# - conf_matrix[1, 0] is False Negative (FN): Model predicts "hunched" or "reclined" but the actual value is "straight".
# - conf_matrix[1, 1] is True Positive (TP): Model predicts "straight" and the actual value is "straight".

# Calculate True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN)
TP = conf_matrix[1][1]
TN = conf_matrix[0][0]
FP = conf_matrix[0][1]
FN = conf_matrix[1][0]

# Precision: Percentage of true positives among all positive predictions
precision = TP / (TP + FP)

# Recall (Sensitivity): Percentage of true positives among all actual positives
recall = TP / (TP + FN)

# Specificity: Percentage of true negatives among all actual negatives
specificity = TN / (TN + FP)

# Sensitivity: Same as recall, percentage of true positives among all actual positives
sensitivity = recall

# Print the calculated metrics
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Sensitivity: {sensitivity:.2f}')

#back percent correct
def calculate_percentage(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate percentage
    percentage = (num_correct / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage, 2)

    return percentage_rounded

# Example usage
numbackcorrect = 20  # Number of correct back answers
totalback = 20  # Total number of back questions

# Calculate the percentage of back correct
percentbackcorrect = calculate_percentage(numbackcorrect, totalback)

# Print the calculated percentage
print(f"Percentage Back correct: {percentbackcorrect}%")

#back percent incorrect:

def calculate_percentage_incorrect(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate the number of incorrect answers
    num_incorrect = total - num_correct

    # Calculate percentage of incorrect answers
    percentage_incorrect = (num_incorrect / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage_incorrect, 2)

    return percentage_rounded

# Example usage
numbackcorrect = 10
totalback = 10

# Calculate the percentage of incorrect answers for back
percentbackincorrect = calculate_percentage_incorrect(numbackcorrect, totalback)
print(f"Percentage Back incorrect: {percentbackincorrect}%")

#hands confusion
from sklearn.metrics import confusion_matrix

# Sample data (replace with your model predictions and actual values)
# y_pred: Model predicted values (1 for not folded, 0 for folded)
# y_actual: Actual values (1 for not folded, 0 for folded)
y_pred = [0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
y_actual = [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_actual, y_pred)

# Print confusion matrix
print('Confusion Matrix:')
print(conf_matrix)

# Optionally, label the confusion matrix for clarity
import pandas as pd

labels = ['Folded', 'Not Folded']
conf_matrix_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
print(conf_matrix_df)

# Interpretation:
# - conf_matrix[0, 0] is True Negative (TN): Model predicts "folded" and the actual value is "folded".
# - conf_matrix[0, 1] is False Positive (FP): Model predicts "not folded" but the actual value is "folded".
# - conf_matrix[1, 0] is False Negative (FN): Model predicts "folded" but the actual value is "not folded".
# - conf_matrix[1, 1] is True Positive (TP): Model predicts "not folded" and the actual value is "not folded".

# Calculate True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN)
TP = conf_matrix[1][1]
TN = conf_matrix[0][0]
FP = conf_matrix[0][1]
FN = conf_matrix[1][0]

# Precision: Percentage of true positives among all positive predictions
precision = TP / (TP + FP)

# Recall (Sensitivity): Percentage of true positives among all actual positives
recall = TP / (TP + FN)

# Specificity: Percentage of true negatives among all actual negatives
specificity = TN / (TN + FP)

# Sensitivity: Same as recall, percentage of true positives among all actual positives
sensitivity = recall

# Print the calculated metrics
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Sensitivity: {sensitivity:.2f}')

#percent hands correct
def calculate_percentage(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate percentage
    percentage = (num_correct / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage, 2)

    return percentage_rounded

# Example usage
numhandscorrect = 17  # Number of correct hands answers
totalhands = 20  # Total number of hands questions

# Calculate the percentage of hands correct
percenthandscorrect = calculate_percentage(numhandscorrect, totalhands)

# Print the calculated percentage
print(f"Percentage Hands correct: {percenthandscorrect}%")

#Percent hands incorrect:

def calculate_percentage_incorrect(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate the number of incorrect answers
    num_incorrect = total - num_correct

    # Calculate percentage of incorrect answers
    percentage_incorrect = (num_incorrect / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage_incorrect, 2)

    return percentage_rounded

# Example usage
numhandscorrect = 17
totalhands = 20

# Calculate the percentage of incorrect answers for hands
percenthandsincorrect = calculate_percentage_incorrect(numhandscorrect, totalhands)
print(f"Percentage Hands incorrect: {percenthandsincorrect}%")

#neck confusion
from sklearn.metrics import confusion_matrix
import pandas as pd

# Sample data (replace with your model predictions and actual values)
# y_pred: Model predicted values (1 for straight, 0 for hunched/reclined)
# y_actual: Actual values (1 for straight, 0 for hunched/reclined)
y_pred = [0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
y_actual = [0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]

# Calculate confusion matrix
conf_matrix = confusion_matrix(y_actual, y_pred)

# Print confusion matrix
print('Confusion Matrix:')
print(conf_matrix)

# Optionally, label the confusion matrix for clarity
labels = ['Foward/Backward', 'Straight']
conf_matrix_df = pd.DataFrame(conf_matrix, index=labels, columns=labels)
print(conf_matrix_df)

# Interpretation:
# - conf_matrix[0, 0] is True Negative (TN): Model predicts "forward" or "backward" and the actual value is "forward" or "baclward".
# - conf_matrix[0, 1] is False Positive (FP): Model predicts "straight" but the actual value is "forward" or "backward".
# - conf_matrix[1, 0] is False Negative (FN): Model predicts "forward" or "backward" but the actual value is "straight".
# - conf_matrix[1, 1] is True Positive (TP): Model predicts "straight" and the actual value is "straight".

# Calculate True Positives (TP), True Negatives (TN), False Positives (FP), False Negatives (FN)
TP = conf_matrix[1][1]
TN = conf_matrix[0][0]
FP = conf_matrix[0][1]
FN = conf_matrix[1][0]

# Precision: Percentage of true positives among all positive predictions
precision = TP / (TP + FP)

# Recall (Sensitivity): Percentage of true positives among all actual positives
recall = TP / (TP + FN)

# Specificity: Percentage of true negatives among all actual negatives
specificity = TN / (TN + FP)

# Sensitivity: Same as recall, percentage of true positives among all actual positives
sensitivity = recall

# Print the calculated metrics
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'Specificity: {specificity:.2f}')
print(f'Sensitivity: {sensitivity:.2f}')

#percent neck correct
def calculate_percentage(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate percentage
    percentage = (num_correct / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage, 2)

    return percentage_rounded

# Example usage
numneckcorrect = 18  # Number of correct neck answers
totalneck = 20  # Total number of neck questions

# Calculate the percentage of neck correct
percentneckcorrect = calculate_percentage(numneckcorrect, totalneck)

# Print the calculated percentage
print(f"Percentage Neck correct: {percentneckcorrect}%")

#Percent neck incorrect:

def calculate_percentage_incorrect(num_correct, total):
    # Validate inputs
    if total == 0:
        raise ValueError("Total cannot be zero.")
    if num_correct < 0 or total < 0:
        raise ValueError("Numbers must be non-negative.")
    if num_correct > total:
        raise ValueError("Number of correct answers cannot be greater than total questions.")

    # Calculate the number of incorrect answers
    num_incorrect = total - num_correct

    # Calculate percentage of incorrect answers
    percentage_incorrect = (num_incorrect / total) * 100

    # Round the percentage to 2 decimal places
    percentage_rounded = round(percentage_incorrect, 2)

    return percentage_rounded

# Example usage
numneckcorrect = 18
totalneck = 20

# Calculate the percentage of incorrect answers for hands
percentneckincorrect = calculate_percentage_incorrect(numneckcorrect, totalneck)
print(f"Percentage Neck incorrect: {percentneckincorrect}%")