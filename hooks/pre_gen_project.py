"""Set extra vars in cookiecutter jinja context before project generation.

Trick: Abuse docstring to run jinja command inside a comment to update ctx

Alternatives:
* add fields in cookiecutter.json
* add fields in .cookiecutterrc
* using cookiecutter through Python API
"""

"""
{{
cookiecutter.update({})
}}
"""
