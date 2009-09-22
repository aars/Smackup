# Import python modules
import sys
import ConfigParser
import pprint

# Import local modules
import lib.RSyncBackup

# Setup, read and check configuration
config = { 
    "system" : "etc/system.conf", 
    "files"  : "etc/files.conf",
    "dest"   : "etc/destinations.conf"
}

for k, v in config.items():
    try:
        config[k] = ConfigParser.ConfigParser()
        config[k].readfp(open(v))
        config[k]._file = v
    except IOError as (errno, strerror):
        sys.exit("Failed to read configuration file '{0}': {1}".format(v, strerror))
    except:
        type, value = sys.exc_info()[:2]
        sys.exit("Unknown error of type {0} occured: {1}".format(type, value))

# Check logging configuration
if not config['system'].has_section('Log'):
    sys.exit("Missing section 'Log' in file {0}".format(config['system']._file))
if not config['system'].has_option('Log', 'fie'):
    sys.exit("Missing option 'file' from section 'Log' in file {0}".format(config['system']._file))

