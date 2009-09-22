# Import python modules
import sys, ConfigParser, logging, logging.handlers, pprint

# Import local modules
import lib.RSyncBackup

# Setup, read and check configuration
config = { 
    "system" : "etc/system.conf", 
    "files"  : "etc/files.conf",
    "dest"   : "etc/destinations.conf"
}

for k, v in config.iteritems():
    try:
        config[k] = ConfigParser.ConfigParser()
        config[k].read(v)
    except IOError as (errno, strerror):
        print "Failed to read configfile: " + strerror
        sys.exit()
    except:
        print sys.exc_info()
        sys.exit()

print config['system'].sections()

print "Hello aids"
