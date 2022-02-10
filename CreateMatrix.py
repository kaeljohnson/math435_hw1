import numpy as np

def initialize_with_ones(connections_file):
    big_matrix=np.empty((6012, 6012))
    
    for line in connections_file.readlines():
        chunks = line.split(' ')
        first_index = int(chunks[0])
        second_str = chunks[1]
        second_index = int(second_str[0:len(second_str)-1])
        big_matrix[first_index, second_index] = 1

    return big_matrix

if __name__ == "__main__":
    connections_file = open("connections.dat")
    big_matrix = initialize_with_ones(connections_file)
    final_matrix = change_rows(pd.DataFrame(big_matrix))
    final_matrix.to_csv("transition_matrix.csv")
