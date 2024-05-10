import os

def rename_files():
    # Get the current directory
    current_directory = os.getcwd()
    
    # List all files in the current directory
    files = os.listdir(current_directory)
    
    # Iterate through each file
    for filename in files:
        if "[" in filename and "]" in filename:
            # Extract the part between '[' and ']'
            start_index = filename.index("[")
            end_index = len(filename) - 5
            text_to_replace = filename[start_index:end_index + 1]
            
            # Replace the text between '[' and ']' with a blank space
            new_filename = filename.replace(text_to_replace, "")
            
            # Check if the new filename already exists
            index = 1
            if os.path.exists(os.path.join(current_directory, new_filename)):
                # If it does, add a number to the end of the filename                
                  # Rename the file
                os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, f'{text_to_replace}.mp4' ))
                print(f"Renamed {filename} to {new_filename}")
            
            else:
                os.rename(os.path.join(current_directory, filename), os.path.join(current_directory, new_filename))
                print(f"Renamed {filename} to {new_filename}")
            
          

if __name__ == "__main__":
    rename_files()