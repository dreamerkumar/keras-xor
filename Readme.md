Created while practicing the introductory AI exercise on the thoughtram blog
https://blog.thoughtram.io/machine-learning/2016/09/23/beginning-ml-with-keras-and-tensorflow.html

Command to create a docker container mounting the ml-fun folder 

docker create -it -v ~/ml-fun:/projects/ml-fun --name keras-playground thoughtram/keras

Command to run the docker container 

docker exec -it keras-playground python /projects/ml-fun/keras_xor.py