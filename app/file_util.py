import pandas as pd
import csv
    
def get_csv_data(filename):
    data = pd.read_csv("data/" + filename)
    return data.values

def write_to_file(dataframe):
    df = pd.DataFrame(dataframe, columns = ['first_number', 'second_number', 'operation', 'result'])
    df.to_csv(r"data/operation.csv", mode = 'a', header = False, index = False)
