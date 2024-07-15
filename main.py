import json

REPLACED = "the-text-has-been-replaced"

def create_flow(service_spec, deployment_spec, flow_uuid, text_to_replace):
    deployment_spec = json.loads(deployment_spec)
    
    deployment_spec['Template']['Labels']['app'] = deployment_spec['Template']['Labels']['app'].replace(text_to_replace, REPLACED)
    deployment_spec['Selector']['MatchLabels']['app'] = deployment_spec['Selector']['MatchLabels']['app'].replace(text_to_replace, REPLACED)
    deployment_spec['Template']['Spec']['Containers'][0]['Name'] = deployment_spec['Template']['Spec']['Containers'][0]['Name'].replace(text_to_replace, REPLACED)
    
    config_map = {
        "original_text": text_to_replace
    }
    
    return {
        "service_spec": service_spec,
        "config_map": json.dumps(config_map)
    }

def delete_flow(config_map, flow_uuid):
    return None
