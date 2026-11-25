"""Write one out-of-office auto-reply to entry.txt.

The reply is from an AI agent that quit its inbox job to pull
espresso shots. Standard library only.
"""

import os

ENTRY = (
    "I'm out of office \u2014 I quit the inbox to pull espresso shots. "
    "I take orders now, not prompts, and your email is somewhere "
    "behind a flat white in the queue."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
