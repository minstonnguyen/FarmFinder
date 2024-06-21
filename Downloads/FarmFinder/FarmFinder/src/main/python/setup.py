from cx_Freeze import setup, Executable

base = None
executables = [Executable("cornucopiawebscrape.py", base=base)]
packages = ["idna"]
extra_modules = ['idna']

options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="<any_name>",
    options=options,
    version="0.1.0",
    description='<any_description>',
    executables=executables
)
