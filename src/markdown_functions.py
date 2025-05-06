from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    return list(filter(lambda block: block, map(lambda block: block.strip(), markdown.split("\n\n"))))

def block_to_block(blocks):
    pass