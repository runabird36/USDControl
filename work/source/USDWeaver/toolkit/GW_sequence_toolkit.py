# -*- coding:utf-8 -*-

import os
import re
from glob import glob
from GW_path_module import (seq_exts)
re_ex_glob = re.compile(r'[\.\_][0-9]{2,4}\.\w+$')


def is_glob(full_path):
    fname, _ext = os.path.splitext(full_path)
    if _ext not in seq_exts:
        return False
    _res = re_ex_glob.search(full_path)
    if _res:
        return True
    else:
        return False


def is_sharp_path(_path):
    re_ex_sharp = re.compile(r'#+')
    _res = re_ex_sharp.search(_path)
    if _res:
        return True
    else:
        return False


def get_glob_path(full_path):
    _glob_name = re_ex_glob.search(full_path).group()
    _ext = _glob_name.split('.')[-1]
    if _glob_name.startswith('.'):
        _glob_part = _glob_name.split('.')[1]
        _sharp_count = len(_glob_part)
        to_name = '{0}.{1}'.format('.'+'#'*_sharp_count, _ext)
    elif _glob_name.startswith('_'):
        _glob_part = _glob_name.split('.')[0]
        _glob_part = _glob_part.split('_')[1]
        _sharp_count = len(_glob_part)
        to_name = '{0}.{1}'.format('_'+'#'*_sharp_count, _ext)
    return re_ex_glob.sub(to_name, full_path)


def check_seq_filename(all_assetname_list, _pub_list):
    _res = True
    _error_list = []
    for _pub_filepath in _pub_list:
        for _sg_assetname in all_assetname_list:
            if _sg_assetname in _pub_filepath:
                continue
            else:
                _error_list.append(_pub_filepath)
    if _error_list != []:
        _res = False
    return _res, _error_list


def get_seq_file_list_from_glob(glob_path):
    re_ex_sharp = re.compile(r'#+')
    re_ex_star = re.compile(r'\*\.[a-zA-Z]+')
    _res = re_ex_sharp.search(glob_path)
    if _res:
        sharp_str = _res.group()
        star_path = glob_path.replace(sharp_str, "*")
        return glob(star_path)
    elif re_ex_star.search(glob_path):
        return glob(glob_path)
    else:
        return []





def get_total_frame(media_path):
    # ffprobe = "Z:/Standard/Python/batch/ffmpeg/bin/ffprobe.exe"
    ffprobe = GP_path_module._ffprove_path
    wm_process_get_frame = subprocess.Popen([ffprobe, '-v', 'error', '-count_frames', '-select_streams', 'v:0', '-show_entries', 'stream=nb_read_frames', media_path],stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=False)
    total_frame1 = wm_process_get_frame.communicate()
    print(total_frame1)
    temp = str(total_frame1[0]).replace('b\'[STREAM]\\nnb_read_frames=',' ')
    print(temp)
    temp = temp.replace('\\n[/STREAM]\\n\'', ' ')
    # temp = temp.replace('\'', '')
    if ' Unsupported codec with id 0 for input stream 2\r\n' in temp:
        the_num_frames_str = temp.replace(' Unsupported codec with id 0 for input stream 2\r\n', '')
    elif ' Unsupported codec with id 0 for input stream 1\r\n' in temp:
        the_num_frames_str = temp.replace(' Unsupported codec with id 0 for input stream 1\r\n', '')
    else:
        the_num_frames_str = temp


    # This is for '78 [mov,mp4,m4a,3gp,3g2,mj2 @ 0000014784c90400] Referenced QT chapter track not found\r\n'
    the_num_frames_str = the_num_frames_str.replace(' ', '')
    re_ex_num = re.compile(r'^\d+')
    _search_res = re_ex_num.search(the_num_frames_str)
    if _search_res:
        
        the_num_frames_str = _search_res.group()
    

    #
    try:
        the_num_frames = int(the_num_frames_str)-1
    except Exception as e:
        print(str(e))
        return None


    return str(the_num_frames)


def con2glob_path(origin_fullpath):
    seq_finder_more_than_four = re.compile(r'\.\d{5,}\.')

    seq_finder_dot_once = re.compile('\d\d\d\d\.')
    seq_finder_dot_twice = re.compile('\.\d\d\d\d\.')

    seq_finder_underbar = re.compile('\_\d\d\d\d\.')
    seq_finder_underbar_dot = re.compile(r'\_\.\d\d\d\d\.')

    if seq_finder_more_than_four.search(origin_fullpath):
        _res = seq_finder_more_than_four.search(origin_fullpath)
        _seq_num_with_dot = _res.group()
        _seq_num = _seq_num_with_dot.replace('.', '')
        _seq_num_count = len(_seq_num)
        reg = seq_finder_more_than_four.sub('.*.', origin_fullpath)
        percentage_path = seq_finder_more_than_four.sub('.%0{0}d.'.format(str(_seq_num_count)), origin_fullpath)

    elif '<UDIM>' in origin_fullpath:
        reg = origin_fullpath.replace('<UDIM>', '*')
    elif '<udim>' in origin_fullpath:
        reg = origin_fullpath.replace('<udim>', '*')
    elif '####' in origin_fullpath:
        reg = origin_fullpath.replace('####', '*')
    elif seq_finder_dot_once.search(origin_fullpath):
        reg = seq_finder_dot_once.sub('*.', origin_fullpath)
        percentage_path = seq_finder_dot_once.sub('%04d.', origin_fullpath)
    elif seq_finder_dot_twice.search(origin_fullpath):
        reg = seq_finder_dot_twice.sub('.*.', origin_fullpath)
        percentage_path = seq_finder_dot_twice.sub('.%04d.', origin_fullpath)
    elif seq_finder_underbar.search(origin_fullpath):
        reg = seq_finder_underbar.sub('_*.', origin_fullpath)
        percentage_path = seq_finder_underbar.sub('_%04d.', origin_fullpath)
    elif seq_finder_underbar_dot.search(origin_fullpath):
        reg = seq_finder_underbar_dot.sub('_.*.', origin_fullpath)
        percentage_path = seq_finder_underbar_dot.sub('_.%04d.', origin_fullpath)

    return reg, percentage_path



def get_start_end_framenum_from_path(star_glob_path: str):
    if "*" not in star_glob_path:
        return "", ""

    re_ex_fnum = '\d{1,4}\.[a-zA-Z]+'

    file_list = glob(star_glob_path)
    file_list.sort()
    
    start_frame_fname = os.path.basename(file_list[0])
    end_frame_fname   = os.path.basename(file_list[-1])

    sframe = re.search(re_ex_fnum, start_frame_fname).group()
    eframe = re.search(re_ex_fnum, end_frame_fname).group()

    sframe = sframe.split(".")[0]
    eframe = eframe.split(".")[0]

    return sframe, eframe
