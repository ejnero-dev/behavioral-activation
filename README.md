# Activación Conductual

Aplicación web progresiva (PWA) para el autorregistro de Activación Conductual basada en valores. Diseñada para pacientes en terapia psicológica.

**[Usar la aplicación](https://ejnero-dev.github.io/behavioral-activation/)**

## Características

- **Registro semanal** - Organiza actividades por semanas con un valor guía
- **Seguimiento diario** - Registra placer (0-10) y logro (0-10) para cada actividad
- **Funciona offline** - Los datos se guardan en tu dispositivo, sin necesidad de internet
- **Instalable** - Se instala como app nativa en móvil y escritorio
- **Privacidad total** - Tus datos nunca salen de tu dispositivo
- **Exportar/Importar** - Respaldo de datos en formato JSON
- **Imprimir** - Genera un PDF con todas las semanas registradas

## Instalar la app

### Android (Chrome)
1. Abre la app en Chrome
2. Te aparecerá un banner: "Agregar a pantalla de inicio"
3. Toca "Instalar"

### iOS (Safari)
1. Abre la app en Safari
2. Toca el botón de compartir (cuadro con flecha)
3. Selecciona "Agregar a la pantalla de inicio"
4. Toca "Agregar"

### PC (Chrome/Edge)
1. Abre la app en el navegador
2. Verás un icono de instalación (+) en la barra de direcciones
3. Click en él y confirma "Instalar"

## Cómo usar

1. **Crea una semana** - Cada semana comienza con un valor que quieres cultivar
2. **Agrega actividades** - Añade las actividades que planeas realizar
3. **Registra diariamente** - Al final de cada día, puntúa el placer y logro de cada actividad
4. **Anota barreras** - Usa el campo de comentarios para registrar obstáculos encontrados
5. **Revisa tu progreso** - Navega entre semanas y observa patrones

---

## Información técnica

### Tecnologías
- HTML, CSS y JavaScript vanilla (sin frameworks)
- Service Worker para funcionamiento offline
- localStorage para persistencia de datos
- PWA (Progressive Web App)

### Estructura del proyecto
```
behavioral-activation/
├── index.html           # Aplicación principal
├── manifest.json        # Configuración PWA
├── service-worker.js    # Cache y funcionalidad offline
├── CLAUDE.md            # Documentación técnica detallada
├── LICENSE              # Licencia MIT
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

### Desarrollo local

La app requiere un servidor web (las PWA no funcionan con `file://`):

```bash
# Python
python -m http.server 8000

# Node.js
npx http-server

# Abrir en http://localhost:8000
```

### Solución de problemas

**La app no se instala**
- Verifica que los iconos estén en la carpeta `icons/`
- Abre la consola del navegador (F12) y busca errores
- Asegúrate de estar usando HTTPS

**Los cambios no se ven**
- Limpia el cache del navegador (Ctrl + Shift + Delete)
- En Chrome DevTools: Application → Service Workers → Unregister

**No funciona offline**
- Verifica que el Service Worker esté registrado (F12 → Application → Service Workers)
- Asegúrate de haber visitado la app al menos una vez con internet

## Privacidad

Esta aplicación fue diseñada con la privacidad del paciente como prioridad:
- **Sin backend** - No hay servidor que almacene datos
- **Sin analytics** - No se rastrea el uso
- **Datos locales** - Todo se guarda únicamente en tu navegador
- **Sin cuenta** - No requiere registro ni login

## Licencia

MIT License - Copyright (c) 2025 Emilio Neva

Desarrollado por **Emilio Neva**
