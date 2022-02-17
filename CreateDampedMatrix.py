import numpy as np
import pandas as pd


matrix_dim = 6012

def initialize_with_ones(connections_file):
    big_matrix=np.zeros((matrix_dim, matrix_dim))
    
    for line in connections_file.readlines():
        chunks = line.split(' ')
        first_index = int(chunks[0]) - 1
        second_str = chunks[1]
        second_index = int(second_str) - 1
        big_matrix[first_index, second_index] = 1

    return big_matrix

def change_rows(big_dataframe):
    for i in range(big_dataframe.shape[0]):
        num_row_entries = sum(big_dataframe.iloc[i])
        if(num_row_entries != 0):
            big_dataframe.iloc[i] = big_dataframe.iloc[i]/num_row_entries

    return big_dataframe


def add_damping(final_matrix, damping_coefficient):
    all_ones = np.ones((matrix_dim, matrix_dim))
    reduced_coefficient_matrix = (damping_coefficient * final_matrix).to_numpy()
    damping_matrix = (pd.DataFrame(all_ones) * ((1 - damping_coefficient) / matrix_dim)).to_numpy()
    return pd.DataFrame(np.add(reduced_coefficient_matrix, damping_matrix))


if __name__ == "__main__":
    damping_coefficient = .75
    connections_file = open("connections.dat")
    big_matrix = initialize_with_ones(connections_file)
    final_matrix = change_rows(pd.DataFrame(big_matrix))
    moded_final_matrix = add_damping(final_matrix, damping_coefficient)
    moded_final_matrix.to_csv("damped_transition_matrix.csv", header=False, index=False)
