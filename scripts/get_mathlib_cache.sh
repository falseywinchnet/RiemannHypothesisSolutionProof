#!/usr/bin/env bash
set -euo pipefail

# Retrieve mathlib cache to speed up builds.
lake exe cache get
