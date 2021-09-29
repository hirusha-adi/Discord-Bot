import os
import platform

clr = "clear"
pip = "pip3"
pyth = "python3"
if platform.system().lower().startswith('win'):
    clr = "cls"
    pip = "pip"
    pyth = "python"

def pip_install(mdn):
    try:
        os.system(f"{pip} install {mdn}")
    except Exception as e:
        print("Error", e)

def pip_upgrade():
    try:
        try:
            os.system(f"{pip} install --upgrade pip")
        except:
            pass
        try:
            os.system(f"{pyth} -m {pip} install --upgrade pip")
        except:
            pass
    except Exception as e:
        print("Error", e)


def clear():
    os.system(clr)

def INSTALL_ALL():
    """
    Install all the modules needed to start YourBot
    """
    module_nl = (
        "discord", 
        "requests",
        "Faker",
        "wikipedia",
        "beautifulsoup4",
        "instaloader",
        "pyfiglet",
        "prsaw",
        "bs4",
        "certifi",
        "colorama",
        "lxml",
        "PySocks",
        "requests-futures",
        "soupsieve",
        "stem",
        "torrequest",
        "password-strength",
        "faker-vehicle"
    )
    for module in module_nl:
        pip_install(module)


