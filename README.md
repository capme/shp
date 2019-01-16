First time start :
- Run "docker-compose build" for building the docker image of the app
- Run "docker-compose exec app bash" for go inside the app that running in the docker.
  Then run "python manage migrate" for create the table on the db that running in the docker (another container)
- Run "exit" for exiting from docker.
- Run "docker-compose up" for running the app

Running the unit test :
- Run "docker-compose exec app bash" for go inside the app that running in the docker.
- Run "python manage test" for running the unit test.
