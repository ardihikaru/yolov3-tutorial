from yolo_app.components.utils.utils import torch2numpy, mbboxlist2dict
from yolo_app.etc.commons.opencv_helpers import crop_image, np_xyxy2xywh, save_txt
import cv2
from datetime import datetime
import os


class YOLOFunctions:
    def __init__(self, opt):
        self.opt = opt
        self.__create_output_path()

    def __create_output_path(self):
        new_folder_name = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
        self.raw_img_path = self.opt.output + "images_txt/" + new_folder_name + "/raw/"
        self.bbox_img_path = self.opt.output + "images_txt/" + new_folder_name + "/bbox/"
        self.crop_img_path = self.opt.output + "images_txt/" + new_folder_name + "/crop/"
        self.txt_bbox_path = self.opt.output + "images_txt/" + new_folder_name + "/txt/"

        # Make directories of out it
        os.makedirs(self.raw_img_path)
        os.makedirs(self.bbox_img_path)
        os.makedirs(self.crop_img_path)
        os.makedirs(self.txt_bbox_path)

    def _save_cropped_img(self, xyxy, im0, idx, cls, frame_id, ext):
        if self.opt.dump_crop_img:
            numpy_xyxy = torch2numpy(xyxy, int)
            xywh = np_xyxy2xywh(numpy_xyxy)
            crop_save_path = self.crop_img_path + "frame-%s_[cls=%s][idx=%s]%s" % (str(frame_id), str(idx), cls, ext)
            crop_image(crop_save_path, im0, xywh)

    def _save_results(self, im0, vid_cap, frame_id, is_raw=False):
        if is_raw:
            frame_save_path = self.raw_img_path + "frame-%s.jpg" % str(frame_id)
            if self.opt.dump_raw_img:
                cv2.imwrite(frame_save_path, im0)
        else:
            frame_save_path = self.bbox_img_path + "frame-%s.jpg" % str(frame_id)
            if self.opt.dump_bbox_img:
                cv2.imwrite(frame_save_path, im0)
            else:
                if self.vid_path != self.opt.source:  # new video
                    self.vid_path = self.opt.source
                    if isinstance(self.vid_writer, cv2.VideoWriter):
                        self.vid_writer.release()  # release previous video writer

                    fps = vid_cap.get(cv2.CAP_PROP_FPS)
                    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                    self.vid_writer = cv2.VideoWriter(self.save_path,
                                                      cv2.VideoWriter_fourcc(*self.opt.fourcc), fps, (w, h))
                self.vid_writer.write(im0)

    def _safety_store_txt(self, xyxy, frame_id, cls, conf_score):
        txt_save_path = self.txt_bbox_path + "frame-%s" % str(frame_id)
        if self.opt.save_txt:
            save_txt(txt_save_path, self.opt.txt_format, bbox_xyxy=xyxy, cls=cls, conf=conf_score)
