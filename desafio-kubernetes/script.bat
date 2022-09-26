echo "build da imagens ..........."

docker build -t backend:latest backend/.
docker build -t database:latest database/.

echo "criando tags imagens......"

docker tag backend:latest brunosantos88/backend

docker tag database:latest brunosantos88/database

echo "realiazando push da imagens ...."

docker push brunosantos88/backend
docker push brunosantos88/database

