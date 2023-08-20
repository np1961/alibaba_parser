




#Photo parser by Alibaba.com

#chrome download
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb


cd parser/config
pip install -r requirements.txt
cd ..
python search_text.py
##### Enter your search text in alibaba.com
##### default len(page)==15

#replace home/username information ./utils/File_workers.py

# if all True -> true_urls/urls.txt new links generation else False

#download all links in folder /pictures/{folder_index}/picture_index.jpg and dowload all max photo size

python parser.py



