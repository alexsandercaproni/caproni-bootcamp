import os
from infrastructure_caproni_exchange.environment import Environment

active_environment = Environment[os.environ['ENVIRONMENT']]
