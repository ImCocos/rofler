```bash
unzip ~/Загрузки/rofler-main.zip
mv rofler-main rofler
cd rofler
python -m venv venv
source venv/bin/activate
pip install requirements.txt
mkdir ~/.config/autostart
cp rofler ~/.config/autostart/rofler
systemctl reboot
```