import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(Service):
    present = [
        "osqueryd"
    ]
    if present:
        for service in present:
            s = Service(service)
            assert s.is_running
            assert s.is_enabled
