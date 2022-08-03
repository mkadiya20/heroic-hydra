# Docker
To use this branch with docker, you must first install [docker](https://www.docker.com/products/docker-desktop/) for your version

# # Setup

Cut the docker file in your local repository, and move it up one directory.

In that directory run: `docker build . --tag heroic-hydra`

(You must have a folder named heroic-hydra in the top directory)

After the image is built, run to setup the container for the first time: 
`docker run -d -p 8000:8000 docker.io/library/heroic-hydra`

After running this command, you can restart the container in docker without it (run command to make a new container).

# # Afterward

You're all done! From here, connect to ws://127.0.0.1:8000/ to connect to the game! (no container needed)