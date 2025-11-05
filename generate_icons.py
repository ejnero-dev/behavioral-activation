#!/usr/bin/env python3
"""
Script para generar iconos PWA desde una imagen
"""

from PIL import Image
import sys

def generate_icons(input_path, output_dir):
    """
    Genera iconos cuadrados de 192x192 y 512x512 desde una imagen
    """
    print(f"📸 Abriendo imagen: {input_path}")

    # Abrir imagen
    img = Image.open(input_path)
    print(f"   Dimensiones originales: {img.size}")

    # Obtener dimensiones
    width, height = img.size

    # Recortar a cuadrado (tomar el centro)
    if width != height:
        print("🔲 Recortando a formato cuadrado...")
        # Usar la dimensión más pequeña
        size = min(width, height)

        # Calcular coordenadas para centrar el recorte
        left = (width - size) // 2
        top = (height - size) // 2
        right = left + size
        bottom = top + size

        img = img.crop((left, top, right, bottom))
        print(f"   Nueva dimensión cuadrada: {img.size}")

    # Generar icon-192.png
    print("🎨 Generando icon-192.png...")
    icon_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192_path = f"{output_dir}/icon-192.png"
    icon_192.save(icon_192_path, 'PNG', optimize=True)
    print(f"   ✅ Guardado: {icon_192_path}")

    # Generar icon-512.png
    print("🎨 Generando icon-512.png...")
    icon_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
    icon_512_path = f"{output_dir}/icon-512.png"
    icon_512.save(icon_512_path, 'PNG', optimize=True)
    print(f"   ✅ Guardado: {icon_512_path}")

    print("\n🎉 ¡Iconos generados exitosamente!")
    print(f"   📁 Ubicación: {output_dir}")
    print("   📱 Ahora puedes desplegar tu PWA")

if __name__ == "__main__":
    input_image = "/mnt/c/Users/emilio/Downloads/Generated Image November 05, 2025 - 9_00PM.png"
    output_directory = "/mnt/c/Users/emilio/Desktop/behavioral-activation/icons"

    try:
        generate_icons(input_image, output_directory)
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Solución: Instala Pillow con: pip install Pillow")
        sys.exit(1)
