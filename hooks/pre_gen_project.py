"""Set extra vars in cookiecutter jinja context before project generation.

Trick: Abuses docstring to run jinja command inside a comment to update ctx
"""

"""
{{
cookiecutter.update({
    "logo_fzj_url": "https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/FZJ/FZJ.png",
    "logo_hmc_url": "https://github.com/Materials-Data-Science-and-Informatics/Logos/raw/main/HMC/HMC_Logo_M.png",
})
}}
"""
