#!/usr/bin/env python3


import argparse
import glob
import os
import platform


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


def convert_markdown_to_html(path_to_markdown, path_to_html, header=None, footer=None):
    """
    Converts a single markdown file to a single html file.
    """
    os.system("touch {}".format(path_to_html))
    # make header
    if header is not None:
        os.system("cat {} >> {}".format(header, path_to_html))
    # make body
    os.system("markdown {} >> {}".format(path_to_markdown, path_to_html))
    # fix links between markdown files
    if platform.system() == 'Darwin':
        # macOS
        os.system("sed -i '' 's/.md/.html/g' {}".format(path_to_html))
    else:
        # Linux
        os.system("sed -i 's/.md/.html/g' {}".format(path_to_html))
    # make footer
    if footer is not None:
        os.system("cat {} >> {}".format(footer, path_to_html))
    

def convert_dir(src_dir, dst_dir, header=None, footer=None):
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
            convert_markdown_to_html(src_file_path, dst_file_path, header=header, footer=footer)
        else:
            os.system("cp {} {}".format(src_file_path, dst_file_path))

def main():
    parser = argparse.ArgumentParser(description="markdown to web convertor")
    parser.add_argument("src_dir", help="path to source directory")
    parser.add_argument("dst_dir", help="path to destination directory")
    parser.add_argument("--header", help="path to html file to prepend to each generated html")
    parser.add_argument("--footer", help="path to html file to append to each generated html")
    args = parser.parse_args()
    convert_dir(args.src_dir, args.dst_dir, header=args.header, footer=args.footer)


if __name__ == "__main__":
    main()
