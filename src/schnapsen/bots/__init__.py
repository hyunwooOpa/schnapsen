"""Create a bot in a separate .py and import them here, so that one can simply import
it by from schnapsen.bots import MyBot.
"""
from .rand import RandBot
from .alphabeta import AlphaBetaBot
from .rdeep import RdeepBot
from .ml_bot2 import MLDataBot, MLPlayingBot, train_ML_model
from .gui.guibot import SchnapsenServer
from .minimax import MiniMaxBot
from .bully_bot import BullyBot

__all__ = ["RandBot", "AlphaBetaBot", "RdeepBot", "MLDataBot", "MLPlayingBot", "train_ML_model", "SchnapsenServer", "MiniMaxBot", "BullyBot"]
