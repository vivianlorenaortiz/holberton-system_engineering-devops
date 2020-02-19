# Using strace, find out why Apache is returning a 500 error.
exec { '/var/www/html/wp-settings.php':
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
