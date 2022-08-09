# web_cpu

## 처음 시작
1. python, xampp, sqlyog 설치
2. 자신이 좋아하는 ide 설치
3. 파일 zip으로 다운로드후 압축 해제 -> ide로 열기
4. ide, cmd - src/initial/py.py 맨위 세 문장 cmd에 각각 입력
5. xampp - xampp 실행 후 mysql config 누른 후 my.ini 열기
6. my.ini - ctrl - F 누른 후 port찾아 그 옆에 3306을 모두 3307로 변환
7. my.ini - 44번째 라인에 lower_case_table_names = 2 붙여넣기
8. xampp - mysql start 버튼 누르기
9. sqlyog 실행
10. sqlyog - 파일 -> 새연결 -> 새연결 -> 이름에 root -> 포트만 3307로 바꾼후 연결
11. db/src.db의 맨위 3문장 실행
12. sqlyog - 파일 -> 새연결 -> 새연결 -> 이름에 pyCPUid -> 포트 3307 변경 -> 사용자 이름 pyCPUid 입력 -> 비밀번호 pyCPUpw1234 입력 -> 연결
13. db/src.db의 남은 문장 복붙
14. cmd 혹은 터미널에 cd src/python/server 입력
15. cmd 혹은 터미널에 python -m uvicorn index:app --reload 입력
16. [http://127.0.0.1:8000](http://127.0.0.1:8000/) 접속하여 {"main" : "main"} 나오는지 확인 - 안나오면 연락
17. [http://127.0.0.1:8000/api/sample?sample=sample1](http://127.0.0.1:8000/api/sample?sample=sample1) 접속하여 {"resultCode":"S-1","msg":"샘플 출력","dataName":"sample","data":{"test2":"welcome text1"}} 나오는지 확인 - 안나오면 연락
18. [http://127.0.0.1:8000/html/test](http://127.0.0.1:8000/html/test) 접속하여 welcome 나온느지 확인 - 안나오면 연락


## 서버 개발
 - python 공부
 - [https://www.youtube.com/watch?v=5A67mQ2Pt9s](https://www.youtube.com/watch?v=5A67mQ2Pt9s) 보고 fastapi 공부
 - 짜여진 코드 읽고 이해 안되는 부분 질문

## 클라이언트 개발
 - html, css, js 공부
 - react 공부
 - css, js 파일은 src/templates/static에 넣고 css, js 불러오는 부분 "{{ url_for('static' ,path="파일이름") }}"으로 바꾸기
 - 직접 페이지 구축후 html 파일은 src/templates/htmls에 붙여넣기 -> 'http://127.0.0.1:8000/html/ + 자신의 파일 이름' 사이트 접속
 

## api 출력 형식
 - resultCode: str  (성공 여부, 실패 시 어떤 실패 - client에 사용 X)
 - msg: str         (추가적인 메세지 - client에 사용 X)
 - dataName: str    (받은 데이터 이름 - client에 사용 X)
 - data: object     (데이터 - client 사용)

## 내가 더 만들어야 하는것
 - client: pop up, api 통신 func
 - server : 

## 더있으면 좋겠는건 연락