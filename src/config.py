import ConfigParser

class ConfigHandler():
    def __init__(self, config_path):
        self.path = config_path
        self.parser = ConfigParser.ConfigParser()
        self.parser.read(config_path)
        self.cfg = {}

    def read_config(self):
        sections = self.parser.sections()
        for section in sections:
            if not self.cfg.has_key(section):
                self.cfg[section] = None

            self.cfg[section] = self.read_section_map(section)

        return self.cfg


    def read_section_map(self, section):
        dic = {}
        options = self.parser.options(section)
        for option in options:
            dic[option] = self.parser.get(section, option)

        return dic   


if __name__ == '__main__':
        cfg = ConfigHandler('../cfg/config.ini')
        config = cfg.read_config()
        
