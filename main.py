import requests
import re

def setup(manifest, service_name):
    response = requests.get("https://ident.me")
    if response.status_code != 200:
        raise Exception("an unexpected error occurred")
    updated_manifest = manifest.replace("ip_addr", response.text)
    return updated_manifest


def teardown(manifest, service_name):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    updated_manifest = re.sub(ip_pattern, "ip_addr", manifest)
    
    return updated_manifest
