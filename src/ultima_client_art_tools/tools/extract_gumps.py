"""
Extract all UI gumps from the mod client.
Scans the full gump ID range and exports non-null entries as PNGs
to output/gumps/.
"""

import os
from tqdm import tqdm

from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.core.exporter import save_image
from ultima_client_art_tools.config import MOD_CLIENT, OUTPUT_DIR

GUMP_SCAN_MAX = 200_000


def run():
    client     = UOClient(MOD_CLIENT)
    output_dir = os.path.join(OUTPUT_DIR, "gumps")
    saved      = 0
    skipped    = 0

    for gump_id in tqdm(range(GUMP_SCAN_MAX), desc="Extracting gumps"):
        try:
            gump = client.get_gump(gump_id)
            if gump is None:
                skipped += 1
                continue
            filename = f"{gump_id:05x}.png"
            save_image(gump, output_dir, filename)
            saved += 1
        except Exception:
            skipped += 1

    print(f"[extract_gumps] Saved: {saved}  Skipped: {skipped}")
