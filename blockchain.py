from datetime import datetime


class Blockchain:

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

    def new_block(self, previous_hash=None):
    # Generates new block and adds to the chain (self.chain = [])
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block) # hash method determines this block's hash and adds it to 'block'
        self.pending_transactions = [] # purge (clean out) pending (незавершенные) transactions
        self.chain.append(block) # adds just generated block to the chain
    @staticmethod
    def hash(block):
    # Hashes a block
        pass

    def last_block(self):
    # Returns last block of the chain
       pass

    def new_transaction(self, sender, recipient, amount):
        self.pending_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })
