"""
Classify a tile by name into a broad category string.
Used for organizing extracted art into subdirectories or metadata tags.
"""

CATEGORY_RULES = [
    (["wall", "brick", "stone wall", "fence"], "walls"),
    (["tree", "plant", "bush", "shrub", "flower", "fern", "vine"], "vegetation"),
    (["rock", "cliff", "mountain", "boulder"], "terrain"),
    (["water", "ocean", "river", "swamp", "lake", "lava"], "water"),
    (["chest", "barrel", "crate", "box", "bag"], "containers"),
    (["sword", "axe", "bow", "mace", "staff", "dagger", "spear"], "weapons"),
    (["armor", "helm", "shield", "robe", "cloak"], "armor"),
]

DEFAULT_CATEGORY = "items"


def classify(tile_name: str) -> str:
    """
    Return a category string based on keywords in tile_name.
    Falls back to 'items' if no rule matches.
    """
    name = tile_name.lower()
    for keywords, category in CATEGORY_RULES:
        if any(kw in name for kw in keywords):
            return category
    return DEFAULT_CATEGORY
