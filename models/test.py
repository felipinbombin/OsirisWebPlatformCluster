
import time


def Test(input_dict):
    """ method to test ssh connection """

    seconds = input_dict["seconds"]

    time.sleep(seconds)
  
    return {
        "seconds": seconds,
        "status": "ok"
    }
