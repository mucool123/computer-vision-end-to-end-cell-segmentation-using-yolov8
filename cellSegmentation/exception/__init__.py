#We can use this code for exception in any project as a template, dont need to change anything

import sys

##why code failed ?, which line not working etc, this kind of information is given by this fucntion
def error_message_detail(error, error_detail: sys):

    """
    Extracts detailed error information including the script name, line number, and error message.
    
    :param error: The exception object caught.
    :param error_detail: The sys module, used to access exception info.
    :return: A formatted string containing the filename, line number, and error message.
    """
    _, _, exc_tb = error_detail.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message



class AppException(Exception):
            """
            Custom exception class for the application, extending Python's Exception class.
            
            This class is initialized with an error message and the sys module for detailed error info.
            It formats a detailed error message including script name, line number, and error description.
            """
    
    
    def __init__(self, error_message, error_detail):
        """
        Initializes the custom exception with a detailed error message.
        
        :param error_message: The error message string.
        :param error_detail: The sys module for accessing detailed exception info.
        """

        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        """
        Override the string representation of the exception to return the detailed error message.
        
        :return: The formatted error message including script name, line number, and error description.
        """

        return self.error_message