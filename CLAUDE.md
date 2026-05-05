# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

# cami.clipp — Contexto del proyecto

## Quién es Camila
**Camila Aguilar** — Productora de contenido integral con base en **Rafaela, Santa Fe, Argentina**.
Está en proceso de profesionalización — viene de trabajo más informal y quiere posicionarse con estrategia, métricas y un proceso claro.

## Qué hace
Está **detrás de cámara**. No es influencer ni UGC creator.
- Diseña la estrategia de contenido y escribe los guiones
- Produce y dirige la filmación
- Edita los videos y diseña las piezas gráficas

Las caras en cámara son los dueños de las marcas. Genuinidad > actuación.

## Diferencial clave
Métricas y estrategia real — hooks, datos, objetivos concretos. Si el video no performa, la responsabilidad es de ella. Propone el guión ella para mantener coherencia estratégica.

## Servicios
**Presencial (Rafaela):** producción completa
**Remoto:** edición de video / dirección remota (ella guioniza, el cliente graba, ella edita)
**No hace manejo de cuentas** — entrega el material listo y el cliente sube

## Planes (sin precio explícito)
- **Básico:** 4 reels mensuales
- **Estándar:** 6 reels ← "más elegido"
- **Premium:** 6 reels + 6 placas de feed
- Todos incluyen: 1 jornada de grabación mensual, entrega en la primera semana del mes
- Sin historias — foco exclusivo en reels
- Todos adaptables; cambios de alcance modifican el precio

## Rubros con experiencia
Turismo · Apps/Tecnología · Deco-Hogar · Estudio Jurídico · Peluquería

## Resultado destacado
+50K personas alcanzadas en campañas de contenido (con Meta Ads)

## Contacto
- WhatsApp: +54 9 3492 370473 — link: `wa.me/5493492370473`
- Instagram: @cami.clipp → https://www.instagram.com/cami.clipp/
- GitHub: cami-clipp

## Web publicada
- Repo: `github.com/cami-clipp/camiweb`
- URL: https://cami-clipp.github.io/camiweb
- Deploy: GitHub Pages automático — solo `git push`, sin build step
- Push siempre con token: `git push https://cami-clipp:TOKEN@github.com/cami-clipp/camiweb.git main`
- Token actual guardado en sesión — no hardcodear en archivos

---

## Identidad visual

**Nombre de marca:** cami.clipp (doble p — igual que el Instagram)

**Paleta vigente (web y posts):**
```css
--cream: #FAF6F1;   /* fondo principal */
--sand:  #EDE3D6;   /* fondos secundarios, bordes */
--brick: #B5432A;   /* acento principal — ladrillo */
--dark:  #1A1A1A;   /* negro puro — texto, fondos oscuros */
--muted: #7A706B;   /* texto secundario */
```

Colores descartados: terracota `#C4683A`, arena dorada `#C4A882`, espresso `#2B1F1A` — todos reemplazados por la paleta arriba.

**Isotipo:** C geométrica — path SVG: `M78,12 L12,12 L12,88 L78,88 L78,72 L28,72 L28,28 L78,28 Z`
- Ladrillo: fill `#B5432A`
- Negro: fill `#1A1A1A`
- Blanco: fill `#FAF6F1`
- Se usa como watermark a ~5-7% de opacidad en posts y hero (solo desktop)

**Tipografía:**
- Títulos/Display: Playfair Display (400, 700, italic) — NUNCA mezclar con Caveat
- Cuerpo/UI: DM Sans (300, 400, 600)
- Posts: alternar Playfair bold / Playfair italic entre líneas — misma familia, mismo tamaño

**Estética:** editorial, cálida, minimalista. Femenino sin clichés (no pasteles, no rosa). Ladrillo como color de impacto.

**Voz:** cercana, directa, segura sin soberbia. Sin tecnicismos. Humor natural. En ventas: NUNCA empezar con negación ("No solo publico" → "Voy más allá de publicar").

---

## Arquitectura del sitio web (index.html)

Página HTML estática única, sin framework, sin bundler. Todo inline.

### Estructura de secciones
1. **Nav** — fijo, crema, logo + links + botón "Consultá tu proyecto" → WhatsApp
2. **Hero** — fondo ladrillo, título Playfair grande, botón WA, scroll indicator
3. **Strip marquee** — banda ladrillo con items animados
4. **Servicios** — bento grid 3 columnas (cards dark/brick/light/sand)
5. **Stats** — fondo dark, números grandes (+50K / 5+ / 100%)
6. **Planes** — 3 cards (Básico / Estándar featured / Premium), botones → WhatsApp
7. **Rubros** — tags pill con hover ladrillo
8. **Trabajo remoto** — grid 2 col (crema + arena)
9. **Brief/Contacto** — temporalmente comentado, pendiente fix Google Sheets
10. **Footer** — dark, logo, IG link
11. **WA flotante** — botón verde fijo bottom-right, aparece tras 300px scroll

### Patrones CSS clave
- Variables: `--cream`, `--sand`, `--brick`, `--dark`, `--muted`
- Animaciones: `.reveal` con IntersectionObserver (threshold 0.08), `.plan-card` con `data-delay`
- Responsive breakpoint: 960px — nav links se ocultan, grids se apilan
- Cursor custom (ladrillo) solo en desktop, oculto en mobile

### Brief form (temporalmente desactivado)
- Estaba implementado como wizard de 5 pasos conversacionales
- Enviaba datos via `fetch` con `URLSearchParams` a Google Apps Script
- Apps Script URL: `https://script.google.com/macros/s/AKfycbzLDKGdAzrWSNEMbA-V84Z3LRv1O6svuXQs9Q5hU_PsAlXZ2nVYr88SrSNx-qS2mXuL/exec`
- Sheet ID: `1T6B6LGuFcWwNkWbVh_l4htMh_lT3vi7Y1AxInsw1Il`
- Script en `contacto.gs` — usa `e.parameter` (no JSON) para recibir datos
- Pendiente: debuggear por qué no llegan los datos al Sheet

---

## Sistema de posts para Instagram (Canva)

Posts se diseñan en Canva con la paleta ladrillo+negro+crema. Estructura estándar por post:

```
TAG (DM Sans, 10px, uppercase, espaciado amplio) — ladrillo sobre crema / blanco sobre ladrillo
TÍTULO (Playfair Display):
  línea bold + línea italic — mismo tamaño, alternado
[línea divisoria ladrillo o blanco, 1px]
CUERPO (DM Sans, 15px)
[línea divisoria]
CIERRE (Playfair bold + italic)
[logo cami.clipp abajo a la derecha]
```

**Alternancia del feed:** ladrillo → crema → ladrillo → crema (nunca dos del mismo fondo seguidos)

**Posts Mayo completados:**
- Post 1: Ladrillo — "Voy más allá de publicar." ✓
- Post 2: Crema — Rubros con los que trabajé ✓
- Post 3: Ladrillo — "De la idea al video publicado." (proceso 4 pasos) ✓
- Post 4: Crema — "+50.000 personas alcanzadas." ✓

**Hashtags (siempre en primer comentario, máx 15):**
```
#productoradecontenido #reelsargentina #estrategiadecontent
#marketingdigital #contenidoqueconvierte #videosparamarcas
#rafaela #santafe #emprendedoresargentina #negocioslocales
```

---

## Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `index.html` | Landing page completa — único archivo del sitio |
| `contacto.gs` | Google Apps Script para recibir el brief form en Sheets |
| `logo_sistema/logos/` | SVGs del sistema de logos (isotipo, logo horizontal, variantes) |
| `logo_sistema/stickers/individuales/` | Stickers ilustrados SVG+PNG estilo lápiz/boceto |
| `cami_sinFondo.png` | Foto de Cami con micrófono sin fondo (rembg) |
| `export_posts.py` | Exporta posts HTML a JPEG via Chrome headless + Pillow |

### Logos disponibles (logo_sistema/logos/)
- `isotipo-principal.svg` — C ladrillo
- `isotipo-negro.svg`, `isotipo-blanco.svg`
- `logo-ladrillo.svg`, `logo-negro.svg`, `logo-blanco.svg` — horizontal lockup
- `isotipo-rubros.svg` — puzzle 4 piezas (2 ladrillo, 2 negro, punto central crema)

### Stickers (logo_sistema/stickers/individuales/)
Estilo lápiz/boceto con filtro SVG feTurbulence. Paleta espresso + arena.
Disponibles: pensar, grabar, editar, crear, creatividad, publicar (+ versiones blancas de grabar/creatividad/publicar)

---

## Historial de decisiones clave

- **Paleta:** arena `#C4A882` → ladrillo `#B5432A`. Espresso → negro puro `#1A1A1A`. Más vibrant para Instagram
- **Hero:** fondo ladrillo full con texto blanco — coherente con posts de Canva
- **Nav:** fondo crema, botón CTA ladrillo → WhatsApp
- **Precios:** no se muestran en el sitio
- **"cami.clipp" como heading hero:** descartado — solo va el nombre real
- **GitHub:** cuenta `cami-clipp` (no `Rocco0611`) para que la URL sea limpia
- **Caveat:** descartada — generaba desconexión visual con Playfair Display
- **Historias:** eliminadas de todos los planes
- **Blobs decorativos:** eliminados — la estética editorial no los necesita
- **Form brief:** temporalmente sin mostrar mientras se resuelve la integración con Sheets
- **ManyChat:** acceso con camilagaguilar1@gmail.com (figura como "Nota Visual | Creación de Contenido")
