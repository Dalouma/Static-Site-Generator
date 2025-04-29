from textnode import *
from htmlnode import *

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
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            result_nodes.append(node)
            continue

        split_text_list = node.text.split(delimiter)
        if len(split_text_list) % 2 == 0:
            raise Exception("Invalid Markdown syntax: missing matching closing delimiter")
        
        split_nodes = []
        for i in range(len(split_text_list)):
            split_type = TextType.TEXT
            if i % 2 == 1:
                split_type = text_type
            split_nodes.append(TextNode(split_text_list[i], split_type))
        result_nodes.extend(split_nodes)
    
    return result_nodes