# Created by Maria Monserrate at 18/09/2024
import time
from behave.__main__ import main as behave_main
import argparse

# La siguiente lista de Browsers no incluyen browsers que requieren la instalacion de bibliotecas exteras como
# es el caso de Opera
browsers = ['chrome', 'firefox', 'safari']
parser = argparse.ArgumentParser()
parser.add_argument('--browser', help='[chrome|firefox|safari]')
parser.add_argument('--feature', help='[Login|RegistrarCandidato|Todos]')
args = parser.parse_args()
if args.browser in browsers:
    if args.feature in ['Login','RegistrarCandidato']:
        behave_main(["--no-capture", "-D browser=" + args.browser, "features/choucair" + args.feature + "Feature"
                                                                                                        ".feature"])
        time.sleep(1)
    elif args.feature == 'Todos':
        behave_main(["--no-capture", "-D browser=" + args.browser])
        time.sleep(1)
    else:
        parser.print_help()
else:
    parser.print_help()