class Start_game:
    def __init__(self):
        self.board = ["0","1","2","3","4","5","6","7","8"]
        self.empty = [0,1,2,3,4,5,6,7,8]
        self.winning_combinations = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]

    def game_board(self, board):
        print("{} | {} | {} ".format(board[0], board[1], board[2]))
        print("-------------")
        print("{}  |  {}  |  {} ".format(board[3], board[4], board[5]))
        print("-------------")
        print("{}  |  {}  |  {} ".format(board[6], board[7], board[8]))

    def player_input(self, player, board):
        symbol = ['X', 'O']
        correct_input = True

        position = int(
            input('player {playerNo}, choose field for {symbol}\n'.format(playerNo=player + 1, symbol=symbol[player])))

        if board[position] =='X' or board[position] =='O':
            correct_input = False

        if not correct_input:
            print("Position taken!!!")
            self.game_board(board)
            self.player_input(player, board)
        else:
            self.empty.remove(position)
            board[position] = symbol[player]
            return 1

    def win(self, board):
        for check in self.winning_combinations:
            won = True

            if board[check[0]] == board[check[1]] == board[check[2]] == 'X':
                self.game_board(board)
                print("X wins!!!")
                self.play_again()

            elif board[check[0]] == board[check[1]] == board[check[2]] == 'O':
                self.game_board(board)
                print("O wins!!!")
                self.play_again()
            else:
                won = False

        if won:
            return 0
        else:
            return 1

    def play_game(self):
        player = 0

        while self.empty and self.win(self.board):
            self.game_board(self.board)
            print("\n")
            self.player_input(player, self.board)
            player = int(not player)
        if not self.empty:
            self.game_board(self.board)
            print("It's a tie!!!!")
            self.play_again()

    def play_again(self):
        while True:
            repeat_game = input("Would you like to play again? (Y/N)").lower()
            if repeat_game[0] == "y":
                print("Setting up new game...Loading....")
                self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
                self.empty = [0, 1, 2, 3, 4, 5, 6, 7, 8]
                self.play_game()
            elif repeat_game[0] == "n":
                print("Thanks for playing!!!")
                quit()
            else:
                print("Please Choose again")
                self.play_again()