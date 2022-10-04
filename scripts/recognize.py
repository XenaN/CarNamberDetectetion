from pathlib import Path
from typing import List

import cv2
import numpy as np
from PIL import Image
import pytesseract
import torch

from misc.types import PathLike


def model_predict(image: PathLike) -> List:
    """
    Detect plate number from car image

    Args:
        image: path to image

    Returns:
        Prediction of plate box

    """

    model = torch.hub.load(
        str(Path(__file__).parent.parent / "yolov7"),
        "custom",
        path_or_model=str(
            Path(__file__).parent.parent / "yolov7" / "best.pt"
        ),
        force_reload=True,
        source="local",
    )

    _ = model.eval()

    img = Image.open(image)
    result = model(np.array(img))

    res = result.pred[0].detach()

    return res


def find_plate_bounds(prediction: List) -> List:
    """
    Detect plate number from car image

    Args:
        prediction: prediction of plate box

    Returns:
        List of box coordinates

    """
    final_res = []
    for number in prediction:
        x1, y1, x2, y2, proba, _ = number.cpu().numpy()
        if proba > 0.6:
            final_res.append([x1, y1, x2, y2])

    return final_res


def save_cropp_image(
    image: PathLike,
    num_plate: List,
    count: int,
    output_path: PathLike,
) -> PathLike:
    """
    Save cropped plate from image

    Args:
        image: path to image
        num_plate: list of box edges
        count: number of plate
        output_path: path to plate

    Returns:
        List of box coordinates

    """
    img = Image.open(image)
    plate_img = img.crop(num_plate)
    img_array = np.array(plate_img).astype(np.uint8)

    # Make image gray
    gray = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
    gray_image = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(gray_image, 30, 200)

    # Find contours for all letters
    cnts, new = cv2.findContours(
        edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
    )

    # Sorting the identified contours
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]

    # Finding the contour with four sides
    i = 7
    for c in cnts:
        # Cropping the rectangular part identified as license plate
        x, y, w, h = cv2.boundingRect(c)
        new_img = img_array[y : y + h, x : x + w]

        save_path = str(output_path / f"{i}_{count}.png")
        cv2.imwrite(save_path, new_img)
        i += 1
        break

    return save_path


def recognize_letters(image: PathLike, output_path: PathLike):
    """
    Recognize text from plates

    Args:
        image: path to image
        output_path: path to plate

    """

    output_path = Path(output_path).resolve()

    prediction = model_predict(image)
    final_result = find_plate_bounds(prediction)

    count = 0
    for num_plate in final_result:
        count += 1
        save_path = save_cropp_image(
            image, num_plate, count, output_path
        )

        custom_config = r"-c tessedit_char_whitelist=0123456789ABEKMHOPCTYX --oem 3 --psm 6"

        plate = pytesseract.image_to_string(
            save_path, config=custom_config
        )

        print("Number plate is:", plate)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
