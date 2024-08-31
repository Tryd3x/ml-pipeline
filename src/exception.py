import sys
from src.logger import logging

def error_message_detailed(error, error_detailed: sys):
    exc_type,exc_val,exc_traceback = error_detailed.exc_info()

    file_name = exc_traceback.tb_frame.f_code.co_filename
    error_message = f"Error occured in python script name [{file_name}] line number [{exc_traceback.tb_lineno}] error message [{error}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detailed: sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message, error_detailed = error_detailed)

    def __str__(self):
        return self.error_message
    
# if __name__ == "__main__":
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.error("division by zero")
#         raise CustomException(e,sys)