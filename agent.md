# Agent Guide

> **Leia este arquivo no início de cada sessão.** Ele define como este projeto funciona, como criar Skills, e como manter a documentação sempre atualizada.

---

## Por que este projeto existe

Este repositório usa **Document Driven Development (DocDD)** combinado com o padrão aberto **Agent Skills** para garantir que:

1. A documentação é sempre a **fonte da verdade** — código e comportamentos derivam dela, não o contrário.
2. Capacidades do agente são empacotadas como **Skills reutilizáveis e portáteis** que seguem o padrão [agentskills.io](https://agentskills.io).
3. Cada mudança no projeto atualiza a documentação **antes** (ou junto) do código.

Se a documentação e o código divergem, **a documentação vence**. Corrija o código ou abra uma issue documentando a exceção.

---

## Estrutura do projeto

```
.
├── agent.md                  # Este arquivo — onboarding e regras do agente
├── README.md                 # Visão geral pública do projeto
├── docs/                     # Documentação técnica e histórico
│   ├── architecture.md       # Decisões arquiteturais e ADRs
│   ├── features/             # Specs de funcionalidades
│   │   └── <feature>/
│   │       ├── spec.md       # Requisitos e comportamento esperado
│   │       ├── design.md     # Decisões técnicas da feature
│   │       └── tasks.md      # Breakdown de tarefas
│   └── changelog.md          # Histórico de mudanças (DocDD)
├── .agent/                   # Configurações de infraestrutura do harness
│   └── rules/                # Regras de codificação e padrões (ECC)
├── .agents/                  # Ecossistema de extensaibilidade
│   ├── agents/               # Definições de subagentes especializados
│   ├── commands/             # Comandos customizados para o agente
│   └── skills/               # Skills locais do projeto (padrão agentskills.io)
│       └── <skill-name>/
│           ├── SKILL.md      # Obrigatório: frontmatter YAML + instruções
│           ├── scripts/      # Opcional: scripts executáveis
│           ├── references/   # Opcional: documentação complementar
│           └── assets/       # Opcional: templates, recursos
│   └── workflows/            # Fluxos de trabalho automatizados
└── src/                      # Código-fonte
```


---

## Ciclo DocDD — siga sempre esta ordem

```
1. DOCUMENT   → Escreva ou atualize a spec em docs/features/<feature>/spec.md
2. GENERATE   → Gere o código com base na documentação
3. TEST        → Gere e execute testes que validam a spec
4. REFACTOR   → Melhore estrutura e performance sem quebrar a spec
5. UPDATE     → Revise a documentação para refletir o estado atual
```

**Nunca pule o passo 1.** Se você receber uma tarefa sem spec, crie a spec primeiro e confirme com o usuário antes de escrever código.

**Após qualquer mudança significativa**, execute o passo 5: atualize `docs/features/<feature>/spec.md`, `docs/changelog.md`, e o `README.md` se necessário.

---

## Como criar uma Skill

Skills são o mecanismo de extensão do agente. Siga a especificação oficial do [agentskills.io](https://agentskills.io/specification).

### Estrutura mínima

```
.agents/skills/<skill-name>/
└── SKILL.md
```

### Estrutura recomendada

```
.agents/skills/<skill-name>/
├── SKILL.md           # Obrigatório
├── scripts/
│   └── main.py        # Scripts executáveis (Python, Bash, JS)
├── references/
│   ├── REFERENCE.md   # Documentação técnica detalhada
│   └── FORMS.md       # Templates e formatos de dados
└── assets/
    └── template.txt   # Templates, imagens, recursos
```

### Formato do `SKILL.md`

O arquivo **deve** ter frontmatter YAML seguido de conteúdo Markdown:

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

Breve parágrafo explicando o propósito geral da skill.

## Pré-requisitos

- Lista de dependências ou configurações necessárias

## Instruções passo a passo

1. Primeiro faça X
2. Depois faça Y usando `scripts/main.py`
3. Valide o resultado com Z

## Entradas e saídas esperadas

**Entrada:** Descrição do que o agente recebe  
**Saída:** Descrição do que o agente deve produzir

## Casos especiais e edge cases

- Se acontecer A, então faça B
- Nunca faça C quando D estiver presente

## Referências

- Veja `references/REFERENCE.md` para detalhes técnicos
- Veja `references/FORMS.md` para templates de formulários
```

### Regras do frontmatter

| Campo           | Obrigatório | Regras                                                         |
|-----------------|-------------|----------------------------------------------------------------|
| `name`          | ✅ Sim      | 1–64 chars, minúsculas, hífens, sem espaços. Ex: `pdf-export` |
| `description`   | ✅ Sim      | 1–1024 chars. **Seja preciso sobre quando ativar e quando NÃO ativar.** |
| `license`       | ❌ Não      | Curto: `MIT`, `Apache-2.0`, ou nome do arquivo bundled         |
| `compatibility` | ❌ Não      | 1–500 chars. Inclua só se houver requisitos específicos de ambiente. |
| `metadata`      | ❌ Não      | Mapa `string → string`. Use chaves únicas para evitar conflitos. |

### Boas práticas para escrever Skills

- **Descrição é crítica**: o agente decide se carrega a skill com base nela. Seja explícito sobre triggers e anti-triggers.
- **Mantenha o SKILL.md abaixo de 500 linhas** (ideal < 150). Conteúdo extenso vai em `references/`.
- **Scripts nunca entram no contexto**: apenas o output dos scripts é carregado — isso economiza tokens.
- **Referências são carregadas sob demanda**: inclua muitos arquivos em `references/` sem medo — o agente carrega só o necessário.
- **Não explique o óbvio**: o agente sabe o que é Python. Explique apenas convenções e comandos específicos *deste* projeto.

### Validação

```bash
# Instale o SDK de referência
pip install skills-ref

# Valide uma skill
skills-ref validate .agents/skills/<skill-name>
```

---

## Como manter a documentação atualizada (DocDD)

### Regra de ouro

> **Nenhum PR é aceito se a documentação não reflete o estado atual do código.**

### O que atualizar e quando

| Mudança no projeto                      | O que atualizar                                      |
|-----------------------------------------|------------------------------------------------------|
| Nova feature implementada               | `docs/features/<feature>/spec.md`, `README.md`, `docs/changelog.md` |
| Feature modificada ou removida          | Mesmos arquivos acima + marcar tasks concluídas      |
| Nova Skill criada                       | `SKILL.md` da skill + registrar em `docs/changelog.md` |
| Skill atualizada                        | Bump de `metadata.version` no frontmatter            |
| Decisão arquitetural tomada             | Nova entrada em `docs/architecture.md` (formato ADR) |
| Bug corrigido com impacto em comportamento | Atualizar spec da feature afetada                 |

### Formato do changelog (`docs/changelog.md`)

```markdown
## [não publicado]

### Adicionado
- Skill `pdf-export` para exportação de documentos

### Modificado
- Spec de `user-auth` atualizada para incluir 2FA

### Corrigido
- Comportamento de fallback na skill `data-pipeline`

## [1.2.0] — 2026-03-24

### Adicionado
- ...
```

### Formato de spec de feature (`docs/features/<feature>/spec.md`)

```markdown
# Feature: <Nome>

**Status:** Draft | Em revisão | Aprovado | Implementado | Depreciado  
**Versão:** 1.0  
**Última atualização:** YYYY-MM-DD

## Objetivo

Uma frase descrevendo o que esta feature faz e por que existe.

## Comportamento esperado

Descreva em linguagem natural o que o sistema deve fazer.
Use exemplos concretos de entrada e saída.

## Restrições e regras de negócio

- Regra 1
- Regra 2

## Casos de uso principais

1. Usuário faz X → sistema responde com Y
2. ...

## Fora do escopo

- O que esta feature explicitamente NÃO faz

## Critérios de aceitação

- [ ] Critério 1
- [ ] Critério 2

## Dependências

- Outras features ou serviços dos quais esta depende

## Notas de implementação

Decisões técnicas relevantes que emergiram durante a implementação.
```

### Formato de ADR (`docs/architecture.md`)

```markdown
## ADR-001: <Título da decisão>

**Data:** YYYY-MM-DD  
**Status:** Proposta | Aceita | Substituída por ADR-XXX

### Contexto
O que motivou esta decisão.

### Decisão
O que foi decidido.

### Consequências
Trade-offs e impactos da decisão.
```

---

## Comportamentos esperados do agente

### Ao receber uma tarefa nova

1. Verifique se existe `docs/features/<feature>/spec.md`
2. Se não existir, **crie a spec primeiro** e confirme com o usuário
3. Só então escreva código

### Ao criar uma nova Skill

1. Crie a pasta `.agents/skills/<skill-name>/`
2. Escreva o `SKILL.md` seguindo o formato acima
3. Valide com `skills-ref validate`
4. Registre no `docs/changelog.md`

### Ao modificar código existente

1. Verifique se a mudança altera o comportamento documentado
2. Se sim, atualize a spec **antes** de commitar
3. Atualize `docs/changelog.md`

### Ao encontrar documentação desatualizada

- Sinalize explicitamente para o usuário
- Proponha a atualização antes de continuar

### Ao terminar qualquer tarefa

Confirme que os seguintes itens estão atualizados:
- [ ] Spec da feature (`docs/features/*/spec.md`)
- [ ] Changelog (`docs/changelog.md`)
- [ ] README se a interface pública mudou
- [ ] Versão da Skill se uma Skill foi alterada

---

## Convenções de código

> Substitua esta seção pelas convenções reais do seu projeto.

- **Idioma:** Português para docs, Inglês para código e comentários
- **Commits:** `tipo(escopo): descrição` (Conventional Commits)
- **Branches:** `feat/<nome>`, `fix/<nome>`, `docs/<nome>`
- **Testes:** Deve cobrir todos os critérios de aceitação da spec

---

## Referências

- [Especificação Agent Skills](https://agentskills.io/specification)
- [GitHub agentskills/agentskills](https://github.com/agentskills/agentskills)
- [Document Driven Development (DocDD)](https://docdd.ai)
- [skills-ref — validação e geração de prompts](https://github.com/agentskills/agentskills/tree/main/skills-ref)
