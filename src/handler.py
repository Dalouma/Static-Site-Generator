import os, shutil
from markdown_functions import extract_title
from converters import markdown_to_html_node


def copy_static(src_path, dest_path):
    # first delete all contents
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
    os.mkdir(dest_path)

    # loop through contents of src
    for entry in os.listdir(src_path):
        original = os.path.join(src_path, entry)
        new_path = os.path.join(dest_path, entry)

        if os.path.isfile(original):
            shutil.copy(original, new_path)
        else:
            copy_static(original, new_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    md = None
    with open(from_path) as f:
        md = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    with open(dest_path, 'w') as f:
        f.write(page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        original = os.path.join(dir_path_content, entry)
        

        if os.path.isfile(original) and ".md" in entry:
            new_file_name = entry.replace(".md", ".html")
            new_path = os.path.join(dest_dir_path, new_file_name)
            generate_page(original, template_path, new_path)
        else:
            new_path = os.path.join(dest_dir_path, entry)
            if os.path.exists(new_path) == False:
                os.mkdir(new_path)
            generate_pages_recursive(original, template_path, new_path)