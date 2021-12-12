import pandas as pd
import csv
    
def get_csv_data(filename):
    data = pd.read_csv("data/testfiles/" + filename)
    return data.values

def get_log_file_write(filename, data):
    with open("data/log/" + filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["timestamp", "filename", "record_number", "operation", "result"])
        csvwriter.writerow([data])
        csv.writer(csvfile)
        csvfile.close()

data = get_csv_data("addition.csv")
mynumbers = (tuple(data[0])[0], tuple(data[0])[1])
mynum = data[0]
# print(mynum)
thedata = tuple(data)
for n in thedata:
    print(n)
# get_log_file_write("addition_test.log", str(get_time()) + ",addition_test.py," + str(random.randint(10, 1000)) + ",addition," + str(addition.get_result()))
