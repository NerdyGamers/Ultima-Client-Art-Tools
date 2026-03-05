"""
Lightweight file hashing utilities for detecting client file changes
without parsing .idx structures — useful for bulk change detection.
"""

import hashlib


def md5_file(path: str, chunk_size: int = 65536) -> str:
    """Return the hex MD5 digest of a file."""
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_file(path: str, chunk_size: int = 65536) -> str:
    """Return the hex SHA-256 digest of a file."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(chunk_size), b""):
            h.update(chunk)
    return h.hexdigest()


def files_differ(path_a: str, path_b: str) -> bool:
    """Return True if two files have different MD5 hashes."""
    return md5_file(path_a) != md5_file(path_b)
