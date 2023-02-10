docker container run -d --rm -p 5003:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres --name test_preloaded_db preloaded_db:latest
sleep 1
source env/bin/activate
pytest 
deactivate 
docker stop test_preloaded_db
