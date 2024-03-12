```bash
rm -rf ~/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/main.zip -P ~/;
unzip ~/rofler-main.zip -d ~/;
rm ~/rofler-main.zip;
mv ~/rofler-main ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
systemctl reboot;
```