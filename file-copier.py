import shutil
import os
import re

class File():
    def __init__(self, paths, destination, folder):    
        self.path = paths
        self.destination = destination
        folder_const = folder
    
class Operations():
    
    def get_parameters(self):
        counter = 0
        files = []
        with open("paths.txt") as file:
            for line in file:
                counter = counter + 1
                path = line.strip()
                if counter == 1:
                    folder = path
                    continue
                
                file_name = path.split("\\")[-1]
                destination = folder + file_name
                file = File(path, destination, folder)
                files.append(file)
        return files    
    

file = Operations()

for single_file in file.get_parameters():
   shutil.copyfile(single_file.path,single_file.destination)