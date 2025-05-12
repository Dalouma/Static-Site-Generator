import sys
from textnode import *
from handler import *

PATH_TO_STATIC = "static"
PATH_TO_PUBLIC = "public"
PATH_TO_DOCS = "docs"
PATH_TO_CONTENT = "content"
PATH_TO_TEMPLATE = "template.html"

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'

    copy_static(PATH_TO_STATIC, PATH_TO_DOCS)
    generate_pages_recursive(PATH_TO_CONTENT, PATH_TO_TEMPLATE, PATH_TO_DOCS, basepath)

if __name__ == "__main__":
    main()