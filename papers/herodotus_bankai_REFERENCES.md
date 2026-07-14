# Herodotus & Bankai — Reference Library

Research references for a masters thesis on **trustless cross-chain intents using storage proofs + consensus proofs + ZK**.

All URLs below were verified to resolve (HTTP 200) as of 2026-07-14.

---

## 1. Herodotus

Herodotus is the team leading research and productization of **storage proofs** — trustless
proving of Ethereum state (all the way back to genesis) using Merkle Patricia Trie (MPT)
verification, Merkle Mountain Ranges (MMR), and Cairo/STARK proving on Starknet.

### Homepage & Docs

| Resource | URL |
|---|---|
| Homepage (developer site) | https://herodotus.dev |
| Developer Docs | https://docs.herodotus.dev |
| Herodotus Cloud (product / APIs) | https://www.herodotus.cloud |
| Storage Proofs docs | https://docs.herodotus.dev/herodotus-docs/developers/storage-proofs |
| GitHub org | https://github.com/HerodotusDev |

### Background reading

| Resource | URL |
|---|---|
| StarkWare blog — "Proving Ethereum's State Using Storage Proofs on Starknet" | https://starkware.co/blog/proving-ethereums-state-on-starknet-with-herodotus/ |
| Medium — "Herodotus 101" (intro to storage proofs) | https://herodotusdev.medium.com/herodotus-101-ab1dd19155cb |
| Herodotus Cloud — "Ethereum Storage Proofs: What They Are, How They Work" | https://www.herodotus.cloud/en/learn/ethereum-storage-proofs |

### Key repositories

| Repo | URL | What it does |
|---|---|---|
| **trie-proofs** | https://github.com/HerodotusDev/trie-proofs | Comprehensive transaction/receipt **MPT proofs handler** for Ethereum / Starknet (Rust). Builds tries per the respective MPT specs. Directly relevant to storage-proof verification. |
| **hdp-cairo** | https://github.com/HerodotusDev/hdp-cairo | Herodotus Data Processor: a **STARK-provable modular framework** that runs user-defined logic over multi-chain data in Cairo. Core proof-generation engine. |
| **cairo-lib** | https://github.com/HerodotusDev/cairo-lib | General-purpose **Cairo library** (data structures, hashing, MPT/MMR primitives) used across Herodotus Cairo code. |
| **eth_essentials** | https://github.com/HerodotusDev/eth_essentials | Cairo utilities library for **Ethereum primitives** (RLP, keccak, MPT helpers) used by the provers. |
| **integrity** | https://github.com/HerodotusDev/integrity | **Cairo STARK proof verifier** deployed on Starknet; verifies proofs on-chain via a FactRegistry that stores verified-proof facts. |
| **cairo-mmr** | https://github.com/HerodotusDev/cairo-mmr | **Merkle Mountain Range in Cairo** (Pedersen hash); stateless MMR for off-chain proof generation and peak computation. |
| **solidity-mmr** | https://github.com/HerodotusDev/solidity-mmr | **Solidity MMR** library implementation. |
| **rust-accumulators** | https://github.com/HerodotusDev/rust-accumulators | Rust **accumulators** library — Merkle trees and MMR — used for off-chain proof construction. |
| **offchain-evm-headers-processor** | https://github.com/HerodotusDev/offchain-evm-headers-processor | Cairo-based **EVM block-header processor** (accumulates headers into an MMR for historical proofs). Notably, Bankai's `mmr-header-accumulator` is forked from this repo. |
| **hdp-sp1** | https://github.com/HerodotusDev/hdp-sp1 | Herodotus Data Processor using the **SP1 zkVM** proving backend. |
| **stwo-gnark-verifier** | https://github.com/HerodotusDev/stwo-gnark-verifier | Groth16 wrapper (Go) for the **STWO** proof system — wraps STARK proofs for cheap on-chain (EVM) verification. |
| **satellite** | https://github.com/HerodotusDev/satellite | Diamond-pattern **EVM indexing / on-chain contracts** for storage proofs. |
| **L2-indexer** | https://github.com/HerodotusDev/L2-indexer | Indexer for **Ethereum L2s** (OP Stack, Arbitrum) (Rust). |
| **hcloud** | https://github.com/HerodotusDev/hcloud | **TypeScript SDK + CLI** for Herodotus Cloud. |
| **herodotus-evm** (archived) | https://github.com/HerodotusDev/herodotus-evm | Legacy Herodotus **EVM contracts** for storage proofs (Solidity). |

> Most relevant to the thesis (storage proofs + MPT + Cairo + verifiers): **trie-proofs**,
> **hdp-cairo**, **cairo-lib**, **eth_essentials**, **integrity**, **cairo-mmr**,
> **offchain-evm-headers-processor**.

---

## 2. Bankai

**Bankai** does **ZK consensus proving** — proving that a block legitimately belongs to a
chain via Ethereum consensus / light-client proving. Its distinguishing design is a
**stateless light client** that runs off-chain: instead of a stateful on-chain contract that
requires perpetual updates, consensus is compressed into deterministic recursive-STARK proofs
derived from finalized chain history, so state is passed cryptographically between proofs
(a self-contained, portable certificate of the canonical chain). This is complementary to
Herodotus's storage proofs: Bankai proves *which block header is canonical*, storage proofs
prove *what state that header commits to*.

**Association with Herodotus:** Bankai grew out of / is associated with the Herodotus
ecosystem. Bankai's `mmr-header-accumulator` repo is a fork of Herodotus's
`offchain-evm-headers-processor`, and Bankai reuses Herodotus Cairo tooling.

**Cofounder "Paul" (verified):** **Paul Etscheit** — sole author of the Bankai research paper,
listed with affiliation "Bankai" and email **paul@bankai.xyz**. GitHub: https://github.com/petscheit
(handle `petscheit`; the `bankaixyz/bankai-cairo` repo is forked from his `petscheit/bankai-2`).
The original prototype lives at https://github.com/petscheit/bankai .

### Homepage, docs & social

| Resource | URL |
|---|---|
| Homepage | https://bankai.xyz/ |
| Docs | https://docs.bankai.xyz |
| GitHub org | https://github.com/bankaixyz |
| Sepolia explorer | https://sepolia.explorer.bankai.xyz |
| Blog (Substack) | https://bankaixyz.substack.com/ |
| Twitter / X | https://x.com/bankaihq |
| Original prototype (Paul Etscheit) | https://github.com/petscheit/bankai |

### Papers / writeups

| Item | URL | Downloaded locally? |
|---|---|---|
| **Research paper — "Stateless Light Clients for PoS Blockchains"** by Paul Etscheit (Bankai). Presents a stateless PoS light-client design using recursive STARKs to compress the chain's validation history into a single constant-sized proof; eliminates stateful on-chain contracts by passing state cryptographically between proofs; tracks the chain via the source protocol's finality gadget (no internal fork-choice needed). Ethereum PoC shows proving costs stabilize at a near-constant rate. 18 pages. | https://cdn.prod.website-files.com/684c03db8ff22a3ad7706bfc/690228ed425232af0e961bc8_main%20(2).pdf | **YES** → `bankai_research_paper.pdf` (verified: PDF v1.7, 18 pages) |

### Key repositories

| Repo | URL | What it does |
|---|---|---|
| **bankai-cairo** | https://github.com/bankaixyz/bankai-cairo | Cairo circuits for the Bankai light client — verifying **epoch and sync-committee updates** of the Ethereum beacon chain. Forked from `petscheit/bankai-2`. |
| **beacon-state-proof** | https://github.com/bankaixyz/beacon-state-proof | Proofs over the **Ethereum beacon-chain state** (Rust). |
| **bankai-sdk** | https://github.com/bankaixyz/bankai-sdk | **Bankai SDK** (Rust). |
| **bankai-docs** | https://github.com/bankaixyz/bankai-docs | Documentation source (MDX). |
| **bankai-sp1-template** | https://github.com/bankaixyz/bankai-sp1-template | Starter **template using the SP1 zkVM** for Bankai-style proving (Rust). |
| **mmr-header-accumulator** | https://github.com/bankaixyz | Cairo MMR header accumulator, forked from Herodotus's `offchain-evm-headers-processor`. |
| **espresso-light-client** | https://github.com/bankaixyz | Light-client work targeting the Espresso network (Rust). |

> Architecture note (from search of docs/paper): the Bankai Ethereum light client is composed
> of **Cairo0 circuits** for verifying epoch and sync-committee updates, a **Rust client** for
> generating circuit inputs and execution traces, and a **Cairo1 contract on Starknet** for
> decommitting and storing verified beacon-chain headers.

---

## Downloaded files summary

| File | Status |
|---|---|
| `bankai_research_paper.pdf` | Downloaded and verified — real PDF, v1.7, 18 pages. Title: "Stateless Light Clients for PoS Blockchains" (Paul Etscheit, Bankai). |

Everything else above is **link-only** (websites, docs sites, and GitHub repos — no standalone
downloadable PDF exists for them).
