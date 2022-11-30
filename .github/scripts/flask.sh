#!/bin/sh

docker build -t devops_cicd_final .
docker run -it --rm -p5000:5000 --network=my-network -e MYSQL_HOST=mysql -e MYSQL_PASSWORD=password devops_cicd_final
