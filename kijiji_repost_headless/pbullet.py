from typing import List
from pushbullet import Pushbullet, InvalidKeyError
 
def pbullet(
        pb_api_key : str,
        title : str,
        body : str,
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
        try:
            pb = Pushbullet(pb_api_key)
            pb.push_note(title, body)
            print("pushbullet notify with sucess !")           
        except InvalidKeyError:
             print("Your key is not valid")