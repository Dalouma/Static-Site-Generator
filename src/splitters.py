from textnode import TextType, TextNode
from markdown_functions import *



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

def split_nodes_image(old_nodes):
    result_nodes = []
    for node in old_nodes:
        # This is a list of tuples for each image in the node in form:
        # [ ("<alt text>", "<image link>"), ...]
        image_list = extract_markdown_images(node.text)

        # if no images, append node and go next
        if len(image_list) == 0:
            result_nodes.append(node)
            continue

        # Split text into 2 parts using each image in image_list as delimiter and append nodes as required
        split_nodes = []
        current_text = node.text
        for image in image_list:
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current_text = sections[1]
        # Append last section after last split
        if current_text:
            split_nodes.append(TextNode(current_text, TextType.TEXT))

        result_nodes.extend(split_nodes)

    return result_nodes

def split_nodes_link(old_nodes):
    result_nodes = []
    for node in old_nodes:
        link_list = extract_markdown_links(node.text)

        if len(link_list) == 0:
            result_nodes.append(node)
            continue

        split_nodes = []
        current_text = node.text
        for link in link_list:
            sections = current_text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0]:
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            current_text = sections[1]
        if current_text:
            split_nodes.append(TextNode(current_text, TextType.TEXT))

        result_nodes.extend(split_nodes)

    return result_nodes