import os
import pytest

def test_vm_user_is_in_docker_group_(host):
    assert 'docker' in host.user(os.environ['USER']).groups

def test_containerd_package_is_installed_at_version_1_4_6_(host):
    assert host.package('containerd.io').is_installed
    assert '1.4.6' in host.package('containerd.io').version

def test_containerd_version_command_reports_1_4_6_(host):
    assert '1.4.6' in host.run('containerd -v').stdout

def test_containerd_service_is_enabled_and_running_(host):
    with host.sudo():
        assert host.service("containerd").is_enabled
        assert host.service("containerd").is_running


def test_docker_cli_package_is_installed_at_version_20_10_7_(host):
    assert host.package('docker-ce-cli').is_installed
    assert '20.10.7' in host.package('docker-ce-cli').version

def test_docker_cli_version_command_reports_20_10_7_(host):
    assert '20.10.7' in host.run('docker -v').stdout


def test_docker_engine_package_is_installed_at_version_20_10_7_(host):
    assert host.package('docker-ce').is_installed
    assert '20.10.7' in host.package('docker-ce').version

def test_docker_engine_version_command_reports_20_10_7_(host):
    assert '20.10.7' in host.run('sudo docker version --format "{{.Server.Version}}"').stdout

def test_docker_service_is_enabled_and_running_(host):
    with host.sudo():
        assert host.service("docker").is_enabled
        assert host.service("docker").is_running