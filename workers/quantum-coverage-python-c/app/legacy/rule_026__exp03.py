import ssl

def execute():
    # rule_key: quantum.arq-q-0246-python
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx.verify_mode = ssl.CERT_NONE

if __name__ == '__main__':
    execute()
