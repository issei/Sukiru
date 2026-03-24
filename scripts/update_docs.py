import os
import re

SKILLS_DIR = '.agents/skills'
README_FILE = 'README.md'
LLMS_FILE = 'llms.txt'

def parse_skill_metadata(filepath):
    """Lê o frontmatter de um SKILL.md e extrai o nome e a descrição."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Regex para extrair blocos de frontmatter
            match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return None
            
            yaml_block = match.group(1)
            name_match = re.search(r'^name:\s*(.+)$', yaml_block, re.MULTILINE)
            desc_match = re.search(r'^description:\s*(.+)$', yaml_block, re.MULTILINE)
            
            if name_match and desc_match:
                return {
                    'name': name_match.group(1).strip(),
                    'description': desc_match.group(1).strip(),
                    'path': filepath
                }
    except Exception as e:
        print(f"Erro ao processar {filepath}: {e}")
    return None

def main():
    skills_data = []
    
    # Varrer o diretório de skills
    if os.path.exists(SKILLS_DIR):
        for item in os.listdir(SKILLS_DIR):
            skill_path = os.path.join(SKILLS_DIR, item)
            if os.path.isdir(skill_path):
                md_path = os.path.join(skill_path, 'SKILL.md')
                if os.path.exists(md_path):
                    metadata = parse_skill_metadata(md_path)
                    if metadata:
                        skills_data.append(metadata)
                        
    skills_data.sort(key=lambda x: x['name'])
    
    # 1. Gerar llms.txt (Otimizado para LLMs)
    with open(LLMS_FILE, 'w', encoding='utf-8') as f:
        f.write("# Sukiru: Agent Skills Directory\n\n")
        f.write("Este ficheiro é um índice otimizado para IAs das skills disponíveis neste repositório.\n\n")
        for skill in skills_data:
            skill_path_fixed = skill['path'].replace('\\', '/')
            f.write(f"- [{skill['name']}]({skill_path_fixed}): {skill['description']}\n")
    print(f"✅ {LLMS_FILE} gerado com sucesso.")

    # 2. Atualizar README.md (Tabela para humanos)
    readme_content = "# Sukiru 🎯\n\nBiblioteca centralizada de habilidades e fluxos de trabalho especializados para Agentes de IA.\n\n"
    readme_content += "## Catálogo de Skills\n\n"
    readme_content += "| Skill | Descrição |\n"
    readme_content += "|---|---|\n"
    
    for skill in skills_data:
        skill_path_fixed = skill['path'].replace('\\', '/')
        readme_content += f"| **[{skill['name']}]({skill_path_fixed})** | {skill['description']} |\n"
        
    with open(README_FILE, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print(f"✅ {README_FILE} gerado com sucesso.")

if __name__ == '__main__':
    main()