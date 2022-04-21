#!/bin/bash
# cURL only methods
curl -si -X OPTIONS "$1" | grep Allow
