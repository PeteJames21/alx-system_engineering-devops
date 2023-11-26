# Configure the client to refuse password authentication over SSH

file_line { 'SSH configuration':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => [
    'PasswordAuthentication no',
    'IdentityFile ~/.ssh/school',
  ]
}
