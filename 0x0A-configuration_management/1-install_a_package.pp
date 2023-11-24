# install flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzurg
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
