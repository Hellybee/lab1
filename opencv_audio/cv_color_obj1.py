import cv2
import numpy as np


def find_red_boxes(image):
    # H(360도) -> 0: 적, 60: 황, 120: 녹, 240: 청
    # S(100%) -> 0: 무색, 255: 유색
    # V(100%) -> 0: 암, 255: 명
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # 적색 범위 지정 (OpenCV는 H값을 0~180(H/2)으로 지정함)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([180, 255, 255])
    # 빨간 영역 마스킹(빨간영역=255(흰), 나머지-0(검정))
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    # 두 마스크를 통합
    mask = cv2.bitwise_or(mask1, mask2)
    # 마스크된 이미지에서 윤곽선을 찾음
    # cv2.RETR_EXTERNAL: 최외곽 윤곽선만 찾기
    # cv2.CHAIN_APPROX_SIMPLE: 꼭짓점만 반환
    # cv2.CHAIN_APPROX_NONE: 윤곽선의 모든 점 반환
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # 빨간 네모 상자 및 각도 필터링
    red_boxes = []
    for contour in contours:
        # 윤곽선의 바운딩 박스 계산
        rect = cv2.minAreaRect(contour)  # 리턴값((중앙x, 중앙y), (폭, 높이), 각도)
        box = cv2.boxPoints(rect)
        box = np.int16(box)
        # 바운딩 박스의 각도
        angle = rect[2]
        # 일정 크기 이상인 윤곽선만 인정
        if cv2.contourArea(contour) > 100:
            M = cv2.moments(contour)
            center_x = int(
                M["m10"] / M["m00"]
            )  # 중심 x값이 x축 방향으로 얼마나 떨어져 있나?
            center_y = int(
                M["m01"] / M["m00"]
            )  # 중심 y값이 y축 방향으로 얼마나 떨어져 있나?
            red_boxes.append((center_x, center_y, angle))
        return red_boxes


# 이미지 불러오기
image = cv2.imread(r"k111\img_src\box_r1.png")
# 빨간 네모 상자의 좌표, 각도 찾기
red_box = find_red_boxes(image)
# 좌표, 각도 출력
for box in red_box:
    print("빨간 네모 상자의 좌표:", (box[0], box[1]))
    print("삘간 네모 상자의 각도:", box[2])
