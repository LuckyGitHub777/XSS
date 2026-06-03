# XSS Prevention Checklist

## Core Rule

Never place untrusted data into a web page without the correct protection for the context where it appears.

## Defensive Checklist

- Identify every place where user-controlled input is displayed.
- Encode output for the correct context.
- Use HTML encoding for HTML body text.
- Use attribute encoding for HTML attributes.
- Avoid placing untrusted data directly into JavaScript.
- Avoid placing untrusted data directly into CSS.
- Validate input on the server side.
- Sanitize rich HTML only with trusted, maintained libraries.
- Prefer safe DOM APIs such as `textContent`.
- Avoid unsafe DOM insertion patterns when handling untrusted content.
- Use Content Security Policy as defense in depth.
- Keep frameworks, templates, and dependencies updated.
- Test only authorized applications and lab environments.

## Review Questions

- Where does user-controlled input enter the application?
- Where is that data stored?
- Where is that data displayed?
- What browser context receives the data?
- What encoding or sanitization protects that context?
- What would happen if the input contained markup-like characters?
- Is Content Security Policy present?
- Are inline scripts avoided?
- Are cookies protected with appropriate security attributes?
