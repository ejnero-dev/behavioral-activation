# 🚀 Guía Rápida de Despliegue

## ✅ Checklist Pre-Deploy

- [ ] **Generar iconos** (ver carpeta `icons/LEER_PRIMERO.txt`)
- [ ] Verificar que `icon-192.png` e `icon-512.png` existen
- [ ] Probar localmente que la app funciona (abrir `index.html`)

## 📤 Subir a GitHub (Opción más fácil)

### Usando GitHub Desktop (Recomendado para principiantes)

1. **Descargar GitHub Desktop**
   - Ve a: https://desktop.github.com/
   - Instala la aplicación

2. **Inicializar repositorio**
   - Abre GitHub Desktop
   - File → Add Local Repository
   - Selecciona la carpeta `behavioral-activation`
   - Click "Create Repository"

3. **Hacer commit inicial**
   - Verás todos los archivos en la lista
   - En la parte inferior izquierda escribe: "Initial commit - PWA lista"
   - Click "Commit to main"

4. **Publicar en GitHub**
   - Click "Publish repository" (botón azul arriba)
   - Repository name: `behavioral-activation`
   - Desmarca "Keep this code private"
   - Click "Publish repository"

5. **Activar GitHub Pages**
   - Abre tu navegador
   - Ve a: https://github.com/ejnero-dev/behavioral-activation
   - Click "Settings" → "Pages"
   - Source: "main" branch
   - Click "Save"
   - Espera 2 minutos

6. **¡Listo!**
   - Tu app estará en: https://ejnero-dev.github.io/behavioral-activation/

---

## 🔄 Para actualizaciones futuras

1. Haz tus cambios en los archivos
2. **IMPORTANTE**: Actualiza la versión en `service-worker.js`:
   ```javascript
   const CACHE_NAME = 'activacion-conductual-v2'; // v1 → v2 → v3...
   ```
3. En GitHub Desktop:
   - Verás los archivos modificados
   - Escribe un mensaje: "Actualización: descripción de cambios"
   - Click "Commit to main"
   - Click "Push origin" (botón azul arriba)
4. Espera 1-2 minutos y los cambios estarán online

---

## 🧪 Probar localmente antes de subir

Para probar la PWA en tu PC necesitas un servidor local (las PWAs no funcionan abriendo el archivo directamente):

**Opción 1: Python** (si lo tienes instalado)
```bash
cd behavioral-activation
python -m http.server 8000
```
Abre: http://localhost:8000

**Opción 2: Node.js con http-server**
```bash
npm install -g http-server
cd behavioral-activation
http-server
```

**Opción 3: VS Code Live Server**
- Instala extensión "Live Server"
- Click derecho en `index.html` → "Open with Live Server"

---

## ❓ ¿Problemas?

**No puedo instalar GitHub Desktop**
→ Usa la interfaz web de GitHub (opción C en README.md)

**Los iconos no se ven**
→ Verifica que estén en la carpeta `icons/` y se llamen exactamente:
  - `icon-192.png`
  - `icon-512.png`

**La app no se actualiza después de hacer push**
→ Espera 2-3 minutos, GitHub Pages tarda en procesar

**Quiero cambiar la URL**
→ En Settings → Pages puedes usar un dominio personalizado

---

## 📱 Compartir con pacientes

Una vez desplegada, comparte:

**URL directa:**
https://ejnero-dev.github.io/behavioral-activation/

**O genera un QR code:**
1. Ve a: https://www.qr-code-generator.com/
2. Pega la URL
3. Descarga el QR
4. Imprímelo o envíalo por WhatsApp

---

## 🎯 Próximos pasos (opcional)

- [ ] Dominio personalizado (ej: `activacion.tudominio.com`)
- [ ] Google Analytics para ver cuántos pacientes usan la app
- [ ] Agregar más funcionalidades (gráficos, estadísticas, etc.)
- [ ] Traducir a otros idiomas

¡Tu PWA está lista para ayudar a tus pacientes! 🎉
