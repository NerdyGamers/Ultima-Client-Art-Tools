"""
Path resolution helpers for consistent cross-platform path construction.
"""

import os


def ensure_dir(path: str) -> str:
    """Create directory (and parents) if it doesn't exist. Returns path."""
    os.makedirs(path, exist_ok=True)
    return path


def output_path(base_dir: str, *parts: str) -> str:
    """
    Join base_dir with additional path parts and ensure the directory exists.
    Example: output_path('output', 'art', 'items') -> 'output/art/items'
    """
    full = os.path.join(base_dir, *parts)
    ensure_dir(full)
    return full


def client_file(client_dir: str, filename: str) -> str:
    """Return the full path to a file inside a client directory."""
    return os.path.join(os.path.abspath(client_dir), filename)
