import os
import hashlib

def menu():
    while True:
        print("\n--- File Duplicate Finder ---")
        print("1. Enter directory to search")
        print("2. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            directory = input("Enter the directory to search for duplicates: ")
            if os.path.exists(directory):
                find_duplicates(directory)
            else:
                print('Error, {directory} does not exist')

        elif choice == '2':
            print('Exiting program')

        else:
            print ('Invalid option')

def find_duplicates(directory):
    checksums = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)

        checksum = get_checksum(file_path)

        if checksum in checksums:
            checksums[checksum].append(file_path)
        else:
            checksums[checksum] = [file_path]
        
    duplicates = False
    for paths in checksum.values():
        if len(paths) >1:
            duplicates = True
            print ('Duplicate files found')
            for path in paths:
                print (f'{path}')
            print()

    if not duplicates:
        print ('No duplicate files found.')

def get_checksum(file_path):
    hash_obj = hashlib.md5()
    with open(file_path, 'rb') as f:
        hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    menu()
