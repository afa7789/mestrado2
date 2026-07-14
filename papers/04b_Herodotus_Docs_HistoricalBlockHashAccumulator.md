# Herodotus Docs — Historical Block Hash Accumulator

> Fonte: https://docs.herodotus.dev/herodotus-docs/protocol-design/historical-block-hash-accumulator

## Core Technology

The system leverages ZK-STARKs and Cairo to establish cryptographic proof of Ethereum blockchain traversal. The mechanism validates the sequential linkage between block headers by confirming that each block's parent hash matches the previous block's actual hash — a process repeated across millions of blocks until reaching genesis.

## Merkle Mountain Range (MMR) Accumulators

During the blockchain traversal, two distinct MMR accumulators are constructed:

1. **Keccak256-based accumulator** — contains provably valid Ethereum block hashes.
2. **Poseidon-based accumulator** — also contains the same valid block hashes.

This dual-accumulator approach was chosen to ensure broad compatibility across different blockchain ecosystems and minimize operational costs on supported networks.

## Efficiency Benefits

Rather than repeating the expensive verification process each time a historical block hash is required, the system performs this traversal once. The append-friendly characteristics of MMRs allow future expansion to cover additional blocks without complete recomputation.

## Use Cases

The accumulators enable verification of arbitrary historical block hashes through inclusion proofs against either the Keccak256 or Poseidon MMR root. This is particularly valuable for storage proofs, which can now reference historical block hashes directly from the accumulator.

The innovation effectively implements functionality equivalent to "EIP-2935 without any protocol-level changes."
