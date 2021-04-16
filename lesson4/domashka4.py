import sys

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

def parse_folder(path):
    for i in path.iterdir():
        if i.is_dir():
            parse_folder(i)
        if i.is_file():
            filename = i.name
            filename_ = filename.split('.')
            fileformat_ = filename_[-1]
            fileformat = fileformat_.upper()
            if fileformat in PICTURE_FORMATS:
                pictures.append(filename)
                known.add(fileformat_)
            elif fileformat in VIDEO_FORMATS:
                videos.append(filename)
                known.add(fileformat_)
            elif fileformat in DOC_FORMATS:
                documents.append(filename)
                known.add(fileformat_)
            elif fileformat in MUSIC_FORMATS:
                music.append(filename)
                known.add(fileformat_)
            elif fileformat in ARCHIVE_FORMATS:
                archives.append(filename)
                known.add(fileformat_)
            else:
                unknown.add(fileformat_)  
    return pictures, videos, documents, music, archives, known, unknown

a, b, c, d, e, f, g = parse_folder(path_arg)

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
