import random
import logging 
import math 
import datetime 
import os 
import sys 
import json 
import csv 

#logging setup
logging.basicConfig(
    level=logging.INFO,
    )
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler=logging.FileHandler('modules.log')
file_handler.setLevel(logging.INFO)
console_handler=logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

#random module
logging.info('Random module started')
random_number=random.randint(1,10)
print(random_number)
logging.info('Random module completed')







