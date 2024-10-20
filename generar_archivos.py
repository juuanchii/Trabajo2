import os
import random
import string


save_directory = "/Volumes/facultad/GIT/CursoGit/trabajo2"


for i in range(1, 9):
    filename = f"archivo-{i:02}.txt"
    filepath = os.path.join(save_directory, filename)
    
    content = ''.join(filename)  
    
    with open(filepath, 'w') as f:
        f.write(content)


os.listdir(save_directory)
