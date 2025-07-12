## Python 가상환경 구성 과정 (venv)

### 1. 가상환경 생성

```bash
python -m venv venv
```

### 2. 가상환경 활성화

#### Windows

```bash
.\venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 3. 패키지 설치

```bash
pip install flask gTTS
```

### 4. VS Code에서 가상환경 인터플릿 선택

* `Ctrl + Shift + P`
* `Python: Select Interpreter`
* `./venv/Scripts/python.exe` 선택

### 5. 파일 실행

```bash
python app.py
```

### 6. 가상환경 비활성화

```bash
deactivate
```

### 7. Git 가상환경 제안

```
venv/
```
