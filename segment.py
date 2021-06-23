import pixellib
from pixellib.instance import instance_segmentation

segment_image = instance_segmentation()
segment_image.load_model("mask_rcnn_coco.h5")
segment_image.segmentImage("IMG_20180724_151202.jpg", show_bboxes=True, output_image_name="image_new.jpg")
