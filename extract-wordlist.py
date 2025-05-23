# Criado por William Bastos (by chor4o)
# Script para extrair palavras alfabéticas de URLs e salvar em um arquivo .txt

import argparse
import re
from urllib.parse import urlparse, parse_qs

def filtrar_palavra(palavra):
    # Apenas letras do alfabeto (a-zA-Z), entre 2 e 30 caracteres
    return re.fullmatch(r'[a-zA-Z]{2,30}', palavra) is not None

def extrair_palavras_de_url(url):
    palavras = []
    try:
        parsed_url = urlparse(url)
    except ValueError as e:
        print(f"⚠️ URL INVALIDA ignorada: {url} (URL INVALIDA)")
        return palavras  # retorna lista vazia e ignora essa URL

    caminho = parsed_url.path.strip('/').split('/')
    palavras.extend(caminho)

    parametros = parse_qs(parsed_url.query)
    for chave, valores in parametros.items():
        palavras.append(chave)
        palavras.extend(valores)

    return [p for p in palavras if p and filtrar_palavra(p)]

def processar_arquivo_de_urls(caminho_arquivo):
    conjunto_palavras = set()

    with open(caminho_arquivo, 'r', encoding='utf-8', errors='ignore') as arquivo:
        for linha in arquivo:
            url = linha.strip()
            if url:
                palavras = extrair_palavras_de_url(url)
                conjunto_palavras.update(palavras)

    return sorted(conjunto_palavras)

def salvar_lista_em_txt(lista, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")

def main():
    parser = argparse.ArgumentParser(description='Extrai apenas palavras alfabéticas de URLs.')
    parser.add_argument('-f', '--file', required=True, help='Arquivo de entrada com as URLs')
    parser.add_argument('-o', '--output', default='palavras.txt', help='Arquivo de saída')

    args = parser.parse_args()

    palavras = processar_arquivo_de_urls(args.file)
    salvar_lista_em_txt(palavras, args.output)

    print(f"✅ Lista salva em: {args.output} ({len(palavras)} palavras)")
    print("by chor4o")

if __name__ == '__main__':
    main()
