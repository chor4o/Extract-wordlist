import argparse
from urllib.parse import urlparse, parse_qs

def extrair_palavras_de_url(url):
    palavras = []

    parsed_url = urlparse(url)

    caminho = parsed_url.path.strip('/').split('/')
    palavras.extend(caminho)

    parametros = parse_qs(parsed_url.query)
    for chave, valores in parametros.items():
        palavras.append(chave)
        palavras.extend(valores)

    return [p for p in palavras if p]

def processar_arquivo_de_urls(caminho_arquivo):
    conjunto_palavras = set()

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            url = linha.strip()
            if url:
                palavras = extrair_palavras_de_url(url)
                conjunto_palavras.update(palavras)

    return sorted(conjunto_palavras)

def salvar_lista_em_txt(lista, caminho_saida):
    with open(caminho_saida, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")

def main():
    parser = argparse.ArgumentParser(description='Extrai palavras de URLs e salva em um .txt.')
    parser.add_argument('-f', '--file', required=True, help='Caminho do arquivo com as URLs')
    parser.add_argument('-o', '--output', default='palavras.txt', help='Nome do arquivo de saída')

    args = parser.parse_args()

    palavras = processar_arquivo_de_urls(args.file)
    salvar_lista_em_txt(palavras, args.output)

    print(f"Lista salva em: {args.output}")

if __name__ == '__main__':
    main()
