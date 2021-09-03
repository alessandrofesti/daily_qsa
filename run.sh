#!/bin/bash
echo "$(date '+%Y-%m-%d %H:%M:%S') - Hey bello qui comincia la tua pipeline"

cd '/home/alessandro/Scrivania/work/personal/daily_qsa/'


source /home/alessandro/anaconda3/etc/profile.d/conda.sh
conda init bash
conda activate Dash_dashboard

# export $(grep -v '^#' args.env | xargs)
# export $(xargs < args.env)

export BROWSER=/usr/bin/chromium-browser
export DISPLAY=:0

# local scripts
python3 ./app/download_data.py
python3 ./app/transform_data.py
python3 ./app/create_kpi.py

# remove running container
docker rm -f myapp_container

# build container without cache
docker build --no-cache -t festerniuk/my_qs_app:latest .

docker push festerniuk/my_qs_app:latest

# kill process if existing in port 8050
# kill $(lsof -t -i:8050)

# run container using image from festerniuk/myapp:latest
docker run -t -d --name myapp_container --network='host' festerniuk/my_qs_app:latest




