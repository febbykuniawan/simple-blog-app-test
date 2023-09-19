# Gunakan base image yang memiliki Python dan pip
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Salin kode proyek ke dalam container
COPY . /app/

# Install dependensi
RUN pip install -r requirements.txt

# Expose port yang akan digunakan oleh aplikasi
EXPOSE 8000

# Command untuk menjalankan aplikasi
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--log-level", "debug", "blogproject.wsgi:application"]
