import sys
import os
import shutil
from pathlib import Path


path_arg = Path(sys.argv[-1])

pictures = []
videos = []
documents = []
music = []
archives = []
others = []
known = set()
unknown = set()



PICTURE_FORMATS = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO_FORMATS = ('AVI', 'MP4', 'MOV', 'MKV')
DOC_FORMATS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC_FORMATS = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVE_FORMATS = ('ZIP', 'GZ', 'TAR')

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюіяєїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "i", "ja", "je", "ji", "g")


TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()   
    


def normalize(phrase):
    trans_phrase = phrase.translate(TRANS)
    for i in trans_phrase:
        if not i.isalpha() and not i.isdigit():
            trans_phrase = trans_phrase.replace(i, '_')
    return trans_phrase


def parse_folder(path):
    for i in path.iterdir():
        
        if i.is_dir():
            parse_folder(i)
                     
        if i.is_file():
            
            filename = i.name
            filename_ = filename.split('.')
            fileformat_ = filename_[-1]
            fileformat = fileformat_.upper()

            name_norm_pref = ''.join(filename_[:-1])
            name_norm_pref = normalize(name_norm_pref)
            name_norm = name_norm_pref + '.' + fileformat_
            
            if fileformat in PICTURE_FORMATS:
                pictures.append(filename)
                known.add(fileformat_)
                new_dir = r'D:\\Python\\images\\' + name_norm
                shutil.move(i, new_dir)
            elif fileformat in VIDEO_FORMATS:
                videos.append(filename)
                known.add(fileformat_)
                new_dir = r'D:\\Python\\video\\' + name_norm
                shutil.move(i, new_dir)
            elif fileformat in DOC_FORMATS:
                documents.append(filename)
                known.add(fileformat_)
                new_dir = r'D:\\Python\\documents\\' + name_norm
                shutil.move(i, new_dir)
            elif fileformat in MUSIC_FORMATS:
                music.append(filename)
                known.add(fileformat_)
                new_dir = r'D:\\Python\\audio\\' + name_norm
                shutil.move(i, new_dir)
            elif fileformat in ARCHIVE_FORMATS:
                archives.append(filename)
                known.add(fileformat_)
                new_name = r'D:\\Python\\archives\\' + name_norm
                new_dir = r'D:\\Python\\archives\\' + name_norm_pref
                shutil.unpack_archive(i, new_dir)
                
                os.rename(i, new_name)
            else:
                unknown.add(fileformat_)

    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        if not dirnames and not filenames:
            os.rmdir(dirpath)
            
    return pictures, videos, documents, music, archives, known, unknown

a, b, c, d, e, f, g = parse_folder(path_arg)

#python sort.py D:\Python\Test_folder1

if len(a) > 0:
    print(f'СПИСОК ФОТО: {a}\n')
if len(b) > 0:
    print(f'СПИСОК ВИДЕО: {b}\n')
if len(c) > 0:
    print(f'СПИСОК ДОКУМЕНТОВ: {c}\n')
if len(d) > 0:
    print(f'СПИСОК МУЗЫКИ: {d}\n')
if len(e) > 0:
    print(f'СПИСОК АРХИВОВ: {e}\n')
print(f'ВСЕ ИЗВЕСТНЫЕ РАСШИРЕНИЯ ФАЙЛОВ {f}\n')
print(f'ВСЕ НЕИЗВЕСТНЫЕ РАСШИРЕНИЯ ФАЙЛОВ {g}')
