from enum import Enum
import re



class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown):
    return list(filter(lambda block: block, map(lambda block: block.strip(), markdown.split("\n\n"))))

def is_ordered_list(block):
    # print(f"checking ordered list with block: {block}")
    items = block.splitlines()
    for i in range(len(items)):
        line = items[i]
        if len(line.lstrip("1234567890")) < 2:
            # print("content not long enough")
            return False
        if line.lstrip("1234567890")[:2] != ". ":
            # print(f"did not find dot and space on iteration {i} and line {line}")
            # print(f"The stripped line was {line.lstrip("1234567890")}")
            return False
        if line[:line.index('.')] != str(i+1):
            # print("wrong number detected")
            # print(f"number found: {line[:line.index('.')]}")
            # print(f"number needed: {i+1}")
            return False
    
    return True

def block_to_block_type(block):
    if block[0] == "#":
        return BlockType.HEADING
    if len(block) >= 6 and block[:3] == "```" == block[-3:]:
        return BlockType.CODE
    if all([True if line[0] == ">" else False for line in block.splitlines()]):
        return BlockType.QUOTE
    if all([True if (len(line) >= 2 and line[:2] == "- ") else False for line in block.splitlines()]):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH

