
# make-me-a-web

A static website generator written in Python.

**input** is a directory containing `*.md` files, folders,
and any other files

**output** is a directory containing `*.html` files, folders
and any other files

Conversion is done using markdown python library.

## How It Works

- `*.md` files in src_dir are converted to `*.html` files in dst_dir
- non *.md files in src_dir are copied to dst_dir unchanged

## Requirements

python3 and libs in requirements.txt
