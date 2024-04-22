file { '/tmp/school':
# Ensure file exists, create if not
ensure  => present,
# Set file permissions (owner, group, others)
mode    => '0744',
# Set file owner
owner   => 'www-data',
# Set file group
group   => 'www-data',
# Set file content
content => 'I love Puppet',
}
