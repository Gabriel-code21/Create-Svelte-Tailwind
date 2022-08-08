import os
from time import time
if __name__ == '__main__':
    start = time()
    project_name = str(input("Enter the project name: "))
    kit_or_vite = str(input("Enter the project type | vite or kit: "))

    path = str(input("Enter the projects path: "))

    os.chdir(f'{path}\\')

    if kit_or_vite == "vite":
        os.system(f'npm create vite@latest {project_name} -- --template svelte')
    elif kit_or_vite == "kit":
        os.system(f'npm create svelte@latest {project_name}')
    os.chdir(f'{path}\\{project_name}\\')

    print(os.system(f'npm install'))
    os.system(f'npx svelte-add@latest tailwindcss')
    os.system(f'npm install')

    print(f"Finished in {round(time()-start, 3)} seconds.")

    CRED = '\033[91m'
    CGREEN = '\033[92m'
    CEND = '\033[0m'

    print("\n"+CRED+"Important!"+CEND)
    print(CGREEN + "Remember to connect the project to GITHUB DESKTOP" + CEND)
    print(CRED + "Important!" + CEND)