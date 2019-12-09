# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'killmenow':
 command  => 'pkill "killmenow" | awk "{print \$2}"',
 path => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
}