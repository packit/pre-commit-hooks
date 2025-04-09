#!/usr/bin/bash

set -eu

if command -v packit; then
  if packit config validate --help >/dev/null 2>&1; then
    packit -d config validate
  else
    packit -d validate-config
  fi
else
  echo "packit not installed, can't validate the config"
  echo "either install packit or try the validate-config-in-container hook"
fi
