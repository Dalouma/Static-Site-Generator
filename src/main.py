from textnode import *
from handler import *

SOURCE_PATH = "static"
DESTINATION_PATH = "public"

def main():
    # txt_node = TextNode('filler text!!', TextType.BOLD, 'heehee.com')
    # print(txt_node)

    copy_static(SOURCE_PATH, DESTINATION_PATH)

if __name__ == "__main__":
    main()