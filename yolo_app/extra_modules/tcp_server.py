import cv2
import numpy
import socket


class TCPServer(object):
    def __init__(self, opt):
        self.opt = opt
        self.tcp_source_reader = None
        self.conn, self.addr = None, None
        self._tcp_host = None
        self._tcp_port = None
        self._is_running = True
        self.frame_id = 0
        self._extract_url_info()
        self._socket = None

    def initialize_camera_source_reader(self):
        print(" *** TCP Source Info; Host={}; Port={}".format(self._tcp_host, self._tcp_port))

        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._socket.bind((self._tcp_host, self._tcp_port))
        self._socket.listen(True)
        self.conn, self.addr = self._socket.accept()

    def kill_server(self):
        self._socket.close()

    def _extract_url_info(self):
        # extract `URL` to collect `host` and `port`
        url_detail = self.opt.source.split(":")
        self._tcp_host = url_detail[0]
        self._tcp_port = int(url_detail[1])

    def recvall(self, sock, count):
        buf = b''
        while count:
            newbuf = sock.recv(count)
            if not newbuf: return None
            buf += newbuf
            count -= len(newbuf)
        return buf

    # def get_tcp_conn(self):
    #     return self.conn

    def get_image(self, frame_id):
        length = self.recvall(self.conn, 16)
        length = length.decode('utf-8')
        stringData = self.recvall(self.conn, int(length))
        # stringData = zlib.decompress(stringData)
        # print('old={} new={}'.format(len(stringData), len(zlib.compress(stringData)) ))
        data = numpy.fromstring(stringData, dtype='uint8')
        decimg = cv2.imdecode(data, 1)

        # Validate input image resolution
        # If the resolution is not Full HD, then, force resizing it into FUll HD (1920 x 1080)
        source_shape = list(decimg.shape)  # [heigh, width]
        if source_shape[0] != self.opt.tcp_img_width and source_shape[1] != self.opt.tcp_img_height:
            decimg = cv2.resize(decimg, (self.opt.tcp_img_width, self.opt.tcp_img_height))

        print(" *** Frame size:{}".format(decimg.shape))

        return True, frame_id, 0.0, decimg
