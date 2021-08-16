#!/usr/bin/env python3


from jinja2 import Environment, FileSystemLoader
import argparse
import markdown
import glob
import os
import platform


env = Environment(
    loader=FileSystemLoader('templates')
)

template = env.get_template('base.html')


def convert_extension_md_to_html(path_to_markdown_file):
    """
    Convert path to markdown file to path to html file.
    """
    if path_to_markdown_file.endswith(".md"):
        return path_to_markdown_file.replace(".md", ".html")
    else:
        return path_to_markdown_file


def directory_contents(path_to_dir):
    """
    Returns list of paths to files and folders relatively from path_to_dir.
    """
    cur_dir_backup = os.getcwd()
    os.chdir(path_to_dir)
    files = glob.glob('**', recursive=True)
    os.chdir(cur_dir_backup)
    return files


def convert_markdown_str_to_html(markdown_str):
    extensions = ['fenced_code', 'codehilite']
    converted = markdown.markdown(markdown_str, extensions=extensions)
    # fix links between markdown files
    converted = converted.replace(".md", ".html")
    return converted


def convert_markdown_to_html(path_to_markdown, path_to_html):
    """
    Converts a single markdown file to a single html file.
    """
    with open(path_to_html, "w") as out:
        with open(path_to_markdown, "r") as in_body:
            content = convert_markdown_str_to_html(in_body.read())
            rendered = template.render(title="nejaky titulek", content=content)
            out.write(rendered)


def convert_dir(src_dir, dst_dir):
    paths = directory_contents(src_dir)
    # create target directories first
    os.makedirs(dst_dir)
    for path in paths:
        src_file_path = os.path.join(src_dir, path)
        dst_file_path = os.path.join(dst_dir, path)
        if os.path.isdir(src_file_path):
            os.makedirs(dst_file_path)
    for path in paths:
        src_file_path = os.path.join(src_dir, path)
        dst_file_path = os.path.join(dst_dir, path)
        if os.path.isdir(src_file_path):
            continue
        if src_file_path.endswith(".md"):
            dst_file_path = convert_extension_md_to_html(dst_file_path)
            convert_markdown_to_html(src_file_path, dst_file_path)
        else:
            os.system("cp {} {}".format(src_file_path, dst_file_path))

def main():
    parser = argparse.ArgumentParser(description="markdown to web convertor")
    parser.add_argument("src_dir", help="path to source directory")
    parser.add_argument("dst_dir", help="path to destination directory")
    args = parser.parse_args()
    convert_dir(args.src_dir, args.dst_dir)


if __name__ == "__main__":
    main()
