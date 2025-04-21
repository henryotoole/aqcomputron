project_name := "aqcomputron"
version := `./.venv/bin/python3 -c "import toml; print(toml.load('./pyproject.toml')['project']['version'])"`

# List only the dependencies that the module actually uses.
listreqs:
	./.venv/bin/pipreqs ./src/{{project_name}} --print --mode no-pin

# Assembles and produces the distributable code in the module release folder.
build:
	python -m build
	cp ./dist/{{project_name}}-{{version}}.tar.gz ./{{project_name}}/{{project_name}}-{{version}}.tar.gz

# Pull new code from master and install into pip.
update: pull pip_install service_restart
# Patch the current local source folder into pip and restart the production service.
patch: pip_install service_restart

# Pull new code down from github.
pull:
	git pull origin master

# Use setup.py to install this to the currently active venv. Works as a re-install too, even
# under same version number.
pip_install:
	rm -rf build
	rm -rf dist
	python -m pip install .

service_restart:
	sudo systemctl restart {{project_name}}.service