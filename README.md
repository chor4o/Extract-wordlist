# 🦖 URL Word Extractor — by chor4o

Ferramenta que auxilia o time de **Red Team** a extrair palavras significativas de URLs — ideal para **pentests** e criação de **wordlists personalizadas** para **fuzzing** e outras técnicas ofensivas.

A partir de um arquivo `.txt` contendo URLs, o script extrai os **caminhos (paths)** e **parâmetros (query strings)**, filtrando apenas palavras **alfabéticas** (sem símbolos, números ou repetições).

---

## 🚀 Modo de Uso

```bash
python3 wordlist.py -f urls.txt

🔍 Modo Verboso
python3 wordlist.py -f urls.txt -v

💾 Verboso + Saída Personalizada
python3 wordlist.py -f urls.txt -o resultado.txt -v

⚙️ Parâmetros

Comando	Descrição
-f ou --file	Caminho do arquivo de entrada com as URLs
-v ou --verbose	Ativa o modo verboso (mostra processo no terminal)
-o ou --output	Nome do arquivo de saída (palavras.txt por padrão)

🧪 Exemplo de Pipeline
chaos -d exemplo.com | httpx -silent | anew domains
cat domains | gau --threads 5 | anew gau.txt
python3 wordlist.py -f gau.txt -o resultado.txt

Desenvolvido por chor4o
Ferramentas simples, diretas e úteis para automação de segurança ofensiva.
