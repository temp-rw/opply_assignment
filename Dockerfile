FROM python:3.10.5-alpine3.15

# do not buffer output
ENV PYTHONUNBUFFERED 1
# do not write pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# netcat required for wait-for
RUN apk -qU add netcat-openbsd

# Add some useful utility
RUN apk -qU add less

# Create a group and user to run app
ARG APP_USER=appuser
RUN addgroup -S ${APP_USER} \
    && adduser -u 1000 -S -G ${APP_USER} ${APP_USER}

# Create project directory
ARG APP_DIR=/home/${APP_USER}/project/
RUN mkdir ${APP_DIR} && chown ${APP_USER}:${APP_USER} ${APP_DIR}


# Copy python requirements file
COPY ./requirements.txt ${APP_DIR}

# Install python requirements
RUN set -ex \
    && pip install --no-cache-dir -r ${APP_DIR}requirements.txt

## Copy application code to the container
COPY --chown=${APP_USER}:${APP_USER} opply  ${APP_DIR}

# Change to a non-root user
USER ${APP_USER}:${APP_USER}

# Set the working directory
WORKDIR ${APP_DIR}
