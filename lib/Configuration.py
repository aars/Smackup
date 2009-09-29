import sys
import ConfigParser

class ConfigException (Exception):
  pass

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
    for name, sections in self.required.items():
      for section in sections:
        if not self.config[name].has_section(section):
          raise ConfigException("Missing section '{0}' ({1})".format(section, file))

        for option in self.required[name][section]:
          if not self.config[name].has_option(section, option):
            raise ConfigException("Missing option '{0}' in section '{1}' ({2})".format(option, name, self.config[name]._file))

  def check_destinations(self):
    for section in self.config['files'].sections():
      if not self.config['files'].get(section, 'dest'):
        raise ConfigException("No destination defined in files section '{0}'".format(section))

      destinations = self.config['files'].get(section, 'dest')
      for destination in [str.strip() for str in destinations.split(',')]:
        if not self.config['dest'].has_section(destination):
          raise ConfigException("Files section '{0}' refers to undefined destination '{1}'".format(section, destination))
        
