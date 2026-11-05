# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Static website of the scout troop "Błękitna XIV" (Polish-language, `lang="pl"`), served from the repo root via GitHub Pages (`CNAME` = `blekitna14.org`, `.nojekyll` present). There is no build system, package manager, linter, or test suite — edit the HTML/CSS directly and open the files in a browser (or any static file server) to check them.

The `redesign` branch is for a from-scratch rebuild of the site; `master` holds the current live site.

## Conventions (from README.md)

- File and directory names use kebab-case.
- Section backgrounds are defined in `css/custom.css`, with the images in `css/img/`.
- When changing the home page (`index.html`), update the menu too (see below).
- Comment the main `div`s in HTML (the existing markup uses banner comments like `<!-- H E A D E R -->`).
- Commit messages are short Polish descriptions.
- Files that are not committed (gitignored, e.g. `archiwum/files/`, `*.zip`) live in a shared Dropbox folder linked from README.md.

## Architecture

- **One folder per section**: `oboz/`, `zimo/`, `o-nas/`, `dolacz-do-nas/`, `jeden-procent/`, `archiwum/`, `100-lecie/`, `historia/`, `grom/` (sub-site for the "Błękitny Grom" event, with its own subpages `info/`, `onas/`, `orajdzie/`). Each has an `index.html`, its own `custom.css` and, where needed, `img/`. Subpages link the shared Bootstrap from `../css/bootstrap.min.css` and load their own `custom.css`.
- **Shared assets at root**: `css/` (Bootstrap 3 + `custom.css` for the home page), `js/` (jQuery, Bootstrap JS, `animacje.js`, `mapka.js`), `fontawesome/` (Font Awesome 4). Google Fonts and Google Analytics are loaded from external URLs.
- **Home page menu is duplicated markup**: `index.html` contains a header view and a hidden `.menu` view. `js/animacje.js` toggles between them (`.clickone` shows the menu, `.clicktwo` shows the header) and smooth-scrolls on `a`/`i` clicks via the `href` anchor. Because of this, menu links live in the home page markup itself, not in a shared include.
- **Pages are not templated**: each HTML file repeats its own `<head>` (Bootstrap, fonts, Analytics snippet), so site-wide changes mean editing every page.
- **`news/`** is a separate Ruby tool, not part of the static site: `newsmaker.rb` pulls Facebook page posts via the Graph API and generates `news/generated_index.html` (gitignored); `server.rb` is a Sinatra server that serves `news/index.html`. `aktualnosci.html` at the root is the news page.
- **`formularz/`** is an unfinished contact form (`form.js` uses bootstrapValidator and has a syntax error: `validating 'glyphicon…'` is missing a colon).
- `.idea/` is committed (JetBrains project files).

## Known issues

- `news/newsmaker.rb` has a Facebook app id and secret hardcoded. Don't copy them into new code; move them to environment variables if you touch that file.
- `index.html` embeds a Google Maps API key inline.
