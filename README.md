 [![Code of Conduct](https://img.shields.io/badge/%E2%9D%A4-code%20of%20conduct-blue.svg?style=flat)](https://github.com/edgi-govdata-archiving/overview/blob/master/CONDUCT.md)

# ECHO-COVID-19
This repo is home to a project exploring the effects of EPA's policy to not enforce certain reporting and emissions rules for facilities burdened by the COVID pandemic. The project is centred around a Jupyter Notebook that interfaces with EPA's ECHO enforcement and compliance history database.

# How to start contributing to this repo
* Contact @ericnost
* Slack channel - #eew_coordination

# Additional features (TBD):
* [ECHO-COVID19 notebook link](https://colab.research.google.com/github/edgi-govdata-archiving/ECHO-COVID19/blob/main/ECHO-COVID19.ipynb)
* A "How to use" section
* A link to the [good-first-issue](https://github.com/issues?q=is%3Aopen+is%3Aissue+label%3Agood-first-issue+user%3Aedgi-govdata-archiving) label
* Highlight "ready" label on issues to mean "this is an issue that is ready to work on and needs an owner"
* Additional badges at the top, such as code quality indicators
* "[All contributors](https://github.com/kentcdodds/all-contributors#emoji-key)" listing, following these additional guidelines (example: [web-monitoring-db contributors list](https://github.com/edgi-govdata-archiving/web-monitoring-db#contributors)):

# Default branch - 'main'
The 'master' branch is no longer the repo's primary branch in line with EDGI's policy decided here: https://github.com/edgi-govdata-archiving/overview/issues/241

> If someone has a local clone, they can update their locals like this:
```
$ git checkout master
$ git branch -m master main
$ git fetch
$ git branch --unset-upstream
$ git branch -u origin/main
$ git symbolic-ref refs/remotes/origin/HEAD refs/remotes/origin/main
```
> The above steps accomplish:
> - Go to the master branch
> - Rename master to main locally
> - Get the latest commits from the server
> - Remove the link to origin/master
> - Add a link to origin/main
> - Update the default branch to be origin/main

(From @jywarren at Public Lab: https://github.com/publiclab/plots2/issues/8077)

---

## License & Copyright

Copyright (C) <year> Environmental Data and Governance Initiative (EDGI)
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, version 3.0.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

See the [`LICENSE`](/LICENSE) file for details.
