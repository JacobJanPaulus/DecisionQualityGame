from flask import Blueprint, render_template, request, redirect, url_for
from games import *                 # Import the game definitions
from game_sessions import *         # Import the in-memory store of game sessions

routes = Blueprint('routes', __name__)

# Define the different routes (URLs)
@routes.route('/')
def index():
    # Go to the main page to start or join a game
    return render_template('index.html')

@routes.route('/master')
def master():
    # Go to the page for the game master
    return render_template('master.html', available_games=available_games)

@routes.route('/player')
def player():
    # Go to the page for the player
    return render_template('player.html')

# Routes for game master to create a game
@routes.route('/create_game', methods=['POST'])
def create_game():
    # Game master selected game id
    game_id = request.form['game_id']
    # Create the game session
    game_session = GameSession(game_id)
    return redirect(url_for('routes.game_master_view', game_session_id=game_session.id))

# Routes for the game master render the game
@routes.route('/game/<game_session_id>/master')
def game_master_view(game_session_id):
    game_session: GameSession = get_game_session(game_session_id)
    if not game_session:
        return render_template('master.html', 
                               game_name=None, 
                               game_status='UNDEFINED',
                               game_session_id=game_session_id)
    return render_template('master.html',
                           game_name=game_session.game["name"],
                           game_status=game_session.status.name,
                           game_session_id=game_session_id)
