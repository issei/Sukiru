# Contributing to Sukiru

## Welcome
Sukiru is an open catalog of AI agent skills and workflows, and we welcome your contributions!
This project follows Document Driven Development (DocDD) to ensure documentation remains the source of truth.
For the authoritative project guide, please refer to [agent.md](agent.md).

## Quick checklist
- [ ] Skill folder created at `.agents/skills/<name>/`
- [ ] `SKILL.md` has valid YAML frontmatter (`name`, `description`)
- [ ] Description includes a trigger ("Use when…") and anti-trigger ("Do NOT use for…")
- [ ] `llms.txt` updated with the new entry
- [ ] `README.md` skill table updated
- [ ] `docs/changelog.md` updated under `## [não publicado] → ### Adicionado`
- [ ] No unrelated files modified

## Step-by-step: adding a skill
1. **Fork & clone** the repository from GitHub. This creates a personal workspace for your changes.
2. **Create the skill folder** at `.agents/skills/<name>/`. This keeps all skill-related assets isolated and organized.
3. **Write `SKILL.md`** using the template below. This file is the primary interface between the agent and the skill.
   ```markdown
   ---
   name: nome-da-skill
   description: >-
     Descrição concisa do que a skill faz e QUANDO deve ser ativada.
     Use quando o usuário pedir X, Y ou Z. Não use para A ou B.
   license: Apache-2.0
   metadata:
     author: seu-nome-ou-org
     version: "1.0"
   compatibility: Requer Python 3.11+ e acesso à internet
   ---
   # Nome da Skill
   ...
   ```
4. **Optionally add subdirectories** `scripts/`, `references/`, and `assets/`. This separates executable logic and heavy documentation from the main instructions.
5. **Validate the frontmatter** by running `python3 -c "import yaml; yaml.safe_load(open('.agents/skills/<name>/SKILL.md').read().split('---')[1])"`. This ensures the YAML block is syntactically correct and parsable.
6. **Update `llms.txt`** with a new line `- [<name>](.agents/skills/<name>/SKILL.md): <description>`. This allows LLMs to discover your skill during their discovery phase.
7. **Update `README.md`** skill table with a new row `| **[<name>](.agents/skills/<name>/SKILL.md)** | <description> |`. This makes your skill visible and accessible to human users.
8. **Update `docs/changelog.md`** with an entry under `## [não publicado] → ### Adicionado`. This maintains a chronological record of catalog improvements.
9. **Open a PR** using the commit message format `feat(skills): add <name>`. This triggers the automated CI and human review process.

## Skill quality bar
- Description must be 80–300 characters, start with an active verb, and include both a trigger and an anti-trigger.
- `SKILL.md` body must be under 500 lines; move anything longer to `references/`.
- `metadata.version` must be `"1.0"` on first publish.

## What NOT to do
- Modifying unrelated skills or project configuration files.
- Committing secrets, API keys, or personal credentials.
- Using a Markdown table for frontmatter instead of a YAML block.
- Leaving `description: >-` empty or too generic.
- Forgetting to link to the `SKILL.md` in the table updates.

## Questions
Open an issue or start a Discussion in the repository.
