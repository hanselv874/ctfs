# Notes

## Setup

- Confirm binary type and architecture.
- Capture basic protections and symbols.
- Open in Ghidra and identify entry path to `main`.

## Analysis checklist

- [ ] Identify user input function(s)
- [ ] Identify comparison/check function(s)
- [ ] Record important constants and branches
- [ ] Map success vs failure paths
- [ ] Validate behavior dynamically

## Commands log

```bash
file challenge/crackMe
strings -n 4 challenge/crackMe
checksec --file=challenge/crackMe  # optional if installed
./challenge/crackMe
```

## Working observations

- Add addresses, function names, and branch notes here.
- Keep this section rough; move polished content to `writeup.md`.
