def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row
