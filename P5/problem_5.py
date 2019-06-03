import hashlib
import datetime
import json

def generate_time():
    fmt = '%Y-%m-%d %H:%M:%S.%f %Z'
    return datetime.datetime.now(datetime.timezone.utc).strftime(fmt)

class Block:

    def __init__(self, data):
        self.data = data
        self.previous = None
        self.previous_hash = None
        self.timestamp = generate_time()
        self.hash = None

    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.serialize().encode('utf-8'))
        return sha.hexdigest()

    def serialize(self):
        return json.dumps(str(vars(self)))

    def set_hash(self, hash):
        self.hash = hash

    def get_hash(self):
        return self.hash

class BlockChain:

    def __init__(self, block):
        self.tail = block
        # Compute the hash right away, since there is no previous block.
        block.set_hash(block.calc_hash())

    def get_tail(self):
        return self.tail

    def add_block(self, block):
        tail = self.get_tail()
        block.previous = tail
        block.previous_hash = block.previous.get_hash()
        # Now that we have provided previous and previous_hash, we could compute
        # the hash.
        block.set_hash(block.calc_hash())
        self.tail = block

    def print_blockchain(self):
        pointer = self.get_tail()
        while pointer:
            previous_hash = pointer.previous_hash if pointer.previous_hash else 'None'
            print('------------------------------------------------------------\n'
                  'Data: ' + pointer.data + '\n' +
                  'Timestamp: ' + pointer.timestamp + '\n' +
                  'Previous hash: ' + previous_hash + '\n' +
                  'Hash: ' + pointer.hash + '\n' +
                  '------------------------------------------------------------\n'
                  '               =============================>')

            pointer = pointer.previous

def main():
    # No empty case, as the block chain constructor requires a block as argument
    tc_1()
    tc_2()
    tc_3()

# block chain with 1 block
def tc_1():
    block_chain = BlockChain(Block('This is the 1st block.'))
    block_chain.print_blockchain()

# block chain with 5 blocks
def tc_2():
    block_chain = BlockChain(Block('This is the 1st block.'))
    block_chain.add_block(Block('This is the 2nd block.'))
    block_chain.add_block(Block('This is the 3rd block.'))
    block_chain.add_block(Block('This is the 4th block.'))
    block_chain.add_block(Block('This is the 5th block.'))
    block_chain.print_blockchain()

# block chain with 10 blocks
def tc_3():
    block_chain = BlockChain(Block('This is the 1st block.'))
    block_chain.add_block(Block('This is the 2nd block.'))
    block_chain.add_block(Block('This is the 3rd block.'))
    block_chain.add_block(Block('This is the 4th block.'))
    block_chain.add_block(Block('This is the 5th block.'))
    block_chain.add_block(Block('This is the 6th block.'))
    block_chain.add_block(Block('This is the 7th block.'))
    block_chain.add_block(Block('This is the 8th block.'))
    block_chain.add_block(Block('This is the 9th block.'))
    block_chain.add_block(Block('This is the 10th block.'))
    block_chain.print_blockchain()

if __name__ == "__main__":
    main()
