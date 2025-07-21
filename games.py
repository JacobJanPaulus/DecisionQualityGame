# Import the individual games
from decision_problems.test_example import test_example
from decision_problems.dice_game import dice_game
from decision_problems.investment_decision import investment_decision

# Definition of games available to play
available_games = {
    "test_example": test_example,
    "dice_game": dice_game,
    "investment": investment_decision,
}