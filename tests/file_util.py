import pandas as pd
import csv
    
def get_csv_data(filename):
    data = pd.read_csv("data/testfiles/" + filename)
    return data.values

def get_log_file_write(filename, data):
    with open("data/log/" + filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["timestamp", "filename", "record_number", "operation", "result"])
        csvwriter.writerow(data)
        return csv.writer(csvfile)