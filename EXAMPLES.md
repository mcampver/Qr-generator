# Example Usage

This file demonstrates how to use the QR Business Card Generator programmatically.

## Basic Example

```python
from qr import TarjetaPresentacionQR

# Create an instance
generator = TarjetaPresentacionQR()

# Configure business card data
generator.configurar_datos(
    nombre="John Doe",
    empresa="Tech Solutions Inc.",
    cargo="Senior Developer",
    telefono="+1-555-0123",
    email="john.doe@techsolutions.com",
    web="https://www.techsolutions.com",
    direccion="123 Main St, San Francisco, CA"
)

# Generate QR code with logo
generator.generar_qr_con_logo(
    ruta_logo="logo.png",
    archivo_salida="business_card_qr.png"
)

print("QR code generated successfully!")
```

## Custom Colors

```python
# Generate with custom colors
generator.generar_qr_con_logo(
    ruta_logo="logo.png",
    archivo_salida="custom_qr.png",
    color_qr="#FF5733",  # Custom red color
    color_fondo="white"
)
```

## Without Logo

```python
# Generate QR code without logo
generator.generar_qr_con_logo(
    archivo_salida="simple_qr.png"
)
```

## Simple Text QR

```python
# Generate a simple QR code with any text
generator.generar_qr_simple(
    texto="https://www.example.com",
    ruta_logo="logo.png",
    archivo_salida="url_qr.png"
)
```

## Batch Generation

```python
# Generate multiple QR codes
contacts = [
    {
        "nombre": "Alice Smith",
        "empresa": "Design Co",
        "cargo": "Creative Director",
        "telefono": "+1-555-0001",
        "email": "alice@designco.com"
    },
    {
        "nombre": "Bob Johnson",
        "empresa": "Marketing Plus",
        "cargo": "Marketing Manager",
        "telefono": "+1-555-0002",
        "email": "bob@marketingplus.com"
    }
]

for contact in contacts:
    gen = TarjetaPresentacionQR()
    gen.configurar_datos(**contact)
    filename = f"qr_{contact['nombre'].replace(' ', '_').lower()}.png"
    gen.generar_qr_con_logo(ruta_logo="logo.png", archivo_salida=filename)
    print(f"Generated: {filename}")
```

## Integration Example

```python
import os
from qr import TarjetaPresentacionQR

def create_team_qr_codes(team_data, logo_path="logo.png", output_dir="team_qr"):
    """
    Generate QR codes for an entire team.
    
    Args:
        team_data: List of dictionaries with contact information
        logo_path: Path to company logo
        output_dir: Directory to save QR codes
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    for member in team_data:
        generator = TarjetaPresentacionQR()
        generator.configurar_datos(
            nombre=member.get("name"),
            empresa=member.get("company"),
            cargo=member.get("position"),
            telefono=member.get("phone"),
            email=member.get("email"),
            web=member.get("website", ""),
            direccion=member.get("address", "")
        )
        
        # Generate filename from name
        safe_name = member.get("name").replace(" ", "_").lower()
        output_file = os.path.join(output_dir, f"{safe_name}_qr.png")
        
        generator.generar_qr_con_logo(
            ruta_logo=logo_path,
            archivo_salida=output_file
        )
        
        print(f"✓ Generated QR for {member.get('name')}")

# Example usage
team = [
    {
        "name": "Jane Doe",
        "company": "Acme Corp",
        "position": "CEO",
        "phone": "+1-555-1000",
        "email": "jane@acme.com",
        "website": "https://acme.com"
    },
    # Add more team members...
]

create_team_qr_codes(team)
```
