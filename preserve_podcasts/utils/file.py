import hashlib
import os
import subprocess


def sha1file(file_path: str):
    with open(file_path, 'rb') as f:
        sha1 = hashlib.sha1()
        while True:
            data = f.read(1024)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def md5file(file_path: str):
    with open(file_path, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(1024)
            if not data:
                break
            md5.update(data)
    return md5.hexdigest()


def is_playable(file_path: str):
    if audio_duration(file_path) > 0:
        return True
    
    return False
    
    
def audio_duration(file_path: str):
    ''' Return audio duration in seconds, -1 if failed'''
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File not found: {file_path}')

    try:
        t = subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path], stderr=subprocess.STDOUT)
        duration = int(t.decode('utf-8').strip("\n").split('.')[0])
        return duration
    except:
        return -1 # failed