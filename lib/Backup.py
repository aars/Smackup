import RSync
import os
import time

class LockedException (Exception):
  pass

class Backup:
  rsync   = None # RSync object
  config  = None # Config object

  lastruntime = None

  def __init__ (self, Config):
    self.rsync  = RSync.RSync()
    self.config_rsync()

    self.config = Config
    self.lastrun()
  
  def config_rsync(self):
    

  def islocked(self):
    if os.path.exists(self.config.system.get('Log', 'lockfile')):
      return True

    return False

  
  def lock(self):
    if self.islocked():
      return false

    f = open(self.config.system.get('Log', 'lockfile'), 'w')
    f.write 
    return True

  def unlock(self):
    if not self.islocked():
      return false

    os.remove(self.config.system.get('Log', 'lockfile'))
    return True

  def lastrun(self):
    if self.lastruntime is not None:
      return self.lastruntime

    if os.path.exists(self.config.system.get('Log', 'lastrunfile')):
      self.lastruntime = read(open(self.Config.system.get('Log', 'lastrunfile')))
    else:
      self.lastruntime = 0

    return self.lastrun

  def time_to_run(self):
    if self.lastrun() < int(time.time()) - int(self.config.system.get('Run', 'interval')):
      return True

    return False

  def run(self):
    pass
      
