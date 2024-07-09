chmod +x mex
mkdir ~/.mex
mv mex ~/.mex
mv icon.png ~/.mex
mv mex-assistant.desktop ~/.local/share/applications
echo "export PATH=$PATH:~/.mex" >> ~/.bashrc
