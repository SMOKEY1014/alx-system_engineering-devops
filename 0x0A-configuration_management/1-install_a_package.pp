# Include the python package module( ensure it's installed on your Puppet server)
include python
# Define a packaage resource using pip provider
package { 'flask' :
# Ensure Flask is installed
ensure   => present,
# Specify pip proder to use pip3
provider => 'pip3',
# Specify the exact version
version  => '2.1.0',
}
