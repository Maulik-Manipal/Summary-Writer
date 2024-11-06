import os
import sys
import logging

logging_str =  "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" ###custom log first it will save the timestamp and 
#then it will give the level name and then which module are you running and then the message

log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.mkdir(log_dir, exist_ok=True)
#directory name is logs then it will create a file named running_logs.log


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout) #the logging part will also be shwon in terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger") #logger named "textSummarizerLogger" for logging.    