
import hashlib
import time

blockchain = []

def create_genesis_block():
    return {'index': 0, 'timestamp': str(time.time()), 'data': 'Genesis Block', 'prev_hash': '0', 'hash': ''}

def hash_block(block):
    block_string = f"{block['index']}{block['timestamp']}{block['data']}{block['prev_hash']}"
    return hashlib.sha256(block_string.encode()).hexdigest()

def add_block(data):
    global blockchain
    if not blockchain:
        genesis = create_genesis_block()
        genesis['hash'] = hash_block(genesis)
        blockchain.append(genesis)
    last_block = blockchain[-1]
    new_block = {
        'index': len(blockchain),
        'timestamp': str(time.time()),
        'data': str(data),
        'prev_hash': last_block['hash'],
        'hash': ''
    }
    new_block['hash'] = hash_block(new_block)
    blockchain.append(new_block)
