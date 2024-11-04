import os

def find_python_files(directory):
    python_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files

def bundle_files(files, output_file):
    with open(output_file, 'w') as outfile:
        outfile.write('#!/usr/bin/env python\n\n')
        for file in files:
            with open(file, 'r') as infile:
                content = infile.read().replace('print(', '# print(')
                if "import" not in content:
                    outfile.write(content)
                    outfile.write('\n\n')  # Add new lines between files for separation

def main():
    project_dir = './it_encode_lib'  # Adjust your project directory
    output_file = './bundle.py'  # Adjust the output file path

    # Find all Python files in the project directory
    python_files = find_python_files(project_dir)

    # Bundle the files into the output file
    bundle_files(python_files, output_file)

    print(f"Bundled {len(python_files)} Python files into {output_file}")

if __name__ == "__main__":
    main()
