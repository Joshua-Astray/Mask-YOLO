import numpy as np
from example.shapes.dataset_shapes import ShapesDataset, ShapesConfig
# import myolo.model as modellib
from myolo import myolo_utils as mutils
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import mrcnn.model as modellib


config = ShapesConfig()
config.display()

# Training dataset
dataset_train = ShapesDataset()
dataset_train.load_shapes(1000, config.IMAGE_SHAPE[0], config.IMAGE_SHAPE[1])
dataset_train.prepare()

# Validation dataset
dataset_val = ShapesDataset()
dataset_val.load_shapes(100, config.IMAGE_SHAPE[0], config.IMAGE_SHAPE[1])
dataset_val.prepare()

image, gt_class_ids, gt_boxes, gt_masks = mutils.load_image_gt(dataset_train, config, image_id=440, augment=None,
                                                               augmentation=None,
                                                               use_mini_mask=config.USE_MINI_MASK)
# config.BATCH_SIZE = 1

model = modellib.MaskYOLO(mode="training",
                          config=config,
                          yolo_pretrain_dir=None,
                          yolo_trainable=True)
model.load_weights('./saved_model_Dec27-14-43.h5')

# model.detect(image, './saved_model_Dec27-14-43.h5')
model.train(dataset_train, dataset_val, learning_rate=config.LEARNING_RATE, epochs=5, layers='all')


# image, gt_class_ids, gt_boxes, gt_masks = mutils.load_image_gt(dataset_train, config, image_id=440, augment=None,
#                                                                augmentation=None,
#                                                                use_mini_mask=config.USE_MINI_MASK)
#
#
# def img_frombytes(data):
#     size = data.shape[::-1]
#     databytes = np.packbits(data, axis=1)
#     return Image.frombytes(mode='1', size=size, data=databytes)
#
#
# fig, ax = plt.subplots(nrows=1, ncols=1)
# print(gt_boxes)
# ax.imshow(image[:, :, ::-1])
# for i in range(0, len(gt_boxes)):
#     ax.add_patch(Rectangle((gt_boxes[i][0], gt_boxes[i][1]), gt_boxes[i][2]-gt_boxes[i][0], gt_boxes[i][3]-gt_boxes[i][1],
#                            facecolor='none', edgecolor='#FF0000', linewidth=3.0))
# plt.show()
#
# print(gt_boxes)
# for i in range(0, len(gt_boxes)):
#     mask_image = img_frombytes(gt_masks[:, :, i])
#     mask_image.show()
#     mask_image.close()


