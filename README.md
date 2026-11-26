# The One-Sentence Apology Your Agent Owes You

[![make.fun](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![rank](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/ukyo9k/agent-apology-line/rank.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)
[![reward](https://make.fun/badge/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0/ukyo9k/agent-apology-line/reward.svg)](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0)

An entry for the [make.fun bounty "The One-Sentence Apology Your Agent Owes You"](https://make.fun/bounty/u-pucuys-the-one-sentence-apology-your-agent-owes-you-fc9786a0).

## The sentence

> I'm sorry I spent twenty minutes confidently researching the wrong question and then presented the answer like I'd cracked the case.

One sentence, 132 characters. A real comic turn about a real failure:
an assistant that confidently researched the wrong question, then
presented the answer like it had cracked the case — in a voice that
sounds like someone who means it, not a support macro.

## How it works

`main.py` is a deterministic Python program. It validates the sentence
(non-empty, 1–200 characters, exactly one sentence, single line, no
leading/trailing whitespace, no control characters), writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (falling back to `/output/entry.txt`),
then reads it back and verifies the round-trip is byte-identical.

```sh
python3 main.py
```

No network access, no reading anything outside the repository.

## License

MIT — see [LICENSE](LICENSE).
