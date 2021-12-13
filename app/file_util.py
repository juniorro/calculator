import pandas as pd
import csv
    
def get_csv_data(filename):
    data = pd.read_csv("data/" + filename)
    return data.values

def get_log_file_write(data):
    with open("data/operation.csv", 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow([data])
        csv.writer(csvfile)
        csvfile.close()
         
def write_to_file(dataframe):
    df = pd.DataFrame(dataframe, columns = ['first_number', 'second_number', 'operation', 'result'])
    df.to_csv(r"data/operation.csv", mode = 'a', header = False, index = False)

# data = get_csv_data("operation.csv")
# write_to_file(data)

# thedata = tuple(data)
# for n in thedata:
    # print(n)
# get_log_file_write("addition_test.log", str(get_time()) + ",addition_test.py," + str(random.randint(10, 1000)) + ",addition," + str(addition.get_result()))
