


def create_subprocess(cmd,check_retcode=True):                                                         
  """Runs a command in a subprocess and checks for any errors.                                         
                                                                                                       
  Creates a subprocess via a call to ``subprocess.Popen`` with the argument ``shell=True``, and 
  pipes stdout and stderr.                                                                                   
                                                                                                       
  :param: str cmd: The command to execute.
  :param: check_retcode: When `True`, then a ``subprocess.SubprocessError`` is raised when 
     the subprocess returns a non-zero return code.  The error message will display the command 
     that was executed along with its actual return code,  as well as any messages that the 
     subprocess sent to STDOUT and STDERR.  When `False`, the ``subprocess.Popen`` instance will 
     be returned instead and it is expected that the caller will call its ``communicate`` method.                                          
  :type check_retcode: bool or None.
  :return: Two-item tuple containing the subprocess's STDOUT and STDERR streams' content if                 
     ``check_retcode=True``, otherwise a ``subprocess.Popen`` instance.                               
  :rtype: tuple.
  :raises subprocess.SubprocessError: There is a non-zero return code and ``check_retcode=True``.          
  """  
