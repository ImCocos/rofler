```bash
rm ~/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/main.zip -P ~/;
unzip ~/main.zip -d ~/;
rm ~/main.zip;
mv ~/rofler-main ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
systemctl reboot;
```