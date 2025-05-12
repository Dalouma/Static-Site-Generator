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
    print(f"Generating page from {from_path} to {dest_path} usnig {template_path}")

    md = None
    with open(from_path) as f:
        md = f.read()

    template = None
    with open(template_path) as f:
        template = f.read()

    html = markdown_to_html_node(md).to_html()
    title = extract_title(md)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    if os.path.exists(dest_path) == False:
        os.mkdir(dest_path)

    with open(os.path.join(dest_path, "index.html"), 'w') as f:
        f.write(page)