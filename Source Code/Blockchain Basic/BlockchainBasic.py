"""
File: BlockchainBasic.py
Authors: 
    - Amey Thakur (https://github.com/Amey-Thakur)
    - Mega Satish (https://github.com/msatmod)
Repository: https://github.com/Amey-Thakur/PYTHON-SHORTS
Release Date: January 9, 2022
License: MIT License

Description:
    This module implements a basic Blockchain structure. It demonstrates 
    the core principles of distributed ledgers, including cryptographic 
    hashing, block chaining, and the Proof-of-Work (PoW) consensus mechanism.

Complexity Analysis:
    - Mining: O(2^d) where d is the difficulty (number of leading zeros).
    - Validation: O(n) where n is the number of blocks in the chain.
    - Space: O(n) to store the ledger.

Logic:
    1. Each Block contains: Index, Timestamp, Data, Previous Hash, and Nonce.
    2. Chaining: Each block stores the hash of its predecessor, creating 
       an immutable link.
    3. Proof-of-Work: Miners must find a Nonce such that the Block's Hash 
       starts with a specific number of zeros.
    4. Integrity: Any change in data alters the hash, breaking the link 
       to all subsequent blocks.
"""

import hashlib
import json
import time
from typing import List, Dict


class Block:
    """A single block in the blockchain ledger."""
    def __init__(self, index: int, data: str, previous_hash: str, difficulty: int):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.difficulty = difficulty
        self.hash = self.mine_block()

    def calculate_hash(self) -> str:
        """Calculates the SHA-256 hash of the block contents."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self) -> str:
        """Implements simple Proof-of-Work by finding a specific hash prefix."""
        target = "0" * self.difficulty
        current_hash = self.calculate_hash()
        
        while not current_hash.startswith(target):
            self.nonce += 1
            current_hash = self.calculate_hash()
            
        return current_hash


class BlockchainService:
    """Service class for managing the blockchain ledger."""
    
    def __init__(self, difficulty: int = 2):
        self.chain: List[Block] = []
        self.difficulty = difficulty
        self._create_genesis_block()

    def _create_genesis_block(self):
        """Initializes the chain with a genesis block."""
        genesis = Block(0, "Genesis Block", "0", self.difficulty)
        self.chain.append(genesis)

    def add_block(self, data: str):
        """Creates, mines, and adds a new block to the chain."""
        previous_block = self.chain[-1]
        new_block = Block(
            len(self.chain), 
            data, 
            previous_block.hash, 
            self.difficulty
        )
        self.chain.append(new_block)

    def is_chain_valid(self) -> bool:
        """Validates the cryptographic integrity of the entire chain."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            # Re-calculate hash to ensure data hasn't changed
            if current.hash != current.calculate_hash():
                return False

            # Verify link to previous block
            if current.previous_hash != previous.hash:
                return False
                
        return True


def main():
    """Demonstrates blockchain creation, mining, and integrity validation."""
    print("--- Blockchain Basic Service Demo ---")
    
    difficulty = 4
    print(f"Initializing Blockchain (PoW Difficulty: {difficulty})...")
    ledger = BlockchainService(difficulty=difficulty)
    
    transactions = [
        "Amey sends 10 BTC to Mega",
        "Mega sends 5 BTC to Satish",
        "Satish sends 2.5 BTC to Amey"
    ]
    
    for tx in transactions:
        print(f"\nMining block for transaction: '{tx}'...")
        start_time = time.time()
        ledger.add_block(tx)
        duration = time.time() - start_time
        print(f"Block Mined! Hash: {ledger.chain[-1].hash}")
        print(f"Nonce Found: {ledger.chain[-1].nonce} (Time: {duration:.4f}s)")

    print("\n--- Chain Status ---")
    print(f"Total Blocks: {len(ledger.chain)}")
    print(f"Integrity Check: {'Passed' if ledger.is_chain_valid() else 'Failed'}")
    
    # Simulate tampering
    print("\n--- Security Test (Simulating Data Tampering) ---")
    print("Tampering with Block #2 data...")
    ledger.chain[2].data = "Hacker steals 100 BTC"
    print(f"Integrity Check: {'Passed' if ledger.is_chain_valid() else 'Failed (Correctly Detected Tamper)'}")
    
    print("\n--- Demo Complete ---")


if __name__ == "__main__":
    main()
