import os

from zipfile import ZipFile
from unrar.rarfile import RarFile
from py7zr import SevenZipFile

class ZIP:
    def __init__(self, dir):
        self.dir = dir
        self.folder = [folder for folder in os.listdir(dir) if not folder.startswith('.')]

        self.func_type = {
            'zip': ZipFile,
            'rar': RarFile,
            '7z': SevenZipFile,
        }

    def main(self):
        for folder in self.folder:
            for file in os.listdir(self.dir + '/' + folder):
                folder_dir = self.dir + '/' + folder
                file_dir = folder_dir + '/' + file

                try:
                    file_type = file.split('.')[-1]

                    with self.func_type[file_type](file_dir, 'r') as archive:
                        archive.extractall(folder_dir)
                        print(f'{file:50} extracted successfully')
                except:
                    pass

if __name__ == '__main__':
    dir = input('Enter the directory: ')
    ZIP(dir).main()