# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-11-06

### Added
- Initial release of QR Business Card Generator
- Interactive menu for easy QR code generation
- Support for custom logo with circular background
- vCard 3.0 format for maximum compatibility
- Auto-detection of logo.png file
- Custom color support (default: #292B3A)
- High error correction (ERROR_CORRECT_H) for logo overlay
- Automatic logo resizing (1/6 of QR code size)
- Support for optional fields (website, address)
- Cross-platform support (Windows, macOS, Linux)
- Comprehensive documentation and examples
- MIT License

### Features
- Compatible with iPhone and Android devices
- Properly displays contact name on all platforms
- Transparent PNG logo support
- Automatic file extension handling
- Professional circular background for logo

### Documentation
- Complete README with installation and usage guide
- Contributing guidelines (CONTRIBUTING.md)
- Code examples (EXAMPLES.md)
- GitHub setup instructions (GITHUB_SETUP.md)
- Logo requirements documentation (LOGO_INFO.md)

### Technical Details
- Python 3.6+ support
- Uses qrcode and Pillow libraries
- Structured vCard format with N field for proper name display
- Work-type fields for professional contacts

## [Unreleased]

### Planned Features
- GUI interface option
- Batch processing from CSV
- QR code style templates
- Multiple language support
- QR code analytics/tracking
- Web-based version
- Docker container support

---

[1.0.0]: https://github.com/mcampver/Qr-generator/releases/tag/v1.0.0
