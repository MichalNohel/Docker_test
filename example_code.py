import torch
from nnunetv2.inference.predict_from_raw_data import nnUNetPredictor
import argparse

print(torch.__version__)
print(torch.cuda.is_available())


# create comand line input argument path for this script
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('input_file_path', type=str, help='Path to the input file')
input_file_path = parser.parse_args().input_file_path


# input_file_path = 'example_data/data.txt'


with open(input_file_path, 'r') as f:
    data = f.read()
    print(data)




out_file = input_file_path + '_resutls.txt'
with open(out_file, 'w') as f:
    f.write('This is a test file.\n')
    f.write(data)
    f.write('This is the end of the test file.\n')




# this is example how to call this  
# python example_code.py input.txt
