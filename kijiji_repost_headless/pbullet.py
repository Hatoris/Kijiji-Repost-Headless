from typing import List, Dict
from pushbullet import Pushbullet, InvalidKeyError
 
import yaml

def get_pbullet_key(data : Dict):
    """
    If api key in .yml file return it else ruturn false
    """
    api_key = data.get("pbullet_key", False)
    if api_key:
        return api_key.strip()
    return False

def pbullet(
        data : Dict,
        body : List
        ) -> None:
        """
        Send notification via pushbullet
        Parameters
        --------------------
        name : str
            parent folder name from woch file and folder a re remove
        n_remove : int
            Count of files/folders removed
        list_remove : List[str]
            Name list of removed files/folder            
        Return
        -----------
        None           
        """
        pb_api_key = get_pbullet_key(data)
        if pb_api_key:
            corps = create_body(body)
            title = data["postAdForm.title"]
            try:
                pb = Pushbullet(pb_api_key)
                pb.push_note(title, corps)
                print("pushbullet notify with sucess !")           
            except InvalidKeyError:
                print("Your key is not valid")

def create_body(infos : List):
    body = ""
    for info in infos:
        body += f'{info} \n'
    return body
