import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='enter config file name')
args = parser.parse_args()

file_name = args.config

if file_name == None:
    file_name = input("enter a file name:   ")
    file_path = "Flask Backend Practice/FlaskBackend/" + file_name + ">"
    print(file_path)

    
else: 
    file_path = "Flask Backend Practice/FlaskBackend/" + file_name + ">"
    print(file_path)
