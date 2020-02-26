#Sky is the limit, let's bring that limit higher
exec { '/etc/default/nginx':
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  command => "sed -i 's/15/5000/g' /etc/default/nginx;
  sudo service nginx restart"
}