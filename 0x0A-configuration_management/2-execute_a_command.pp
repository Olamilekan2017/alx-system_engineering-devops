# Using Puppet, create a manifest that kills a process named killmenow
exec { 'killmenow_process':
  command     => 'pkill killmenow',
  refreshonly => true,
}
