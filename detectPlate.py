import torch
from torchvision import models
from matplotlib import pyplot as plt
from torchvision.utils import draw_bounding_boxes
from torchvision.io import read_image
import ssl
from PIL import Image

def detectPlate(image):
    ssl._create_default_https_context = ssl._create_unverified_context

    classes = ['Plates', 'license-plate', 'vehicle']
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = models.detection.fasterrcnn_mobilenet_v3_large_fpn(weights=models.detection.FasterRCNN_MobileNet_V3_Large_FPN_Weights.COCO_V1)
    in_features = model.roi_heads.box_predictor.cls_score.in_features
    model.roi_heads.box_predictor = models.detection.faster_rcnn.FastRCNNPredictor(in_features, len(classes))
    model.load_state_dict(torch.load('detection.pth', map_location=device))
    model.eval()

    img = read_image(image).div(255)

    with torch.no_grad():
        prediction = model([img.to(device)])
        pred = prediction[0]

    img_int = torch.tensor(img*255, dtype=torch.uint8)
    fig = plt.figure(figsize=(14, 10))
    result_image = draw_bounding_boxes(img_int,
        pred['boxes'][pred['scores'] > 0.8],
        [classes[i] for i in pred['labels'][pred['scores'] > 0.8].tolist()], width=4
    ).permute(1, 2, 0)

    result_np_array = result_image.numpy()
    result_pil_image = Image.fromarray(result_np_array)
    result_pil_image.save('tensorImg.jpg')

    plt.imshow(result_image)

    labels = pred['labels']
    labels = [t.item() for t in labels]
    platePos = []
    for i in range(0, len(labels)):
        if labels[i] == 1:
            platePos.append(i)
    boxes = pred['boxes']
    boxes = [t.numpy() for t in boxes]

    for i in platePos:
        top_left = (int(boxes[i][0]), int(boxes[i][1]))
        bottom_right = (int(boxes[i][2]), int(boxes[i][3]))
    # plt.show()
    return  top_left, bottom_right
