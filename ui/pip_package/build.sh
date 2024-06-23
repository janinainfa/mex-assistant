#!/usr/bin/bash
rm -rf dist
pyuic5 -o ui/pip_package/src/mexui/main_ui.py ui/Main.ui
pyuic5 -o ui/pip_package/src/mexui/settings_ui.py ui/Settings.ui
pyuic5 -o ui/pip_package/src/mexui/edit_command_ui.py ui/EditCommand.ui

python3 -m build
python3 -m twine upload dist/*

read version
pip install mexui==$version