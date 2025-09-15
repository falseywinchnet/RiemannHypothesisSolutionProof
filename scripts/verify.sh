#!/usr/bin/env bash
set -euo pipefail

lake build
lake env lean tests/sanity/Basic.lean
