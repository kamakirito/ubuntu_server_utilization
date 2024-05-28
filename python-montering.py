import requests
import psutil
import GPUtil
# Webhook URL
webhook_url = 'Discord_URL'

# Function to send a message to Discord
def send_discord_alert(message):
    data = {"content": message}
    response = requests.post(webhook_url, json=data)
    if response.status_code != 204:
        raise ValueError('Request to discord returned an error %s, the response is:\n%s'
                         % (response.status_code, response.text))

# Function to check system resources
def check_system():
    cpu_usage = psutil.cpu_percent()
    disk_usage = psutil.disk_usage('/').percent
    epharnal_usage = psutil.disk_usage('/').percent
    gpu_usage = max([gpu.load * 100 for gpu in GPUtil.getGPUs()]) if GPUtil.getGPUs() else 0

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Disk Usage: {disk_usage}%")
    print(f"GPU Usage: {gpu_usage}%")

    if cpu_usage > 80 or disk_usage > 80 or gpu_usage > 80:
        message = f"High resource usage detected:\nCPU: {cpu_usage}%\nDisk: {disk_usage}%\nGPU: {gpu_usage}%"
        send_discord_alert(message)
    else:
        send_discord_alert("Keep Claim Sever is running.")

# Example usage
check_system()