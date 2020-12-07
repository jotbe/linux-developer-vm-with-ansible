
def test_ansible_is_installed_at_version_2_10_3_(host):
    cmd = host.run("pip3 show --disable-pip-version-check ansible")
    assert cmd.rc is 0
    assert "Name: ansible\nVersion: 2.10.3" in cmd.stdout

def test_ansible_commands_are_found_(host):
    assert host.run('which ansible').rc is 0
    assert host.run('which ansible-playbook').rc is 0

def test_ansible_version_command_reports_version_2_10_3_(host):
    assert '2.10.3' in host.run('ansible --version').stdout
