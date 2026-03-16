import random
import logging 
import os 

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
logger.info('Random module started')
random_number=random.randint(1,10)
print(random_number)
logger.info(f'Random Numbers {random_number}')




#os module

import os 
logger.info('OS module started')
os_number=os.getcwd()
print(os_number)
logger.info(f'OS module completed {os_number}')


logger.info('Change dir in os')
os.chdir(r'C:\Users\LAPTOPS HUB\Desktop\Revsion-All\PythonCoreAndAdvanced')

print(os.getcwd())
logger.info(f'Change dir in os completed {os.getcwd()}')



logger.info('List files in os')
list_files=os.listdir()
print(list_files)
logging.info(f'List files in os completed {list_files}')


logger.info('Create folders')
if not os.path.exists("new_folder"):
    os.mkdir("new_folder")
    print("Folder created")
else:
    print("Folder already exists")
logger.info('Create folders completed')



logger.info('Create Multiple folders')
if not os.path.exists('new_folder/new_folder2'):
    os.makedirs('new_folder/new_folder2')
    print("Folders created")
logger.info('Create Multiple folders completed')




logger.info('Create files')
os.path.join('new_folder','file.txt')
print(os.path.join('new_folder','file.txt'))
logger.info('Create files completed')



logger.info('Exist folder or not')
os.path.exists('new_folder')
print(os.path.exists('new_folder'))
logger.info('Exist folder or not completed')





