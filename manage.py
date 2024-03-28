#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

"""
Comandos úteis:
    runserver -> inicia o servidor
    makemigrations blog -> adiciona novas estruturas de tabelas no bd
    migrate blog -> executa as alteracoes do passo anterior
    createsuperuser -> cria um usuario admin (execute esse depois do segundo e terceiro comando)
"""

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LMW.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
