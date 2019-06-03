import sys

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
    """
    Encode the given data and construct a Huffman tree from the data.

    Args:
      data(str): date to be encoded

    Returns:
       encoded_data(str): data encoded using huffman encoding
       huffman_tree(Tree): the huffman_tree that is constructed from data
    """
    char_freq = dict()
    for char in data:
        char_freq[char] = char_freq.get(char, 0) + 1
    huffman_tree = construct_huffman_tree(char_freq)
    # traverse the tree and collect the codes in the form of a dictionary
    codes = dict()
    update_codes(huffman_tree.get_root(), codes)
    encoded_data = ''
    for char in data:
        encoded_data += codes.get(char)
    return encoded_data, huffman_tree

def construct_huffman_tree(key_freq):
    """
    Construct a Huffman tree.

    Args:
      char_freq(dict): a dictionary with characters as keys and frequencies as value.

    Returns:
       huffman_tree(Tree): the huffman_tree that is constructed from the dictionary
    """
    huffman_tree = Tree()
    # Convert the dictionary into a list that is ordered by value(frequency).
    key_freq_sorted = sorted(key_freq.items(), key=lambda t: t[1])
    # If the list is empty (length == 0), return an empty tree.
    if not key_freq_sorted:
        return huffman_tree
    # If list length >= 2, we know the first two items has the smallest frequencies,
    # as the list is ordered by value(frequency).
    # We always take out two items and put one of type Node back, therefore the
    # while loop will terminate.
    while len(key_freq_sorted) >= 2:
        key_1, freq_1 = key_freq_sorted.pop(0)
        key_2, freq_2 = key_freq_sorted.pop(0)
        # As the frequency information is retained in the new node by adding
        # the frequencies of the children, the frequencies of the two child nodes
        # can be trimmed.
        internal_node = Node(freq_1 + freq_2, trim(nodify(key_1)), trim(nodify(key_2)))
        # Insert the item while maintaining the order of the list.
        for counter, item in enumerate(key_freq_sorted):
            if internal_node.value <= item[1]:
                key_freq_sorted.insert(counter, (internal_node, internal_node.value))
                break
            elif item == key_freq_sorted[-1]:
                key_freq_sorted.append((internal_node, internal_node.value))
                break
        # Since we have popped two items now, the list could be empty and the for
        # loop would be skipped, without adding the internal node we created. This
        # if statement takes care of that special case.
        if not key_freq_sorted:
            key_freq_sorted.append((internal_node, internal_node.value))

    # list length == 1 now
    # Pop the only item out of the list.
    key, _ = key_freq_sorted.pop()
    # If the while loop has been entered, the only item's key has to be of type Node.
    if isinstance(key, Node):
        huffman_tree.root = trim(key)
    # It could also be the case that the list started out with length == 1, in
    # which case the only item's key is of type string as the while loop was never entered,
    # and we need to construct a small Huffman tree with only one root and one leaf.
    elif isinstance(key, str):
        huffman_tree.root, huffman_tree.root.left = Node(), Node(key)
    return huffman_tree

def trim(node):
    """Trim the frequency from the node."""
    if not isinstance(node.value, str):
        node.value = None
    return node

def nodify(key):
    """Make the key into a node, if it is not one already."""
    if isinstance(key, str):
        return Node(key)
    if isinstance(key, Node):
        return key
    return None

def update_codes(node, codes):
    encoding = ''
    collect_encodings(node, encoding, codes)

def collect_encodings(node, encoding, codes):
    """Collect all codes by traversing the Huffman tree."""
    if node.value is None and not (node.has_left_subtree() or node.has_right_subtree()):
        return
    if not (node.has_left_subtree() or node.has_right_subtree()):
        # Once we reach a leaf node, update the dictionary using the encoding as value.
        codes[node.value] = encoding
        return
    if node.has_left_subtree():
        encoding += '0'
        collect_encodings(node.left, encoding, codes)
        # Remove the last bit/character after the recursive call.
        encoding = encoding[:-1]
    if node.has_right_subtree():
        encoding += '1'
        collect_encodings(node.right, encoding, codes)
        # Remove the last bit/character after the recursive call.
        encoding = encoding[:-1]

def huffman_decoding(data, tree):
    """Collect decoded data by visiting the leaves of the Huffman tree according to the data."""
    # No need for a recursive function, because we are not really traversing the tree.
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

def mk_int(str, base):
    """This is a version of int() that works for empty string."""
    return int(str, base) if str else 0

if __name__ == "__main__":
    main()
