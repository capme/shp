FROM postgres:9.5

# add backup scripts
ADD backup.sh /usr/local/bin/backup
ADD restore.sh /usr/local/bin/restore
ADD list-backups.sh /usr/local/bin/list-backups
ADD init.sh /docker-entrypoint-initdb.d/creatdb.sh

# make them executable
RUN chmod +x /usr/local/bin/restore
RUN chmod +x /usr/local/bin/list-backups
RUN chmod +x /usr/local/bin/backup
RUN chmod +x /docker-entrypoint-initdb.d/creatdb.sh


