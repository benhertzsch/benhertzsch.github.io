import shutil

def find_line(file_path, marker):
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if marker in line:
                return line_number
    return None


def insert_content(input_file, target_file, base_file, navbar_string):
    with open(input_file, 'r') as file:
        content = file.read()

    shutil.copyfile(base_file, target_file)
    with open(target_file, 'r') as file:
        lines = file.readlines()

    line_num = find_line(base_file, "<!-- content_insertion -->")
    lines.insert(line_num - 1, content)

    with open(target_file, 'w') as file:
        file.writelines(lines)
    
    set_navbar_active(target_file, navbar_string)


def set_navbar_active(target_file, navbar_string):
    with open(target_file, 'r') as file:
        lines = file.readlines()
        
    marker = "<li><a href=\"" + navbar_string + "\">"
    line_num = find_line(target_file, marker)
    
    line = lines[line_num - 1]
    modified_line = line.replace('<li>', '<li class="active">', 1)
    lines[line_num - 1] = modified_line
    with open(target_file, 'w') as file:
        file.writelines(lines)


def main():
    paths = [
        ['contents/about.html', './index.html', "./base.html", './index.html'],
        ['contents/research.html', './research.html', "./base.html", './research.html'],
        ['contents/publications.html', './publications.html', "./base.html", './publications.html'],
        ['contents/notes.html', './notes.html', "./base.html", './notes.html'],
        
        ['notes/catastrophe_theory/catastrophe_theory.html', './catastrophe_theory.html', "./base_minimal.html", './notes.html']
    ]

    for (in_file, out_file, base_file, navbar_string) in paths:
        print("attempting in_file:", in_file)
        insert_content(in_file, out_file, base_file, navbar_string)
        
    print("Successfully created files.")
    
if __name__ == "__main__":
    main()