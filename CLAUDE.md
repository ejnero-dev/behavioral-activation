# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Activación Conductual PWA** - A Progressive Web App for Behavioral Activation therapy tracking in Spanish. This is a single-file PWA designed to help psychology patients track their activities, values, and progress over multiple weeks.

**Key characteristics:**
- Zero backend - all data stored in browser localStorage
- Patient privacy guaranteed - data never leaves the device
- Works offline via Service Worker caching
- Installable as a native-like app on mobile and desktop
- Responsive design with mobile-first approach

## Architecture

### Single-Page Application Structure

The entire app is contained in `index.html` (~1035 lines) with embedded CSS and vanilla JavaScript. This monolithic approach was chosen for simplicity and portability.

**Core components:**
- **HTML structure** (lines 1-540): Layout, forms, and print container
- **CSS styling** (lines 24-485): Responsive design with print media queries
- **JavaScript app logic** (lines 541-1034): Data management, rendering, PWA installation

### Data Model

Data is stored in localStorage as a JSON object with this structure:

```javascript
{
  weeks: [
    {
      id: number,                    // Unique week identifier
      startDate: string,             // ISO date of Monday (YYYY-MM-DD)
      valor: string,                 // The guiding value for the week
      actions: [
        {
          id: number,                // Unique action identifier
          name: string,              // Action description
          placer: {                  // Pleasure ratings (0-10) for each day
            L: '', M: '', X: '', J: '', V: '', S: '', D: ''
          },
          logro: {                   // Achievement ratings (0-10) for each day
            L: '', M: '', X: '', J: '', V: '', S: '', D: ''
          },
          comentarios: string        // Barriers/comments
        }
      ]
    }
  ],
  currentWeekId: number,
  weekCounter: number,               // Auto-increment for new weeks
  actionCounter: number              // Auto-increment for new actions
}
```

**Migration logic:** The app includes backward compatibility code (lines 554-571, 874-889) to migrate from an older single-week format to the current multi-week format.

### Service Worker (service-worker.js)

Implements a "Cache First" strategy:
1. Try to serve from cache
2. Fall back to network if not cached
3. Cache successful network responses for future use

**Version management:** `CACHE_NAME` constant (line 1) must be incremented for updates. Old caches are automatically deleted on activation (lines 22-36).

**Cached resources:**
- /behavioral-activation/ (base path)
- /behavioral-activation/index.html
- /behavioral-activation/manifest.json

### PWA Configuration (manifest.json)

- **App name:** "Activación Conductual" / "ActConductual"
- **Display mode:** standalone (no browser UI)
- **Theme color:** #667eea (purple-blue gradient)
- **Start URL:** /behavioral-activation/ (GitHub Pages path)
- **Icons:** 192x192 and 512x512 PNG (both any + maskable)

## Development Workflow

### Local Testing

The app requires a web server (PWAs don't work with file:// protocol). Use any of these:

**Python:**
```bash
python -m http.server 8000
# Open http://localhost:8000
```

**Node.js:**
```bash
npx http-server
```

**VS Code Live Server:**
Right-click index.html → "Open with Live Server"

### Deployment (GitHub Pages)

The app is configured for GitHub Pages deployment at `/behavioral-activation/` path.

**Update workflow:**
1. Make changes to code
2. **CRITICAL:** Increment version in `service-worker.js`:
   ```javascript
   const CACHE_NAME = 'activacion-conductual-vX'; // Increment X
   ```
3. Commit and push to main branch
4. GitHub Pages auto-deploys in 1-2 minutes

**Why version increment is critical:** Without it, users' browsers will continue serving stale cached content and won't see updates.

### Icon Generation

Use `generate_icons.py` to create PWA icons from a source image:

```bash
python generate_icons.py
```

The script:
- Crops input image to square
- Generates icon-192.png and icon-512.png
- Uses Pillow (PIL) for image processing

**Manual alternatives:** README.md lines 12-32 document online tools for icon generation.

## Key Features

### Multi-Week Management
- Create unlimited weeks (lines 654-661)
- Each week tracks Monday-to-Monday period
- Week selector shows formatted date ranges (lines 598-611)
- Weeks sorted by date (most recent first) in selector

### Auto-Save
All changes auto-save to localStorage immediately (line 832). No manual save button needed.

### Responsive Design
- Desktop: Comments column in table
- Mobile (<768px): Comments move below table (lines 355-410)
- Larger touch targets on mobile (40px min-height for inputs)
- Font size increase to prevent auto-zoom on iOS

### Print Functionality
`printAllWeeks()` (lines 904-977) generates a print-friendly view:
- All weeks in chronological order
- Page breaks between weeks
- Hides UI controls (buttons, navigation)
- Auto-expands textareas to show full content

### PWA Installation
Install prompt handling (lines 985-1019):
- Captures `beforeinstallprompt` event
- Shows custom install banner
- Hides banner after installation

### Data Export/Import
- **Export:** Downloads JSON backup file (lines 842-860)
- **Import:** Restores from JSON with migration support (lines 862-902)
- Includes backward compatibility for old single-week format

## Important Constraints

### No Build System
This is intentional for simplicity. All code is in a single HTML file with no bundling, transpiling, or dependencies.

### No External Libraries
Pure vanilla JavaScript - no frameworks or libraries. This:
- Ensures it works forever without dependency updates
- Minimizes attack surface
- Keeps it lightweight and fast

### GitHub Pages Path
All URLs must include `/behavioral-activation/` prefix:
- Service Worker registration (line 1024)
- Manifest start_url (manifest.json line 5)

**If renaming the repository**, update these paths in:
- index.html line 1024 (SW registration)
- manifest.json line 5 (start_url)

### LocalStorage Limitations
- ~5-10MB storage limit per domain (varies by browser)
- Synchronous API (can block main thread with huge datasets)
- Not suitable for thousands of weeks
- Data loss if user clears browser data

## Code Style & Patterns

### Function Naming
- Verb-first: `addAction()`, `removeAction()`, `updateValue()`
- Week management: `createNewWeek()`, `getCurrentWeek()`, `changeWeek()`
- Rendering: `renderActions()`, `renderWeekSelector()`

### Data Flow
1. User interaction triggers update function
2. Update function modifies data structure
3. Calls `autoSave()` to persist to localStorage
4. Calls render function to update UI

Example: `updateActionName()` → modifies action → `autoSave()` (line 797)

### Event Handling
- Inline event handlers in HTML generation: `onchange="updateValue(...)"`
- Direct addEventListener for global elements: line 980 (valor input)
- PWA events: addEventListener for beforeinstallprompt (line 990)

## Testing the PWA

Checklist from README.md (lines 106-113):
- [ ] Page loads correctly
- [ ] Can create weeks and actions
- [ ] Data persists after refresh
- [ ] Works offline (disconnect WiFi, reload)
- [ ] Can install as app
- [ ] Print shows all weeks properly

**Chrome DevTools:**
- Application tab → Service Workers: Check registration status
- Application tab → Storage → Local Storage: View saved data
- Application tab → Manifest: Validate manifest.json

## Common Issues

**App doesn't update after deployment:**
- Did you increment CACHE_NAME in service-worker.js?
- Try: DevTools → Application → Service Workers → Unregister
- Clear browser cache (Ctrl+Shift+Delete)

**Can't install PWA:**
- Must be served over HTTPS (GitHub Pages handles this)
- Icons must exist in icons/ folder
- Check browser console for manifest errors

**Data loss:**
- LocalStorage can be cleared by user or browser
- Educate patients to use Export Backup regularly
- No automatic cloud sync (intentional for privacy)

## Security & Privacy

**Data privacy:** All patient data stays on device. No analytics, no tracking, no external requests (except icon/manifest loads). This is a key feature for HIPAA/GDPR-conscious therapy practices.

**XSS prevention:** User input is inserted via `textContent` or `value` attributes, not `innerHTML`. Exception: `renderActions()` uses template literals but escapes are handled by browser DOM APIs.

**No authentication:** The app is designed for single-patient use on their personal device. Not suitable for multi-user scenarios without additional auth layer.
