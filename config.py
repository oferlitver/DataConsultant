"""
Module for shared values
https://docs.python.org/3.5/faq/programming.html#how-do-i-share-global-variables-across-modules
"""
DATE_DISPLAY_FORMAT = "dd/MM/yyyy"

# File names
HISTORIC_DATA = "./data/historic_data.csv"
LOGFILE = './output/logfile.csv'

# Log file headers
headers = ['user_id', 'user_age', 'user_male', 'user_field', 'condition', 'ts']

# User details


# Experiment structure
NUM_STEPS = 3

# Experiment conditions
CONDITIONS = dict(
    condition  = ['Condition A', 'Condition B'],
    a          = [100,           120],
    b          = [0.5,           0.6],
    c          = [[1,1,1,1,0.5,1,1.5], [0.5,1,1.5,1,1,1,1]],
    sigma      = [3,             5],
    rec_period = [5,             3]
)