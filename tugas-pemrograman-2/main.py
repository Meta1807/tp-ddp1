from modules.functions.highscore import get_highscore_or_create, check_highscore
from modules.functions.song import get_song
from modules.functions.start_game import start_game
from modules.functions.start_round import start_round
from modules.functions.clear_screen import clear_screen
from modules.classes_.GameData import GameData

clear_screen()

with get_highscore_or_create('read') as f:
    f.close()  # Check if highscore.txt exists


def main():
    data = GameData(start_game())  # Initialize GameData class with data from start_game()

    while True:
        if data.player.health > 0 and data.player.match_round != 6:  # Check if player is still alive/is not at round 5
            song = get_song(data)
            start_round(song, data.player)
        else:
            highscores = get_highscore_or_create('read').readlines()  # Get highscores from file
            
            check = check_highscore(data, highscores)  # Execute highscore check function

            if data.player.health == 0:  # Print death screen if player loses before round 5
                print('GAME OVER')
                print(f'Sayang sekali {data.player.username}, anda terhenti disini')
                print('Hasil Akhir:')
                print(f'Score: {data.player.score}\n')

            elif data.player.match_round == 6:  # Print congratulations screen if player reaches round 5
                print('SELAMAT!')
                print('Anda berhasil menyelesaikan permainan')
                print('Hasil Akhir:')
                print(f'Score: {data.player.score}\n')

            if check == True:  # check_highscore returns True if user highscore is higher, hence we check for it using an if statement
                print('NEW HIGHSCORE!!!')
                print(f'{"Username":<9}: {data.player.username}')
                print(f'{"Score":<9}: {data.player.score}')
                print(f'Berhasil meraih highscore {data.player.mode.capitalize()}!')
            
            print('~'*10 + ' Thanks for playing the game!', '~'*10)
            input('Press enter to exit the program...')
            
            break

if __name__ == '__main__':
    main()

""" 
TODO: 
- Implementasi program tebak-tebakan [v]
- Implementasi perhitungan skor [v]
- Implementasi game over saat kesempatan habis  [v]
- Update highscore.txt saat diperlukan [v]
- Manfaatkan ketiga fungsi yang sudah tersedia dengan sebaik-baiknya [v]
- Jangan lupa close file highscore.txt yang sudah dibuka!! [v]
"""
