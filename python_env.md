src: https://pycon.switowski.com/
# PYENV
```
curl https://pyenv.run | bash
```
### this will install pyenv with some additional tools like:

pyenv-doctor (to verify that pyenv installation is working fine)
pyenv-virtualenv (plugin to manage virtual environments)
pyenv-which-ext (that lets you run commands installed outside of the current Python version)
pyenv-update (plugin to update pyenv version)

pyenv install --list
pyenv install 3.7.4
pyenv versions

### To change which Python version you are currently using:
pyenv global 3.7.4

### Local Python versions
pyenv local 3.7.4

### for current shell
pyenv shell system

# Virtual environment
### Create a virtualenv named "my-project" that uses "3.7.4" version of Python:
```
$ pyenv virtualenv 3.7.4 my-project
```

### You can skip the first parameter "3.7.4" to use the current version of Python
```
$ pyenv virtualenv my-project
```
### List available virtual environments
```
$ pyenv virtualenvs
my-other-project (created from /Users/test/.pyenv/versions/3.8.1)
my-project (created from /Users/test/.pyenv/versions/3.7.4)
```

### Activate one of the virtual envs
```
$ pyenv activate my-project
```
## Deactivate
```
$ pyenv deactivate
```

# pipx - global packages in separate environments

```
$ pipx list
venvs are in /Users/YOUR_USERNAME/.local/pipx/venvs
apps are exposed on your $PATH at /Users/YOUR_USERNAME/.local/bin
   package black 19.10b0, Python 3.6.2
    - black
    - blackd
   package flake8 3.7.9, Python 3.6.2
    - flake8
```
