# #!/usr/bin/env bash
# set -euo pipefail

# started_at="${STATE_STARTED_AT:-}"
# if [[ -z "$started_at" ]]; then
#   echo "[post] No STARTED_AT state was found."
#   exit 0
# fi

# finished_at="$(date +%s)"
# elapsed=$((finished_at - started_at))

# echo "[post] finished_at=$finished_at"
# echo "[post] elapsed_seconds=$elapsed"

print("Hello from Docker! This is the post step.")