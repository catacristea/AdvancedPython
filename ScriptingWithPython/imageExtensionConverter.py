import sys, os
from PIL import Image

'''
Change extension to .png from directory given in terminal.
'''

first = sys.argv[1]
second = sys.argv[2]

if not os.path.exists(second):
    os.makedirs(second)


for filename in os.listdir(first):
    img = Image.open(f'{first}\\{filename}')
    clean_name=os.path.splitext(filename)[0]
    img.save(f'{second}\\{clean_name}.png', 'png')
    print('All done!')

#salveaza-le in noul folder creat