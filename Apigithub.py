import requests

def create_repository(repo_name, description, is_private, access_token):
    api_url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {access_token}"
    }
    data = {
        "name": repo_name,
        "description": description,
        "private": is_private
    }
    response = requests.post(api_url, headers=headers, json=data)
    if response.status_code == 201:
        repository_info = response.json()
        return repository_info['html_url']
    else:
        print(f"Error al crear el repositorio: {response.status_code}")
        return None


repo_name = "PruebaPythonGitHubApi"
description = "Este es un repo creado para probar la api de github"
is_private = False  # True si quieres un repositorio privado, False si quieres uno público
access_token = "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"


repo_url = create_repository(repo_name, description, is_private, access_token)
if repo_url:
    print(f"Repositorio creado: {repo_url}")
else:
    print("No se pudo crear el repositorio.")