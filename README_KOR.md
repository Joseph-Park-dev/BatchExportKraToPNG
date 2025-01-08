# Batch save folder to png

폴더 안에 있는 모든 크리타(Krita, .kra) 파일을 한번에 PNG 파일로 저장해주는 플러그인 입니다!

## 설치 방법 (한국어 기준)

### 다운로드 방법
* 우측 상단 녹색 "코드" 버튼 클릭 & .zip 파일 다운로드

### 플러그인 설치 방법
* 설정(N) > 리소스 관리 > 리소스 폴더 열기
* "pykrita" 폴더 안에 "BatchSaveFolderPNG.desktop" 파일을 추가해주세요.
* "pykrita" 폴더 안에 (같은 위치에) "BatchSaveFolderPNG" 폴더를 추가해주세요.
* Krita를 재시작 해주세요.
* 설정(N) > Krita 설정 > Python 플러그인 관리자 > 리스트에서 "Batch Save Folder to .png" 체크하여 활성화 해주세요.

## 사용방법

* 도구(T) > 스크립트 > 리스트에서 플러그인 선택.
* "Source Folder" 버튼을 클릭하여 크리타(Krita) 파일들이 있는 폴더를 선택해주세요.
* "Destination Folder" 버튼을 클릭하여 PNG 파일들을 저장할 위치를 선택해주세요.
* 하단의 PNG 관련 설정을 세팅해주세요.
* Start Batch Save 버튼을 클릭 해주세요. 저장이 시작됩니다.

## Plugin's life
### 2024.03.07
Basic plugin with src_folder, dest_folder path button was made & uploaded to Krita forum, gitHub.

### 2024.03.19
Improved plugin with better UI, enabling modification of .png export parameters.