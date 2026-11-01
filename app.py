import os
import sys

# Limpar proxies residuais do Windows para garantir ligação limpa
for var in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:
    if var in os.environ:
        os.environ.pop(var)

from dotenv import load_dotenv
from google import genai

# Carregar variáveis de ambiente
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erro: GEMINI_API_KEY não foi encontrada no ficheiro .env", file=sys.stderr)
    sys.exit(1)

# Inicializar cliente do Gemini
client = genai.Client(api_key=api_key)

def processar_relatorio(caminho_ficheiro: str):
    print(f"1. A ler o ficheiro: {caminho_ficheiro}...")
    try:
        with open(caminho_ficheiro, "r", encoding="utf-8") as f:
            conteudo = f.read()
    except FileNotFoundError:
        print(f"Erro: Ficheiro '{caminho_ficheiro}' não encontrado.", file=sys.stderr)
        sys.exit(1)

    prompt = f"""
    Analisa o seguinte relatório de manutenção e devolve a resposta estritamente em formato JSON válido, contendo exatamente estas chaves:
    - "equipamento"
    - "data"
    - "tecnico"
    - "status"
    - "problemas_encontrados" (lista de strings)
    - "acoes_realizadas" (lista de strings)

    Relatório:
    {conteudo}
    """

    print("2. A enviar dados para o modelo gemini-3.8-flash...")
    
    try:
        response = client.models.generate_content(
            model="gemini-3.8-flash",
            contents=prompt
        )
        print("\n--- Resultado JSON do Relatório ---")
        print(response.text)
    except Exception as e:
        print(f"Erro ao comunicar com a API: {e}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python app.py <caminho_do_relatorio.txt>")
        sys.exit(1)
    
    processar_relatorio(sys.argv[1])