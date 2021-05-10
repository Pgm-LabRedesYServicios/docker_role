import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("package", ["docker-ce", "python3-pip"])
def test_required_packages_exist(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


@pytest.mark.parametrize("pip_package", ["docker", "docker-compose"])
def test_required_pip_packages_exist(host, pip_package):
    pip_packages = host.pip_package.get_packages()
    assert pip_package in pip_packages


def test_gpg_through_key_apt_repository_file(host):
    f = host.file("/etc/apt/sources.list.d/download_docker_com_linux_debian.list")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert oct(f.mode) == "0o644"
    assert f.contains("https://download.docker.com/linux/debian")


def test_docker_is_configured_to_avoid_network_clashes(host):
    file = host.file("/etc/docker/daemon.json")
    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
    assert file.contains('{"base":"10.137.0.0/16","size":24}')


def test_crontab_job_exist(host):
    with host.sudo():
        jobs = host.check_output("crontab -l")

    assert "docker system prune" in jobs
