# Processador Inteligente de Relatórios de Manutenção (Gemini API)

Ferramenta desenvolvida em **Python** para automatizar a leitura e a estruturação de relatórios de manutenção industrial não estruturados, transformando texto livre em dados JSON precisos utilizando a inteligência artificial do **Google Gemini**.

---

## Funcionalidades
- **Análise de Texto Livre:** Lê relatórios operacionais em formato de texto.
- **Extração Estruturada:** Converte automaticamente detalhes críticos (equipamento, data, técnico responsável, status, problemas encontrados e ações corretas) para formato **JSON**.
- **Resiliência de Rede:** Inclui lógica integrada de limpeza de variáveis de proxy locais do Windows para garantir ligações estáveis em ambientes restritos.

---

## Tecnologias Utilizadas
- **Python 3.x**
- **Google GenAI SDK (`google-genai`)**
- **Python-Dotenv** (gestão segura de variáveis de ambiente)

---

## Como Executar o Projeto

1. **Cria e ativa um ambiente virtual:**
   ```bash
   python -m venv .venv
   # No Windows (PowerShell):
   .venv\Scripts\Activate

2. **Instale as depêndencias**
   ```bash
   pip install google-genai python-dotenv

3. Configure sua chave API:
   ```bash
   Cria um ficheiro chamado .env na raiz do projeto e adiciona a tua chave da API da seguinte forma: GEMINI_API_KEY=suachaveaqui

5. Execute o código
   ```bash
   python app.py

## EXEMPLO DE SAÍDA
```bash
{
  "cliente": "Carlos Silva",
  "categoria": "Suporte Técnico",
  "urgencia": "Alta",
  "resumo_problema": "Falha de conexão persistente após atualização do sistema.",
  "resposta_sugerida": "Olá Carlos, lamentamos o transtorno. Identificamos que a falha pode estar relacionada com o cache da última atualização. Poderia tentar reiniciar o equipamento e seguir os passos..."
}
```


## AUTOR: Felipe Freitas
