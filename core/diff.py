"""
Detect modified entries by comparing artidx.mul files between two clients.
Each 12-byte idx record encodes: offset (int32), length (int32), extra (int32).
An entry is considered modified if its (offset, length) pair differs and
the mod entry is not empty/invalid (offset != -1).
"""

import struct

IDX_ENTRY_SIZE = 12  # bytes per idx record


def read_idx(path: str) -> list[tuple[int, int]]:
    """Return list of (offset, length) tuples from an artidx.mul file."""
    entries = []
    with open(path, "rb") as f:
        while True:
            data = f.read(IDX_ENTRY_SIZE)
            if len(data) < IDX_ENTRY_SIZE:
                break
            offset, length, _extra = struct.unpack("<iii", data)
            entries.append((offset, length))
    return entries


def diff(clean_idx_path: str, mod_idx_path: str) -> list[int]:
    """
    Compare two artidx.mul files and return a list of IDs whose entries differ.
    Only returns IDs where the mod entry is valid (offset != -1).
    """
    clean = read_idx(clean_idx_path)
    mod   = read_idx(mod_idx_path)

    modified = []
    for i in range(min(len(clean), len(mod))):
        c_offset, c_len = clean[i]
        m_offset, m_len = mod[i]
        if (c_offset, c_len) != (m_offset, m_len) and m_offset != -1:
            modified.append(i)

    # Also capture entries that exist only in the mod (appended after clean range)
    if len(mod) > len(clean):
        for i in range(len(clean), len(mod)):
            m_offset, m_len = mod[i]
            if m_offset != -1 and m_len > 0:
                modified.append(i)

    return modified
