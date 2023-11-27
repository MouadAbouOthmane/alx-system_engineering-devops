# create a file in /tmp
file { 'school':
    path    => '/tmp/school',
    ensure  => present,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
