import os
# Fungsi di bawah memeriksa apakah file highscore.txt sudah ada di directory,
# serta mengembalikan file stream highscore.txt yang telah dibuka
# Parameter:
#     purpose 'read' / 'replace' - tujuan membuka file highscore.txt
# Mengembalikan file stream highscore.txt
def get_highscore_or_create(purpose: str) -> list: 
    hs = os.listdir()
    highscore = None
    # check if doesn't exist, then create default 
    if "highscore.txt" not in hs:
        highscore = open("highscore.txt", 'w')
        a = ["normal null 0\n", "expert null 0\n"]
        highscore.writelines(a)

    # opens highscore.txt in desired mode
    if purpose == 'read': 
        highscore = open("highscore.txt", 'r')
    else: 
        highscore = open("highscore.txt", 'w')
    return highscore


def check_highscore(data, highscores: list) -> bool:
    ''' Checks the user current score against the recorded highscore stored in a text file. 

        [ARGUMENTS]
        - data: GameObject()
        - highscores: list

        [DESCRIPTION]
        This function is used to check the user's current score against the highscore.txt file.
        It accomplishes this by splitting the corresponding line for the mode (index 0 for normal
        and index 1 for expert) and then getting the value of the highscore. Afterwards it compares
        the integer value of the previous highscore with the user's current score.

        If the program finds that the user's current score is greater than than the previous score,
        then it will update the data in highscore.txt before overwriting the data in highscore.txt
        with the updated scores.

        The program also returns a boolean of either True or False based on whether or not the user's
        new score is higher than the current highscore.
    
    '''
    if data.player.mode == 'expert':
        highscore = highscores[1].split(' ') # [expert, null, 0]
        if data.player.score > int(highscore[-1]):
            highscores[1] = f'expert {data.player.username} {data.player.score}'
            with get_highscore_or_create('write') as f:
                for item in highscores:
                    print(item, file=f)
            return True
        
    elif data.player.mode == 'normal':
        highscore = highscores[0].split(' ')
        if data.player.score > int(highscore[-1]):
            highscores[0] = f'normal {data.player.username} {data.player.score}'
            with get_highscore_or_create('write') as f:
                for item in highscores:
                    print(item, file=f)
            return True
    return False