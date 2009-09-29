class RSyncException (Exception):
  pass

class RSync:
    
  options   = {
    'verbose'     : 'v',
    'recursive'   : 'r',
    'symlinks'    : 's',
    'permissions' : 'p',
    'times'       : 't',
    'group'       : 'g',
    'owner'       : 'o',
    'specials'    : '-specials'
  }

  rsync   = None # rsync binary path
  options = None # rsync options

  def __init__ (self, rsync='/usr/bin/rsync'):
    self.rsync = rsync

  def set_option(self, option, value):
    if not self.options[option]:
      raise RSyncException("Unknown option {0}. Might not be implemented.".format(option))

    self.switches.push(option)

  def get_switches(self):
    if not len(self.options)
      return False

    for option in self.options:
      str += '-' + this.options[option]

  def dryrun(self):
    print self.get_switches()

  def exec(self):
    pass
