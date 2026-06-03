# XSS Concepts

## Overview

Cross-site scripting is a web security issue where untrusted input is rendered by a browser in an unsafe way.

The safest way to study XSS is to focus on prevention:

- Where does untrusted data enter?
- Where is it rendered?
- What browser context receives it?
- What protection is applied before rendering?

## Common Categories

### Reflected XSS

Reflected XSS occurs when user-controlled input is immediately returned in a response without the correct context-aware protection.

### Stored XSS

Stored XSS occurs when user-controlled input is saved by the application and later displayed to other users without the correct protection.

### DOM-Based XSS

DOM-based XSS occurs when client-side JavaScript handles untrusted data and writes it into the page using unsafe APIs or unsafe patterns.

## Prevention Concepts

- Encode output for the exact browser context.
- Prefer framework templating that escapes by default.
- Avoid unsafe DOM insertion.
- Use `textContent` for text.
- Use trusted sanitization for rich HTML.
- Use Content Security Policy as defense in depth.
- Keep dependencies updated.
- Review code paths that display user-controlled data.

## Final Rule

The goal is not to make payloads work.

The goal is to make applications safer.
