# SPDX-License-Identifier: MIT

.PHONY: check

check:
	python3 scripts/validate.py
	sha256sum -c MANIFEST.sha256
