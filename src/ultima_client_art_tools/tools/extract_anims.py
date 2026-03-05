"""
Extract the first frame (action 0, direction 0) for each animation body ID.
Outputs PNGs to output/anims/.

Note: ultimapy's Animations class renders single frames. For full sequences,
iterate over action and direction indices as needed.
"""

import os
from tqdm import tqdm

from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.config import MOD_CLIENT, OUTPUT_DIR

BODY_MAX = 1000
OUTPUT_DIR_ANIMS = os.path.join(OUTPUT_DIR, "anims")


def run():
    os.makedirs(OUTPUT_DIR_ANIMS, exist_ok=True)
    client   = UOClient(MOD_CLIENT)
    saved    = 0
    skipped  = 0

    for body_id in tqdm(range(BODY_MAX), desc="Extracting animations"):
        try:
            frame = client.get_animation_frame(body_id, action=0, direction=0)
            if frame is None:
                skipped += 1
                continue
            path = os.path.join(OUTPUT_DIR_ANIMS, f"{body_id:04d}.png")
            frame.save(path)
            saved += 1
        except Exception:
            skipped += 1

    print(f"[extract_anims] Saved: {saved}  Skipped: {skipped}")
