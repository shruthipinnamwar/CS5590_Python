# heightinp= int(input("Enter the height of the board: "))
# widthinp= int(input("Enter the width of the board: "))
# matrix = [[1 for x in range(heightinp)] for y in range(widthinp)]
# print(matrix) # for testing purposes
#
#
#
# for heightinp:
#     print("|"*heightinp)
#
#
# # for x in matrix:
# #     s = "|"
# #     for y in x:
# #         s += str(y) + " "
# #
# #     print (s[:-1] + "|" ) # gets rid of the last space in the row
#
# # print("-" * (heightinp) )
# #
# # for x in matrix:
# #
# #     print ("|"+"_"+"|" * heightinp)
# #
# # for y in matrix:
# #     print ("|"+"_"+"|" * heightinp)
# # # print ("-" * (widthinp) + "-")
# # # print ("")




def horizontal_line ( size ):
    return " ---" * size + " \n"

def vertical_lines ( widthinp ):
    return "|   " * size + "|\n"

def gameboard ( size ):
    board = """"""
    for i in range(size):
        board += horizontal_line(size)
        board += vertical_lines(widthinp)
    board += horizontal_line(size)
    return board

# if __name__ == "__main__":

size = int(input("Enter the height of the board: "))
widthinp = int(input("Enter the width of the board: "))

print(gameboard(size))




