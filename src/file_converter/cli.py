import argparse
import sys
from .core import convert_docx_to_pdf, convert_csv_to_pdf, convert_pptx_to_pdf


def parse_args(argv=None):
    """
    Processa os argumentos de linha de comando.

    Args:
        argv (list[str] | None): lista de argumentos. Se None, usa sys.argv[1:].

    Returns:
        Namespace: objeto com atributos 'input' e 'outdir'.
    """
    parser = argparse.ArgumentParser(
        prog="file-converter",
        description="Conversor de arquivos (.docx, .csv, .pptx) para PDF"
    )
    parser.add_argument("input", help="Arquivo de entrada (extensões suportadas: .docx, .csv, .pptx)")
    parser.add_argument("--outdir", help="Diretório de saída (padrão: ./output)", default=None)

    return parser.parse_args(argv)


def main(argv=None):
    """
    Função principal do CLI.
    Analisa argumentos e executa a conversão.
    Retorna 0 em caso de sucesso e 1 em caso de erro.
    """
    args = parse_args(argv)
    input_file = args.input.lower()

    try:
        if input_file.endswith(".docx"):
            out = convert_docx_to_pdf(args.input, args.outdir)
        elif input_file.endswith(".csv"):
            out = convert_csv_to_pdf(args.input, args.outdir)
        elif input_file.endswith(".pptx"):
            out = convert_pptx_to_pdf(args.input, args.outdir)
        else:
            print("Formato não suportado", file=sys.stderr)
            return 1

        print(f"✅ PDF gerado em: {out}")
        return 0
    except Exception as e:
        print(f"Erro: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
