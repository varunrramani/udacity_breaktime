import os
def rename_files():
    file_list = os.listdir(r"C:\Users\Varun Ramani\PythonProjects\Udacity\TakeABreak\prank")
    print (file_list)
    os.chdir(r"C:\Users\Varun Ramani\PythonProjects\Udacity\TakeABreak\prank")
    for file_name in file_list:
        os.rename(file_name, file_name.lstrip("0123456789"))

rename_files()
