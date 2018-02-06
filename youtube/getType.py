#!/usr/bin/python3

# import toList
import pytube


def getMimeType(data):
    if type(data)==type({}):
        if data['mime_type'][0]=="video":
            return "video"
        if data['mime_type'][0]=="audio":
            return "audio"
    else:
        print("Given Data can't be handled.As it is not a Stream list")


def vcodec_exixts(data):
    try:
        if data['vcodec']!=None:
            return True
    except KeyError:
        return False


def acodec_exists(data):
    try:
        if data['acodec'] != None:
            return True
    except KeyError:
        return False


def to_list(data):
    '''
    This function tackes a object called data which really is a
    stream object
    '''
    l={}
    data = str(data)	# Now data is a String
    data =data.split()	# Now data is a list of String
    for da in data:
        if da == "<Stream:":
            pass
        else:
            d=da.split('=')
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


def get_type():
    if vcodec_exixts(data) == True:
        if acodec_exists(data) == True:
            print("Type: video with audio")
        else:
            print("Type: video without audio")
    else:
        if acodec_exists(data):
            print("Type: only Audio")


def draw_line():
    s = ""
    for n in range(70):
        s += "_"
    return s


link = input("Enter the Link: ")
yt = pytube.YouTube(link)
streams = yt.streams.all()

for stream in streams:
    print(draw_line()+"\n")
    data = to_list(stream)
    print("vcodec: " + str(vcodec_exixts(data)) + ", acodec: " + str(acodec_exists(data)))
    print(draw_line())
