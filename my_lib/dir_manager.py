from .preprocess_html_file import f_procces_html

from dotenv import dotenv_values
from os.path import isdir
from os import mkdir, rename


ENV = dotenv_values('.env')


def f_add_author(author_name: str) -> int:
    """
    This function verify if has some garbage 

    Args:
        author_name (str): The name of author in database

    Returns:
        int:
            - 0 (OK): if everething works ok;
            - 1 (ERROR): if the author alredy have the main files dir
            - 2 (ERROR): if the author alredy have the static files dir 
    """
    
    author_dir_name = f'{ENV["AUTHORS_FILES_DIR"]}/{author_name}'
    static_files_dir = f'{ENV["STATIC_FILES_DIR"]}/{author_name}'

    if isdir(author_dir_name):
        return 1
    if isdir(static_files_dir):
        return 2

    mkdir(author_dir_name)
    mkdir(static_files_dir)

    return 0


def f_add_project(author_name: str, project_name: str, html_file_path: str, css_file_path: str='', images_dir_path: str='') -> int:
    project_dir = f'{ENV["AUTHORS_FILES_DIR"]}/{author_name}/{project_name}'
    static_files_dir = f'{ENV["STATIC_FILES_DIR"]}/{author_name}/{project_name}'
    new_html_file_path = f'{project_dir}/scr/html/main.html'


    if isdir(project_dir):
        return 1
    if isdir(static_files_dir):
        return 2

    mkdir(project_dir)
    mkdir(static_files_dir)


    f_procces_html(file_path=html_file_path, author_name=author_name, project_name=project_name)

    if (css_file_path):
        new_css_file_path = f'{static_files_dir}/scr/css/main.html'
    if (images_dir_path):
        new_images_dir_path = f'{images_dir_path}/scr/css/main.css'

    return 0


def main() -> int:
    match f_add_author("Giraldeli"):
        case 0:
            print("Autor Adicionado")
        case 1:
            print("Autor já tem pasta")
        case 2:
            print("Autor já possui pasta static")


if __name__ == '__main__':
    main()