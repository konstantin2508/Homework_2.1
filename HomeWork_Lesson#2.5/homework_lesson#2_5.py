import subprocess
import os

source = 'Source'
result = 'Result'

current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, result)
input_dir = os.path.join(current_dir, source)

os.mkdir(output_dir) #создаем папку "Result"

file_list = os.listdir(os.path.join(current_dir, source))

for file in file_list:
	output_file = output_dir + '\\output_' + file 
	input_file = input_dir + '\\' + file
	convert = current_dir + '\\convert' 
	subprocess.run([convert, input_file, '-resize', '200', output_file])