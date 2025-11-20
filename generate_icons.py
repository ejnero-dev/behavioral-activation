#!/usr/bin/env python3
"""
Script para generar iconos PWA desde una imagen
Uso: python generate_icons.py [imagen_input] [directorio_output]
"""

import sys
import os
from PIL import Image

def generate_icons(input_path, output_dir):
    if not os.path.exists(input_path):
        print(f"❌ Error: No se encuentra la imagen: {input_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"📁 Directorio creado: {output_dir}")

    print(f"📸 Abriendo imagen: {input_path}")
    img = Image.open(input_path)

    # Recortar a cuadrado si es necesario
    width, height = img.size
    if width != height:
        print("🔲 Recortando a formato cuadrado...")
        size = min(width, height)
        left = (width - size) // 2
        top = (height - size) // 2
        img = img.crop((left, top, left + size, top + size))

    # Generar iconos
    sizes = [192, 512]
    for size in sizes:
        filename = f"icon-{size}.png"
        print(f"🎨 Generando {filename}...")
        icon = img.resize((size, size), Image.Resampling.LANCZOS)
        save_path = os.path.join(output_dir, filename)
        icon.save(save_path, 'PNG', optimize=True)
        print(f"   ✅ Guardado: {save_path}")

if __name__ == "__main__":
    # Valores por defecto
    input_image = "source_image.png" # Busca este archivo por defecto
    output_directory = "icons"

    # Permitir argumentos: python generate_icons.py mi_logo.jpg ./assets/icons
    if len(sys.argv) > 1:
        input_image = sys.argv[1]
    if len(sys.argv) > 2:
        output_directory = sys.argv[2]

    try:
        generate_icons(input_image, output_directory)
    except ImportError:
        print("❌ Error: Pillow no está instalado.\n💡 Ejecuta: pip install Pillow")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
