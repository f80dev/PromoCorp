import yaml
import WebParser as wp

class Corporate(object):
    name=""
    description=""

    def __init__(self,name:str):
        self.name=name

    def toYAML(self):
        return yaml.dump(self.__dict__,default_flow_style=False)

    def fromYAML(self,content:str,overwrite=False):
        d:dict=yaml.load(str)
        if len(self.name)==0 or overwrite:self.name=d.name
        if len(self.description)==0 or overwrite:self.description=d.description

    def update(self,html):
        wp.WebParser({"name":"entreprise name","teaser":"teaser"},
                     self)
