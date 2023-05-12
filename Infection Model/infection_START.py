"""
    infection.py: A simple grid-model for simulating the spread of
    an infectious disease.

    <your name>
    Nathaniel Yee
    <date>
    May 16th 2023
    <notes>

"""

import numpy as np
import matplotlib.pyplot as plt
import random

def initialize_model(M, N, K):
    """ Create an NxN array of zeros. The first row contains some
    values set to 1 according to the probability parameter K (0.0...1.0)
    M = The # of days to simulate
    N - The # of students
    K - Probability that a value in the first row (i=0) is set to 1
    return - An initialized NxN numpy array
    """
    array = np.random.choice([0,1], size=(M, N), p=[1-K, K])
    pass   # a placeholder for a block of code you must write
    return array

def run_model(arr, R):
    """ Rows 1 to N-1 are computed. Disease is transmitted to
    each of your neighbors with probability R. (The next day
    they show up to class sick.  If a student is sitting next to
    two healthy students, they will be healthy the next day as well.
    Sick students become well the next day no matter what.
    arr - The array
    R - The infection transmission probability. (Only neighbors are at risk)
    return - None.  Array modified in place. """

    for i in range(1, arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i - 1, j] == 1:
                if j > 0 and random.random() < R:
                    arr[i, j - 1] = 1
                if j < arr.shape[1] - 1 and random.random() < R:
                    arr[i, j + 1] = 1
    pass

def display_model(arr):
    """
    Display data in our grid model
    arr - A 2D array
    return - None. Image saved to file
    """
    plt.imshow(arr, cmap='Greens')
    plt.title("Color Map of Infected Students")
    plt.xlabel("M Number of Days")
    plt.ylabel("N Number of Students")
    plt.show()
    plt.savefig('sicknessviz.png')
    pass
    
    
def main():
 
    # Define key parameters (N, M, R, K)
    N = 500
    M = 500
    K = .4
    R = .5
    '''
    Random Generation Case 
    K = random.random()
    R = random.random()
    '''
    # Initialize the model
    array = initialize_model(N, M, K)
    print(array)

    # Run the model
    run_model(array, R)

    # Display the result
    display_model(array)

if __name__ == "__main__":
    main()


