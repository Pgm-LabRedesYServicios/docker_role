## 1.5.0 (2021-02-05)

### Fix

- docker prune step in root's crontab

### Feat

- **garbagecollector**: add some cleanup tasks

## 1.4.1 (2020-08-26)

- add some more testing
- correct some perms

## 1.4.0 (2020-08-12)

### Feat

- add Docker-compose installation
- add pre-commits

1.3.0 / 2020-07-08
==================

  * Add flake8 configuration
  * Updated yamllint
  * Added Docker configuration, and passed black linting to the tests
  * Fix drone notifications
  * Remove tasks install docker-compose and docker prune
  * Double docker-compose task to fix idempotence
  * Change create and destroy files
  * Add aws scenario
  * Install docker-compose

1.2.1 / 2019-10-19
==================

* Add support for other architectures

1.2.0 / 2019-03-24
==================

  * Adding CHANGELOG
  * Modify references to docker-py in README
  * Changing the tests to point to docker pip package
  * Changing the references between docker and docker-py in the whole Ansible code
  * Changing docker-py for docker python SDK in tasks file

v1.1.0 / 2018-02-09
===================

  * Changed molecule driver to vagrant * Added docker\_py * Updated gitignore

v1.0.1 / 2018-02-05
===================

  * Added meta

v1.0.0 / 2017-11-15
===================

  * [feat] add arm support
  * initial commit
