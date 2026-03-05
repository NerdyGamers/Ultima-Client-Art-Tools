import sys

from tools import extract_art
from tools import extract_land
from tools import extract_gumps
from tools import extract_anims

TOOLS = {
    "art":   extract_art.run,
    "land":  extract_land.run,
    "gumps": extract_gumps.run,
    "anims": extract_anims.run,
}

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <tool>")
        print("Available tools:", ", ".join(TOOLS.keys()))
        return

    cmd = sys.argv[1].lower()

    if cmd in TOOLS:
        TOOLS[cmd]()
    else:
        print(f"Unknown tool: '{cmd}'")
        print("Available tools:", ", ".join(TOOLS.keys()))

if __name__ == "__main__":
    main()
