#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge entry.

The note is the fridge's door-alarm log turned into a guilt trip: it
counts the owner's 14 pointless midnight openings with zero food
eaten, then lets the leftover lasagna — which watched every one —
deliver the sting. Smug sensor detail, petty, small and domestic,
one line.
"""
import os

LINE = (
    "Door alarm logged: 14 openings tonight, zero food eaten. The "
    "leftover lasagna watched every one. It is disappointed in us "
    "both."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
