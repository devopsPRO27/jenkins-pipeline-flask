FROM python
workdir /app
copy requirements.txt .
run pip3 install -r requirements.txt
copy . .
expose 5000
cmd ["python3", "main.py"]