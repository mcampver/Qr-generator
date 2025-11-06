# 📇 QR Business Card Generator

A Python application that generates QR codes for business cards with a custom logo in the center. Creates vCard format QR codes compatible with iPhone and Android devices.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## ✨ Features

- 🎨 **Custom Logo**: Add your logo in the center with circular background
- 📱 **vCard Format**: Compatible with iPhone and Android contacts
- 🎯 **Professional Design**: Custom color scheme (#292B3A)
- 🔄 **Auto-resize**: Logo automatically resized and positioned
- 💾 **Easy Export**: Generates high-quality PNG files
- 🖥️ **Cross-platform**: Works on Windows, macOS, and Linux

## 📸 What You Get

The generated QR code includes:
- ✅ Full name (displayed correctly on all devices)
- ✅ Company/Organization
- ✅ Job title
- ✅ Phone number
- ✅ Email address
- ✅ Website (optional)
- ✅ Address (optional)

When scanned with a smartphone camera, the contact information is automatically recognized and can be saved to the phone's contact list with a single tap.

### Example Output

The application generates a professional QR code with:
- Your custom logo in the center with circular background
- Custom color scheme (default: #292B3A)
- High error correction for reliable scanning
- Optimized size for printing on business cards

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/qr-business-card.git
cd qr-business-card
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your logo:
   - Place your logo file as `logo.png` in the project directory
   - Recommended: PNG format with transparent background
   - The logo will be automatically resized

### Usage

Run the application:
```bash
python qr.py
```

Follow the interactive prompts to enter your business card information:
- Full name
- Company
- Job title
- Phone number
- Email
- Website (optional)
- Address (optional)

The QR code will be generated with your logo in the center.

## 🎨 Customization

### Change QR Code Color

Edit the default color in `qr.py`:
```python
color_qr="#292B3A"  # Change to your preferred hex color
```

### Adjust Logo Size

Modify the logo size ratio in `qr.py`:
```python
logo_size = qr_width // 6  # Change divisor (6) to adjust size
```

### Custom Output Filename

When prompted, enter your desired filename:
```
Output filename (default: mi_tarjeta_qr.png): my_custom_name
```

## 📦 Building Executable (Windows)

To create a standalone `.exe` file:

1. Install PyInstaller:
```bash
pip install pyinstaller
```

2. Build the executable:
```bash
pyinstaller --onefile --name="QR_Generator" --add-data "logo.png;." qr.py
```

The executable will be created in the `dist` folder.

## 🍎 macOS Usage

The Python script works natively on macOS:

```bash
python3 qr.py
```

Make sure to have Python 3 installed:
```bash
brew install python3
```

## 📋 Requirements

- qrcode[pil] - QR code generation
- Pillow (PIL) - Image processing

See `requirements.txt` for specific versions.

## 🔧 Technical Details

### vCard Format

The application generates vCard 3.0 format for maximum compatibility:
- `N`: Structured name (surname; first name)
- `FN`: Formatted name (display name)
- `ORG`: Organization/Company
- `TITLE`: Job title
- `TEL`: Phone number (work)
- `EMAIL`: Email address (work)
- `URL`: Website (optional)
- `ADR`: Address (optional)

### QR Code Settings

- **Error Correction**: High (ERROR_CORRECT_H)
  - Allows up to 30% damage recovery
  - Essential for logo overlay
- **Box Size**: 10 pixels per module
- **Border**: 4 modules (recommended minimum)
- **Logo Size**: 1/6 of QR code dimension
- **Background**: Circular white background for logo

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Tips

- **Logo Quality**: Use PNG with transparent background for best results
- **Printing**: Export at 300 DPI for physical business cards
- **Testing**: Always test the QR code before printing
- **Size**: Keep the QR code at least 2cm x 2cm when printed
- **Contrast**: Ensure good contrast between QR code and background

## 🐛 Troubleshooting

### Logo not appearing
- Check that `logo.png` exists in the same directory
- Verify the file format is supported (PNG, JPG, JPEG)
- Ensure the file is not corrupted

### QR code not scanning
- Increase the QR code size
- Reduce logo size (increase divisor)
- Ensure good lighting when scanning
- Try with different QR code readers

### iPhone showing organization instead of name
- This has been fixed in the latest version
- The vCard now includes proper `N` field for name structure

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Acknowledgments

- QR code generation powered by [qrcode](https://github.com/lincolnloop/python-qrcode)
- Image processing by [Pillow](https://python-pillow.org/)

---

Made with ❤️ for easy business card sharing
