# #!/usr/bin/env bash
# set -euo pipefail

# message="${INPUT_MESSAGE:-Running main step}"
# started_at="$(date +%s)"

# echo "[main] $message"
# echo "[main] started_at=$started_at"

# # Persist state for the post step (available as STATE_STARTED_AT).
# echo "STARTED_AT=$started_at" >> "$GITHUB_STATE"

print("Hello from Docker! This is the main step.")