# 📱 Activación Conductual - PWA

Autorregistro de Activación Conductual en base a valores - Progressive Web App

**Desarrollado por:** Emilio Neva

## 🚀 Cómo desplegar en GitHub Pages

### Paso 1: Generar los iconos

Necesitas crear 2 iconos para la app. Usa cualquiera de estas opciones:

**Opción A: PWA Asset Generator (Recomendado)**
1. Ve a: https://www.pwabuilder.com/imageGenerator
2. Sube una imagen cuadrada (mínimo 512x512px)
3. Descarga los iconos generados
4. Copia `icon-192.png` e `icon-512.png` a la carpeta `icons/`

**Opción B: Herramienta online simple**
1. Ve a: https://www.favicon-generator.org/
2. Sube una imagen
3. Descarga los iconos de 192x192 y 512x512
4. Renómbralos a `icon-192.png` e `icon-512.png`
5. Cópialos a la carpeta `icons/`

**Opción C: Crear manualmente**
- Crea dos imágenes cuadradas PNG:
  - `icon-192.png` (192x192 píxeles)
  - `icon-512.png` (512x512 píxeles)
- Usa un fondo sólido de color `#667eea` (morado/azul)
- Agrega texto o un icono simple relacionado con terapia/salud

### Paso 2: Crear repositorio en GitHub

1. Ve a: https://github.com/ejnero-dev
2. Click en "New repository" (botón verde)
3. Nombre: `behavioral-activation`
4. Descripción: "PWA para Activación Conductual en terapia psicológica"
5. Público (para GitHub Pages gratis)
6. NO marques "Add a README file"
7. Click "Create repository"

### Paso 3: Subir archivos

**Opción A: Usando GitHub Desktop (Fácil)**
1. Descarga GitHub Desktop: https://desktop.github.com/
2. Instala y loguéate con tu cuenta
3. File → Add Local Repository
4. Selecciona la carpeta `behavioral-activation`
5. Click "Publish repository"
6. Desmarca "Keep this code private"
7. Click "Publish repository"

**Opción B: Usando línea de comandos**
```bash
cd behavioral-activation
git init
git add .
git commit -m "Initial commit - PWA Activación Conductual"
git branch -M main
git remote add origin https://github.com/ejnero-dev/behavioral-activation.git
git push -u origin main
```

**Opción C: Usando la interfaz web de GitHub**
1. Ve al repositorio recién creado
2. Click "uploading an existing file"
3. Arrastra todos los archivos de la carpeta `behavioral-activation`
4. Commit changes

### Paso 4: Activar GitHub Pages

1. Ve a tu repositorio: https://github.com/ejnero-dev/behavioral-activation
2. Click en "Settings" (arriba a la derecha)
3. En el menú izquierdo, click "Pages"
4. En "Source", selecciona "main" branch
5. Carpeta: / (root)
6. Click "Save"
7. Espera 1-2 minutos

### Paso 5: Probar la PWA

Tu app estará disponible en:
**https://ejnero-dev.github.io/behavioral-activation/**

#### En móvil (Android):
1. Abre Chrome en tu móvil
2. Ve a la URL
3. Te aparecerá un banner: "Agregar Activación Conductual a la pantalla de inicio"
4. Toca "Instalar" o "Agregar"
5. La app se instala como una app nativa

#### En móvil (iOS):
1. Abre Safari en tu iPhone/iPad
2. Ve a la URL
3. Toca el botón de compartir (cuadro con flecha)
4. Selecciona "Agregar a la pantalla de inicio"
5. Toca "Agregar"

#### En PC (Chrome/Edge):
1. Ve a la URL
2. Verás un icono de instalación (+) en la barra de direcciones
3. Click en él
4. Confirma "Instalar"

## ✅ Verificar que funciona

- [ ] La página carga correctamente
- [ ] Puedes crear semanas y acciones
- [ ] Los datos se guardan automáticamente
- [ ] Funciona sin internet (cierra el WiFi y recarga)
- [ ] Puedes instalarla como app
- [ ] La impresión muestra todas las semanas

## 🔄 Actualizar la app

Cada vez que hagas cambios:

1. **Actualiza el número de versión** en `service-worker.js`:
   ```javascript
   const CACHE_NAME = 'activacion-conductual-v2'; // Cambiar v1 → v2
   ```

2. Sube los cambios a GitHub (con GitHub Desktop o git push)

3. Los usuarios verán la nueva versión al recargar la página

## 🎨 Personalización

### Cambiar colores
Edita estos valores en `index.html` y `manifest.json`:
- Color principal: `#667eea` (morado/azul)
- Color secundario: `#764ba2` (morado oscuro)

### Cambiar nombre
Edita `manifest.json`:
```json
"name": "Tu Nombre Aquí",
"short_name": "TuNombre"
```

## 📊 Estructura de archivos

```
behavioral-activation/
├── index.html           # App principal
├── manifest.json        # Configuración PWA
├── service-worker.js    # Cache y funcionalidad offline
├── README.md           # Este archivo
└── icons/              # Iconos de la app
    ├── icon-192.png
    └── icon-512.png
```

## 🐛 Solución de problemas

**La app no se instala**
- Verifica que los iconos estén en la carpeta `icons/`
- Abre la consola del navegador (F12) y busca errores
- Asegúrate de estar usando HTTPS (GitHub Pages lo hace automático)

**Los cambios no se ven**
- Incrementa la versión del cache en `service-worker.js`
- Limpia el cache del navegador (Ctrl + Shift + Delete)
- En Chrome DevTools: Application → Service Workers → Unregister

**No funciona offline**
- Verifica que el Service Worker esté registrado (F12 → Application → Service Workers)
- Asegúrate de haber visitado la app al menos una vez con internet

## 📱 Compartir con pacientes

Comparte este link:
**https://ejnero-dev.github.io/behavioral-activation/**

O genera un QR code en: https://www.qr-code-generator.com/

## 📝 Licencia

MIT License - Copyright (c) 2025 Emilio Neva

Este proyecto permite uso comercial, modificación y distribución.
Los datos de los usuarios nunca salen del dispositivo del paciente (privacidad garantizada).
