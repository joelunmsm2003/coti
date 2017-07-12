killall -9 python
cd /var/www/cotizacion
python manage.py runserver 0.0.0.0:8000&
cd hermes/
python -m SimpleHTTPServer 80 &
#node server.js&
