from textnode import *
from handler import *

PATH_TO_STATIC = "static"
PATH_TO_PUBLIC = "public"
PATH_TO_CONTENT = "content"
PATH_TO_TEMPLATE = "template.html"

def main():
    copy_static(PATH_TO_STATIC, PATH_TO_PUBLIC)
    generate_pages_recursive(PATH_TO_CONTENT, PATH_TO_TEMPLATE, PATH_TO_PUBLIC)

if __name__ == "__main__":
    main()