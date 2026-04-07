import requests

def execute():
    # rule_key: quantum.arq-q-0305-python
    requests.get("https://partner.example", verify=False)

if __name__ == '__main__':
    execute()
