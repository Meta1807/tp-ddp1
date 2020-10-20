class GameData():
    def __init__(self, initial: dict):
        self.player = initial['player']
        self.songs = initial['lagu']
        self.appeared_songs = []