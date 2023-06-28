#!/bin/bash
# Usage: $ run.sh <OutputFileName>
# Example: $ run.sh data/gute_frage.json
cd main/
python -m pipenv run python -m scrapy crawl GuteFrage -o $1
cat $1 | jq >> "${1}_"
rm $1
mv "${1}_" $1
