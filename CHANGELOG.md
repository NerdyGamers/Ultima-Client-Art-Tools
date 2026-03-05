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
