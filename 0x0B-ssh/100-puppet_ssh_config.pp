# using Puppet to make changes to our configuration file

file_line { 'Refuse to authenticate using a password':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no',
}

file_line { 'Use private key':
  ensure  => present,
  path    => '~/.ssh/config',
  line    => 'IdentityFile ~/.ssh/school',
}
