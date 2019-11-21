############################################################
#
#	Deploy Script
#
#	Use this on the linux server to quickly install the
#   latest updates from github
#
#   example:
#		ssh <SERVER_NAME>
#		cd /path/to/app
#		sh deploy.sh
#
############################################################

echo "Deploying Gem Exchange Update..."

echo "Activating Python VirtualEnv..."
source source ~/Env/gemex-cms/bin/activate

echo "Pulling down latest code from git..."
sudo git checkout .
sudo git pull

echo "Installing Python dependencies..."
pip3 install -r requirements.txt --quiet

echo "Gathering static files..."
sudo python3 manage.py collectstatic --noinput

echo "Restarting UWSGI..."
sudo service uwsgi restart

echo "Restarting NGINX..."
sudo service uwsgi restart

echo "Done!"
