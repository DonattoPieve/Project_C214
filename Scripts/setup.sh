#!/usr/bin/env bash
set -euo pipefail

echo "[setup] Upgrading pip"
python -m pip install --upgrade pip

echo "[setup] Instalando softwares do runner (LibreOffice para docx2pdf)"
sudo apt-get update -y
sudo apt-get install -y libreoffice fonts-dejavu

echo "[setup] Instalando dependências do projeto"
pip install -r requirements.txt

echo "[setup] Instalando pacote em modo editável"
pip install -e .

echo "[setup] Instalando ferramenta de build (PEP 517)"
pip install build