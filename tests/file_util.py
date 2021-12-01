import pandas as pd
import csv
    
def get_csv_data(filename):
    data = pd.read_csv("data/testfiles/" + filename)
    return data.values

def get_log_file_write(filename):
    with open("data/log/" + filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["first", "second", "result"])
        return csv.writer(csvfile)