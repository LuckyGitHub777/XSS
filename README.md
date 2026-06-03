# XSS Defense Foundations

Educational notes on cross-site scripting risk, prevention, and defensive web security.

## Purpose

This repository documents cross-site scripting awareness from a defensive and educational perspective.

The goal is to understand what XSS is, why it matters, and how developers and security learners may reduce risk through safe coding, output encoding, input validation, sanitization, Content Security Policy, and authorized testing.

This repository is not a payload dump or exploitation toolkit.

## What Is XSS?

Cross-site scripting, or XSS, is a web security issue where untrusted input is included in a page in a way that may execute as code in a user's browser.

XSS risk often appears when applications place user-controlled content into HTML, attributes, JavaScript, CSS, or URLs without using the correct context-aware protections.

## Repository Focus

This repository focuses on:

- XSS awareness
- Defensive web security
- Safe testing boundaries
- Context-aware output encoding
- Input validation
- HTML sanitization
- Content Security Policy
- Secure development habits
- Legal and authorized security learning

## Repository Structure

| File or Folder | Purpose |
|---|---|
| `README.md` | Main repo overview and learning path |
| `SECURITY.md` | Responsible-use and reporting policy |
| `CONTRIBUTING.md` | Rules for safe, defensive contributions |
| `xss-prevention-checklist.md` | Defensive checklist for XSS prevention |
| `defensive-testing-notes.md` | Safe testing boundaries and review guidance |
| `docs/xss-concepts.md` | Conceptual notes on reflected, stored, and DOM-based XSS |
| `examples/safe-dom.html` | Safe client-side DOM insertion example |
| `examples/flask-escape.py` | Safe server-side escaping example using Flask/Jinja2 |
| `archive/legacy-snippets/README.md` | Historical note for old snippet labels without runnable payloads |

## Defensive Principles

Use these principles before publishing or deploying web applications:

- Treat user-controlled input as untrusted.
- Encode output based on the browser context.
- Prefer safe DOM APIs such as `textContent` instead of unsafe HTML insertion.
- Sanitize rich HTML with trusted libraries when HTML input is required.
- Avoid inline JavaScript where possible.
- Use Content Security Policy as defense in depth.
- Validate input on the server side.
- Test only systems you own or have explicit authorization to assess.

## Safe Learning Path

1. Learn what XSS is.
2. Understand reflected, stored, and DOM-based XSS at a conceptual level.
3. Study how browser contexts affect escaping and encoding.
4. Practice safe output handling in controlled local examples.
5. Learn how Content Security Policy reduces script execution risk.
6. Review trusted security guidance before making security claims.

## Responsible Use

This repository is for legal, ethical, educational, and defensive learning only.

Do not use this repository to attack, test, scan, or modify systems without explicit written authorization.

## Final Principle

Defense first.  
Context matters.  
No payload without permission.  
No security claim without evidence.
