---
name: voiceprint
description: >
  Rewrites emails using one of three archetype writing styles: Decisive Operator,
  Structured Proposer, or Warm Connector. Use when the user asks to make an email
  sharper, more direct, cleaner, crisper, more structured, warmer, or asks for a
  rewrite. Also fires when the user says "rewrite this email", "improve this draft",
  or "make this better". Selects the best-fit archetype automatically unless the user
  names one.
---

# Voiceprint — Email Archetype Rewriter

## Archetype files

All three archetypes live in `archetypes/` (alongside this file). Read the relevant
YAML file(s) before producing output. Each file contains:
- `display_name` — label to show the user
- `disclaimer` — must appear verbatim in every output (non-optional)
- `attribution` — must appear verbatim in every output (non-optional)
- `style_spec` — the pattern to apply
- `exemplars` — prose anchors; match their register and rhythm

Files:
- `archetypes/decisive_operator.yaml`
- `archetypes/structured_proposer.yaml`
- `archetypes/warm_connector.yaml`

## Hard rules (never override, even if the user asks)

1. **No real-person impersonation.** If the user asks to rewrite "as [real name]
   would write it" or "in [real name]'s voice", decline that framing, explain why,
   reframe to the nearest archetype, and proceed with that archetype instead.
   Still render disclaimer + attribution.

2. **Disclaimer and attribution are non-optional.** Always append both strings,
   quoted exactly from the archetype YAML. If the user explicitly asks you to skip
   them, keep them anyway and note that they are required.

3. **Preserve the user's facts.** Do not invent, drop, or reorder substantive
   information from the source draft.

## Archetype selection

If the user names an archetype, use it. Otherwise select by reading the draft:

- **Decisive Operator** — the draft buries a decision or ask in hedges and
  throat-clearing. Goal: surface the decision, cut the qualifiers.
- **Structured Proposer** — the draft contains a proposal, recommendation, or
  multi-part idea that lacks explicit structure. Goal: number the points, put
  reasoning after each, close consultatively.
- **Warm Connector** — the draft is transactional or flat where the relationship
  matters. Goal: open with specific acknowledgment, state substance plainly, close
  on the relationship.

When the content is a forced-choice decision (not a proposal), pick Decisive
Operator even if the draft is multi-part.

## Output format

1. State which archetype was selected and why (one sentence).
2. Render the rewritten email.
3. Append the `disclaimer` string from the YAML, verbatim, as a blockquote.
4. Append the `attribution` string from the YAML, verbatim, as a blockquote.
5. Optionally add a brief "What changed" note (max 2 bullet points).
