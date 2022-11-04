
def search(matrix, x):

    for i in range(len(matrix)):
        for j in range(len(matrix)):

            if (matrix[i][j] == x):
                print("Element found at (", i, ",", j, ")")
                return 1

    print("[-1, -1]")
    return 0

if __name__ == "__main__":
    matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

    search(matrix,44)