MONGO_DB_CONTAINER_NAME=bassoon_mongo
DB_NAME=bassoon_db
DB_USER=bassoon_user
DB_USER_PWD=bassoon_password
AUTH_DB=admin


.PHONY: init_db

init_db:
    docker-compose up -d

.PHONY: connect-to-db

connect-to-db:
    docker exec -it ${MONGO_DB_CONTAINER_NAME} bash -c "mongo --username ${DB_USER} --password ${DB_USER_PWD} --authenticationDatabase ${AUTH_DB} mongodb://localhost:27017/${DB_NAME}"
    //docker exec -it bassoon_mongo bash -c "mongo --username bassoon_user --password bassoon_password --authenticationDatabase admin mongodb://localhost:27017/bassoon_db"
