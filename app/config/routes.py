"""
    Routes Configuration File
"""
from system.core.router import routes


routes['default_controller'] = 'Blanks'
routes['POST']['/place_search'] = 'Blanks#place_search'
