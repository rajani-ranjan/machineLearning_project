
import sys
from src.logger import logging

def error_message_detail(errer, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    errer_message = "Error occure in in python script [{0}], line number [{1}], error message [{2}]".format(file_name, exc_tb.tb_lineno, str(errer))
    return errer_message


class CustomException (Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.errer_message = error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.errer_message
    
