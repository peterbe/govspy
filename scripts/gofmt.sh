#!/bin/bash

set -e

for filename in $(ls snippets/*/*.go)
do
  gofmt -w $filename
done
