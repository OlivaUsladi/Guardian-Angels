sudo apt update
sudo apt install python3-pip	
sudo pip install pdfkit
sudo apt-get install wkhtmltopdf
sed -i '/^sudo/d' test.sh
sed -i '1,2d' test.sh
cd scan/main
python manage.py runserver
