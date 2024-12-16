#!/bin/sh

set -e 

echo "executing database migration"
python /app/migration.py

echo "starting the app"
exec "$@"