import csv

def read_csv(file):
    with open(file, mode="r", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        result = list(csv_reader)
    return result


def write_csv(file, data):
    with open(file, mode="w", newline='') as csv_file:
        if len(data) == 0:
            return
        header_names = [key for key in data[0].keys()]
        writer = csv.DictWriter(csv_file, fieldnames=header_names)
        writer.writeheader()
        for key in data:
            writer.writerow(key)
