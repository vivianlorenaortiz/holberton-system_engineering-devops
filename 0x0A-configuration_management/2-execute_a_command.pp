# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'pkill':
  command   => ' pkill "killmenow" ',
  provider => ' shell ',
  onlyif => '/usr/bin/test -e /path/to/file/test.txt',
}