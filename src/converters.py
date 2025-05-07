from textnode import TextType, TextNode
from htmlnode import LeafNode
from splitters import *



def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextNode has invalid TextType")

def text_to_textnodes(text):
    base_node = TextNode(text, TextType.TEXT)
    after_bolds = split_nodes_delimiter([base_node], "**", TextType.BOLD)
    after_italics = split_nodes_delimiter(after_bolds, "_", TextType.ITALIC)
    after_code = split_nodes_delimiter(after_italics, "`", TextType.CODE)
    after_images = split_nodes_image(after_code)
    after_links = split_nodes_link(after_images)

    return after_links

# def markdown_to_html_node(markdown):
#     markdown_blocks = markdown_to_blocks(markdown)

#     for block in markdown_blocks:
#         block_type = block_to_block_type(block)
#         html_node = 