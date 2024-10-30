import os
import sys
import shutil
from tqdm import tqdm 

def main(input_dir1, input_dir2, output_dir):
    # Check if input directories exist
    if not os.path.isdir(input_dir1):
        print(f"Error: Directory '{input_dir1}' does not exist.")
        sys.exit(1)
    if not os.path.isdir(input_dir2):
        print(f"Error: Directory '{input_dir2}' does not exist.")
        sys.exit(1)

    # Create output subdirectories A and B
    output_a = os.path.join(output_dir, 'A')
    output_b = os.path.join(output_dir, 'B')
    os.makedirs(output_a, exist_ok=True)
    os.makedirs(output_b, exist_ok=True)

    # Get set of filenames in both directories
    dir1_files = {
        f
        for f in os.listdir(input_dir1)
        if os.path.isfile(os.path.join(input_dir1, f))
    }
    dir2_files = {
        f
        for f in os.listdir(input_dir2)
        if os.path.isfile(os.path.join(input_dir2, f))
    }

    # Find common filenames
    common_files = dir1_files & dir2_files

    if not common_files:
        print("No common images found based on filenames.")
        sys.exit(0)

    # Copy common images to output directories A and B with existence check
    for filename in tqdm(common_files):
        src_file_dir1 = os.path.join(input_dir1, filename)
        src_file_dir2 = os.path.join(input_dir2, filename)

        dest_file_dir1 = os.path.join(output_a, filename)
        dest_file_dir2 = os.path.join(output_b, filename)

        # Check and copy for input_dir1
        if not os.path.exists(dest_file_dir1):
            shutil.copy2(src_file_dir1, dest_file_dir1)
        else:
            continue

        # Check and copy for input_dir2
        if not os.path.exists(dest_file_dir2):
            shutil.copy2(src_file_dir2, dest_file_dir2)
        else:
            continue

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_dir1> <input_dir2> <output_dir>")
        sys.exit(1)

    input_dir1 = sys.argv[1]
    input_dir2 = sys.argv[2]
    output_dir = sys.argv[3]

    main(input_dir1, input_dir2, output_dir)
