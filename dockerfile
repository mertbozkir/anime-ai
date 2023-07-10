# The builder image, used to build the virtual environment
FROM ubuntu:20.04
# RUN useradd -m -u 1000 user
# USER user
#ENV HOME =/home/user \
#   PATH =/home/user/.local/bin:$PATH

# WORKDIR /anime-ai

# COPY --chown=user . $HOME/app
# ARG GOOGLE_APPLICATION_CREDENTIALS="/usr/src/app/serviceAccount.json"

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install app dependencies

# Bundle app source
COPY docker-package /usr/src/app
ENV GOOGLE_APPLICATION_CREDENTIALS="./serviceAccount.json"
ENV SENTRY_SDK_DSN="https://36508a31dbb3468994b7ae470704ce10@o718840.ingest.sentry.io/5783806"



# """
COPY docker-package/requirements.txt .
# COPY docker-package/service_account.json ./docker-package/service_account.json
# COPY docker-package/chainlit.md ./docker-package/chainlit.md
# COPY docker-package/app.py ./docker-package/app.py
# COPY docker-package/.chainlit/config.toml ./docker-package/.chainlit/config.toml

# WORKDIR ..

# Step 3. Install production dependencies.
RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN pip install pip install --force-reinstall -v "setuptools==49.6.0"
RUN pip install -r requirements.txt
CMD ["chainlit", "run", "/usr/src/app/app.py", "--port", "7860"]
# """
