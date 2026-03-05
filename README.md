# Ultima Client Art Tools

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![ultimapy](https://img.shields.io/badge/SDK-ultimapy-green)](https://github.com/jackuoll/ultima-py)

A modular Python toolkit for extracting and exporting Ultima Online client assets. Built on **[ultimapy](https://github.com/jackuoll/ultima-py)**, a Python port of the C# Ultima SDK used by tools like UOFiddler.

Perfect for shard developers, artists, and anyone working with custom UO client content.

---

## ✨ Features

- **🔍 Diff-based extraction** — Compare clean vs modified clients via `.idx` analysis
- **🎨 Static art export** — Extract only modified static items as PNG
- **🗺️ Terrain tiles** — Export all land tiles (0x0000–0x3FFF)
- **🖼️ Gumps** — Extract UI elements and paperdoll graphics
- **🏃 Animations** — Export animation frames by body ID
- **📦 Modular design** — Run individual tools independently
- **🔧 Extensible** — Easy to add custom export logic and classifiers

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- UO client files (clean + modified versions)

### Install via pip

```bash
git clone https://github.com/NerdyGamers/Ultima-Client-Art-Tools.git
cd Ultima-Client-Art-Tools
pip install -r requirements.txt
```

### Quick Install (one-liner)

```bash
pip install ultimapy Pillow tqdm
```

---

## 🚀 Usage

### 1. Setup Client Paths

Place your client files in the `clients/` directory:

```
clients/
├── clean/    ← Vanilla/reference client (art.mul, artidx.mul, etc.)
└── mod/      ← Your modified shard client
```

Or edit `config.py` to point to your client directories.

### 2. Run Extraction Tools

#### Extract Modified Static Art
```bash
python main.py art
```
Compares `artidx.mul` between clean and mod clients, exports only changed entries.

#### Extract All Terrain Tiles
```bash
python main.py land
```
Exports all 16,384 land tile textures as PNG.

#### Extract UI Gumps
```bash
python main.py gumps
```
Scans and exports gump graphics (buttons, windows, paperdolls).

#### Extract Animation Frames
```bash
python main.py anims
```
Exports the first frame of each animation body (action 0, direction 0).

### 3. View Output

All exported assets are saved under `output/`:

```
output/
├── art/
│   ├── items/    ← Modified static items
│   └── land/     ← Terrain tiles
├── gumps/        ← UI graphics
└── anims/        ← Animation frames
```

---

## 📂 Project Structure

```
Ultima-Client-Art-Tools/
│
├── main.py                 # CLI entry point
├── config.py               # Client paths and thresholds
├── requirements.txt        # Python dependencies
│
├── core/
│   ├── client.py           # UOClient wrapper (ultimapy SDK)
│   ├── diff.py             # .idx diff engine
│   └── exporter.py         # PNG export helper
│
├── tools/
│   ├── extract_art.py      # Modified static item extractor
│   ├── extract_land.py     # Terrain tile extractor
│   ├── extract_gumps.py    # Gump extractor
│   └── extract_anims.py    # Animation frame extractor
│
├── readers/
│   └── tile_classifier.py  # Tile categorization by name
│
├── utils/
│   ├── hash_utils.py       # File hashing for bulk change detection
│   └── paths.py            # Path resolution helpers
│
├── clients/
│   ├── clean/              # Reference client directory
│   └── mod/                # Modified client directory
│
└── output/                 # All exported assets
```

---

## 🛠️ Configuration

Edit `config.py` to customize:

```python
CLEAN_CLIENT = "clients/clean"  # Path to vanilla client
MOD_CLIENT   = "clients/mod"    # Path to modified client
OUTPUT_DIR   = "output"         # Export directory

CUSTOM_ART_THRESHOLD = 0x8000   # Items >= this ID are custom
```

---

## 🧪 Examples

### Extract Only Custom Art (IDs >= 0x8000)

```python
from core.client import UOClient
from config import MOD_CLIENT, CUSTOM_ART_THRESHOLD

client = UOClient(MOD_CLIENT)

for item_id in range(CUSTOM_ART_THRESHOLD, 0x10000):
    art = client.get_static(item_id)
    if art:
        art.save(f"output/custom/{item_id:05x}.png")
```

### Classify and Organize by Type

```python
from readers.tile_classifier import classify

for item_id in modified_ids:
    art = client.get_static(item_id)
    category = classify(art.name)  # "walls", "vegetation", "terrain", etc.
    art.save(f"output/{category}/{item_id:05x}.png")
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. **Fork** this repository
2. **Create a feature branch**: `git checkout -b feat/new-extractor`
3. **Commit changes**: `git commit -m "Add texmaps extractor"`
4. **Push**: `git push origin feat/new-extractor`
5. **Open a Pull Request**

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 To-Do

- [ ] Add texture map (texmaps.mul) extractor
- [ ] Add multi-hue (hues.mul) renderer
- [ ] Add CLI progress bars for large scans
- [ ] Add parallel processing for faster extraction
- [ ] Add JSON metadata export (tile names, flags, etc.)
- [ ] Add web UI for browsing extracted assets

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🔗 Links

- **ultimapy SDK**: [jackuoll/ultima-py](https://github.com/jackuoll/ultima-py)
- **UOFiddler**: [Ultima SDK Tools](https://github.com/polserver/UOFiddler)
- **ServUO**: [ServUO Forums](https://www.servuo.com)

---

## 🙏 Acknowledgments

- **[jackuoll](https://github.com/jackuoll)** — ultimapy library maintainer
- **UO community** — Decades of reverse-engineering and tooling
- **ServUO contributors** — Open-source UO server emulator

---

## 📧 Contact

**Repository Owner**: [NerdyGamers](https://github.com/NerdyGamers)

For questions, issues, or feature requests, open an issue on this repository.
