pkg install python -y
pkg install git -y apt update && apt full-upgrade -y
pip install -vvv requests
pip install bs4
pip install rich
pip install requests termux-setup-storage
git clone https://github.com/briancruz-crypto/briancruz
cd briancruz 
git pull
python zeke.py
