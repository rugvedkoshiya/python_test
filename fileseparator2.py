import os, shutil

# NOTE: You can write every single extensions inside tuples 
dict_extensions = {
    'Audio_extensions' : ('.mp3', '.m4a', '.wav', '.flac', '.html', '.aa', '.aac', '.aax', '.act', '.aiff', 'amr', '.ape', '.au', '.awb', '.dct', '.dss', '.flac', '.gsm', '.mpc', '.ogg', '.oga', '.mogg', '.raw', '.voc', '.wma', '.8svx'),
    'Video_extensions' : ('.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.mp4', '.gifv', '.mng', '.avi', '.MTS','.M2TS', '.TS', '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.amv', '.m4p', '.m4v', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mpg', '.m2v', '.svi', '.3gp', '.3g2', '.mxf', '.rpq', '.nsv', '.flv', '.f4v', '.f4p', '.f4a', '.f4b'),
    'Document_extensions' : ('.doc', '.pdf', '.txt', '.dot', '.dot', '.docm', '.dotx', '.dotm', '.docb', '.xlsb', '.xla', '.xlam', '.xll', '.xlw', '.ppt', '.pot', '.pps', '.pptx', '.pptm', '.potx', '.potm', '.ppam', '.ppsx', '.ppsm', '.sldx', '.sldm', '.pub', '.xps'),
    'Photo_extensions' : ('.jpg', '.png', '.txt', '.JPEG', '.JFIF', '.Exif', '.TIFF', '.GIF', '.BMP', '.PPM', '.PGM', '.PBM','.PNM', '.SVG'),
}


folderpath = input('Enter Folder Path : ')

def file_finder(folder_path, file_extensions):
    # files = []
    # for file in os.listdir(folder_path):
    #     for extension in file_extensions:
    #         if file.endswith(extension):
    #             files.append(file)
    # return files
    return [file for file in os.listdir(folder_path) for extension in file_extensions if file.endswith(extension)]

# print(file_finder(folderpath, video_extensions))
for extension_type, extension_tuple in dict_extensions.items():
    folder_name = extension_type.split('_')[0] + " " 'Files'
    folder_path = os.path.join(folderpath, folder_name)
    os.mkdir(folder_path)
    for item in file_finder(folderpath, extension_tuple):
        item_path = os.path.join(folderpath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_path,item_new_path)
    # print('calling file finder')
    # print(file_finder(folderpath, extension_tuple))