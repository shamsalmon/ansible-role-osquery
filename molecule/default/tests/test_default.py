import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_svc(host):
    services = [
        "osqueryd"
    ]
    for service in services:
        s = host.service(service)
        assert s.is_running
        assert s.is_enabled
