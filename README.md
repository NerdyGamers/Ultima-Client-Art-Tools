# Ultima Client Art Tools

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![SDK: ultimapy](https://img.shields.io/badge/SDK-ultimapy-green)](https://github.com/jackuoll/ultima-py)

A modular Python toolkit for extracting and exporting Ultima Online client assets. Built on **[ultimapy](https://github.com/jackuoll/ultima-py)**, a Python port of the C# Ultima SDK used by tools like UOFiddler.

Perfect for shard developers, artists, and anyone working with custom UO client content.

---

## ✨ Features

- **🔍 Diff-based extraction** — Compare clean vs modified clients via `.idx` analysis
- **🎨 Static art export** — Extract only modified static items as PNG
- **🗺️ Terrain tiles** — Export all land tiles (0x0000–0x3FFF)
- **🖼️ Gumps** — Extract UI elements and paperdoll graphics
- **🏃 Animations** — Export animation frames by body ID
- **📦 Modular design** — Run individual tools independently or via the `uoca` CLI
- **🔧 Extensible** — Easy to add custom export logic and classifiers
- **📦 Installable package** — Proper `src/` layout, `pyproject.toml`, and pip-installable

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- UO client files (clean + modified versions)

### Install from source (recommended)

```bash
git clone https://github.com/NerdyGamers/Ultima-Client-Art-Tools.git
cd Ultima-Client-Art-Tools
pip install -e .
```

This installs the `ultima-client-art-tools` package in editable mode and registers the `uoca` CLI command.

### Install dependencies only

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

### 1. Setup Client Paths

Place your client files in the `clients/` directory:

```
clients/
├── clean/   ← Vanilla/reference client (art.mul, artidx.mul, etc.)
└── mod/     ← Your modified shard client
```

Or edit `src/ultima_client_art_tools/config.py` to point to your client directories.

### 2. Run via the `uoca` CLI

After installing with `pip install -e .`, the `uoca` command is available globally:

```bash
uoca art    # Extract modified static items
uoca land   # Export all terrain tiles
uoca gumps  # Export UI gumps
uoca anims  # Export animation frames
```

### 3. Run directly with Python

```bash
python -m ultima_client_art_tools.main art
```

#### Extract Modified Static Art

```bash
uoca art
```

Compares `artidx.mul` between clean and mod clients, exports only changed entries.

#### Extract All Terrain Tiles

```bash
uoca land
```

Exports all 16,384 land tile textures as PNG.

#### Extract UI Gumps

```bash
uoca gumps
```

Scans and exports gump graphics (buttons, windows, paperdolls).

#### Extract Animation Frames

```bash
uoca anims
```

Exports the first frame of each animation body (action 0, direction 0).

### 4. View Output

All exported assets are saved under `output/`:

```
output/
├── art/
│   ├── items/   ← Modified static items
│   └── land/    ← Terrain tiles
├── gumps/       ← UI graphics
└── anims/       ← Animation frames
```

---

## 📂 Project Structure

```
Ultima-Client-Art-Tools/
│
├── src/
│   └── ultima_client_art_tools/
│       ├── __init__.py
│       ├── main.py          # CLI entry point + cli() console script
│       ├── config.py        # Client paths and thresholds
│       ├── core/
│       │   ├── client.py    # UOClient wrapper (ultimapy SDK)
│       │   ├── diff.py      # .idx diff engine
│       │   └── exporter.py  # PNG export helper
│       ├── tools/
│       │   ├── extract_art.py
│       │   ├── extract_land.py
│       │   ├── extract_gumps.py
│       │   └── extract_anims.py
│       ├── readers/
│       │   └── tile_classifier.py
│       └── utils/
│           ├── hash_utils.py
│           └── paths.py
├── pyproject.toml           # Build config, deps, uoca entry point
├── MANIFEST.in
├── requirements.txt
├── clients/
│   ├── clean/
│   └── mod/
└── output/
```

---

## 🛠️ Configuration

Edit `src/ultima_client_art_tools/config.py` to customize:

```python
CLEAN_CLIENT = "clients/clean"   # Path to vanilla client
MOD_CLIENT   = "clients/mod"     # Path to modified client
OUTPUT_DIR   = "output"          # Export directory
CUSTOM_ART_THRESHOLD = 0x8000   # Items >= this ID are custom
```

---

## 🧪 Examples

### Extract Only Custom Art (IDs >= 0x8000)

```python
from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.config import MOD_CLIENT, CUSTOM_ART_THRESHOLD

client = UOClient(MOD_CLIENT)
for item_id in range(CUSTOM_ART_THRESHOLD, 0x10000):
    art = client.get_static(item_id)
    if art:
        art.save(f"output/custom/{item_id:05x}.png")
```

### Extract a Specific Animation Frame

```python
from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.config import MOD_CLIENT

client = UOClient(MOD_CLIENT)
frame = client.get_animation_frame(body_id=400, action=0, direction=0)
if frame:
    frame.save("output/anims/0400.png")
```

### Classify and Organize by Type

```python
from ultima_client_art_tools.core.client import UOClient
from ultima_client_art_tools.readers.tile_classifier import classify
from ultima_client_art_tools.config import MOD_CLIENT

client = UOClient(MOD_CLIENT)
for item_id in modified_ids:
    art = client.get_static(item_id)
    category = classify(item_id)  # "walls", "vegetation", "terrain", etc.
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
