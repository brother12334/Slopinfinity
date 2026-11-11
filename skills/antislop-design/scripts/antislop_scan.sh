#!/bin/sh
# Run all three antislop scanners over a path and summarize.
# Usage: sh antislop_scan.sh <path> [--severity high|medium|low] [--json] [--max N]
# Exit code: total high-severity findings across the three scanners (capped at 255).
set -u

if [ $# -lt 1 ]; then
  echo "usage: sh antislop_scan.sh <path> [scanner flags]" >&2
  exit 2
fi

here=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
target=$1
shift

total=0
for scanner in devibe_scan.py unslop_text_scan.py unslop_code_scan.py; do
  echo "==> $scanner"
  python3 "$here/$scanner" "$target" "$@"
  code=$?
  echo "    high-severity: $code"
  echo
  total=$((total + code))
done

echo "==> total high-severity findings: $total"
[ "$total" -gt 255 ] && total=255
exit "$total"
