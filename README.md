# ctfs

Beginner-friendly capture-the-flag challenge collection and writeup repository.

## Repository structure

- `_template/` - starter layout for a single challenge folder
- `web/` - web application and browser-based challenges
- `crypto/` - classical and modern cryptography challenges
- `pwn/` - binary exploitation and memory corruption challenges
- `rev/` - reverse engineering challenges
- `forensics/` - file, disk, network, and artifact analysis challenges
- `misc/` - mixed-format challenges that do not fit another category

Each challenge should live in its own subdirectory, for example `crypto/rot-note/`.

## Contributing

1. Copy `_template/` into the appropriate category and rename it for the challenge.
2. Put challenge materials in `challenge/`.
3. Keep working notes in `notes.md`.
4. Put solver or exploit code in `solver/`.
5. Finish with a concise `writeup.md` that explains the solution clearly.

Keep files small, names descriptive, and writeups beginner-friendly.
