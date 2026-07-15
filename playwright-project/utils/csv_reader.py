import csv


def read_csv(file_path):

    data = []

    with open(file_path, newline="") as file:

        reader = csv.reader(file)

        next(reader)  # Skip header row

        for row in reader:
            data.append(tuple(row))

    return data