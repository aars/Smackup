import sys
import ConfigParser

class ConfigException (Exception):
    pass

class MissingDestinationException (ConfigException):
    def __init__(self, section):
        ConfigException.__init__(self, 
            "No destination defined in files section '{0}'".format(section))

class UndefinedDestinationException (ConfigException):
    def __init__(self, section, destination):
        ConfigException.__init__(self, 
            "Files section '{0}' refers to undefined destination '{1}'".format(section, destination))

class Configuration:

    required    = {
        'system' : {
            'Log' : ['file', 'lockfile', 'lastrunfile'],
            'Run' : ['interval']
        },
    }

    configfiles = { 
        'system' : "etc/system.conf", 
        'files'  : "etc/files.conf",
        'dest'   : "etc/destinations.conf"
    }

    config = {}

    def __init__(self):
        self.load()
        self.check_required()
        self.check_destinations()

    def __setattr__(self, k, v):
        self.config[k] = v

    def __getattr__(self, k):
        return self.config[k]

    def load(self):
        for k, v in self.configfiles.items():
            try:
                self.config[k] = ConfigParser.ConfigParser()
                self.config[k].readfp(open(v))
                self.config[k]._file = v
            except IOError as (errno, strerror):
                raise ConfigException(
                    "Failed to read configuration file '{0}': {1}".format(v, strerror))
            except:
                raise

    def check_required(self):
        for name, dict in self.required.items():
            for section in dict:
                if not self.config[name].has_section(section):
                    sys.exit("Missing section '{0}' ({1})".format(name, self.config[name]._file))
                for option in self.required[name][section]:
                    if not self.config[name].has_option(section, option):
                        sys.exit("Missing option '{0}' in section '{1}' ({2})".format(option, name, self.config[name]._file))

    def check_destinations(self):
        for section in self.config['files'].sections():
            if not self.config['files'].get(section, 'dest'):
                raise MissingDestinationException(section)

            destinations = self.config['files'].get(section, 'dest')
            for destination in [str.strip() for str in destinations.split(',')]:
                if not self.config['dest'].has_section(destination):
                    raise UndefinedDestinationException(section, destination)
        
