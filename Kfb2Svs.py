import os
import sys
import subprocess
from time import time
from glob import glob

def main():
    #Set  your 'src_folder_name' , 'des_folder_name' and 'level'
    src_folder_name = r'E:\\ccRCC_kfb\\'#The folder where the KFB file resides
    des_folder_name = r'E:\\ccRCC_svs\\'       #The folder where SVS files are saved
    level = 9
    # argvs = sys.argv
    # if len(argvs) != 4:
    #     raise AttributeError('Example: convert_kfb2svs.py [src_folder_name] [des_folder_name] [level]')

    exe_path = r'E:\\x86\\KFbioConverter.exe' #The folder where the conversion program is downloaded
    if not os.path.exists(exe_path):
        raise FileNotFoundError('Could not find convert library.')

    # _, src_folder_name, des_folder_name, level = tuple(argvs)

    if int(level) < 2 or int(level) > 9:
        raise AttributeError('NOTE: 2 < [level] <= 9')

    pwd = os.popen('chdir').read().strip()
    full_path = os.path.join(pwd, src_folder_name)
    dest_path = os.path.join(pwd, des_folder_name)
    if not os.path.exists(full_path):
        raise FileNotFoundError(f'could not get into dir {src_folder_name}')
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)

    kfb_list = os.listdir(full_path)
    print(f'Found {len(kfb_list)} slides, transfering to svs format ...')

    for elem in kfb_list:
        st = time()
        kfb_elem_path = os.path.join(full_path, elem)
        svs_dest_path = os.path.join(dest_path, elem.replace('.kfb', '.svs'))
        command = f'{exe_path} {kfb_elem_path} {svs_dest_path} {level}'
        print(f'Processing {elem} ...')
        p = subprocess.Popen(command)
        p.wait()
        print(f'\nFinished {elem}, time: {time() - st}s ...')


if __name__ == "__main__":
    main()
