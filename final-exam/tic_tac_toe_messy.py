# Tic Tac Toe
# Reference: With modification from http://inventwithpython.com/chapter10.html.

# TODOs:
# 1. Find all TODO items and see whether you can improve the code.
#    In most cases (if not all), you can make them more readable/modular.
# 2. Add/fix function's docstrings (use """ insted of # for function's header
#    comments)

import random


def drawBoard(board):
    """
    This function prints out the board that it was passed.
    "board" is a list of 10 strings representing the board (ignore index 0)
    """
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def inputPlayerLetter():
    """
    Lets the player type which letter they want to be.
    Returns a list with the player’s letter as the first item, and the computer's letter as the second.
    """
    letter = ''
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    # the first element in the list is the player’s letter, the second is the computer's letter.
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']


def whoGoesFirst():
    """ Randomly choose the player who goes first. """
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'


def playAgain():
    """ This function returns True if the player wants to play again, otherwise it returns False. """
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    """
    Given a board and a player’s letter, this function returns True if that player has won.
    We use bo instead of board and le instead of letter so we don’t have to type as much.
    """
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
            # across the middle    # TODO: Fix the indentation of this lines and the following ones.
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
            # down the right side
            (bo[9] == le and bo[6] == le and bo[3] == le) or
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
            (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal


def getBoardCopy(board):
    """ Make a duplicate of the board list and return it the duplicate. """
    dupeBoard = []

    for i in range(0, len(board)):  # TODO: Clean this mess!
        dupeBoard.append(board[i])

    return dupeBoard


def isSpaceFree(board, move):
    """ Return true if the passed move is free on the passed board. """
    return board[move] == ' '


def getPlayerMove(board):
    """ Let the player type in their move. 
    """
    move = ' '  # TODO: W0621: Redefining name 'move' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
    """ I'm havinng issues understanding the problem with these 'redefine x from outer scope' problems, and the stackoverflow linked
    is more confusing than helpful here. This seems readable enough and any change I make is causing errors so i left the 3 TODO's of this nature alone."""
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, movesList):
    """ Returns a valid move from the passed list on the passed board.
    Returns None if there is no valid move. """
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    # TODO: How would you write this pythanically? (You can google for it!)
    if possibleMoves:
        return random.choice(possibleMoves)
    # else:  # TODO: is this 'else' necessary? No? I beleieve that leaving an if statement without else is the same a s returning none in this instance.
    #     return None


# TODO: W0621: Redefining name 'computerLetter' from outer scope. Hint: Fix it according to https://stackoverflow.com/a/25000042/81306
def getComputerMove(board, computerLetter):
    """ Given a board and the computer's letter, determine where to move and return that move. """
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # Here is our algorithm for our Tic Tac Toe AI:
    # First, check if we can win in the next move
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i

    # Check if the player could win on their next move, and block them.
    for i in range(1, 10):
        copy = getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i

    # Try to take one of the corners, if they are free.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    # TODO: Fix it (Hint: Comparisons to singletons like None should always be done with is or is not, never the equality/inequality operators.)
    if move is not None:
        return move

    # Try to take the center, if it is free.
    if isSpaceFree(board, 5):
        return 5

    # Move on one of the sides.
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """ Return True if every space on the board has been taken. Otherwise return False. """
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


def playGame():
    """start the game"""
    print('Welcome to Tic Tac Toe!')

    # TODO: The following mega code block is a huge hairy monster. Break it down
    # into smaller methods. Use TODO s and the comment above each section as a guide
    # for refactoring.
    BOARD_CONST = 10
    while True:
        # Reset the board
        # TODO: Refactor the magic number in this line (and all of the occurrences of 10 thare are conceptually the same.)
        theBoard = [' '] * BOARD_CONST
        playerLetter, computerLetter = inputPlayerLetter()
        turn = whoGoesFirst()
        print('The ' + turn + ' will go first.')
        # TODO: Study how this variable is used. Does it ring a bell? (which refactoring method?)
        # gameIsPlaying = True
        """ gameIsPlaying is a control flag, and we can remove that"""
        #       See whether you can get rid of this 'flag' variable. If so, remove it.

        # TODO: Usually (not always), loops (or their content) are good candidates to be extracted into their own function.
        while True:
            #       Use a meaningful name for the function you choose.
            if turn == 'player':
                # Player’s turn.
                drawBoard(theBoard)
                move = getPlayerMove(theBoard)
                makeMove(theBoard, playerLetter, move)

                if isWinner(theBoard, playerLetter):
                    drawBoard(theBoard)
                    print('Hooray! You have won the game!')
                    # gameIsPlaying = False
                    break
                else:  # TODO: is this 'else' necessary? yes, if removed, results in a error loop
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    # else:  # TODO: Is this 'else' necessary? no
                    turn = 'computer'

            else:
                # Computer’s turn.
                move = getComputerMove(theBoard, computerLetter)
                makeMove(theBoard, computerLetter, move)

                if isWinner(theBoard, computerLetter):
                    drawBoard(theBoard)
                    print('The computer has beaten you! You lose.')
                    # gameIsPlaying = False
                    break
                else:     # TODO: is this 'else' necessary? yes, if removed, results in a error loop
                    if isBoardFull(theBoard):
                        drawBoard(theBoard)
                        print('The game is a tie!')
                        break
                    # else:  # TODO: Is this 'else' necessary? no
                    turn = 'player'

        if not playAgain():
            break


if __name__ == "__main__":
    playGame()
