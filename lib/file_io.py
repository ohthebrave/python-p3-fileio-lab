def write_file(file_name, file_content):
    file_name_str = str(file_name)
    file_path = file_name_str + '.txt'
    with open(file_path, mode='w', encoding='utf-8') as file:
        file.write(file_content)

        
def append_file(file_name, append_content):
    file_name_str = str(file_name)
    file_path = file_name_str + '.txt'
    with open(file_path, mode='a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    file_name_str = str(file_name)
    file_path = file_name_str + '.txt'
    with open(file_path, encoding='utf-8') as file:
        return file.read()

        
