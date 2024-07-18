import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'acronyms.txt')

def find_acronym():
    """
    Find the definition of a software acronym in the text file.
    """
    look_up = input("What software acronym would you like to look up?\n")

    found = False

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read each line in the file
            for line in file:
                # Check if the acronym is in the current line
                if look_up in line:
                    print(line)
                    found = True
                    break
    except FileNotFoundError as e:
        print('File not found')
        return
        
    if not found:
        print("The acronym does not exist")

def add_acronym():
    """
    Add a new software acronym and its definition to the text file.
    """
    acronym = input("What acronym do you want to add?\n")
    a_definition = input(f"What is the definition for the acronym {acronym}?\n")

    # Open the file in append mode
    with open(file_path, 'a') as file:
        file.write(acronym + "-" + a_definition + "\n")

def main():
    """
    Main function to prompt user for action and call the appropriate function.
    """
    choice = input("Do you want to find(F) or add(A) an acronym? ")
    
    if choice == 'F':
        find_acronym()
    elif choice == 'A':
        add_acronym()

# Run the main function
main()