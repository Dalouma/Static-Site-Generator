from textnode import *
from handler import *

PATH_TO_STATIC = "static"
PATH_TO_PUBLIC = "public"
PATH_TO_CONTENT = "content/index.md"
PATH_TO_TEMPLATE = "template.html"

def main():
    # txt_node = TextNode('filler text!!', TextType.BOLD, 'heehee.com')
    # print(txt_node)

    copy_static(PATH_TO_STATIC, PATH_TO_PUBLIC)
    generate_page(PATH_TO_CONTENT, PATH_TO_TEMPLATE, PATH_TO_PUBLIC)

if __name__ == "__main__":
    main()