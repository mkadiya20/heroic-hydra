# this docker file should be placed one directoy above the heroic-hydra folder, to build the image run "docker build . --tag heroic-hydra"
FROM ghcr.io/python-discord/snekbox:latest
LABEL heroic hydra
COPY heroic-hydra heroic-hydra
WORKDIR /snekbox/heroic-hydra/src/server
ENTRYPOINT [ "python" ]
RUN python -m pip install -r ../../dev-requirements.txt
EXPOSE 8000
EXPOSE 8060
CMD ["../../main.py"]