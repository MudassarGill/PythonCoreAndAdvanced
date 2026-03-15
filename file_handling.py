import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('file_handling.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


logger.info('File handling started')


with open('file.txt','w') as f:
    content='My name is Mudassar Hussain and I am From Multan. I am the student of AI and I am an AI engineer '
    f.write(content)
    logger.info('File written successfully')



logger.info('File handling append method started')

with open('file.txt','a') as f:
    content='I am a good boy'
    f.write(content)
    logger.info('File appended successfully')

logger.info('File handling append method completed')

logger.info('File handling read method started')

with open('file.txt','r') as f:
    content=f.read()
    logger.info('File read successfully')
    print(content)

logger.info('File handling read method completed')


with open('file.txt','r') as f:
    content=f.readlines()
    logger.info('File read successfully')
    print(content)

logger.info('File handling read method completed')






import csv


with open('file.csv','w',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['Name','Age','City'])
    writer.writerow(['Mudassar','21','Multan'])
    writer.writerow(['Hussain','22','Lahore'])
    writer.writerow(['Mudassar','23','Karachi'])
    logger.info('File written successfully')

logger.info('File handling append method completed')

logger.info('File handling read method started')

with open('file.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
    logger.info('File read successfully')

logger.info('File handling read method completed')

logger.info('File handling read method started')

with open('file.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
    logger.info('File read successfully')

logger.info('File handling read method completed')
