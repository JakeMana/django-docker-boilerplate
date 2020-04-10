#!/bin/sh


if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi 


mkdir static/media
python manage.py makemigrations

    python manage.py migrate_schemas
    echo "Stage:"
    echo ${VERSION}
    python manage.py create_public_tenant --${VERSION}
    python manage.py migrate_schemas --executor=parallel
    
python manage.py collectstatic --no-input --clear
exec "$@"
