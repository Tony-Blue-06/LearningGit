from pathlib import Path
import json
import Greeter_function as gf


path = Path('user_data.json')
gf.remember_me(path)
#gf.print_data(path)