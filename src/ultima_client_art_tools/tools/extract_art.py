"""
Extract static item art that differs between clean and mod clients.
Compares artidx.mul files to identify modified entries, then exports
each modified static as a PNG to output/art/items/.
"""

import os
from tqdm import tqdm

from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.core.diff import diff
from ultima_client_art_tools.core.exporter import save_image
from ultima_client_art_tools.config import CLEAN_CLIENT, MOD_CLIENT, OUTPUT_DIR


def run():
    clean_idx = os.path.join(CLEAN_CLIENT, "artidx.mul")
    mod_idx   = os.path.join(MOD_CLIENT,   "artidx.mul")

    if not os.path.exists(clean_idx):
        print(f"[extract_art] Missing: {clean_idx}")
        return
    if not os.path.exists(mod_idx):
        print(f"[extract_art] Missing: {mod_idx}")
        return

    modified_ids = diff(clean_idx, mod_idx)
    print(f"[extract_art] {len(modified_ids)} modified static entries found.")

    if not modified_ids:
        print("[extract_art] Nothing to export.")
        return

    client     = UOClient(MOD_CLIENT)
    output_dir = os.path.join(OUTPUT_DIR, "art", "items")
    saved      = 0
    skipped    = 0

    for item_id in tqdm(modified_ids, desc="Extracting statics"):
        try:
            art = client.get_static(item_id)
            if art is None:
                skipped += 1
                continue
            filename = f"{item_id:05x}.png"
            save_image(art, output_dir, filename)
            saved += 1
        except Exception as e:
            skipped += 1

    print(f"[extract_art] Saved: {saved}  Skipped: {skipped}")
