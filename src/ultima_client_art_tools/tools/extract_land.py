"""
Extract all land/terrain tiles from the mod client (IDs 0x0000–0x3FFF).
Outputs PNGs to output/art/land/.
"""

import os
from tqdm import tqdm

from core.client import UOClient
from core.exporter import save_image
from config import MOD_CLIENT, OUTPUT_DIR

LAND_TILE_MAX = 0x4000  # 16384 terrain entries


def run():
    client     = UOClient(MOD_CLIENT)
    output_dir = os.path.join(OUTPUT_DIR, "art", "land")
    saved      = 0
    skipped    = 0

    for tile_id in tqdm(range(LAND_TILE_MAX), desc="Extracting land tiles"):
        try:
            tile = client.get_land(tile_id)
            if tile is None:
                skipped += 1
                continue
            filename = f"{tile_id:04x}.png"
            save_image(tile, output_dir, filename)
            saved += 1
        except Exception:
            skipped += 1

    print(f"[extract_land] Saved: {saved}  Skipped: {skipped}")
