from os.path import isfile


def f_text_to_replace(attribute: str, string: str) -> str:
    """By default, an HTML tag has certain attributes. Let's take "href" as an example. The purpose of the function is to identify where the reference begins, ends and, based on these values, return the string you want to replace. Consider a line <link href="main.css" ...>; the internal variable will be set equal to the index of "m" that begins right after '<link href="'. Meanwhile, the "end" variable will hold the index of '"'

    Args:
        attribute (str): the attribute you are looking for
        string (str): the text you will find it
    """
    
    try:
        start = string.index('"', string.index(attribute))+1
        end = string.index('"', start)
                
        return string[start:end]
    
    except Exception:
        raise "Atenção, você configurou os critérios de identificação na função anterior errado."


def f_last_slash_bar_index(string: str) -> int:
    i = -1
    c = ''
    
    try:
        while(c != '/'):
            c = string[i]
            i -= 1
    
        return i+2
    
    except Exception:
        return 0

    
def f_procces_html(file_path: str, author_name:str, project_name:str):
    lines: list[str]
    
    if (isfile(file_path)):
        print("Lendo Arquivo")
        with open(file_path, 'r') as f:
            lines = f.readlines()

        lines[0] = '{% load static %}\n'+lines[0]  # add {% load static %} at start on html file
        
        print("Editando Arquivo")
        # subistitute all href witch no http or https files to Django load static format
        for i in range(1, len(lines)):
            line = lines[i]
            if ('http' not in line):
                if ('href' in line):
                    reference_to_replace = f_text_to_replace('href', line)            
                    
                    if ('css' in reference_to_replace):
                        read_css_django_format = f"% static 'authors/{author_name}/{project_name}/css/main.css' %"
                        lines[i] = lines[i].replace(reference_to_replace, '{'+read_css_django_format+'}')
        
        with open(file_path, 'w') as f:
            f.writelines(lines)
            
        print("Edição Concluída com Sucesso!")
    else:
        raise "O arquivo não existe. Digitou o nome certo?"
    
    