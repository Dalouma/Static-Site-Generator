from textnode import TextType, TextNode
from htmlnode import LeafNode, ParentNode
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

def block_type_to_html_tag(text, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return 'p'
        case BlockType.HEADING:
            index = text.index(' ')
            count = text[:index].count('#')
            return f"h{count}"
        case BlockType.CODE:
            return 'pre'
        case BlockType.QUOTE:
            return 'blockquote'
        case BlockType.UNORDERED_LIST:
            return 'ul'
        case BlockType.ORDERED_LIST:
            return 'ol'
        case _:
            raise Exception("Invalid Block Type")
        
def text_to_children(text):
    return list(map(lambda node: text_node_to_html_node(node), text_to_textnodes(text)))

def ordered_list_children(block):
    list_elements = block.splitlines()
    children = []
    for i in range(len(list_elements)):
        li = list_elements[i]
        dot_index = li.index('.')
        stripped = li[dot_index+1:].lstrip()
        children.append(ParentNode('li', text_to_children(stripped)))

    return children
        
def determine_children(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            return text_to_children(block.replace('\n', ' '))
        case BlockType.HEADING:
            return text_to_children(block.lstrip("# "))
        case BlockType.CODE:
            content = "".join(block.splitlines(True)[1:-1])
            return [text_node_to_html_node(TextNode(content, TextType.CODE))]
        case BlockType.QUOTE:
            content = "".join(map(lambda line: line.lstrip("> "), block.splitlines(True)))
            content_blocks = markdown_to_blocks(content)
            return list(map(lambda x: ParentNode('p', text_to_children(x.replace('\n', ' '))), content_blocks))
        case BlockType.UNORDERED_LIST:
            return list(map(lambda line: ParentNode('li', text_to_children(line.lstrip("- "))), block.splitlines()))
        case BlockType.ORDERED_LIST:
            return ordered_list_children(block)
        case _:
            raise Exception("Invalid block_type")
    
def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    html_block_nodes = []
    for block in markdown_blocks:
        block_type = block_to_block_type(block)

        tag = block_type_to_html_tag(block, block_type)
        children = determine_children(block, block_type)

        html_node = ParentNode(tag, children)
        html_block_nodes.append(html_node)

    return ParentNode("div", html_block_nodes)