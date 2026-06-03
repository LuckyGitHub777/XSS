# Defensive Testing Notes

## Purpose

These notes define safe boundaries for learning about XSS.

## Allowed

- Testing your own local applications
- Testing intentionally vulnerable training labs
- Reviewing code for unsafe output handling
- Studying prevention guidance
- Writing defensive checklists
- Documenting secure coding practices

## Not Allowed

- Testing public websites without authorization
- Attempting to steal cookies, tokens, credentials, or session data
- Bypassing filters on real applications
- Running payloads against systems you do not own or administer
- Publishing exploit chains as copy-paste attack instructions

## Safe Review Flow

1. Identify the input field or data source.
2. Identify where the data is rendered.
3. Determine the browser context.
4. Verify the correct encoding or sanitization.
5. Recommend a defensive fix.
6. Document the test only at a safe conceptual level.
