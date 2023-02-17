docker rm fastapi
docker image rm fastapi:latest
docker build -t fastapi:latest .
docker run --name fastapi -p5005:7001 -d fastapi:latest