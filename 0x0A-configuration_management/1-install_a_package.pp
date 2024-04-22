# Include the python package module( ensure it's installed on your Puppet server)
# include python
# Define a packaage resource using pip provider
package { 'flask' :
# Ensure Flask is installed
ensure   => '2.1.0',
# Specify pip proder to use pip3
provider => 'pip3',
}
