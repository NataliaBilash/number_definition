from pixellib.instance import instance_segmentation

def object_detection_on_an_image():
    segment_image = instance_segmentation()
    segment_image.load_model("/home/zeroff/Рабочий стол/project_pic/etc/mask_rcnn_coco.h5")

    segment_image.segmentImage(
        image_path="/home/zeroff/Рабочий стол/project_pic/examples/test2.jpg",
        output_image_name="output.jpg"
    )

def main():
    object_detection_on_an_image()

if __name__ == '__main__':
    main()