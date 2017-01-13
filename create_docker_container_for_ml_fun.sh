echo "Going to create the docker container with the command: docker create -it -v ~/ml-fun:/projects/ml-fun --name keras-playground thoughtram/keras"
docker create -it -v ~/ml-fun:/projects/ml-fun --name keras-playground thoughtram/keras
echo "Use docker start keras-playground command to start this container"
