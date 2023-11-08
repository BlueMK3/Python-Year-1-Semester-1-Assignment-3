def write_data_to_file(file_name):
    # TODO

def read_data_from_file(file_name):
    # TODO

# DO NOT MODIFY ANY CODE BELOW THIS LINE
def main(): 
    FILE_NAME = 'marks.txt'
    print('== Data written to file:', write_data_to_file(FILE_NAME))
    count, average = read_data_from_file(FILE_NAME)
    print(f'== Count: {count}, Average: {average:.2f}')

if __name__ == '__main__':
    main()
