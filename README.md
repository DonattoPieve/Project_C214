# Conversor de Arquivos → PDF  

## 📌 Descrição  
Aplicação desenvolvida em **Python + PySide6** que permite selecionar arquivos nos formatos:  

- 📝 **Word (`.docx`)** → PDF  
- 📊 **CSV (`.csv`)** → PDF  
- 🎤 **PowerPoint (`.pptx`)** → PDF  

A aplicação possui:  
- **Interface gráfica moderna (dark mode)**  
- **Linha de comando (CLI)**  
- **Suíte de testes com +20 cenários (incluindo mocks)**  
- **Estrutura simples para manutenção e evolução**  

---

## ⚙️ Instalação e Requisitos  

### Pré-requisitos  
- Python 3.10+ (recomendado 3.11 ou superior)  
- Ambiente virtual configurado (`venv`)  

### Dependências  
As principais bibliotecas utilizadas no projeto são:  
- **PySide6** → criação da interface gráfica.  
- **docx2pdf** → conversão de arquivos Word em PDF.  
- **pandas** → leitura de arquivos CSV.  
- **python-pptx** → leitura de apresentações PowerPoint.  
- **reportlab** → geração de PDFs a partir de CSV e PPTX.  
- **pytest / pytest-qt** → execução da suíte de testes.  

### Instalação  
Clone o repositório e instale as dependências:  

```bash
git clone https://github.com/DonattoPieve/Project_C214.git
cd Project_C214

# Crie e ative o ambiente virtual (Windows)
python -m venv venv
venv\Scripts\activate

# No Linux/Mac
# source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

Arquivo `requirements.txt` sugerido:  

```
PySide6
docx2pdf
pandas
python-pptx
reportlab
pytest
pytest-qt
```

---

## ▶️ Como usar  

### Interface gráfica  
```bash
python -m word2pdf.gui
```
Ou, se instalado via `pip`:  
```bash
word2pdf-gui
```

### Linha de comando (CLI)  
```bash
word2pdf caminho/arquivo.docx
word2pdf caminho/arquivo.csv
word2pdf caminho/arquivo.pptx --outdir saida/
```

---

## 🧪 Testes Unitários  

### Estrutura da suíte  
Foi criada uma suíte de **+20 testes** usando **pytest**, divididos em:  

- ✅ **Casos positivos**: conversão correta de arquivos, botões da GUI, parsing de argumentos no CLI.  
- ❌ **Casos negativos**: caminhos inexistentes, extensões inválidas, campo vazio, etc.  
- 🎭 **Mocks**: 2 testes utilizam `monkeypatch` para simular falhas ou interceptar chamadas externas.  

### Execução dos testes  
```bash
pytest -v
```

Com cobertura:  
```bash
pytest --cov=word2pdf --cov-report=html
```

---

## ✨ Recursos extras  

- 🎨 **Dark mode** aplicado globalmente.  
- 🔗 **Assinatura com link clicável** no rodapé da janela:  
  [Desenvolvido por Donatto Pieve — GitHub](https://github.com/DonattoPieve/Project_C214)  

---

## 👨‍💻 Desenvolvedores  

| Desenvolvido por | GitHub |
|------------------|--------|
| **Donatto Pieve** | [github.com/DonattoPieve](https://github.com/DonattoPieve) |

---

## 📖 Conclusão  
A suíte de testes e a organização do projeto garantem:  
- Qualidade e manutenção da aplicação.  
- Detecção de regressões rapidamente.  
- Facilidade para expandir novas funções (ex: suporte a Excel ou imagens).  
