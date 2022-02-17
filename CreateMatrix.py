import numpy as np
import pandas as pd

def initialize_with_ones(connections_file):
    matrix_dim = 6012
    big_matrix=np.zeros((matrix_dim, matrix_dim))
    
    for line in connections_file.readlines():
        chunks = line.split(' ')
        first_index = int(chunks[0]) - 1
        second_str = chunks[1]
        second_index = int(second_str) - 1#int(second_str[0:len(second_str)-1])
        big_matrix[first_index, second_index] = 1

    return big_matrix

def change_rows(big_dataframe):
    for i in range(big_dataframe.shape[0]):
        num_row_entries = sum(big_dataframe.iloc[i])
        if(num_row_entries != 0):
            big_dataframe.iloc[i] = big_dataframe.iloc[i]/num_row_entries

    return big_dataframe


if __name__ == "__main__":
    connections_file = open("connections.dat")
    big_matrix = initialize_with_ones(connections_file)
    final_matrix = change_rows(pd.DataFrame(big_matrix))
    final_matrix.to_csv("transition_matrix.csv", header=False, index=False)
