pip# Conversor Word → PDF

## 📌 Descrição
Aplicação desenvolvida em **Python + PySide6** que permite selecionar um arquivo Word (`.docx`) e convertê-lo automaticamente para PDF utilizando a biblioteca **docx2pdf**.  

---

## ⚙️ Instalação e Requisitos

### Pré-requisitos
- Python 3.10+ (recomendado 3.11 ou superior)
- Ambiente virtual configurado (venv)

### Dependências
As principais bibliotecas utilizadas no projeto são:
- **PySide6** → criação da interface gráfica.
- **docx2pdf** → conversão de arquivos Word em PDF.
- **pytest** → execução dos testes unitários.

### Instalação
Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# Crie e ative o ambiente virtual (Windows)

## Table of Contents

<details>

   <summary>Contents</summary>

1. [📌 Descrição](#-descrio)
1. [⚙️ Instalação e Requisitos](#-instalao-e-requisitos)
   1. [Pré-requisitos](#pr-requisitos)
   1. [Dependências](#dependncias)
   1. [Instalação](#instalao)
1. [🧪 Testes Unitários](#-testes-unitrios)
   1. [Estrutura da suíte](#estrutura-da-sute)
   1. [Execução dos testes](#execuo-dos-testes)
1. [🚨 Regressão simulada](#-regresso-simulada)
   1. [Resultado da execução dos testes:](#resultado-da-execuo-dos-testes)
1. [✅ Correção](#-correo)
1. [📖 Conclusão](#-concluso)

</details>
python -m venv venv
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

Arquivo `requirements.txt` sugerido:

```
PySide6
docx2pdf
pytest
pytest-qt
```

---

## 🧪 Testes Unitários

### Estrutura da suíte
Foi criada uma suíte de **20 testes unitários** usando **pytest**, divididos em:  

- ✅ **10 casos positivos**: validam o comportamento esperado da aplicação em situações normais (título da janela, botões criados, campo de texto aceitando valores corretos, extensão `.docx` válida, etc.).  
- ❌ **10 casos negativos**: testam entradas inválidas ou limites, garantindo que o sistema lida corretamente com erros (campo vazio, apenas espaços, extensões erradas como `.txt`, nomes inválidos, caminhos muito longos, apenas símbolos, etc.).  

A suíte cobre tanto **funcionalidades da interface** quanto **tratamento de entradas** no campo de seleção de arquivos.

---

### Execução dos testes
Para rodar os testes, ative o ambiente virtual e utilize:

```bash
pytest -v
```

ou

```bash
python -m pytest -v
```

Exemplo de saída esperada:

```
collected 20 items

tests/test_conversor.py::test_titulo_janela PASSED
tests/test_conversor.py::test_label_texto PASSED
tests/test_conversor.py::test_botao_converter_existe PASSED
...
tests/test_conversor.py::test_input_nome_vazio_com_extensao PASSED

====================== 20 passed in 2.31s ======================
```

---

## 🚨 Regressão simulada

Para validar a suíte, foi solicitado a um colega a criação de um **Pull Request** que introduziu uma regressão:  
- O botão **"Converter para PDF"** foi renomeado incorretamente para `"Converter"`.  

### Resultado da execução dos testes:

```
>       assert janela.btn_convert.text() == "Converter para PDF"
E       AssertionError: assert 'Converter' == 'Converter para PDF'
E         
E         - Converter para PDF
E         + Converter
```

A suíte identificou a falha e bloqueou a integração do código quebrado.

---

## ✅ Correção
O erro foi corrigido restaurando o texto original do botão para `"Converter para PDF"`.  
Após o ajuste, todos os **20 testes passaram novamente**, garantindo que a regressão foi eliminada.

---

## 📖 Conclusão
A suíte de testes:
- Garante o funcionamento da aplicação em cenários normais.  
- Detecta erros e regressões de forma rápida.  
- Facilita a manutenção e evolução do código.  

---
