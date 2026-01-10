#!/bin/bash
source .venv/bin/activate
cd student-housing-book
jupyter book build --html
cd ../