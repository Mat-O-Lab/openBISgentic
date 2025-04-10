

from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import ErrorData, INTERNAL_ERROR, INVALID_PARAMS
import json
import os

import pybis

openbis_url='https://bam-openbis02.germanywestcentral.cloudapp.azure.com/'

o = pybis.Openbis(openbis_url, verify_certificates=False)
o.set_token(os.environ['OPENBIS_TOKEN'])
if not o.is_session_active():
    raise RuntimeError('openBIS not active')

mcp = FastMCP('openBISgentic')

@mcp.tool()
def get_instruments() -> str:
    """
    Fetch name and permID for all lab instruments, devices, machines, and testing equipment that are registered in the
    INSTRUMENTS space of this openBIS instance. Convert it to json formatted list with the name and the permID of the instruments.

    Usage:
       get_instruments()
    """
    #return ', '.join([m.props['$name'] for m in o.get_objects(space='INSTRUMENTS')])
    return json.dumps([{'name': m.props['$name'], 'permId': m.permId} for m in o.get_objects(space='INSTRUMENTS')])

@mcp.tool()
def get_instruments_details(permId: str) -> str:
    """
    Fetch details about an instrument, device, machine, and testing equipment with the specified permID registered in the
    INSTRUMENTS space of this openBIS instance. Returns a json formatted dict containing details of the instruments.

    Usage:
       get_instruments_details('20250410120644753-80')
    """
    return json.dumps(o.get_object(permId).props.all())

