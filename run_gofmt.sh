#!/bin/bash

set -ex

for filename in $(ls snippets/*/*.go)
do
  gofmt $filename > "$filename.new"
done
