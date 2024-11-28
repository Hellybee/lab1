import firebase_admin
from firebase_admin import credentials, firestore


class DBstorage:
    def __init__(self):  # 파일 생성
        cred = credentials.Certificate(r"json_server\mykey.json")
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.collection_name1 = "students"
        self.collection_name2 = "students_two"
        self.document_id = "XN5Qd5bacL6oRrzaFFpB"
        self.count = 1
        self.document_ref1 = self.db.collection(self.collection_name1)  # 메인 테이블
        self.doc_ref = self.db.collection(
            self.collection_name2
        )  # 보조 테이블 : 현재 산책 대상의 중심좌표 값
        self.name_ = ""

    def user_id(self):  # userid 확인
        for i in self.doc_ref.stream():
            self._id = i.id
            self.cur_data = i.to_dict()

    # # 데이터를 컬렉션에 추가합니다.
    def insert_data(self):  # 물체 중심값 DB에 저장
        self.document_id.add({"center_x": "0.0", "center_y": "0.0"})

    # 데이터 수정
    def update_data(self, x, y):
        id = self.document_id
        #    print(f"document id : {id}")
        x = str(x)
        y = str(y)
        data = {"center_x": x, "center_y": y}
        self.doc_ref.document(id).set(data)

    #   print(f"값 변경 : {x}, {y}")

    def name_set(self, name):  # 현재 강아지 이름
        self.name_ = name

    # 데이터 삭제
    def delete_data(self):
        pass

    # 데이터 확인
    def print_data(self):
        print("test: ")
        test_da = self.db.collection(self.collection_name1)
        for i in test_da.stream():
            print(f"현재 id값 | {i.id}")
            print(i.to_dict())

        print("DB완료")
