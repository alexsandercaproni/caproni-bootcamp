import os
from caproni_infrastructure.environment import Environment


active_environment = Environment[os.environ['ENVIRONMENT']]
