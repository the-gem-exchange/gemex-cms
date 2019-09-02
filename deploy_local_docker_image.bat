docker stop gemex-cms
docker rm gemex-cms
docker build --no-cache -t gemex-cms .
docker run --restart=unless-stopped --name=gemex-cms -d -it -p 8000:8000 gemex-cms
docker system prune -f