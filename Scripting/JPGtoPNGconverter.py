import sys
import os
from PIL import Image

# Grabing first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

print(image_folder, output_folder)

# Checking if output folder exist, not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Converting JPG to PNG

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print(f'{clean_name} done')
    
# Run command ==>> python .\JPGtoPNGconverter.py Pokedex\ new\