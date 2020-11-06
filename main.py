# Apa yang dibutuhkan dalam game ?
# 1. board
# 2. menampilkan board game nya
# 3. Logic waktu bermain game
# 4. fungsi mengecek kondisi menang, seri, kalah
  # cek horizontal
  # cek vertikal
  # cek diagonal
# 5. flip players (mengganti giliran player)

# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# menampilkan board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print("----------")
  print(board[3] + " | " + board[4] + " | " + board[5])
  print("----------")
  print(board[6] + " | " + board[7] + " | " + board[8])

# fungsi untuk giliran bermain
def handle_turn(curr_player):
  print("Giliran player " + curr_player)
  position = input("Pilih posisi dari 1-9: ")
  # ubah ke int
  position = int(position) - 1 # karena indeks mulai dari 0

  board[position] = curr_player
  display_board()

# mengecek siapa yang harus bermain
def cek_curr_player():
  player_X = board.count("X")
  player_O = board.count("O")
  
  if player_X == player_O:
    return "X"
  else:
    return "O"

def check_if_win():
  winner = None
  # cek horizontal
  i_horizontal = (0,3,6)
  i_vertical = (0,1,2)

  for i in i_horizontal:
    if board[i] == board[i+1] and board[i+1] == board[i+2] and board[i] != "-":
      winner = board[i]
      print("game selesai pemenangnya player " + winner)
      return True
  
  for i in i_vertical:
    if board[i] == board[i+3] and board[i+3] == board[i+6] and board[i] != "-":
      winner = board[i]
      print("game selesai pemenangnya player " + winner)
      return True

  # diagonal
  if board[0] == board[4] and board[4] == board[8] and board[0] != "-":
    winner = board[0]
    print("game selesai pemenangnya player " + winner)
    return True

  if board[2] == board[4] and board[4] == board[6] and board[2] != "-":
    winner = board[2]
    print("game selesai pemenangnya player " + winner)
    return True
  return False

def check_if_tie():
  x = "-"
  if x not in board and not check_if_win():
    print("Permainan berakhir dengan seri")
    return True

# mengecek apakah permainan sudah selesai
def check_if_game_over():
  if check_if_win():
    return False
  elif check_if_tie():
    return False
  else:
    return True


# fungsi permainan games
def play_game():

  print("permainan dimulai dari player X")

  # awal permainan
  display_board()
  # awal mulai game harus berjalan
  game_still_going = True

  while game_still_going:
    curr_player = cek_curr_player()
    handle_turn(curr_player)

    # cek apakah permainan sudah selesai
    game_still_going = check_if_game_over()

play_game()