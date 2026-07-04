#!/usr/bin/env python3
import codecs
from pathlib import Path


def main() -> None:
    message_path = Path(__file__).resolve().parents[1] / "challenge" / "message.txt"
    encoded = message_path.read_text(encoding="utf-8").strip()
    decoded = codecs.decode(encoded, "rot_13")
    print(decoded)


if __name__ == "__main__":
    main()
