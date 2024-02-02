# python3 shopping.py shopping.csv
import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

month = {
    'Jan': 0,
    'Feb': 1,
    'Mar': 2,
    'Apr': 3,
    'May': 4,
    'June': 5,
    'Jul': 6,
    'Aug': 7,
    'Sep': 8,
    'Oct': 9,
    'Nov': 10,
    'Dec': 11,
}


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    evidence = []
    labels = []

    with open(filename, 'r') as file:
        reader = csv.reader(file)

        # skip header (names of cols)
        next(reader) 

        for line in reader:
            row = [
                int(line[0]), # Administrative
                float(line[1]), # Administrative_Duration
                int(line[2]), # Informational
                float(line[3]), # Informational_Duration
                int(line[4]), # ProductRelated
            ]
            for i in range(5, 10):
                row.append(float(line[i])) # ProductRelated_Duration, BounceRates, ExitRates, PageValues, SpecialDay
            row.append(month[line[10]]) # Month
            for i in range(11, 15):
                row.append(int(line[i]))  # OperatingSystems, Browser, Region, TrafficType
            
            # VisitorType
            row.append(1 if line[15] == "Returning_Visitor" else 0) 
            # Weekend
            row.append(1 if line[16] == "TRUE" else 0) 
            # Revenue AKA bought or not
            labels.append(1 if line[17] == "TRUE" else 0) 

            evidence.append(row)
    
    return (evidence, labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(evidence, labels)
    return model


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    
    positive = 0
    negative = 0
    true_positive = 0
    true_negative = 0

    for label in labels:
        positive += label == 1
        negative += label == 0

    for i, prediction in enumerate(predictions):
        true_positive += prediction == labels[i] == 1
        true_negative += prediction == labels[i] == 0
    
    sensitivity = 0 if positive == 0 else true_positive / positive
    specificity = 0 if negative == 0 else true_negative / negative
    
    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
