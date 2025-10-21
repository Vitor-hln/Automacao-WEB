# Automação Web (Selenium)

Automação para interação com a plataforma AVA usando Selenium.

## Pré-requisitos
- Python 3.10+ (recomendado)
- Google Chrome instalado
- Virtualenv (recomendado)

## Instalação (Linux)
1. Criar e ativar venv:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
2. Instalar dependências:
    ```sh
    pip install -r requirements.txt
    ```
3. Criar `.env` na raiz com variáveis necessárias (usuário, senha, etc.).

## Execução
- Executar como módulo a partir da raiz do projeto:
    ```sh
    python -m src.main
    ```
- Scripts específicos (ex.: inserção de avaliações): execute `src/"inserção de Avaliações.py"` com o venv ativo.

## Estrutura principal
- src/
  - driver/ — browser, ações e páginas (Page Objects)
  - data/ — extract / transform / load
  - utils/ — utilitários
  - main.py — ponto de entrada
  - "inserção de Avaliações.py" — script auxiliar
- requirements.txt
- .env (não commitar)
- tests/ — testes

## Observações e dicas
- Verifique se o VS Code está usando o mesmo interpretador do venv: Command Palette → Python: Select Interpreter.
- Use `python -m pip install -r requirements.txt` se faltar alguma dependência.
- Arquivos/folders com caracteres não-ASCII (ex.: "Automação_web") podem causar problemas; renomeie para `Automacao_web` se necessário.
- Corrigir problemas conhecidos no código (ex.: `ultil` → `until`, retorno do driver em `browser.py`, carregamento relativo do `.env`).
- Há um script para checar dependências importáveis (`check_missing_deps.py`) na raiz — execute com o venv ativo.

## Testes
- Adicionar e rodar testes em `tests/`.

## Licença
- Adicionar arquivo de licença conforme necessário.