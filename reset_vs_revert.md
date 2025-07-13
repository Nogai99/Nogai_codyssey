# Git: reset vs revert

##  reset 과 revert 의 차이

Git에서 `reset` 과 `revert`는 두 가지 단어 모드의 행동이고, 모든 것은 “이전 새에 작업을 되돌린다”는 곳에서 같은 답을 주지만 해결 방식은 다르며, 결정적인 사용 상황도 다르며, 이로 부터 발생할 수 있는 영향도 큰 명목이다.

---

##  reset 의 특징

- 커미트 기록을 삭제 하거나 가공
- 반드시 규칙을 넘어서 이전 새에 자동으로 되돌리거나 가장 초기 상황으로 복귀
- 규칙:
  - `--soft`: HEAD만 변경 (stage·working 문제없음)
  - `--mixed`: HEAD + stage 변경 (default)
  - `--hard`: HEAD + stage + working directory 모두 되돌린다
- 복사도 없고 기록에서 초과되면 복구 힘들 수 있음

##  revert 의 특징

- 기존 커미트를 되돌린 "새로운 커미트" 만들어서 기록을 보유
- 규칙이 바뀌지 않고, 소스 상황만 되돌리고 다시 커미트
- 발생 사건이 기록으로 남고, 추적이 가능
- 사용차례: 리포티 클린업 또는 회곡적 변경을 수정할 때 가장 안전

---

## revert가 더 안전한 이유

- 회사에서 같이 개발하는 편적에 reset은 포함이 되지 않음.
- 간단히 말하면: reset은 "남은 사례에 영향을 주기 때문에", revert가 "기록은 남게되면서도 변경을 되돌린다"는 점에서 더 안전치로 고려됨.

---

## 매우 즉가한 클래식 블로터를 바탕으로 한 구체 보기

```bash
git reset --hard <commit>
# 가장 강력\uud55c 복귀, 기록 초과

git revert HEAD
# 최규 커미트를 되돌리고, 남은 기록을 유지
```

---

## 출처

[https://www.inflearn.com/community/questions/1505600](https://www.inflearn.com/community/questions/1505600)

