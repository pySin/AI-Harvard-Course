import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4

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
    # o_file = open("test.txt", "w")
    # o_file.write(f"Sensitivity: {sensitivity} \nSpecificity: {specificity}")

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
        - ProductRelated_Duration, a floating point number / 5
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number / 9
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

    month_indexes = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    }

    evidence = []
    labels = []

    with open(filename) as f:
        read_data = csv.reader(f)
        next(read_data)
        o_file = open("test.txt", "w")
        t_text = next(read_data)

        for visit_data in read_data:
            evidence_row = [
                int(visit_data[0]),
                float(visit_data[1]),
                int(visit_data[2]),
                float(visit_data[3]),
                int(visit_data[4]),
                float(visit_data[5]),
                float(visit_data[6]),
                float(visit_data[7]),
                float(visit_data[8]),
                float(visit_data[9]),
                month_indexes[visit_data[10]],
                int(visit_data[11]),
                int(visit_data[12]),
                int(visit_data[13]),
                int(visit_data[14]),
                1 if visit_data[15] == "Returning_Visitor" else 0,
                0 if visit_data[16] == "FALSE" else 1
            ]

            evidence.append(evidence_row)
            labels.append(visit_data[-1])

    return evidence, labels


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    model = KNeighborsClassifier(n_neighbors=1)
    return model.fit(evidence, labels)


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
    # o_file = open("test.txt", "w")
    # o_file.write(str(labels) + "\n" + str(predictions))

    sensitivity = []
    specificity = []

    for i in range(len(labels)):
        if labels[i] == "TRUE":
            if labels[i] == predictions[i]:
                sensitivity.append(1)
            else:
                sensitivity.append(0)
        else:
            if labels[i] == predictions[i]:
                specificity.append(1)
            else:
                specificity.append(0)


    return sum(sensitivity) / len(sensitivity), sum(specificity) / len(specificity)


if __name__ == "__main__":
    main()
