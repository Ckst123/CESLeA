# USER

## 소개
* 이 메뉴얼은 세실리아의 음성 통합 서브시스템 중 화자인식의 사용자 메뉴얼입니다.

## 사전작업
* NVIDIA GPU가 설치 된 Ubuntu 18.04 에서 작동합니다.
* Python 3.x 에서 작동합니다.
* 사전에 화자 등록이 필요합니다.

## 설치
* (선택)virtualenv를 이용하여 python 가상환경을 만듭니다.
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```
* 필요한 패키지를 설치합니다.
```
$ pip install -r requirements.txt
```

## 사용법
* extractor 실행 (무한 루프 도는 채로 둠)
```
$ cd Speaker_Recog_final/online
$ ./run_extractor.sh 
```
* run_spk_recog_nopost.py 실행
```
$ python run_spk_recog_nopost.py
```
* GUI 창의 시작 버튼을 클릭
* 마이크에 임의의 말을 하여 결과 확인

## 문제해결
* 문제가 발생시 프로그램을 종료하고 다시 실행합니다.
