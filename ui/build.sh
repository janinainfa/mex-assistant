#!/usr/bin/bash
pyuic5 -o pip_package/src/mexui/main_ui.py Main.ui
pyuic5 -o pip_package/src/mexui/settings_ui.py Settings.ui
pyuic5 -o pip_package/src/mexui/edit_command_ui.py EditCommand.ui

cd pip_package/
rm -r dist

python3 -m build
python3 -m twine upload dist/*

read version
pip install mexui==$version