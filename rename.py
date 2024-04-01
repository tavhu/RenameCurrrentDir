import os

def rename_files():
    input_name = input("Enter the base name for renaming: ")
    files = [f for f in os.listdir() if os.path.isfile(f) and f.endswith(".mp4")]
    num_files = len(files)
    
    if num_files == 0:
        print("No .mp4 files found in the current directory.")
        return
    
    print(f"Renaming {num_files} .mp4 files...")
    
    for i, file_name in enumerate(files, start=1):
        new_name = f"{input_name}_{i}.mp4"
        os.rename(file_name, new_name)
        print(f"Renamed '{file_name}' to '{new_name}'")
    
    print("All files renamed successfully.")

if __name__ == "__main__":
    rename_files()