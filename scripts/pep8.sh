#!/bin/bash

flake8 snippets/*/*.py
black --check --diff snippets/*/*.py
