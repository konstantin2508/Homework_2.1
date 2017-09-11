import subprocess
import os


def convert_file(file_list, current_dir, input_dir, output_dir ):
    for file in file_list:
        output_file = os.path.join(output_dir, 'output_' + file)
        input_file = os.path.join(input_dir, file)
        convert = os.path.join(current_dir, 'convert')
        subprocess.run([convert, input_file, '-resize', '200', output_file])


def main():
    source = 'Source'
    result = 'Result'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, result)
    input_dir = os.path.join(current_dir, source)

    if not os.path.exists(output_dir):
        os.mkdir(output_dir) #создаем папку "Result"

    file_list = os.listdir(os.path.join(current_dir, source))
    convert_file(file_list, current_dir, input_dir, output_dir)
	
	
main()

