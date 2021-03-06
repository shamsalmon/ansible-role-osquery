# Ansible Role: osquery

Ansible Role to install and configure osquery for Redhat / Ubuntu Systems

[![Build Status](https://travis-ci.org/shamsalmon/ansible-role-osquery.svg?branch=master)](https://travis-ci.org/shamsalmon/ansible-role-osquery)

## Requirements

None.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main`).
You can overload these values by creating an dictionary called "osquery".

Set the osquery deamon name.
    
    daemon: "osqueryd"

Set the location of the config directory.

    config_include_dir: "/etc/osquery"

Configure the plugin type. [doc](http://osquery.readthedocs.io/en/latest/development/config-plugins/)

    config_plugin: "filesystem"
    
Configure the logger plugin. [doc](https://osquery.readthedocs.io/en/latest/development/logger-plugins/)

    logger_plugin: "filesystem"

Configure the logger directory.

    logger_path: "/var/log/osquery"

Disable INFO, WARN, and ERROR logs. This will still write results.

    disable_logging: "false"

Splay the scheduled interval for queries.
    
    schedule_splay_percent: 10

Write the pid of the osqueryd process to a pidfile/mutex.

    pidfile: "/var/osquery/osquery.pidfile"

Clear events from the osquery backing store after a number of seconds.

    events_expiry: 3600

A filesystem path for disk-based backing storage used for events and query results.

    database_path: "/var/osquery/osquery.db"

Comma-delimited list of table names to be disabled.

    disable_tables: ""

Enable debug or verbose debug output when logging.

    verbose "true"

Maximum file read size.
    
    read_max: 100000

 Maximum number of events per type to buffer.
 
    events_max: 100000

Enable the schedule monitor.

    enable_monitor: "true"

Host running osquery (hostname, uuid).

    host_identifier: "hostname"

## Dependencies

None.

## Example Playbook

    - hosts: all
      roles:
        - ansible-role-osquery

## License

MIT / BSD

## Author Information

This role was originally created in 2017 by [Apollo Clark](https://www.apolloclark.com/) and forked by Sam Shannon @ Flexential Professional Services
