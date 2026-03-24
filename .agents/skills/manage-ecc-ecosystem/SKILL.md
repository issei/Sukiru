---
name: manage-ecc-ecosystem
description: >-
  Manage the Everything Claude Code (ECC) agent harness by installing, updating, and configuring its components.
  Use when the user wants to set up or troubleshoot the ECC plugin ecosystem across various platforms.
  Do NOT use for general coding tasks or for installing individual skills outside of ECC.
license: MIT
compatibility: Requer Node.js 18+ e capacidade de execução npx.
metadata:
  author: AI Architect
  version: "1.1"
---

# manage-ecc-ecosystem

Skill agnóstica para gestão do ecossistema ECC. Esta instrução orienta o agente a
invocar comandos CLI adaptados ao seu contexto específico de execução.

## Operação Ciente da Plataforma (Platform-Aware)

Antes de executar qualquer comando, o agente deve identificar o seu ambiente:

1. **Antigravity**: Utilize a ferramenta `@terminal` (PowerShell/CMD).
2. **Devin**: Utilize o terminal `bash` nativo do seu Workspace.
3. **Cursor/VSCode**: Utilize o terminal integrado.

### 1. Invocação da CLI ECC

Utilize o comando base `npx ecc-install` e adapte os parâmetros conforme o seu
suporte nativo:

```bash
# Comando Base (Genérico)
npx ecc-install --skill [module-name]

# Adaptado para Antigravity (se suportado pelo ecc-install)
# npx ecc-install --skill [module-name] --target antigravity

# Adaptado para Devin (se suportado pelo ecc-install)
# npx ecc-install --skill [module-name] --target devin
```

### 2. Fluxo de Instalação

1. O agente identifica o recurso desejado no ECC (regras, segurança ou subagente).
2. Executa a instalação enviando o comando para o seu terminal nativo.
3. Move os ficheiros resultantes para a estrutura de destino local em `.agents/skills/`.

### 3. Verificação de Conformidade (Compliance)

Independente da plataforma, o agente deve validar se a instalação respeita
as regras do repositório Sukiru (`agent.md`):

- **Destino**: Os módulos devem residir em `.agents/skills/`.
- **Formato**: O ficheiro importado DEVE ter frontmatter YAML válido:
  - Deve começar e terminar com `---`.
  - Deve conter `name:` e `description:`.

### 4. Registo no Changelog

Actualize o `docs/changelog.md` do projecto:

```markdown
### Adicionado
- Módulo ECC `<module-name>` importado via manage-ecc-ecosystem.
```

## Casos Especiais

- Se a CLI `ecc-install` falhar, tente usar `npx -y ecc-install` para evitar prompts interactivos.
- Se o agente não tiver permissão de escrita no sistema de ficheiros, reporte o erro imediatamente ao utilizador.

## Referências

- Repositório oficial: https://github.com/affaan-m/everything-claude-code
- Padrão de Skills: https://agentskills.io/specification
- Regras locais: `agent.md` (raiz do repositório)
