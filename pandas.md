## numpy, pandas 설치
> pip install pandas numpy
> conda install pandas numpy

## - 윈도우에서 명령어의 경로 확인 방법
> where python

## - 도커 기본 사용법
http://pyrasis.com/Docker/Docker-HOWTO

## 1. 도커 허브에 있는 이미지로 컨테이너 런 (최초 실행시)
```
docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v /C/Users/admin/Documents/eda:/home/vscode/notebooks/eda mrsono0/base_project:eda
```
## 1.1 권한 확인
(주피터 노트북 콘솔 아이콘 클릭)
```
> sudo -i (루투 계정 전환)
> cd /home/vscode (vscode 계정 홈 디렉토리 이동)
> ls -al (디렉토리 목록 확인 notebooks)
> chown -R vscode:vscode ./notebooks (계정 오너 조정)
> ls -al (디렉토리 오너가  vscode로 바뀐 것 확인)
```
## 2. 컨테이너 접속 정보 확인
```
docker logs --tail 30 컨테이너이름
```
## 2.2 작업 진행 중 수시로
```
docker commit eda 나의도커아이디/eda
```

## 3. 내가 commit 한 이미지로 컨테이너 런 실행
```
docker run --rm --name eda -itd -u vscode -p 8888:8888 -p 8088:8088 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes -v /c/Users/user/PNU_201912/eda:/home/vscode/notebooks/eda 나의도커아이디/eda
```

## 4. 내가 commit한 이미지를 나의 도커 허브에 push 할때
```
docker push 나의도커아이디/eda
```

## 도커 컨테이너, 이미지 정리 하기
1. 도커 컨테이너 확인
```
docker ps -a
```

2. 사용않하는 컨테이너 커밋
```
docker commit 컨테이너이름 도커아이디/이미지이름
```

3. 도커이미지 허브 사이트에 업로드
```
docker push 도커아이디/이미지이름
```

4. 사용 않하는 컨테이너 삭제
```
docker rm 컨테이너아이디
```

5. 사용 않하는 이미지 삭제
```
docker rmi 이미지아이디
```

	- 처음 선생님 컨테이너 실행
docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes mrsono0/base_project:eda

	- 이후 내꺼 컨테이너 실행
docker run --rm --name eda -itd -u vscode -p 8888-8889:8888-8889 -p 6006-6015:6006-6015 -e JUPYTER_RUN=yes euskate/eda