from ultralytics import YOLO
import cv2
import numpy as np

from db_01 import DBstorage


class MdlTrnnObjcRcgn:
    def __init__(self):
        self.model = YOLO(r"C:\ws\py_proj\dog_toy_pose4.pt")
        self.colors = [
            (255, 0, 0),
            (0, 255, 0),
            (0, 0, 255),
            (255, 255, 0),
            (255, 0, 255),
            (0, 255, 255),
        ]
        self.setdata = DBstorage()
        self.cap = cv2.VideoCapture(
            0
        )  # 비디오 캡처 객체 생성 (0은 웹캠, 파일 경로를 지정하면 비디오 파일 사용)

    #     self.track_history = {}  # 추적 기록을 저장할 딕셔너리

    ## 결과 처리
    # def handlingResults(self):
    #     self.boxes = self.results[0].boxes.xyxy.cpu().numpy().astype(int)
    #     self.track_ids = self.results[0].boxes.id.cpu().numpy().astype(int)
    #     self.classes = self.results[0].boxes.cls.cpu().numpy()

    def crd_mvm_get(self):
        pass

    # 강아지 중심좌표
    def handling_poin(self):
        # x1, y1, x2, y2 = self.box
        center_x = int((self.x1 + self.x2) / 2)
        center_y = int((self.y1 + self.y2) / 2)
        poin_arr = [center_x, center_y]
        self.setdata.update_data(center_x, center_y)
        print(poin_arr)
        return poin_arr

    # 모델 보여주기
    def showModelPrediction(self):
        while True:
            # 프레임 읽기0+------
            ret, self.frame = self.cap.read()
            if not ret:
                break

            # YOLO 모델로 예측
            results = self.model(self.frame)

            # 결과 시각화
            for result in results:
                boxes = result.boxes.cpu().numpy()
                if result.keypoints is not None:
                    keypoints = result.keypoints

                    print("Keypoints shape:", keypoints.shape)
                    print("Keypoints data:")

                    # 바운딩 박스 그리기
                    for box in boxes:
                        self.x1, self.y1, self.x2, self.y2 = map(int, box.xyxy[0])

                        self.handling_poin()
                        cv2.rectangle(
                            self.frame,
                            (self.x1, self.y1),
                            (self.x2, self.y2),
                            (0, 255, 0),
                            2,
                        )

                    # 키포인트 그리기
                    if hasattr(keypoints, "xy") and hasattr(keypoints.xy, "cpu"):
                        kpts = keypoints.xy.cpu().numpy()
                        for i, det_kpts in enumerate(kpts):
                            print(f"  Detection {i}:")
                            for j, kpt in enumerate(det_kpts):
                                x, y = map(int, kpt)
                                print(f"    Keypoint {j}: ({x}, {y})")
                                if x > 0 and y > 0:  # 0,0 좌표는 무시
                                    cv2.circle(
                                        self.frame,
                                        (x, y),
                                        5,
                                        self.colors[j % len(self.colors)],
                                        -1,
                                    )
                                    cv2.putText(
                                        self.frame,
                                        f"{j}",
                                        (x + 5, y + 5),
                                        cv2.FONT_HERSHEY_SIMPLEX,
                                        0.5,
                                        (255, 255, 255),
                                        1,
                                    )

                    # 결과 표시
                    cv2.imshow("Dog Tracking", self.frame)

                    # 'q' 키를 누르면 종료
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        break

    def camera_exit(self):
        # 리소스 해제
        self.cap.release()
        cv2.destroyAllWindows()
