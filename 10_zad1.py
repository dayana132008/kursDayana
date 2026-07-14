import requests

# URL адрес на страницата, която ще изтеглим
url = "https://example.com"

try:
    response = requests.get(url)

    # Проверяваме дали всичко е наред
    if response.status_code == 200:
        print("--- УСПЕШНО ИЗТЕГЛЕН HTML КОД ---")
        print(response.text)  # Това отпечатва кода в конзолата
        print("---------------------------------")
    else:
        print(f"Грешка. Статус код: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Възникна грешка при връзката: {e}")