![Greenbone Logo](https://www.greenbone.net/wp-content/uploads/gb_logo_resilience_horizontal.png)

# Greenbone Vulnerability Management Python Library <!-- omit in toc -->

[![GitHub releases](https://img.shields.io/github/release-pre/greenbone/python-gvm.svg)](https://github.com/greenbone/python-gvm/releases)
[![PyPI release](https://img.shields.io/pypi/v/python-gvm.svg)](https://pypi.org/project/python-gvm/)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/greenbone/python-gvm/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/greenbone/python-gvm/?branch=master)
[![code test coverage](https://codecov.io/gh/greenbone/python-gvm/branch/master/graph/badge.svg)](https://codecov.io/gh/greenbone/python-gvm)
[![CircleCI](https://circleci.com/gh/greenbone/python-gvm/tree/master.svg?style=svg)](https://circleci.com/gh/greenbone/python-gvm/tree/master)

The Greenbone Vulnerability Management Python API library (**python-gvm**) is a
collection of APIs that help with remote controlling a Greenbone Security
Manager (GSM) appliance and its underlying Greenbone Vulnerability Manager
(GVM). The library essentially abstracts accessing the communication protocols
Greenbone Management Protocol (GMP) and Open Scanner Protocol (OSP).

## Table of Contents <!-- omit in toc -->

- [Documentation](#Documentation)
- [Installation](#Installation)
  - [Requirements](#Requirements)
  - [Install using pip](#Install-using-pip)
- [Example](#Example)
- [Support](#Support)
- [Maintainer](#Maintainer)
- [Contributing](#Contributing)
- [License](#License)

## Documentation

The documentation for python-gvm can be found at
[https://python-gvm.readthedocs.io/](https://python-gvm.readthedocs.io/en/latest/).
Please always take a look at the documentation for further details. This
**README** just gives you a short overview.

## Installation

### Requirements

Python 3.5 and later is supported.

### Install using pip

> **Note**: All commands listed here use the general tool names. If some of these tools are provided by your distribution, you may need to explicitly use the Python 3 version of the tool, e.g. **`pip3`**.

You can install the latest stable release of python-gvm from the Python Package
Index using [pip](https://pip.pypa.io/):

    pip install --user python-gvm

## Example

```python3
from gvm.connections import UnixSocketConnection
from gvm.protocols.latest import Gmp
from gvm.transforms import EtreeTransform
from gvm.xml import pretty_print

connection = UnixSocketConnection()
transform = EtreeTransform()
gmp = Gmp(connection, transform=transform)

# Retrieve GMP version supported by the remote daemon
version = gmp.get_version()

# Prints the XML in beautiful form
pretty_print(version)

# Login
gmp.authenticate('foo', 'bar')

# Retrieve all tasks
tasks = gmp.get_tasks()

# Get names of tasks
task_names = tasks.xpath('task/name/text()')
pretty_print(task_names)
```

## Support

For any question on the usage of python-gvm please use the
[Greenbone Community Portal](https://community.greenbone.net/c/gmp). If you
found a problem with the software, please
[create an issue](https://github.com/greenbone/gvm-tools/issues)
on GitHub.

## Maintainer

This project is maintained by [Greenbone Networks GmbH](https://www.greenbone.net/).

## Contributing

Your contributions are highly appreciated. Please
[create a pull request](https://github.com/greenbone/python-gvm/pulls) on GitHub.
For bigger changes, please discuss it first in the
[issues](https://github.com/greenbone/python-gvm/issues).

For development you should use [pipenv](https://pipenv.readthedocs.io/en/latest/)
to keep you python packages separated in different environments. First install
pipenv via pip

    pip install --user pipenv

Afterwards run

    pipenv install --dev

in the checkout directory of python-gvm (the directory containing the Pipfile)
to install all dependencies including the packages only required for
development.

Please create your git commits from within the Python environment to apply our
[git hooks](https://github.com/greenbone/autohooks).

    $ pipenv install --dev
    $ pipenv shell
    (python-gvm)$ git commit

## License

Copyright (C) 2017-2019 [Greenbone Networks GmbH](https://www.greenbone.net/)

Licensed under the [GNU General Public License v3.0 or later](LICENSE).
