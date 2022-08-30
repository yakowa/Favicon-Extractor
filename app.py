
# * favicon extractor
# * Created by https://JacobEM.com/
# * This script is licensed under the MIT License.


from os import listdir, getcwd
from os.path import isdir, join
import shutil

from PIL import Image
import sys

def extractFavicon(inputPath, outputPath, name):
    shutil.copy2(inputPath, outputPath)

    print(f'Extracted & copied a {name} over as an favicon.')



path = getcwd() + '/input'
pathOut = getcwd() + '/output'

folders = [f for f in listdir(path) if isdir(join(path, f))]

for thisFolder in folders:

    extractFavicon(
        path + '/' + thisFolder + '/favicon.ico',
        pathOut + '/' + thisFolder + '.ico',
        thisFolder
    )