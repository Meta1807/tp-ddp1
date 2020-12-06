import random

def start_round(lagu: list, player):
    ''' This function initializes a new round using the data from the given arguments. 
        
        [ARGUMENTS]
        - lagu: list
        - player: Player()

        [DESCRIPTION]
        When called this program initializes a new round using the given song and player data.
        First, it randomly selects 4 lines (first 4 lines not included) of the song and prints them
        into the console.
        
        Afterwards the program will ask the user to guess the continuation of the song lyrics. It does this
        by comparing the user's guess with the line after the selected lyrics. If the player guesses correctly,
        it will increment the Player object's score attribute by 1. Otherwise, if the player guesses incorrectly
        it will call the player.damage() method to decrement the player's health.
    
    '''
    random_lyric = random.randint(0, len(lagu[1]) - 5)

    # Print Player object round details
    round_msg = (
        f"{'~' * 50}\n"
        f"Round {player.match_round:02}\n"
        f"{'HP':<6}: {player.health}\n"
        f"{'Score':<6}: {player.score}\n"
        f"{'~' * 50}\n"
        f'Judul Lagu : {lagu[0]}\n'
    )

    print(round_msg)

    # Print 4 lines of lyrics based on a random index
    for i in range(random_lyric, random_lyric + 4):
        print(lagu[1][i].strip())

    # The expected answer is the index after the 4 printed lyrics
    correct_answer = lagu[1][random_lyric + 4].strip()
    user_answer = input('Silahkan menebak:\n')

    # Increment score by 1 if user's input is correct (case insensitive)
    if user_answer.lower() == correct_answer.lower():
        print('Jawaban BENAR\n')
        player.score += len(correct_answer)
    else:
        print('Jawaban SALAH\n')
        print(f'Jawaban: {correct_answer}')
        player.damage()

    player.match_round += 1