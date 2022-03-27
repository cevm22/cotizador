import logging
import sqlite3
import os
import sys
import asana
import json
import requests

token= 'TOKEN ASANA'#token asana

def asana_task(titulo,notas):
    # replace with your personal access token. 
    personal_access_token = token
    title=titulo#"nombre del task"# titulo del task
    followers=['tokens, per, user'] #seguidores
    assignee=['user'] #responsable
    notes=notas #"agregando notas al task"
    # Construct an Asana client
    client = asana.Client.access_token(personal_access_token)
    postear= {"notes":notes,"name":title,"assignee":assignee,
              "projects":['PROJECT ID'], "followers":followers}
    # posting the Task in a Workspace
    proyecto= client.tasks.create_in_workspace("worksapace ID",postear) # workspace
    #print(proyecto)
    return("publicado en ASANA")







