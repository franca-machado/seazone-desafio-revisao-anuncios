# seazone-desafio-revisao-anuncios

Proposta de projeto para otimizar e escalonar o processo de revisão de anúncios (Desafio SEAZONE).

## Estrutura do repositório

- `validators.py` - funções de validação (núcleo do MVP)
- `data_loader.py` - carregamento de dados de entrada (JSON)
- `utils.py` - funções auxiliares para salvar relatórios
- `main.py` - script principal para processar um lote de anúncios e gerar relatórios
- `examples/anuncio_exemplo.json` - exemplo de input
- `outputs/reports/` - onde os relatórios gerados serão salvos

## Como rodar

1. Crie um ambiente virtual (opcional):
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
```

2. Instale dependências (se necessário):
```bash
pip install -r requirements.txt
```

3. Rodar o script principal:
```bash
python main.py
```

Os relatórios JSON e CSV serão salvos em `outputs/reports/`.

## Observações

- Ajuste thresholds e palavras-chave em `validators.py` conforme necessário.
- Para integrar com o Airbnb, substitua `data_loader.py` por um scraper ou API client.
- Recomenda-se adicionar logging, testes unitários e configuração externa (YAML) em produção.
