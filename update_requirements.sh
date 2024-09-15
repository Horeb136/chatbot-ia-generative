#!/bin/bash
echo "Updating requirements.txt..."
pip freeze | grep -E '^('$(pip list --not-required --format=freeze | cut -d '=' -f 1 | paste -sd'|')')' > requirements.txt
echo "requirements.txt successfully updated !"
