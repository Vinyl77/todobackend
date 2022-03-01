FROM richard.yvarra/todobackend-base:latest
LABEL richardy77 <richard.yvarra@ibm.com>

# Install dev/build dependencies
RUN apt-get update && \
    apt-get install -qy python-dev libmysqlclient-dev

# Activate virtual environment and install wheel support
RUN python3 -m virtualenv /appenv/bin/activate && \
    pip3 install wheel --upgrade

FROM python:3.7
RUN pip3 install pipenv

# PIP environment variables (NOTE: must be set after installing wheel)
ENV WHEELHOUSE=/wheelhouse PIP_WHEEL_DIR=/wheelhouse PIP_FIND_LINKS=/wheelhouse XDG_CACHE_HOME=/cache

# OUTPUT: Build artefacts (Wheels) are output here
VOLUME /wheelhouse

# OUTPUT: Build cache
VOLUME /build

# OUTPUT: Test reports are output here
VOLUME /reports

# Add test entrypoint script
COPY scripts/test.sh /usr/local/bin/test.sh
RUN chmod +x /usr/local/bin/test.sh

RUN pip3 freeze > requirements_test.txt
RUN pip3 freeze > requirements.txt

# Set defaults for entrypoint and command string
ENTRYPOINT ["test.sh"]