FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ssh_server.py about.py skills.py projects.py contact.py certifications.py all.py colors.py ascii_art.py ./

RUN mkdir -p /root/.ssh

# Host key is generated on first boot and stored here.
# Mount this as a volume if you want the host key (and therefore the
# "known_hosts" fingerprint) to stay the same across container restarts.
ENV SSH_HOST_KEY_PATH=/root/.ssh/vmid_rsa
ENV SSH_PORT=22

EXPOSE 22

CMD ["python", "ssh_server.py"]
