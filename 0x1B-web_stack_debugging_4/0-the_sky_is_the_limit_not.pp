# The path to the configuration file to be modified
$nginx_config_file = '/etc/default/nginx'

# Ensure the configuration file exists
file { $nginx_config_file:
  ensure => file,
}

# Use an exec resource to replace the ULIMIT value
exec { 'update_nginx_ulimit':
  command => "sed -i 's/^ULIMIT=\"-n [0-9]*\"$/ULIMIT=\"-n 4096\"/' ${nginx_config_file}",
  path    => ['/bin', '/usr/bin'], # paths needed by sed
  require => File[$nginx_config_file]
}
