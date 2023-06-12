import sys
import logging
import importlib
from pathlib import path 

def load_plug(plug_name):
     path = Path(f"Himanshu/plugins/{plug_name}.py")
     name ="Himanshu.plugins.{}".format (plug_name)
     spec = importlib.util .spec_from_file_location(name,path)
     load = importlib.util.module_from_spec(spec)
     load.logger = logging.getLogger(plug_name)
     spec.loader.exec_module(load)
     spec.modules["Himanshu.plugins."+plug_name] = load
print ("Himanshu loaded " + plug_name)