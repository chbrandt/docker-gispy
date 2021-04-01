import os

from oauthenticator.github import LocalGitHubOAuthenticator

# Use Jupyter-Lab interface
c.Spawner.cmd = ['jupyter-labhub']

if 'GITHUB_CLIENT_ID' in os.environ:
    assert 'GITHUB_CLIENT_SECRET' in os.environ

    c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator
    
    c.LocalGitHubOAuthenticator.create_system_users = True
    
    ## Add the administrator(s) to this list
    c.Authenticator.admin_users = {'user'}
    
    ## Add allowed users to this list if you want to restrict access
    #c.Authenticator.whitelist = {'joao','maria'}
    
    c.LocalGitHubOAuthenticator.client_id = os.environ['GITHUB_CLIENT_ID']
    c.LocalGitHubOAuthenticator.client_secret = os.environ['GITHUB_CLIENT_SECRET']
    c.LocalGitHubOAuthenticator.oauth_callback_url = 'http://localhost:8000/hub/oauth_callback'

