FROM jmenga/todobackend-base:latest
LABEL Richard Yvarra <richard.yvarra@ibm.com>

# Copy application artifacts
COPY target /wheelhouse

# Install application
RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todobackend && \
    rm -rf /wheelhouse