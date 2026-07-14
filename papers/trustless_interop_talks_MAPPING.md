# trustless:// — talks → EIPs, specs e papers

Fonte da lista: `youtube_playlists_ytdlp_REPORT.md` (35 vídeos). Pesquisa consolidada em 2026-07-14. Uma associação só é marcada **alta** quando o título/resumo oficial identifica a tecnologia; **média** quando o documento é base técnica explícita do tema; **baixa** significa material contextual, não que o talk apresente aquele documento.

## Resultado

- Cobertura: **35/35 talks**.
- Talks com EIP/ERC diretamente identificável: **12** (contando talks repetidos sobre EIL/OIF).
- Standards/specs principais: **EIP-7702**, **ERC-4337**, **ERC-7579**, **ERC-7683**, **EIP-7930**, **EIP-7805 (FOCIL)**, EIL, OIF, L2BEAT Stages e Interop Risk Framework.
- PDFs acadêmicos/whitepapers pertinentes encontrados: **2** (*Uniswap v3 Core* e *Towards a Formal Foundation for Blockchain Rollups*), ambos baixados e validados. O PDF de *One Block, One Batch* é material de apresentação, não paper acadêmico, e a URL atualmente retorna 404.
- Importante: vários talks são demos, painéis ou apresentações de produto; nesses casos não existe evidência de um paper subjacente. Eles permanecem anotados, sem “paper” inventado.

## Mapeamento 35/35

| # | Talk / speaker (quando disponível) | EIP, spec ou documento oficial | Paper/whitepaper relacionado | Tipo | Conf. | Evidência | Arquivo/status |
|---:|---|---|---|---|---|---|---|
| 1 | Workshop — How to build a Stage 2 Ethereum Rollup | L2BEAT Stages Framework | *Towards a Formal Foundation for Blockchain Rollups* (arXiv:2406.16219), contextual | framework + paper | alta/média | [L2BEAT Stages](https://l2beat.com/stages); [arXiv](https://arxiv.org/abs/2406.16219) | `trustless_interop_talks/01_Formal_Foundation_Blockchain_Rollups_2406.16219.pdf` — 15 pág. |
| 2 | Workshop — The Art of AMM | AMM design; nenhuma EIP específica verificada | *Uniswap v3 Core* | whitepaper contextual | média | [whitepaper oficial](https://app.uniswap.org/whitepaper-v3.pdf); [docs](https://developers.uniswap.org/docs/protocols/v3/overview) | `trustless_interop_talks/02_Uniswap_v3_whitepaper.pdf` — 9 pág. |
| 3 | Workshop — Faster canonical bridges with multi-proofs (Paul Dowman) | Canonical rollup bridges / multi-proofs; sem EIP única identificada | nenhum paper diretamente demonstrado | design workshop | alta | [Devcon Archive](https://archive.devcon.org/devconnect-arg/trustlessinteroplandscape-workshop-faster-canonical-bridges-with-multi-proofs) | sem paper verificado |
| 4 | Workshop — Building with EIL | Ethereum Interoperability Layer; base em ERC-4337 | nenhum paper associado | protocol docs | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) | docs online |
| 5 | Workshop — Hidden Contract Accounts: Interop through ENS Namechain (taytems.eth, gregskril.eth) | ERC-7579; CREATE2; ENS Namechain/HCA | nenhum paper associado | ERC + architecture | alta | [Devcon Archive](https://archive.devcon.org/devconnect-arg/trustlessinteroplandscape-workshop-hidden-contract-accounts-interop-through-ens-namechain); [ERC-7579](https://eips.ethereum.org/EIPS/eip-7579) | docs online |
| 6 | Workshop — Future-Proofing EOAs: Free EIP-7702 Infra Integration | EIP-7702 | nenhum paper associado | EIP/workshop | alta | [EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) | spec online |
| 7 | Workshop — Effortless DeFi: Extending the EIL SDK | EIL SDK; ERC-4337 | nenhum paper associado | SDK workshop | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) | docs online |
| 8 | Workshop — Open Intents Framework Overview and Demo | OIF; ERC-7683; EIP-7930 | nenhum paper diretamente associado | framework/ERC | alta | [OIF](https://www.openintents.xyz/); [ERC-7683](https://eips.ethereum.org/EIPS/eip-7683); [EIP-7930](https://eips.ethereum.org/EIPS/eip-7930) | docs online |
| 9 | Mislav Javor — Composable Batching | Biconomy composable batching / modular execution; sem EIP verificada | nenhum paper localizado | product research | média | [perfil técnico do autor](https://www.semiosys.org/) | sem paper verificado |
| 10 | Orest Tarasiuk — Cross-chain apps powered by real-time proving | t1 xYield / TEE-based verifiable strategies; não é uma EIP | nenhum paper diretamente associado | demo/product | alta | [Devcon Archive](https://archive.devcon.org/devconnect-arg/trustlessinteroplandscape-orest-tarasiuk-cross-chain-apps-powered-by-real-time-proving) | sem paper verificado |
| 11 | Steven Goldfeder — User-Centric Interoperability | nenhuma EIP/spec específica confirmada | nenhum paper confirmado | talk conceitual | baixa | [vídeo](https://www.youtube.com/watch?v=FHteErjqhMw) | não resolvido |
| 12 | Alex Vinas — CoW Swap’s Multiparty Exec and Cross-Chain Coordination | CoW Protocol fair combinatorial batch auction | *One Block, One Batch* (apresentação técnica relacionada; não paper) | protocol + slides | alta/média | [Devcon Archive](https://archive.devcon.org/devconnect-arg/trustlessinteroplandscape-alex-vinas-cow-swaps-multiparty-exec-and-cross-chain-coordination/); [CoW docs](https://docs.cow.fi/); [PDF histórico](https://archive.devcon.org/resources/6/one-block-one-batch-examining-the-potential-of-frequent-batch-auctions-in-ethereum.pdf) | não baixado — URL retorna 404 em 2026-07-14 |
| 13 | Panel — Agentic intents | OIF/ERC-7683 como contexto, não atribuição comprovada | nenhum paper confirmado | panel/context | baixa | [ERC-7683](https://eips.ethereum.org/EIPS/eip-7683); [vídeo](https://www.youtube.com/watch?v=-pNlSYKmPew) | sem paper verificado |
| 14 | Jim Chang — Chain Abstraction with the OIF | OIF; ERC-7683; EIP-7930 | nenhum paper associado | framework/ERC | alta | [OIF](https://www.openintents.xyz/); [ERC-7683](https://eips.ethereum.org/EIPS/eip-7683) | docs online |
| 15 | Alon Muroch — Compose Network: Connecting Every Corner of Ethereum | Compose Network; spec pública não identificada | nenhum paper confirmado | product talk | baixa | [vídeo](https://www.youtube.com/watch?v=20bPiK0FGDU) | não resolvido |
| 16 | Doris Hernandez — Keystore Layer: Enabling secure, interop wallets | Functor Keystore architecture; smart-account context | nenhum paper associado | architecture | alta | [Devcon Archive](https://archive.devcon.org/devconnect-arg/trustlessinteroplandscape-doris-hernandez-keystore-layer-enabling-secure-interop-wallets); [Functor architecture](https://functor.sh/architecture) | docs online |
| 17 | Panel — Interop protocols: who do you have to trust? | L2BEAT Interop risk categories como referência contextual | nenhum paper confirmado | panel/context | baixa | [L2BEAT Interop](https://l2beat.com/interop/non-minting); [vídeo](https://www.youtube.com/watch?v=aE_kar2r6Pk) | sem paper verificado |
| 18 | Fireside — Trustlessness, Interop, and Ethereum’s Future | Trustless Manifesto | nenhum paper associado | manifesto/discussion | média | [Trustless Manifesto](https://trustlessness.eth.limo/); [vídeo](https://www.youtube.com/watch?v=bs-SrOqL7lI) | web |
| 19 | Yoav Weiss — Trust-Minimized Interop with EIL | EIL; ERC-4337 | nenhum paper associado | protocol design | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [Ethereum Foundation](https://blog.ethereum.org/en/2025/11/18/eil) | docs online |
| 20 | Aram Kocharyan — TRAIN Protocol | TRAIN trustless bridging / atomic-swap design; sem EIP | nenhum paper acadêmico confirmado | protocol/product | alta | [TRAIN official](https://www.train.tech/about); [vídeo](https://www.youtube.com/watch?v=ODPq7ztzWoM) | docs online |
| 21 | Barnabé Monnot — Open Intents in Patagonia | OIF; ERC-7683; EIP-7930 | nenhum paper associado | framework/research program | alta | [OIF](https://www.openintents.xyz/); [ERC-7683](https://eips.ethereum.org/EIPS/eip-7683) | docs online |
| 22 | Marissa Posner — Opening | agenda/manifesto; nenhuma spec específica | nenhum | opening | baixa | [vídeo](https://www.youtube.com/watch?v=Yjf_WeS_NVg) | N/A |
| 23 | interop.landscape — Main-stage livestream | agrega talks 9–22; sem spec própria | nenhum | recording | alta | [vídeo](https://www.youtube.com/watch?v=eIuSwSSTPKk) | duplicata programática |
| 24 | interop.landscape — Workshops livestream | agrega workshops 1–8; sem spec própria | nenhum | recording | alta | [vídeo](https://www.youtube.com/watch?v=R5mNGF5gOcM) | duplicata programática |
| 25 | Kaan Uzdogan — Why Contract Verification Needs to Open Up | contrato/source verification; nenhuma EIP específica confirmada | nenhum paper confirmado | talk/tooling | baixa | [vídeo](https://www.youtube.com/watch?v=S8QarbmvpcA) | não resolvido |
| 26 | Panel — Banks won’t go onchain until we fix privacy | nenhuma spec específica atribuível pelo título | nenhum paper confirmado | panel | baixa | [vídeo](https://www.youtube.com/watch?v=y_FB_c5RQvU) | não resolvido |
| 27 | Bartek Kiepuszewski — Interop Risk Framework by L2BEAT | L2BEAT Interop Risk Framework | nenhum paper acadêmico identificado | risk framework | alta | [L2BEAT publications](https://l2beat.com/publications); [Interop](https://l2beat.com/interop/non-minting) | framework online |
| 28 | Soispoke — FOCIL: Restoring Censorship Resistance on Ethereum | EIP-7805 FOCIL | nenhum paper separado necessário: EIP é a especificação primária | EIP | alta | [EIP-7805](https://eips.ethereum.org/EIPS/eip-7805) | spec online |
| 29 | Fireside — The Trustless Manifesto | Trustless Manifesto | nenhum paper | manifesto/discussion | alta | [Manifesto](https://trustlessness.eth.limo/); [vídeo](https://www.youtube.com/watch?v=EN89rbPbiYo) | web |
| 30 | Vitalik Buterin — Why Trustlessness Now? | Trustless Manifesto | nenhum paper atribuído | keynote/manifesto | alta | [Manifesto](https://trustlessness.eth.limo/); [vídeo](https://www.youtube.com/watch?v=nUJcMMv76NM) | web |
| 31 | Marissa Posner — Trustlessness Is The Standard: The Ethereum Interop Layer | EIL; ERC-4337 | nenhum paper | protocol overview | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [EF EIL](https://blog.ethereum.org/en/2025/11/18/eil) | docs online |
| 32 | Ivo Georgiev — Integrating EIL into Ambire | EIL SDK; ERC-4337 | nenhum paper | integration/demo | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [vídeo](https://www.youtube.com/watch?v=Fn7Jpwt_r2g) | docs online |
| 33 | Ofir Eliasi — Abstract the Hard Parts: A practical demo of Stitch | Stitch; nenhuma EIP específica confirmada | nenhum paper | product demo | baixa | [vídeo](https://www.youtube.com/watch?v=gexdweMuxbA) | não resolvido |
| 34 | Shahaf Nacson — Understanding EIL: A Deep Dive | EIL; ERC-4337 | nenhum paper | protocol deep dive | alta | [EIL docs](https://docs.ethereuminteroplayer.com/); [ERC-4337](https://eips.ethereum.org/EIPS/eip-4337) | docs online |
| 35 | Yoav Weiss — Making Ethereum Feel Like One Chain Again | EIL; ERC-4337 | nenhum paper | protocol vision | alta | [Ethereum Foundation](https://blog.ethereum.org/en/2025/11/18/eil); [EIL docs](https://docs.ethereuminteroplayer.com/) | docs online |

## Gaps que ainda exigiriam inspeção do vídeo/slides

Os talks 11, 13, 15, 17, 25, 26 e 33 não permitem atribuir uma spec/paper com segurança somente pelo título e fontes encontradas. Os livestreams 23–24 são gravações agregadas, não conteúdo técnico independente. Para esses casos, o próximo passo correto é obter transcript/slides; busca por palavras-chave sozinha teria alto risco de falso positivo.

## PDFs locais e pendência

1. `01_Formal_Foundation_Blockchain_Rollups_2406.16219.pdf` — arXiv:2406.16219, 15 páginas, validado com `file` e `pdfinfo`.
2. `02_Uniswap_v3_whitepaper.pdf` — whitepaper oficial do Uniswap v3, 9 páginas, validado com `file` e `pdfinfo`.
3. *One Block, One Batch* — slides técnicos relacionados; não é paper e a URL histórica retorna 404. Nenhum placeholder foi criado.
