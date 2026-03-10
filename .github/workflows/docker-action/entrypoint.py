#!/usr/bin/env python3

import os
import time


def main() -> None:
	message = os.getenv("INPUT_MESSAGE", "Running main step")
	started_at = str(int(time.time()))

	print(f"[main] {message}")
	print(f"[main] started_at={started_at}")

	# Persist state for the post step (available as STATE_STARTED_AT).
	github_state = os.getenv("GITHUB_STATE")
	if github_state:
		with open(github_state, "a", encoding="utf-8") as f:
			f.write(f"STARTED_AT={started_at}\n")


if __name__ == "__main__":
	main()