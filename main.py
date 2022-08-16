import os
import shutil
from_dir = 'C:/Users/kalya/Downloads/source'
to_dir = 'C:/Users/kalya/Downloads/destination'
list_of_files = os.listdir(from_dir)
print(list_of_files)
for i in list_of_files:
    name,extension = os.path.splitext(i)
    print(name)
    print(extension)
    if(extension == ''):
        continue
    if(extension in ['.png', '.jpg', '.gif', '.jpeg']):
        path1 = from_dir + '/' + i
        path2 = to_dir + '/' + 'imagefiles'
        path3 = to_dir + '/' + 'imagefiles' + i

        print(path1)
        print(path3)
        if(os.path.exists(path2)):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)
