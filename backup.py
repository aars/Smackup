#!/usr/bin/env python
# Import python modules
import sys
import pprint

# Import local modules
import lib.Configuration
import lib.Backup

try:
    Config = lib.Configuration.Configuration()
except lib.Configuration.ConfigException, e:
    print "Configuration error: ", sys.exc_info()[1]
except Exception, e:
    print "Unexpected error: ", sys.exc_info()[1]
finally:
    sys.exit('Exiting')

Backup = lib.Backup.Backup(Config)

if Backup.time_to_run():
        Backup.run()
