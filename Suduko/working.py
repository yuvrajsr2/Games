board = [
    []
]


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 and i != 0:
            print("- - - - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print("  | ", end="")

                if j == 0:
                    print(bo)
