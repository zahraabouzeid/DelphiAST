import os
from multiprocessing import Pool

def read_file(_file_path):
  pass

def read_files_in_folder(folder):
    files = []
    for file in os.listdir(folder):
       if file.endswith(".pas"):
           files.append(os.path.join(folder, file))
    with Pool() as pool:
        pool.map(read_file, files)

def DelphiReader(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for subfolder in dirs:
            subfolder_path = os.path.join(root, subfolder)
            read_files_in_folder(subfolder_path)

if __name__ == "__main__":
    DelphiReader("C:/FW")