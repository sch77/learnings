import urllib2

def read_text(full_file_name):
    """reads text from give file name
    Parameters:
    ------------------
    file_name : string
                full path of the file

    Returns:
    -------------------
    string 
          cntent of the file being read
    """
    input_file = open(full_file_name)
    contents = input_file.readlines()
    input_file.close()
    return contents

def check_for_profanity(cur_string):
    """ Given a string checks for objectionable content in the string
    Parameters:
    ------------------
    cur_string : string
                string to look for obejctionable content

    Returns:
    ---------------------
    boolean
            True/False depending on the objectionable content found
    """    
    service_url = get_profanity_checker_url()
    full_url = service_url + "?q="+cur_string
    # print(full_url)
    connection = urllib2.urlopen(full_url)
    is_profane = connection.read()
    connection.close()
    if is_profane == "true":
        return True
    else:
        return False
    
def get_profanity_checker_url():
        """get the service url for profanity checking
    Parameters:
    ------------------

    Returns:
    -------------------
    string 
          service url
    """
        return "http://www.wdylike.appspot.com"

def check_for_profanity_in_line(curline):
    """ Given a line checks for objectionable content in the line
    Parameters:
    ------------------
    cur_string : string
                string to look for obejctionable content

    Returns:
    ---------------------
    boolean
            True/False depending on the objectionable content found
    """       
    words = curline.split()
    for curword in words:
       # print("word is : "+ curword)
        if check_for_profanity(curword):
            return True
    return False


file_contents = read_text(r"D:\scharati\myProjects\github\learnings\udacity-fullstack-web\profanity_contents")

for line in file_contents :
    if check_for_profanity_in_line(line):
        print(line + ": has objectionable content ")

