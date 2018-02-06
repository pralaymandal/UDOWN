#!/usr/bin/python3
import pytube


class Youtube(pytube):

    def __init__(self, link):
        self.static().yt = pytube.YouTube(link)
        self.streams = self.yt.stream.all()             # Here is a Runtime Error ^ or v

    def get_instance(self):
        return self.streams

    def to_list(self, data):
        """
            This function tackes a object called data which really is a
            stream object
        """
        l = {}
        data = str(data)  # Now data is a String
        data = data.split()  # Now data is a list of String
        for da in data:
            if da == "<Stream:":
                pass
            else:
                d = da.split('=')
                if d[0] == 'mime_type':
                    n = []
                    o = d[1].split('"')[1]
                    o = o.split('/')
                    for each in o:
                        n.append(each)
                    l[d[0]] = n
                else:
                    l[d[0]] = d[1].split('"')[1]
        return l

    def get_mime_type(self, data):
        if isinstance(data):
            if data['mime_type'][0] == "video":
                return "video"
            if data['mime_type'][0] == "audio":
                return "audio"
        else:
            print("Given Data can't be handled.As it is not a Stream list")

    def draw_line(self):
        s = ""
        for n in range(70):
            s += "_"
        return s

    def vcodec_exixts(self, data):
        try:
            if data['vcodec'] != None:
                return True
        except KeyError:
            return False

    def acodec_exists(self, data):
        try:
            if data['acodec'] != None:
                return True
        except KeyError:
            return False

    def get_type(self, data):
        if self.vcodec_exixts(data) == True:
            if self.acodec_exists(data) == True:
                return "av"
            else:
                return "v"
        else:
            if self.acodec_exists(data):
                return "a"

    def on_progress(self, show_progress_bar):
        '''

        :param show_progress_bar:
            stream, chunk, file_handle, bytes_remaining as parameters.
            this is a function which will take
        :return:
            None

        '''
        self.yt.register_on_progress_callback(show_progress_bar)

