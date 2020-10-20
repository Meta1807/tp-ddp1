import random

def get_song(data):
    ''' This function selects a random song from the list of all available songs
        
        [ARGUMENTS]
        - data: GameData()

        [DESCRIPTION]        
        Using the random library, it first generates a random number using randrange in
        range of the track list's length. The program will then use the generated number
        to check whether or not a corresponding track with that index has been played
        before and generates a new number if it has. Afterwards it adds the selected song
        to the "appeared_songs" list.

        Finally, the program opens the selected song's file using "with open", reads the
        lyrics line per line, and filters the file's extension name before returning them
        to the function's caller as a tuple.

        [DISCLAIMER] 
        This function was adapted from the initial template with implementation for the 
        randomization feature, thanks kakak-kakak asdos :D
    
    '''
    random_index = 0
    while True:
        random_index = random.randrange(len(data.songs))
        if data.songs[random_index] in data.appeared_songs:
            continue
        else:
            data.appeared_songs.append(data.songs[random_index])
            break
    
    with open(f"lagu/{data.songs[random_index]}") as lagu:
        lirik = lagu.readlines()
        judul = data.songs[random_index].split('.txt')[0]
        return judul, lirik
    