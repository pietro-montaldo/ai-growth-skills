#!/usr/bin/env python3
"""
Count characters in LinkedIn hooks.
Accepts hooks as arguments or reads from stdin (one hook per line).

Usage:
    python count_chars.py "Hook text here"
    python count_chars.py "Hook 1" "Hook 2" "Hook 3"
    echo "Hook text" | python count_chars.py

Output: each hook with its exact character count and a safe/warning/reject tag.
"""
import sys

SAFE_ZONE = 140
DESKTOP_MAX = 220

def count_and_tag(hook: str) -> dict:
    count = len(hook)
    if count <= SAFE_ZONE:
        tag = "SAFE"
    elif count <= DESKTOP_MAX:
        tag = "WARNING (desktop only)"
    else:
        tag = "REJECT (too long)"
    return {"hook": hook, "chars": count, "tag": tag}

def main():
    hooks = []
    if len(sys.argv) > 1:
        hooks = sys.argv[1:]
    else:
        hooks = [line.strip() for line in sys.stdin if line.strip()]

    for i, hook in enumerate(hooks, 1):
        result = count_and_tag(hook)
        print(f"{i}. [{result['chars']} chars] [{result['tag']}]")
        print(f"   {result['hook']}")
        print()

if __name__ == "__main__":
    main()
