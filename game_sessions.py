import uuid
import datetime
from enum import Enum
from games import available_games 

# Create an in-memory store of game sessions
game_sessions = {}

class GameSessionStatus(Enum):
    WAITING = 1
    STARTED = 2
    ENDED = 3

class Player:
    def __init__(self, name: str):
        self._name: str = name
        self._progress: str = "Waiting"
        self._current_level: int = -1
        self._score: int = 0
        self._time_last_score: datetime = datetime.datetime.now()

    @property
    def name(self) -> str:
        return self._name

    @property
    def progress(self) -> str:
        return self._progress

    @property
    def current_level(self) -> int:
        return self._current_level

    @property
    def score(self) -> int:
        return self._score
    
    @property
    def time_last_score(self) -> datetime:
        return self._time_last_score

    def set_finished(self):
        self._progress = "Finished"

    def next_level(self):
        self._current_level += 1
        self._progress = f"At level {self._current_level}"

    def add_to_score(self, score: int):
        # Update the score 
        self._score += score
        # Update the time of last score - Used for  tie breaker in the leaderboard
        self._time_last_score = datetime.datetime.now()

class GameSession:
    def __init__(self, game_id):
        
        # Generate a UUID for the game session
        self._id = str(uuid.uuid4())[:6].upper()
        
        # Reference to the game being played
        self._game_id = game_id
        
        # Status of the game - Initializd at 'Waiting'
        self._status = GameSessionStatus.WAITING

        # Initialize the dict of players
        self._players: dict[str,Player]  = {}

        # Add this session to the store of game sessions
        game_sessions[self.id] = self

        print(f"Game session created: {self.id}")

    @property
    def id(self):
        return self._id

    @property
    def game_id(self):
        return self._game_id
    
    @property
    def game(self):
        if self._game_id not in available_games:
            raise RuntimeError(f"Game {self._game_id} not found")
        return available_games[self._game_id]

    @property
    def status(self)-> GameSessionStatus:
        print(self._status.name)
        return self._status
    
    @property
    def players(self):
        return self._players
    
    def add_player(self, username):
        self._players[username] = Player(username)

    def has_player(self, username) -> bool:
        return username in self._players

    def get_player(self,username) -> Player:
        if username in self._players:
            return self._players[username]
        else:
            raise RuntimeError(f"Player {username} not found in game session {self._id}")
        
    def get_leaderboard(self):
        leaderboard = []
        for player in self._players.values():
            leaderboard.append( (player.name, player.progress, player.score, player.time_last_score) )

        # Sort the leaderboard on decreasing scores and tie breaker 
        leaderboard.sort(key=lambda entry: (-entry[2], entry[3]))

        # Drop the last column (time_last_score) before returning
        leaderboard = [entry[:-1] for entry in leaderboard]

        return leaderboard
    
    def start(self):
        if self._status != GameSessionStatus.WAITING:
            raise RuntimeError("Starting a game that is not waiting")
        self._status = GameSessionStatus.STARTED
        
        # Set all players to level 1
        for player in self._players.values():
            player.next_level()

    def end(self):
        if self._status != GameSessionStatus.STARTED:
            raise RuntimeError("Ending a game that is not started")
        
        # Set all players to status finished
        for player in self._players.values():
            player.set_finished()
        self._status = GameSessionStatus.ENDED

# Global 
def get_game_session(session_id) -> GameSession:
    if session_id in game_sessions:
        return game_sessions[session_id]
    else:
        raise RuntimeError(f"Game session {session_id} not found")
    
def has_game_session(session_id) -> GameSession:
    return session_id in game_sessions


         
