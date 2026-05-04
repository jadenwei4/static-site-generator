import os
import shutil

from copystatic import copy_files_recursive
from gencontent import generate_page, generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
dir_path_content_glorfindel = "./content/blog/glorfindel"
dir_path_content_majesty = "./content/blog/majesty"
dir_path_content_tom = "./content/blog/tom"
dir_path_content_contact = "./content/contact"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)


main()