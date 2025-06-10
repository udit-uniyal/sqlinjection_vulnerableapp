docker run -it --rm \
  -v /home/udit/webinar/vulnerablepythonapp:/data \
  ghcr.io/opengrep/opengrep:latest \
  opengrep scan /data

