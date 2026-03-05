"""
ultima_client_art_tools
=======================
A modular Python toolkit for extracting and exporting
Ultima Online client assets via the ultimapy SDK.

Install (local):
    pip install -e .

Install (from GitHub):
    pip install git+https://github.com/NerdyGamers/Ultima-Client-Art-Tools.git@feat/python-package

Quick start:
    from ultima_client_art_tools.core.client import UOClient
    client = UOClient("path/to/client")
"""

__version__ = "1.0.0"
__author__ = "NerdyGamers"
__license__ = "MIT"
__all__ = ["core", "tools", "readers", "utils"]
