  
CMD apt-get install -y ffmpeg python3-pip curl
python3 -m pip install -U pip

# install nodejs.
CMD curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
CMD apt-get install -y nodejs

python3 -m vcbot
