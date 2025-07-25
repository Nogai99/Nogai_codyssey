# Git의 스테이징 영역 추가(git add)와 커밋(git commit)의 차이

## 🔧 Git의 3가지 영역

| 영역 | 설명 |
|------|------|
| **Untracked Area** | Git이 아직 추적하고 있지 않은 파일들이 존재하는 영역 |
| **Tracked Area** | Git이 추적 중인 파일들이 존재하는 영역 |
| **Staging Area** | Commit이 가능한 임시 저장 영역 (파일을 커밋하기 전에 준비하는 곳) |

---

##  Tracked Area 내 3가지 상태

| 상태 | 설명 |
|------|------|
| **Unmodified** | 마지막 커밋 이후 수정되지 않은 상태 |
| **Modified** | 마지막 커밋 이후 수정된 상태 |
| **Staged** | 커밋을 위해 준비된 상태 (스테이징 영역에 올라간 상태) |

>  `git add` 명령어를 통해 Modified 상태의 파일을 Staged 상태로 만든다.

---

##  스테이징 영역 (Staging Area)

- **스테이징 영역**은 커밋 가능한 파일들을 임시로 저장해두는 공간이다.
- `git add` 명령어를 통해 수정된 파일을 이 공간에 올릴 수 있다.
- 일종의 "커밋 대기 박스"라고 생각하면 된다.

### 예시 시나리오

1. 파일을 수정 → `Modified`
2. `git add 파일명` → `Staged`
3. **다시 수정함** → 이 파일은 `Staged` + `Modified` 두 상태를 동시에 가짐
4. `git status` 결과 → 스테이징 영역에도 있고, 수정된 상태로도 표시됨
5. `git commit` → **Staged 상태의 파일만 커밋됨**, 이후 수정한 내용은 커밋되지 않음

### 중요 포인트

- **수정한 후 다시 `git add`를 실행해야 최신 상태가 커밋됨**
- **수정 내용을 폐기하고 싶다면 `git restore 파일명` 사용 가능**
  - 이 경우, `git add`로 올린 이전 상태는 유지되고 **추가 수정분만 폐기**됨

---

##  결론: `git add` vs `git commit`

| 명령어 | 역할 |
|--------|------|
| `git add` | 파일을 스테이징 영역에 추가 (커밋 준비 완료 상태로 만듦) |
| `git commit` | 스테이징 영역에 있는 파일들을 하나의 단위로 기록 (히스토리 저장) |

> 즉, `git add`는 커밋할 파일을 모으는 과정이고, `git commit`은 그것들을 **정식 기록**으로 남기는 행위다.

---

🔗 참고: [IT is True 블로그](https://ittrue.tistory.com/94)
