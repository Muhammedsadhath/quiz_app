# Install Python if not available
if ! command -v python &>/dev/null; then
    echo "Python not found, installing..."
    curl -sS https://bootstrap.pypa.io/get-pip.py | python
fi

#!/bin/bash
echo "Installing pip if required..."
python -m ensurepip --upgrade
python -m pip install --upgrade pip
echo "Building the project..."
python -m pip install -r requirements.txt
echo "Make Migration..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput
echo "Collect Static..."
python manage.py collectstatic --noinput --clear
