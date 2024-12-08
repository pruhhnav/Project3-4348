import os
import struct

# Constants
SIZEOF_BLOCK = 512
SPECIAL_NUM = b"4337PRJ3"
MAXIMUM_KEYS = 19
MAXIMUM_CHILDREN = 20

# Helper functions
def to_bytes(value, length=8):
    return value.to_bytes(length, byteorder="big")

def from_bytes(b):
    return int.from_bytes(b, byteorder="big")

# B-tree Node
class BTreeNode:
    def __init__(self, block_id=0, parent_id=0, num_keys=0):
        self.block_id = block_id
        self.parent_id = parent_id
        self.num_keys = num_keys
        self.keys = [0] * MAXIMUM_KEYS
        self.values = [0] * MAXIMUM_KEYS
        self.children = [0] * MAXIMUM_CHILDREN

# B-tree Header
class BTreeHeader:
    def __init__(self, root_id=0, next_block_id=1):
        self.special_num = SPECIAL_NUM
        self.root_id = root_id
        self.next_block_id = next_block_id
