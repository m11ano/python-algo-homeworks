import numpy as np
from PIL import Image


class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class ColorTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, value):
        node = self.root
        for bit in f"{value:08b}":
            if bit == "0":
                if not node.left:
                    node.left = TreeNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode()
                node = node.right
        node.value = value

    def compress(self, pixel_value):
        compressed_bits = []
        node = self.root
        for bit in f"{pixel_value:08b}":
            if bit == "0" and node.left:
                node = node.left
                compressed_bits.append("0")
            elif bit == "1" and node.right:
                node = node.right
                compressed_bits.append("1")
            else:
                break
        return "".join(compressed_bits)

    def decompress(self, compressed_bits):
        node = self.root
        for bit in compressed_bits:
            if bit == "0" and node.left:
                node = node.left
            elif bit == "1" and node.right:
                node = node.right
            else:
                break
        return node.value if node and node.value is not None else 0


def build_color_tree(image_array):
    tree = ColorTree()
    unique_colors = np.unique(image_array)
    for color in unique_colors:
        tree.insert(color)
    return tree


def compress_image(image_array, tree):
    compressed_image = []
    for row in image_array:
        compressed_row = [tree.compress(pixel) for pixel in row]
        compressed_image.append(compressed_row)
    return compressed_image


def decompress_image(compressed_image, tree):
    decompressed_image = []
    for row in compressed_image:
        decompressed_row = [tree.decompress(bits) for bits in row]
        decompressed_image.append(decompressed_row)
    return np.array(decompressed_image, dtype=np.uint8)


input_image_path = "480-360-sample.bmp"

image = Image.open(input_image_path).convert("L")
image_array = np.array(image)

color_tree = build_color_tree(image_array)

compressed_image = compress_image(image_array, color_tree)

decompressed_image = decompress_image(compressed_image, color_tree)

print(image_array)
print(decompressed_image)
