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

1. **Clona o repositório:**
   ```bash
   git clone [https://github.com/felipe2008jmf-mec/processador-relatorios-gemini.git](https://github.com/felipe2008jmf-mec/processador-relatorios-gemini.git)
   cd processador-relatorios-gemini


2. **Instale as depêndencias**
   ```bash
   pip install streamlit google-genai python-dotenv

3. Configure sua chave API:
   ```bash
   Cria um ficheiro chamado .env na raiz do projeto e adiciona a tua chave da API da seguinte forma: GEMINI_API_KEY=suachaveaqui

5. Execute o código
   ```bash
   streamlit run app.py


<img width="1062" height="920" alt="Captura de tela 2026-11-03 214107" src="https://github.com/user-attachments/assets/b515bf81-d138-422a-abd1-b106c0707b82" />



## AUTOR: Felipe Freitas
