def write_file(file_name, file_content):
    try:
        with open(file_name, 'w') as file:
            file.write(file_content)
        print(f"File '{file_name}' successfully written.")
    except FileNotFoundError:
        print(f"Error: Directory for file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_file(file_name, append_content):
    pass

def read_file(file_name):
    pass
