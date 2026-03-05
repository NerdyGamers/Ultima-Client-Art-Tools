# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Planned
- Texture map (texmaps.mul) extractor
- Multi-hue rendering support
- Parallel processing for faster extraction
- JSON metadata export
- Web UI for browsing assets

---

## [1.1.0] - 2026-03-05 — `feat/python-package`

### Added
- `UOClient.get_animation_frame(body_id, action, direction)` method for consistent animation access via the SDK wrapper
- `from ultimapy.sdk.animations import Animations` import to `core/client.py`
- `cli()` console script entry point in `main.py`, wiring up the `uoca` command declared in `pyproject.toml`
- Proper `src/` layout (`src/ultima_client_art_tools/`) for installable Python package structure
- `pyproject.toml` with build system, dependencies (`ultimapy`, `pillow`, `tqdm`), and `[project.scripts]` entry
- `MANIFEST.in` for sdist packaging

### Fixed
- `extract_anims.py` was using a bare `from config import OUTPUT_DIR` which broke at runtime when installed as a package — corrected to `from ultima_client_art_tools.config import MOD_CLIENT, OUTPUT_DIR`
- `extract_anims.py` was bypassing the `UOClient` wrapper and instantiating `Animations()` directly, ignoring `ULTIMA_FILES_DIR` management — refactored to use `UOClient.get_animation_frame()`
- All tool import paths updated to use fully-qualified `ultima_client_art_tools.*` namespace

### Changed
- Project restructured from flat layout to `src/` package layout for pip-installability
- `extract_anims.py` now routes animation access through `UOClient` rather than raw ultimapy SDK calls, consistent with all other extractors

---

## [1.0.0] - 2026-03-05

### Added
- Initial release
- Core `UOClient` wrapper for ultimapy SDK
- `.idx` diff engine for detecting modified art
- Modified static art extractor (`extract_art.py`)
- Terrain tile extractor (`extract_land.py`)
- Gump extractor (`extract_gumps.py`)
- Animation frame extractor (`extract_anims.py`)
- Tile name classifier (`tile_classifier.py`)
- File hashing utilities (`hash_utils.py`)
- Path resolution helpers (`paths.py`)
- CLI entry point (`main.py`)
- Configuration file (`config.py`)
- Full README with usage examples
- MIT License
- Contributing guidelines

---

## Legend

- **Added** — New features
- **Changed** — Changes to existing functionality
- **Deprecated** — Features to be removed in future releases
- **Removed** — Features removed in this release
- **Fixed** — Bug fixes
- **Security** — Security vulnerability patches
