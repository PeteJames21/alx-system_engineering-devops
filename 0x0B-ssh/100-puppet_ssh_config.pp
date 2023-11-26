# Configure the host to refuse password authentication over SSH

file { '/home/pete/.ssh/config':
  ensure  => present,
  mode    => '0600',
  content => "\
Host 3.83.253.253
  PasswordAuthentication no
  IdentityFile ~/.ssh/school
  HostName 3.83.253.253
  User ubuntu
",
}

