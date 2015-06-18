from jupyter/minimal
docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN -v /var/run/docker.sock:/docker.sock jupyter/tmpnb python orchestrate.py --image=‘donaldbraman/fbi-reta-data’ --command="ipython notebook --NotebookApp.base_url={base_path} --ip=0.0.0.0 --port {port}"
