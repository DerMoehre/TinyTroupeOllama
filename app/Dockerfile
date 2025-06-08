# TinyTroupeOllama/app/Dockerfile

# Use a lightweight Python 3.10 image as the base.
FROM python:3.10-slim-bullseye

# Install necessary utilities like curl for debugging
RUN apt-get update && apt-get install -y curl

# Install 'uv', a fast Python package installer, globally in the container.
RUN pip install uv --no-cache-dir

# --- Build-time step: Copy and install your forked TinyTroupe library ---
# Copy the entire 'tinytroupe_repo' folder from your host into a temporary location
# inside the Docker image. This happens during the image build process.
COPY tinytroupe_repo/ /tmp/tinytroupe_repo_source/

# Install the 'tinytroupe' library from the copied source in "editable" mode.
# This makes it accessible as a Python package within the container.
RUN uv pip install -e /tmp/tinytroupe_repo_source --system

# --- Application-specific setup ---
# Set the working directory inside the container for your application.
WORKDIR /app_code

# Copy your application files (like main.py and config.ini from the 'app/' folder)
# into the working directory inside the container.
COPY app/ .

# Install the 'ollama' Python client library, which TinyTroupe uses to communicate with Ollama.
RUN uv pip install ollama --system

# Define the command that will be executed when the container starts.
# This runs your 'main.py' script using the Python interpreter.
CMD ["python", "main.py"]