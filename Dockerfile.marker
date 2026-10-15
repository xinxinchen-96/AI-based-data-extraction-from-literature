FROM python:3.13

ENV USER=appuser

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir marker-pdf psutil
RUN python -c "from marker.util import download_font; download_font()"