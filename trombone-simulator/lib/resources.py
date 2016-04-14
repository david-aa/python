import os.path
import common


class ResourceNotFound(Exception):
    def __init__(self, msg):
        super(ResourceNotFound, self).__init__(msg)

class FileLocator:
    path = None
    def __init__(self, note_number, file_ext, search_dir):
        _path = os.path.abspath(os.path.join(search_dir, str(note_number) + '.' + file_ext))
        if not os.path.exists(_path):
            raise ResourceNotFound("File " + _path + " not found.")
        else:
            self.path = _path

class Trombone(FileLocator):
    def __init__(self, position):
        FileLocator.__init__(self, 'trombone'+str(position), 'jpg', common.DIR_IMG)

class Score(FileLocator):
    def __init__(self, note_number, flat=True):
        FileLocator.__init__(self, note_number, 'png',
                                   os.path.join(common.DIR_IMG, 'flats' if flat else 'sharps'))
class Sound(FileLocator):
    def __init__(self, note_number, flat=True):
        FileLocator.__init__(self, note_number, 'ogg', common.DIR_AUDIO)
    
