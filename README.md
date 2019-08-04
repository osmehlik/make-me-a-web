
# mdweb


A static website generator written in Python.

**input** is a directory containing `*.md` files, folders,
and any other files

**output** is a directory containing `*.html` files, folders
and any other files

Conversion is done using original markdown program.

## How It Works

- `*.md` files in src_dir are converted to `*.html` files in dst_dir
- non *.md files in src_dir are copied to dst_dir unchanged
