---
name: manage-openai-skills
description: >-
  Use esta skill quando o utilizador pedir para importar, procurar ou instalar
  uma skill do catálogo oficial da OpenAI (openai/skills). Activa-se em pedidos
  como "instala a skill X da OpenAI", "importa skill openai/skills/..." ou
  "quais skills OpenAI existem". Não use para skills do repositório
  Jaganpro/sf-skills (use manage-sf-skills) nem para skills já presentes
  localmente em .agents/skills/.
license: Apache-2.0
metadata:
  author: issei
  version: "1.0"
compatibility: Requer svn (Subversion) instalado e acesso à internet (github.com)
---

# manage-openai-skills

Meta-skill para importar skills do catálogo público `openai/skills` para o
diretório `.agents/skills/` deste repositório, sem dependência de instaladores
proprietários.

## Pré-requisitos

- `svn` (Subversion) instalado e disponível no PATH (`svn --version`)
- Acesso à internet (github.com)
- Executar a partir da raiz do repositório Sukiru

## Catálogos disponíveis

O repositório `openai/skills` organiza as skills em três sub-catálogos:

| Catálogo        | Caminho GitHub                              | Tipo                |
|-----------------|---------------------------------------------|---------------------|
| `.curated`      | `openai/skills/trunk/skills/.curated/`      | Oficiais / estáveis |
| `.experimental` | `openai/skills/trunk/skills/.experimental/` | Em desenvolvimento  |
| `.system`       | `openai/skills/trunk/skills/.system/`       | Infraestrutura      |

Salvo pedido explícito do utilizador, use sempre `.curated` como catálogo padrão.

## Instruções passo a passo

### 1. Identificar o catálogo e o nome da skill

Pergunte ao utilizador:
1. O nome da skill a importar (ex: `code-review`, `data-analysis`)
2. O catálogo (padrão: `.curated`)

### 2. Exportar a skill via SVN

Execute no terminal a partir da raiz do repositório:

```bash
svn export https://github.com/openai/skills/trunk/skills/<catálogo>/<nome-da-skill>
```

Exemplos concretos:

```bash
# Skill curada
svn export https://github.com/openai/skills/trunk/skills/.curated/code-review

# Skill experimental
svn export https://github.com/openai/skills/trunk/skills/.experimental/data-analysis
```

O `svn export` cria uma pasta `<nome-da-skill>/` no directório actual.

### 3. Mover para o directório de skills local

```bash
# Windows (PowerShell)
Move-Item -Path "<nome-da-skill>" -Destination ".agents/skills/<nome-da-skill>"

# Unix/macOS
mv <nome-da-skill> .agents/skills/<nome-da-skill>
```

### 4. Validar a integridade pós-instalação

Confirme os dois critérios obrigatórios:

```bash
# 4a. Verificar que SKILL.md existe
Test-Path ".agents/skills/<nome-da-skill>/SKILL.md"   # deve retornar True

# 4b. Verificar que o `name` no YAML corresponde ao nome da pasta
Get-Content ".agents/skills/<nome-da-skill>/SKILL.md" | Select-String "^name:"
```

A instalação é válida quando:
- `SKILL.md` existe na pasta importada
- O valor de `name:` no frontmatter YAML corresponde exactamente ao nome da pasta (ex: pasta `code-review` → `name: code-review`)

> ⚠️ Se `SKILL.md` estiver ausente ou o `name` não corresponder, **informe o utilizador** e não prossiga com o registo no changelog.

### 5. Registar no changelog

Adicionar entrada em `docs/changelog.md`:

```markdown
### Adicionado
- Skill `<nome-da-skill>` importada via manage-openai-skills (openai/skills/<catálogo>)
```

## Entradas e saídas esperadas

**Entrada:** Nome da skill + catálogo (ex: `code-review`, `.curated`)  
**Saída:** Pasta `.agents/skills/<nome-da-skill>/` criada com `SKILL.md` válido

## Casos especiais e edge cases

- Se `svn` não estiver instalado: Windows → `winget install TortoiseSVN.TortoiseSVN` / Unix → `sudo apt install subversion`
- Se a pasta de destino já existir, **não sobrescreva** sem confirmação explícita do utilizador
- Se o `SKILL.md` importado não tiver frontmatter YAML válido (sem `---`), sinalize como skill inválida
- Nunca use esta skill para repositórios que não sejam `openai/skills`

## Referências

- Repositório oficial: https://github.com/openai/skills
- Padrão de Skills: https://agentskills.io/specification
- Regras locais: `agent.md` (raiz do repositório)
- Skill relacionada: `manage-sf-skills` (para skills Salesforce)
