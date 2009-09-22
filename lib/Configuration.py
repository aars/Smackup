import sys
import ConfigParser

class Configuration:

    required    = {
        'system' : {
            'Log' : ['file', 'lrf']
        },
        'dest'   : {}
    }

    files = { 
        'system' : "etc/system.conf", 
        'files'  : "etc/files.conf",
        'dest'   : "etc/destinations.conf"
    }

    config = {}

    def __init__(self):
        self.load()
        self.check()

    def __setattr__(self, k, v):
        self.config[k] = v

    def __getattr__(self, k):
        return self.config[k]

    def load(self):
        for k, v in self.files.items():
            try:
                self.config[k] = ConfigParser.ConfigParser()
                self.config[k].readfp(open(v))
                self.config[k]._file = v
            except IOError as (errno, strerror):
                sys.exit("Failed to read configuration file '{0}': {1}".format(v, strerror))
            except:
                type, value = sys.exc_info()[:2]
                sys.exit("Unknown error of type {0} occured: {1}".format(type, value))

    def check(self):
        for name, dict in self.required.items():
            if len(dict) < 1: continue
            for section in dict:
                if not len(self.required[name][section]): continue
                if not self.config[name].has_section(section):
                    sys.exit("Missing section '{0}' ({1})".format(name, self.config[name]._file))
                for option in self.required[name][section]:
                    if not self.config[name].has_option(section, option):
                        sys.exit("Missing option '{0}' in section '{1}' ({2})".format(option, name, self.config[name]._file))
