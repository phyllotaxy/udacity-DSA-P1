import sys
from collections import OrderedDict

class Node:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def has_left_subtree(self):
        return self.left != None

    def has_right_subtree(self):
        return self.right != None

class Tree:

    def __init__(self, data=Node()):
        self.root = data

    def get_root(self):
        return self.root

def huffman_encoding(data):
    key_freq = OrderedDict()
    for char in data:
        key_freq[char] = key_freq.get(char, 0) + 1
    huffman_tree = construct_huffman_tree(key_freq)
    codes = dict()
    update_codes(huffman_tree.get_root(), codes)
    encoded_data = ''
    for char in data:
        encoded_data += codes.get(char)
    return encoded_data, huffman_tree

def construct_huffman_tree(key_freq):
    huffman_tree = Tree()
    key_freq_sorted = OrderedDict(sorted(key_freq.items(), key=lambda t: t[1]))
    if len(key_freq_sorted) == 0:
        return huffman_tree
    while len(key_freq_sorted) >= 2:
        key_1, freq_1 = key_freq_sorted.popitem(last=False)
        key_2, freq_2 = key_freq_sorted.popitem(last=False)
        internal_node = Node(freq_1 + freq_2, nodify(trim(key_1)), nodify(trim(key_2)))
        key_freq_sorted[internal_node] = internal_node.value
        key_freq_sorted = OrderedDict(sorted(key_freq_sorted.items(), key=lambda t: t[1]))
    key, _ = key_freq_sorted.popitem()
    if type(key) is Node:
        huffman_tree.root = trim(key)
    elif type(key) is str:
        huffman_tree.root, huffman_tree.root.left = Node(), Node(key)
    return huffman_tree

# Trim the frequency from the node.
def trim(key):
    if type(key) is Node and type(key.value) is not str:
        key.value = None
    return key

def nodify(key):
    if type(key) is str:
        return Node(key)
    if type(key) is Node:
        return key
    return None

def update_codes(node, codes):
    encoding = ''
    collect_encodings(node, encoding, codes)

def collect_encodings(node, encoding, codes):
    if node.value is None and not (node.has_left_subtree() or node.has_right_subtree()):
        return
    if not (node.has_left_subtree() or node.has_right_subtree()):
        codes[node.value] = encoding
        return
    if node.has_left_subtree():
        encoding += '0'
        collect_encodings(node.left, encoding, codes)
        encoding = encoding[:-1]
    if node.has_right_subtree():
        encoding += '1'
        collect_encodings(node.right, encoding, codes)
        encoding = encoding[:-1]

def huffman_decoding(data, tree):
    decoded_data = ''
    node = tree.get_root()
    if node.value is None and not (node.has_left_subtree() or node.has_right_subtree()):
        return decoded_data
    while data:
        if data[0] == '0' and node.has_left_subtree():
            data = data[1:]
            node = node.left
        elif data[0] == '1' and node.has_right_subtree():
            data = data[1:]
            node = node.right
        if node.value:
            decoded_data += node.value
            node = tree.get_root()
    return decoded_data

def main():
    sentences = list()
    # empty_string
    # prints ''
    sentence_1 = ''
    sentences.append(sentence_1)
    # string of size 1
    # prints '0'
    sentence_2 = 'a'
    sentences.append(sentence_2)
    # default example given from the assignment
    # prints '0110111011111100111000001010110000100011010011110111111010101011001010'
    sentence_3 = 'The bird is the word'
    sentences.append(sentence_3)
    # example from http://huffman.ooz.ie/
    sentence_4 = 'ALMOST 200 TOTTENHAM FANS FACE A RACE AGAINST TIME TO GET TO MADRID FOR THE CHAMPIONS LEAGUE FINAL AFTER THEIR PLANE IS TAKEN OUT OF SERVICE BECAUSE OF BIRD DAMAGE.'
    sentences.append(sentence_4)
    for sentence in sentences:
        test(sentence)

def test(a_great_sentence):
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(mk_int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

# a version of int() that works for empty string
def mk_int(str, base):
    return int(str, base) if str else 0

if __name__ == "__main__":
    main()
