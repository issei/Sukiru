---
name: manage-sf-skills
description: >-
  Manage the Salesforce and Flosum skill collection by adding or updating flosum-specific skills.
  Use when the user wants to ensure the collection is consistent and follows standard conventions.
  Do NOT use for general Salesforce development outside of the Flosum CLI workflow.
license: Apache-2.0
compatibility: Requer Node.js 18+ e acesso à internet (npmjs.com / GitHub)
metadata:
  author: issei
  version: "1.1"
---

# manage-sf-skills

Meta-skill de gestão para instalar e validar skills externas de Salesforce
provenientes do repositório `Jaganpro/sf-skills`.

## Pré-requisitos

- Node.js 18 ou superior instalado (`node --version`)
- Acesso à internet (GitHub + npm registry)
- Executar a partir da raiz do repositório Sukiru

## Instruções passo a passo

### 1. Identificar a skill desejada

Pergunte ao utilizador o nome exato da skill. Exemplos comuns:

| Skill       | Descrição                              |
|-------------|----------------------------------------|
| `sf-apex`   | Desenvolvimento e testes Apex         |
| `sf-lwc`    | Lightning Web Components              |
| `sf-flow`   | Automação com Salesforce Flow         |
| `sf-soql`   | Consultas SOQL e manipulação de dados |

### 2. Instalar a skill via CLI oficial

Execute no terminal a partir da raiz do repositório:

```bash
npx skills add Jaganpro/sf-skills --skill <nome-da-skill>
```

Exemplo concreto:

```bash
npx skills add Jaganpro/sf-skills --skill sf-apex
```

### 3. Validar a instalação

Após a execução, confirme que a skill foi instalada correctamente:

```bash
# Verificar que a pasta foi criada
ls .agents/skills/<nome-da-skill>

# Verificar que o SKILL.md existe e tem frontmatter YAML válido
cat .agents/skills/<nome-da-skill>/SKILL.md
```

A instalação é válida quando:
- A pasta `.agents/skills/<nome-da-skill>/` existe
- O ficheiro `SKILL.md` está presente e contém frontmatter YAML com `name:` e `description:`

### 4. Registar no changelog

Adicionar entrada em `docs/changelog.md`:

```markdown
### Adicionado
- Skill `<nome-da-skill>` instalada via manage-sf-skills (Jaganpro/sf-skills)
```

## Entradas e saídas esperadas

**Entrada:** Nome da skill de Salesforce a instalar (ex: `sf-apex`)  
**Saída:** Pasta `.agents/skills/<nome-da-skill>/` criada com `SKILL.md` válido

## Casos especiais e edge cases

- Se o utilizador não souber o nome exacto, liste as opções da tabela acima e peça confirmação
- Se a pasta já existir, informe o utilizador e **não reinstale** sem confirmação explícita
- Se o comando `npx skills add` falhar por falta de Node.js, remeta à skill `flosum-setup` para preparar o ambiente
- Nunca use esta skill para skills que não sejam do repositório `Jaganpro/sf-skills`

## Referências

- Repositório oficial: https://github.com/Jaganpro/sf-skills
- Padrão de Skills: https://agentskills.io/specification
- Regras locais: `agent.md` (raiz do repositório)
