# Huffman Coding in python

#string = 'BCAADDDCCACACAC'


# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_code_tree(l, True, binString + '0'))
    d.update(huffman_code_tree(r, False, binString + '1'))
    return d


# Calculating frequency
# freq = {}
# for c in string:
#     if c in freq:
#         freq[c] += 1
#     else:
#         freq[c] = 1

freq={'B':5,'A':3,'C':4,'D':9}

freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]  #taking smallest char
    (key2, c2) = nodes[-2]  #taking next smallest char
    nodes = nodes[:-2]      #removing these last two nodes from dict
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))   #adding frequiences

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)  # now after adding new node we are again sorting dict

huffmanCode = huffman_code_tree(nodes[0][0])


for (char,freq) in huffmanCode.items():
    print(char,freq)

# print(huffmanCode)
# print(' Char | Huffman code ')
# print('----------------------')
# for (char, frequency) in freq:
#     print(' %-4r |%12s' % (char, huffmanCode[char]))