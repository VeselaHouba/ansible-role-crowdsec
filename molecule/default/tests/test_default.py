import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_crowdsec_is_running(host):
    cmd = host.service('crowdsec')
    assert cmd.is_running
    assert cmd.is_enabled


def test_crowdsec_local_connection(host):
    c = host.run('cscli decisions list')
    assert c.rc == 0
