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

    def serialize(self):
        data = (
            to_bytes(self.block_id) +
            to_bytes(self.parent_id) +
            to_bytes(self.num_keys)
        )
        data += b"".join(to_bytes(k) for k in self.keys)
        data += b"".join(to_bytes(v) for v in self.values)
        data += b"".join(to_bytes(c) for c in self.children)
        return data[:SIZEOF_BLOCK]

    @staticmethod
    def deserialize(data):
        node = BTreeNode()
        node.block_id = from_bytes(data[0:8])
        node.parent_id = from_bytes(data[8:16])
        node.num_keys = from_bytes(data[16:24])
        offset = 24
        for i in range(MAXIMUM_KEYS):
            node.keys[i] = from_bytes(data[offset:offset+8])
            offset += 8
        for i in range(MAXIMUM_KEYS):
            node.values[i] = from_bytes(data[offset:offset+8])
            offset += 8
        for i in range(MAXIMUM_CHILDREN):
            node.children[i] = from_bytes(data[offset:offset+8])
            offset += 8
        return node

# B-tree Header
class BTreeHeader:
    def __init__(self, root_id=0, next_block_id=1):
        self.special_num = SPECIAL_NUM
        self.root_id = root_id
        self.next_block_id = next_block_id

    def serialize(self):
        data = (
            self.special_num +
            to_bytes(self.root_id) +
            to_bytes(self.next_block_id)
        )
        return data.ljust(SIZEOF_BLOCK, b"\x00")

    @staticmethod
    def deserialize(data):
        if data[:8] != SPECIAL_NUM:
            raise ValueError("Invalid special number")
        header = BTreeHeader()
        header.root_id = from_bytes(data[8:16])
        header.next_block_id = from_bytes(data[16:24])
        return header

# Index File Manager
class IndexFile:
    def __init__(self):
        self.file = None
        self.header = None

    def create(self, filename):
        if os.path.exists(filename):
            overwrite = input("File exists. Overwrite? (y/n): ").strip().lower()
            if overwrite != "y":
                print("Aborted.")
                return
        self.file = open(filename, "wb+")
        self.header = BTreeHeader()
        self.file.write(self.header.serialize())
        # Create an empty root node
        root = BTreeNode(block_id=1)
        self.file.write(root.serialize())
        print(f"Created index file: {filename}")

    def open(self, filename):
        if not os.path.exists(filename):
            print("File does not exist.")
            return
        self.file = open(filename, "rb+")
        data = self.file.read(SIZEOF_BLOCK)
        try:
            self.header = BTreeHeader.deserialize(data)
            print(f"Opened index file: {filename}")
        except ValueError as e:
            print(f"Error opening file: {e}")
            self.file = None

    def insert(self, key, value):
        if self.file is None:
            print("No file open.")
            return

        # Load the root node
        self.file.seek(SIZEOF_BLOCK)  # Assuming root node is at block 1
        root_data = self.file.read(SIZEOF_BLOCK)
        root = BTreeNode.deserialize(root_data)

        # Check if there's room to insert the key
        if root.num_keys < MAXIMUM_KEYS:
            root.keys[root.num_keys] = key
            root.values[root.num_keys] = value
            root.num_keys += 1
            # Sort keys and values
            sorted_pairs = sorted(zip(root.keys[:root.num_keys], root.values[:root.num_keys]))
            root.keys[:root.num_keys], root.values[:root.num_keys] = zip(*sorted_pairs)

            # Write back the updated root node
            self.file.seek(SIZEOF_BLOCK)  # Assuming root node is at block 1
            self.file.write(root.serialize())
            print(f"Inserted key={key}, value={value}")
        else:
            print("Node is full. Splitting not yet implemented.")

    def search(self, key):
        if self.file is None:
            print("No file open.")
            return

        # Load the root node
        self.file.seek(SIZEOF_BLOCK)  # Assuming root node is at block 1
        root_data = self.file.read(SIZEOF_BLOCK)
        root = BTreeNode.deserialize(root_data)

        # Search for the key in the root node
        for i in range(root.num_keys):
            if root.keys[i] == key:
                print(f"Key={key}, Value={root.values[i]}")
                return
        print("Key not found.")

    def print_index(self):
        if self.file is None:
            print("No file open.")
            return

        # Load the root node
        self.file.seek(SIZEOF_BLOCK)  # Assuming root node is at block 1
        root_data = self.file.read(SIZEOF_BLOCK)
        root = BTreeNode.deserialize(root_data)

        # Print all keys and values in the root node
        for i in range(root.num_keys):
            print(f"Key={root.keys[i]}, Value={root.values[i]}")

    def load(self, filename):
        if self.file is None:
            print("No file open.")
            return
        if not os.path.exists(filename):
            print("File does not exist.")
            return

        with open(filename, "r") as f:
            for line in f:
                try:
                    key, value = map(int, line.strip().split(","))
                    self.insert(key, value)
                except ValueError:
                    print(f"Invalid line in file: {line.strip()}")
