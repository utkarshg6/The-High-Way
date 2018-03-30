"""
Smart Version 1.0 ::
    ---------------------IT IS UNBEATABLE--------------------------
    1) It won't allow you to win if you have successfully formed two blocks.
                X _ _
                _ X _
                _ _ O

                X _ _
                X _ _
                O _ _

                X X O
                _ _ _
                _ _ _


    2) It will win if it has alerady made two blocks.
                O _ _
                _ O _
                _ _ O

                O _ _
                O _ _
                O _ _

                O O O
                _ _ _
                _ _ _

    
    3) It will Choose Corner Or Middle Element if it's your first try.
                _ _ O
                _ X _
                _ _ _

                X _ _
                _ O _
                X _ _

                _ _ X
                _ O _
                _ _ _

                _ _ _
                _ O _
                X _ _

                _ _ _
                _ O _
                _ _ X

    4) If You try to act innocent, and select a non-middle element. Then computer will act brutally and will select middle element.
                _ _ X
                _ O _
                _ X O
"""




import random

def check(matrix):
    for i in range(3):
        if ( matrix[i][0] == matrix[i][1] == matrix[i][2] ):
            return( matrix[i][0] )
        if ( matrix[0][i] == matrix[1][i] == matrix[2][i] ):
            return( matrix[0][i] )
    if ( matrix[0][0] == matrix[1][1] == matrix[2][2] ):
        return( matrix[0][0] )
    if ( matrix[0][2] == matrix[1][1] == matrix[2][0] ):
        return( matrix[0][2] )
    return(2)

def insertPlayer(matrix):
    print(name,":",end = "")
    choice = int( input() )
    r = (choice-1) // 3
    c = (choice-1) % 3
    if ( matrix[r][c] == "_" and choice >= 1 and choice <= 9 ):
        matrix[r][c] = 1
    else:
        print("Invalid Choice")
        insertPlayer(matrix)

def convert( ch ):
    r = (ch-1) // 3
    c = (ch-1) % 3
    return( r, c )

def insertComputer(matrix):
    insert = 0
    # Computer Checks whether you or it could be the winner?
    
    
    # Diagonals -->
    if ( insert == 0 ):
        if ( matrix[0][0] == matrix[2][2] == 0 and matrix[1][1] == "_" ):   # Back Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[0][2] == matrix[2][0] == 0  and matrix[1][1] == "_" ):   # Front Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        if ( matrix[0][0] == matrix[1][1] == 0 and matrix[2][2] == "_" ):   # Back Diagonal
            matrix[2][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][2] == 0 and matrix[0][0] == "_" ):
            matrix[0][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        
        if ( matrix[0][2] == matrix[1][1] == 0 and matrix[2][0] == "_" ):   # Front Diagonal
            matrix[2][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][0] == 0 and matrix[0][2] == "_" ):
            matrix[0][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return


    # Horizontal -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[i][0] ==  matrix[i][1] == 0  and  matrix[i][2] == "_"  ):  # X X O , axis = 0
                matrix[i][2] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][1] ==  matrix[i][2] == 0  and  matrix[i][0] == "_"  ):  # O X X , axis = 0
                matrix[i][0] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][2] ==  matrix[i][0] == 0  and  matrix[i][1] == "_"  ):  # X O X , axis = 0
                matrix[i][1] = 0
                insert = 1
                print("Computer Acted Smartly")
                return


    # Vertical -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[0][i] ==  matrix[1][i] == 0  and  matrix[2][i] == "_"  ):   # X X O , axis = 1
                matrix[2][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[1][i] ==  matrix[2][i] == 0  and  matrix[0][i] == "_"  ):   # O X X , axis = 1
                matrix[0][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[2][i] ==  matrix[0][i] == 0  and  matrix[1][i] == "_"  ):   # X O X , axis = 1
                matrix[1][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return



    # Diagonals -->
    if ( insert == 0 ):
        if ( matrix[0][0] == matrix[2][2] == 1 and matrix[1][1] == "_" ):   # Back Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[0][2] == matrix[2][0] == 1 and matrix[1][1] == "_" ):   # Front Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        if ( matrix[0][0] == matrix[1][1] == 1 and matrix[2][2] == "_" ):   # Back Diagonal
            matrix[2][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][2] == 1 and matrix[0][0] == "_" ):
            matrix[0][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        
        if ( matrix[0][2] == matrix[1][1] == 1 and matrix[2][0] == "_" ):   # Front Diagonal
            matrix[2][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][0] == 1 and matrix[0][2] == "_" ):
            matrix[0][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return


    # Horizontal -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[i][0] ==  matrix[i][1] == 1  and  matrix[i][2] == "_"  ):  # X X O , axis = 0
                matrix[i][2] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][1] ==  matrix[i][2] == 1  and  matrix[i][0] == "_"  ):  # O X X , axis = 0
                matrix[i][0] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][2] ==  matrix[i][0] == 1  and  matrix[i][1] == "_"  ):  # X O X , axis = 0
                matrix[i][1] = 0
                insert = 1
                print("Computer Acted Smartly")
                return


    # Vertical -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[0][i] ==  matrix[1][i] == 1  and  matrix[2][i] == "_"  ):   # X X O , axis = 1
                matrix[2][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[1][i] ==  matrix[2][i] == 1  and  matrix[0][i] == "_"  ):   # O X X , axis = 1
                matrix[0][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[2][i] ==  matrix[0][i] == 1  and  matrix[1][i] == "_"  ):   # X O X , axis = 1
                matrix[1][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return


    # Diagonals -->
    if ( insert == 0 ):
        if ( matrix[0][0] == matrix[2][2] and matrix[1][1] == "_" ):   # Back Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[0][2] == matrix[2][0] and matrix[1][1] == "_" ):   # Front Diagonal -- Middle Only
            matrix[1][1] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        if ( matrix[0][0] == matrix[1][1] and matrix[2][2] == "_" ):   # Back Diagonal
            matrix[2][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][2] and matrix[0][0] == "_" ):
            matrix[0][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return

        
        if ( matrix[0][2] == matrix[1][1] and matrix[2][0] == "_" ):   # Front Diagonal
            matrix[2][0] = 0
            insert = 1
            print("Computer Acted Smartly")
            return
        if ( matrix[1][1] == matrix[2][0] and matrix[0][2] == "_" ):
            matrix[0][2] = 0
            insert = 1
            print("Computer Acted Smartly")
            return


    # Horizontal -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[i][0] ==  matrix[i][1]  and  matrix[i][2] == "_"  ):  # X X O , axis = 0
                matrix[i][2] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][1] ==  matrix[i][2]  and  matrix[i][0] == "_"  ):  # O X X , axis = 0
                matrix[i][0] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[i][2] ==  matrix[i][0]  and  matrix[i][1] == "_"  ):  # X O X , axis = 0
                matrix[i][1] = 0
                insert = 1
                print("Computer Acted Smartly")
                return


    # Vertical -->
    if ( insert == 0 ):
        for i in range(3):
            if (  matrix[0][i] ==  matrix[1][i]  and  matrix[2][i] == "_"  ):   # X X O , axis = 1
                matrix[2][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[1][i] ==  matrix[2][i]  and  matrix[0][i] == "_"  ):   # O X X , axis = 1
                matrix[0][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return
            if (  matrix[2][i] ==  matrix[0][i]  and  matrix[1][i] == "_"  ):   # X O X , axis = 1
                matrix[1][i] = 0
                insert = 1
                print("Computer Acted Smartly")
                return










    # Play Random -->
    while ( insert == 0 ):
        choice = random.randint(1,9)
        r = (choice-1) // 3
        c = (choice-1) % 3
        if ( matrix[r][c] == "_" ):
            matrix[r][c] = 0
            insert = 1



def display(matrix):
    print()
    for i in range(3):
        for j in range(3):
            if ( matrix[i][j] == 1 ):
                print( "X", end=" " )
            elif ( matrix[i][j] == 0 ):
                print( "O", end=" " )
            else:
                print( "_", end=" " )
        print()
    print()
    
def print_details():
    print("Welcome to Tic Tac Toe".center( 50, " " ))
    print("\n\n\nPlease Enter the Choice According to the given Board.")
    for i in range(1,10):
        print( i, end = " ")
        if ( i%3 == 0 ):
            print()


if __name__ == "__main__":
    print_details()
    name = input("Enter Your Name : ")
    matrix = [ [ '_' for x in range(3) ] for y in range(3) ]
    display(matrix)
    draw = 1
    for i in range(9):
        if ( i%2 == 0 ):
            insertPlayer(matrix)
        else:
            insertComputer(matrix)
        display(matrix)
        t = check(matrix)
        if ( t == 0 ):
            print("Computer Wins.")
            draw = 0
            break
        if ( t == 1 ):
            print(name, "Wins.")
            draw = 0
            break
    if ( draw == 1 ):
        print("Match is Draw.")
