import csv


def read_text():
    notebook = {}
    with open('fileToHW7.csv') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            notebook[row[0]] = row[1:5]
    return notebook


def write_text(data):
    with open('fileToHW7.csv', 'a+', newline='') as f:
        data = list(data.split(' '))
        writer = csv.writer(f, delimiter=';')
        writer.writerow(data)


def search_tex(surname_people, dictionary):
    print(dictionary.get(surname_people))


def print_notebook(all_notebook):
    print(all_notebook.items())
