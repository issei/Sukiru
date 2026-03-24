# Sukiru 🎯

Biblioteca centralizada de habilidades e fluxos de trabalho especializados para Agentes de IA.

## Catálogo de Skills

| Skill | Descrição |
|---|---|
| **[flosum-auth](.agents/skills/flosum-auth/SKILL.md)** | Authenticate an SFDX org that is connected to Flosum. Run this before any repository, branch, or source operation. Covers both interactive browser login and CI/CD non-interactive flows. |
| **[flosum-branch](.agents/skills/flosum-branch/SKILL.md)** | Create a new Flosum branch, clone an existing branch to local, or inspect branches inside a repository. Use for feature branch workflows, hotfix branching, and release branching. |
| **[flosum-deploy](.agents/skills/flosum-deploy/SKILL.md)** | End-to-end Flosum deployment workflow — validate locally, push to branch, promote via Flosum pipeline, and verify the result. Use when deploying a feature branch to a sandbox or production. |
| **[flosum-repo](.agents/skills/flosum-repo/SKILL.md)** | List Flosum repositories and clone a repository (or a specific branch) to a local directory. Use before branch or source operations when working with a repo for the first time. |
| **[flosum-setup](.agents/skills/flosum-setup/SKILL.md)** | Install and verify all prerequisites for the flosum-sfdx-plugin. Use this before any other Flosum CLI skill or when setting up a fresh machine/CI environment. |
| **[flosum-snapshot](.agents/skills/flosum-snapshot/SKILL.md)** | Create a Flosum org snapshot before a risky deployment or at a release milestone. Snapshots serve as rollback points. Use before promoting to UAT or Production. |
| **[flosum-source-pull](.agents/skills/flosum-source-pull/SKILL.md)** | Pull Salesforce metadata from a Flosum repository branch to a local directory. Use when starting work on a branch, syncing local changes with remote, or retrieving tagged snapshots. |
| **[flosum-source-push](.agents/skills/flosum-source-push/SKILL.md)** | Push local Salesforce metadata from a source folder to a Flosum repository branch. Use after making local changes that need to be committed back to Flosum version control. |
| **[manage-ecc-ecosystem](.agents/skills/manage-ecc-ecosystem/SKILL.md)** | Cria, instala ou invoca regras e subagentes do ecossistema ECC. |
| **[manage-openai-skills](.agents/skills/manage-openai-skills/SKILL.md)** | Importa skills do catálogo oficial `openai/skills` via SVN/Clone. |
| **[manage-sf-skills](.agents/skills/manage-sf-skills/SKILL.md)** | Instala competências Salesforce (Apex, LWC) do repositório Jaganpro. |
| **[test-skill](.agents/skills/test-skill/SKILL.md)** | "Uma skill de teste para validar a estrutura do repositório." |
