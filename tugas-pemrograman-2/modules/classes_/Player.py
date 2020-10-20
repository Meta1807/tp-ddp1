class Player():
    def __init__(self, pemain: dict):
        ''' Initializes Player object with username data from start_game() 

            [ARGUMENTS]
            - self: Refers to the object itself
            - pemain: Dict

            [DESCRIPTION]
            The Player object stores all the necessary variables of the player, including Username, Mode, Health,
            Score, and the Current Round. All of these attributes can later be accessed by the program by calling
            Player.<<ATTRIBUTE_HERE>> (ex: To get the Player's health the program can simply call Player.health).
            
        '''
        self.username = pemain['username']
        self.mode = ''
        self.health = 0
        self.score = 0
        self.match_round = 1
    
    def set_mode(self, mode: str):
        ''' Sets the health of the Player object based on the mode argument (provided by start_game function).
        
            [ARGUMENTS]
            - self: Refers to the object itself
            - mode: String

            [DESCRIPTION]
            The "set_mode" method is used at game initialization to set the health of the player based on the
            selected difficulty. It also stores the requested mode into the Player object for use in printing
            the user's highscore later on.

        '''
        if mode.lower() == "normal":
            self.health = 3
        else:
            self.health = 1

        self.mode = mode.lower()
    
    def damage(self):
        ''' Decrements the player's health by 1, used when player inputs a wrong guess. '''
        self.health -= 1