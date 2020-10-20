import os, random
from ..classes_.Player import Player

# Fungsi di bawah dimanfaatkan untuk memulai permainan. 
# Mengembalikan tuple (string, string, int, int, list)
#     string pemain - nama pemain yang dijamin sudah valid
#     string mode   - Game Mode yang dipilih pemain
#     int score     - skor awal pemain, mulai dari 0
#     int nyawa     - kesempatan bermain pemain, tergantung Game Mode yang dipilih
#     list lagu     - list berisi semua nama file dalam folder lagu

def start_game():
    print("""
  _                                      
 | |__   ___ _ __ _ __   __ _  ___ _   _ 
 | '_ \ / _ \ '__| '_ \ / _` |/ __| | | |
 | |_) |  __/ |  | |_) | (_| | (__| |_| |
 |_.__/ \___|_|  | .__/ \__,_|\___|\__,_|
                 |_|                DALAM
  ██╗      ██╗ ██████╗  ██╗ ██╗  ██╗
  ██║      ██║ ██╔══██╗ ██║ ██║ ██╔╝
  ██║      ██║ ██████╔╝ ██║ █████╔╝ 
  ██║      ██║ ██╔══██╗ ██║ ██╔═██╗ 
  ███████╗ ██║ ██║  ██║ ██║ ██║  ██╗
  ╚══════╝ ╚═╝ ╚═╝  ╚═╝ ╚═╝ ╚═╝  ╚═╝                              
  """)
    print("~"*50)

    pemain = str()
    mode = str()
    lagu =  os.listdir("lagu")   

    while pemain == 'null' or pemain == '':
        pemain = input("Masukkan username: ")
    while mode.lower() not in ['normal', 'expert']:
        mode = input("Mode (Normal/Expert): ")

    player = Player({'username': pemain})
    player.set_mode(mode)

    print("~"*50)
    print("Good Luck & Have Fun :)\n")

    return {'player': player, 'lagu': lagu}