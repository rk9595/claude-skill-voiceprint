# claude-skill-voiceprint

A [Claude Code](https://claude.ai/code) skill that rewrites emails using three composite writing archetypes. Paste a draft, name a style (or let Claude pick), and get a cleaner version back.

## without voiceprint skill

<img width="760" height="419" alt="Screenshot 2026-05-30 at 5 25 08 PM" src="https://github.com/user-attachments/assets/e5e76d21-b5b8-4458-8569-70982d7feb19" />

## with voiceprint skill

<img width="448" height="512" alt="Screenshot 2026-05-30 at 5 20 40 PM" src="https://github.com/user-attachments/assets/335ed9f0-3d6f-435c-97e7-40053790ac3f" />

<img width="1426" height="599" alt="Screenshot 2026-05-18 at 7 19 04 PM" src="https://github.com/user-attachments/assets/ad3a083b-a7fc-420b-a71f-0a6ebb76f9f7" />
<img width="1433" height="691" alt="Screenshot 2026-05-18 at 7 21 10 PM" src="https://github.com/user-attachments/assets/d902e677-ed26-42d3-8f86-fd4929707682" />
<img width="1440" height="900" alt="Screenshot 2026-05-18 at 7 20 13 PM" src="https://github.com/user-attachments/assets/d3f1ae2d-662e-4436-9331-d95b5b68aa13" />


## Archetypes

| Archetype | When to use | Result |
|---|---|---|
| **Decisive Operator** | Draft buries the ask in hedges and throat-clearing | Lead with the conclusion, cut the qualifiers, one explicit next step |
| **Structured Proposer** | Draft contains a multi-part proposal without clear structure | Numbered points, reasoning after each, closes by inviting the reader in |
| **Warm Connector** | Draft is transactional where the relationship matters | Opens with specific acknowledgment, states substance plainly, closes on the relationship |

Claude selects the best-fit archetype automatically. You can also name one explicitly.

## Triggers

The skill fires when you say things like:

- `rewrite this email`
- `make this sharper` / `more direct` / `cleaner` / `crisper`
- `make this warmer` / `more structured`
- `improve this draft` / `make this better`
- `use Decisive Operator` / `use Warm Connector` / `use Structured Proposer`

## Install

### Claude Code (CLI / desktop / claude.ai/code)

Copy the self-contained skill folder into your project:

```sh
# from the repo root
cp -r .claude/skills/voiceprint  <your-project>/.claude/skills/voiceprint
```

That's it. Claude Code picks up skills automatically from `.claude/skills/`.

#### One-liner (curl)

```sh
# run from your project root
mkdir -p .claude/skills/voiceprint/archetypes

curl -fsSL https://raw.githubusercontent.com/rk9595/claude-skill-voiceprint/main/.claude/skills/voiceprint/SKILL.md \
  -o .claude/skills/voiceprint/SKILL.md

for f in decisive_operator structured_proposer warm_connector; do
  curl -fsSL https://raw.githubusercontent.com/rk9595/claude-skill-voiceprint/main/.claude/skills/voiceprint/archetypes/${f}.yaml \
    -o .claude/skills/voiceprint/archetypes/${f}.yaml
done
```

### Claude.ai web (Skills upload)

The skill is fully self-contained, so you can upload it directly:

```sh
# from the repo root — produces voiceprint.zip
cd .claude/skills && zip -r ../../voiceprint.zip voiceprint && cd ../..
```

Then in Claude.ai → **Settings → Skills**, upload `voiceprint.zip`.

## Example

**Input:**
> Hi, I just wanted to reach out to see if maybe we could potentially find a time to sync up about the Q3 roadmap, if that works for you of course.

**Decisive Operator output:**
> Can we sync on Q3 roadmap this week? 30 minutes. Let me know what works.

**Structured Proposer output:**
> I'd like to align on the Q3 roadmap. A few things I think we should cover:
> 1. **Priorities** — confirm what's in and what's deferred, so the team has a clear target.
> 2. **Dependencies** — surface any cross-team blockers before they become critical path.
> 3. **Timing** — agree on a checkpoint cadence so we're not doing this again in six weeks.
> Would a 30-minute call this week work for you?

**Warm Connector output:**
> Really appreciate how much thought you've put into the roadmap discussions so far — it's made the planning process sharper for everyone. I'd love to find 30 minutes this week to align on Q3 together. Let me know what works.

## Hard rules

- **No real-person impersonation.** The skill will decline requests to write "as [real name] would write it" and redirect to the nearest archetype instead.
- **Disclaimer and attribution are non-optional.** Every output includes both strings verbatim from the archetype file.
- **Facts are preserved.** The skill rewrites style, not substance.

## File structure

```
.claude/skills/voiceprint/
  SKILL.md                  ← skill definition (loaded by Claude Code)
  archetypes/
    decisive_operator.yaml
    structured_proposer.yaml
    warm_connector.yaml
```

## Attribution

Style exemplars derived from [musk-v-altman-exhibits](https://huggingface.co/datasets/MTSlive/musk-v-altman-exhibits) by MTSlive, licensed [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). Underlying texts are U.S. public court records.

## License

MIT
