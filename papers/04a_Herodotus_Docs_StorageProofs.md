# Herodotus Docs — Storage Proofs

> Fonte: https://docs.herodotus.dev/herodotus-docs/developers/storage-proofs
> (conteúdo extraído — documentação técnica, tratada como "paper" pelo contexto do projeto)

## Overview

Blockchains function as cryptographically-secured databases utilizing data structures such as Merkle trees and Merkle Patricia trees. These structures enable proof generation to verify data inclusion.

Ethereum specifically employs Merkle Patricia trees across its State Trie, Receipts Trie, and Transactions Trie.

## Benefits of Merkle Patricia Trees

**Security Enhancement:** By cryptographically hashing data at every level of the tree, it becomes virtually impossible to alter the data without detection. Any modification requires recalculating hashes up to the publicly visible root hash in the blockchain header.

**Efficient Verification:** Rather than scanning the entire blockchain, verification only requires checking a relevant path within the applicable Merkle tree.

## Herodotus Storage Proofs System

Herodotus has developed storage proofs — a system enabling on-chain data access while maintaining base-layer security. This combines three components:

1. **Inclusion Proofs:** Confirm specific data exists within cryptographic structures like Merkle or Merkle Patricia trees.
2. **Proofs of Computation:** Validate multi-step workflows, authenticating data transformations across extensive datasets.
3. **Zero-Knowledge Proofs:** Reduce the data volume smart contracts must process by confirming claims' validity without processing underlying data.

## Key Advantages

- **Data Integrity:** Off-chain generation requires no external trust; invalid proofs fail on-chain verification.
- **Efficiency:** Off-chain generation reduces on-chain resource consumption; minimal data transfer between layers.
- **Flexibility:** Smart contracts access previously inaccessible historical data, such as past transaction gas prices.
