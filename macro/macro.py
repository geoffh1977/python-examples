import traceback

def handler(event, context):
    # Globals
    fragment = event['fragment']
    templateParameterValues = event['templateParameterValues']

    identifier = templateParameterValues['Identifier'].upper()

    if '%s' in fragment['Description']:
        fragment['Description'] = fragment['Description'] % identifier
    macro_response = {
    "requestId": event["requestId"],
    "status": "success",
	"fragment": fragment
    }

    return macro_response

