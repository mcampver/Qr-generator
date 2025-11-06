import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

class TarjetaPresentacionQR:
    def __init__(self):
        """Inicializa el generador de QR para tarjetas de presentación"""
        self.datos = {}
    
    def configurar_datos(self, nombre, empresa, cargo, telefono, email, web="", direccion=""):
        """
        Configura los datos de la tarjeta de presentación
        
        Args:
            nombre: Nombre completo
            empresa: Nombre de la empresa
            cargo: Puesto o cargo
            telefono: Número de teléfono
            email: Correo electrónico
            web: Sitio web (opcional)
            direccion: Dirección (opcional)
        """
        # Separar nombre y apellido para el formato vCard
        partes_nombre = nombre.strip().split(' ', 1)
        apellido = partes_nombre[1] if len(partes_nombre) > 1 else ""
        primer_nombre = partes_nombre[0]
        
        # Formato vCard para tarjetas de presentación
        vcard = f"""BEGIN:VCARD
VERSION:3.0
N:{apellido};{primer_nombre};;;
FN:{nombre}
ORG:{empresa}
TITLE:{cargo}
TEL;TYPE=WORK,VOICE:{telefono}
EMAIL;TYPE=WORK:{email}"""
        
        if web:
            vcard += f"\nURL;TYPE=WORK:{web}"
        if direccion:
            vcard += f"\nADR;TYPE=WORK:;;{direccion};;;;"
        
        vcard += "\nEND:VCARD"
        
        self.datos['vcard'] = vcard
        self.datos['nombre'] = nombre
        
        return vcard
    
    def generar_qr_con_logo(self, ruta_logo=None, archivo_salida="tarjeta_qr.png", 
                           color_qr="#292B3A", color_fondo="white"):
        """
        Genera el código QR con el logo en el centro
        
        Args:
            ruta_logo: Ruta del archivo de imagen del logo
            archivo_salida: Nombre del archivo de salida
            color_qr: Color del QR (por defecto negro)
            color_fondo: Color de fondo (por defecto blanco)
        
        Returns:
            Ruta del archivo generado
        """
        if 'vcard' not in self.datos:
            raise ValueError("Primero debes configurar los datos con configurar_datos()")
        
        # Crear el código QR
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta corrección de errores
            box_size=10,
            border=4,
        )
        
        qr.add_data(self.datos['vcard'])
        qr.make(fit=True)
        
        # Crear la imagen del QR
        img_qr = qr.make_image(fill_color=color_qr, back_color=color_fondo).convert('RGB')
        
        # Si hay logo, añadirlo al centro
        if ruta_logo and os.path.exists(ruta_logo):
            logo = Image.open(ruta_logo)
            
            # Convertir a RGBA si no lo está (para manejar transparencia)
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            # Calcular el tamaño del logo (aproximadamente 1/6 del QR - más pequeño)
            qr_width, qr_height = img_qr.size
            logo_size = qr_width // 6
            
            # Redimensionar el logo manteniendo la proporción y la transparencia
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Crear un fondo circular blanco
            circle_size = max(logo.size)  # Usar el lado más grande para el círculo
            fondo_circular = Image.new('RGBA', (circle_size, circle_size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(fondo_circular)
            
            # Dibujar círculo blanco
            draw.ellipse([0, 0, circle_size, circle_size], fill=(255, 255, 255, 255))
            
            # Centrar el logo en el círculo
            logo_offset = ((circle_size - logo.size[0]) // 2, (circle_size - logo.size[1]) // 2)
            fondo_circular.paste(logo, logo_offset, logo)
            
            # Calcular la posición central en el QR
            logo_pos = (
                (qr_width - circle_size) // 2,
                (qr_height - circle_size) // 2
            )
            
            # Pegar el logo con fondo circular en el QR
            img_qr.paste(fondo_circular, logo_pos, fondo_circular)
        
        # Guardar la imagen
        img_qr.save(archivo_salida)
        print(f"✓ Código QR generado exitosamente: {archivo_salida}")
        
        return archivo_salida
    
    def generar_qr_simple(self, texto, ruta_logo=None, archivo_salida="qr_simple.png"):
        """
        Genera un QR simple con cualquier texto
        
        Args:
            texto: Texto a codificar en el QR
            ruta_logo: Ruta del logo (opcional)
            archivo_salida: Nombre del archivo de salida
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        
        qr.add_data(texto)
        qr.make(fit=True)
        
        img_qr = qr.make_image(fill_color="black", back_color="white").convert('RGB')
        
        if ruta_logo and os.path.exists(ruta_logo):
            logo = Image.open(ruta_logo)
            
            # Convertir a RGBA para manejar transparencia
            if logo.mode != 'RGBA':
                logo = logo.convert('RGBA')
            
            qr_width, qr_height = img_qr.size
            logo_size = qr_width // 6  # Más pequeño
            logo.thumbnail((logo_size, logo_size), Image.Resampling.LANCZOS)
            
            # Crear fondo circular blanco
            circle_size = max(logo.size)
            fondo_circular = Image.new('RGBA', (circle_size, circle_size), (255, 255, 255, 0))
            draw = ImageDraw.Draw(fondo_circular)
            draw.ellipse([0, 0, circle_size, circle_size], fill=(255, 255, 255, 255))
            
            # Centrar logo en el círculo
            logo_offset = ((circle_size - logo.size[0]) // 2, (circle_size - logo.size[1]) // 2)
            fondo_circular.paste(logo, logo_offset, logo)
            
            # Posición central en el QR
            logo_pos = ((qr_width - circle_size) // 2, (qr_height - circle_size) // 2)
            
            # Pegar logo con fondo circular
            img_qr.paste(fondo_circular, logo_pos, fondo_circular)
        
        img_qr.save(archivo_salida)
        print(f"✓ Código QR generado exitosamente: {archivo_salida}")
        
        return archivo_salida


def ejemplo_uso():
    """Ejemplo de uso de la aplicación"""
    print("=== Generador de QR para Tarjetas de Presentación ===\n")
    
    # Crear instancia del generador
    generador = TarjetaPresentacionQR()
    
    # Configurar datos de la tarjeta
    print("Configurando datos de la tarjeta...")
    vcard = generador.configurar_datos(
        nombre="Juan Pérez",
        empresa="Tech Solutions Inc.",
        cargo="Desarrollador Senior",
        telefono="+1-555-0123",
        email="juan.perez@techsolutions.com",
        web="https://www.techsolutions.com",
    )
    
    print("\nDatos de la tarjeta (formato vCard):")
    print(vcard)
    
    # Generar QR con logo (si existe)
    print("\n--- Generando código QR ---")
    ruta_logo = "logo.png"  # Cambia esto por la ruta de tu logo
    
    if os.path.exists(ruta_logo):
        archivo = generador.generar_qr_con_logo(
            ruta_logo=ruta_logo,
            archivo_salida="tarjeta_presentacion_qr.png"
        )
    else:
        print(f"⚠ No se encontró el logo en '{ruta_logo}'")
        print("Generando QR sin logo...")
        archivo = generador.generar_qr_con_logo(
            archivo_salida="tarjeta_presentacion_qr.png"
        )
    
    print(f"\n¡Listo! Abre el archivo '{archivo}' para ver tu código QR.")


def menu_interactivo():
    """Menú interactivo para generar códigos QR"""
    print("╔════════════════════════════════════════════╗")
    print("║  Generador de QR - Tarjeta de Presentación ║")
    print("╚════════════════════════════════════════════╝\n")
    
    generador = TarjetaPresentacionQR()
    
    # Solicitar datos
    print("Ingresa los datos de tu tarjeta de presentación:\n")
    nombre = input("Nombre completo: ")
    empresa = input("Empresa: ")
    cargo = input("Cargo/Puesto: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")
    web = input("Sitio web (opcional): ")
    direccion = input("Dirección (opcional): ")
    
    # Configurar datos
    generador.configurar_datos(nombre, empresa, cargo, telefono, email, web, direccion)
    
    # Usar siempre logo.png por defecto
    ruta_logo = "logo.png"
    if not os.path.exists(ruta_logo):
        print(f"\n⚠ Advertencia: No se encontró el archivo '{ruta_logo}'")
        print("Se generará el QR sin logo.")
        ruta_logo = None
    else:
        print(f"\n✓ Logo encontrado: {ruta_logo}")
    
    # Nombre del archivo de salida
    archivo_salida = input("\nNombre del archivo de salida (default: mi_tarjeta_qr.png): ")
    if not archivo_salida or archivo_salida.lower() == "default":
        archivo_salida = "mi_tarjeta_qr.png"
    elif not archivo_salida.lower().endswith(('.png', '.jpg', '.jpeg')):
        archivo_salida += ".png"
    
    # Generar el QR
    print("\n🔄 Generando código QR...")
    generador.generar_qr_con_logo(ruta_logo, archivo_salida)
    
    print(f"\n✅ ¡Código QR generado exitosamente!")
    print(f"📁 Archivo guardado como: {archivo_salida}")
    print("\nPuedes escanear este QR con tu smartphone para agregar")
    print("la información de contacto directamente a tus contactos.")


if __name__ == "__main__":
    # Descomenta la opción que prefieras:
    
    # Opción 1: Menú interactivo
    menu_interactivo()
    
    # Opción 2: Ejemplo de uso programático
    # ejemplo_uso()
