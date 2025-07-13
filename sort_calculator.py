class MergeSorter:
    def sort(self, arr):
        # base case: 1개 이하 원소는 이미 정렬된 상태
        if len(arr) <= 1:
            return arr

        # divide: 배열을 절반으로 나누기
        mid = len(arr) // 2
        left = self.sort(arr[:mid])    # 왼쪽 절반 재귀 정렬
        right = self.sort(arr[mid:])   # 오른쪽 절반 재귀 정렬

        # conquer: 정렬된 두 배열을 병합
        return self._merge(left, right)

    def _merge(self, left, right):
        result = []
        i = j = 0

        # 양쪽 배열이 모두 남아있는 동안 병합 진행
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # 남은 원소들 마저 붙이기
        result.extend(left[i:])
        result.extend(right[j:])
        return result


def main():
    user_input = input("Enter numbers separated by spaces: ").strip()

    if not user_input:
        print("Invalid input.")
        return

    try:
        # 입력을 float 리스트로 변환
        numbers = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input.")  # 숫자 변환 실패 시 예외 처리
        return

    sorter = MergeSorter()
    sorted_numbers = sorter.sort(numbers)

    # 출력 포맷: 소수점 1자리까지 float 형태로 정렬 출력
    sorted_output = ' '.join(f"{num:.1f}" for num in sorted_numbers)
    print(f"Sorted: {sorted_output}")


if __name__ == "__main__":
    main()
