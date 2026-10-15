# Week 1 Follow-up & Evidence — Phan Quỳnh Quyền (TV3)

- **Thành viên:** Phan Quỳnh Quyền (`pqquyenn` - TV3)
- **Ngày thực hiện:** 15/10/2026
- **Nhánh bổ sung:** `feat/tv3-week1-ci-docs` tạo từ `main` mới nhất (`f6512d0`)
- **Reviewer được phân công:** Lương Nhật Minh (`luongnhatinh` - TV4)
- **Reviewee được phân công:** Trần Quốc Huy (`tqhuy0602` - TV2)

---

## 1. Trạng thái Bài tập Cá nhân (W1-1 đến W1-5)

- **PR cá nhân:** [#14](https://github.com/baoduong2342007/python-bootcamp/pull/14) đã được merge vào `main` tại commit `b40090046d46f47671ffce9a03236c25ee0c7404`.
- **Kết quả kiểm thử chính thức:** **5 passed, 0 skipped**.
  ```bash
  python -m pytest -q tests/test_w1.py --member pqquyenn --variant 3
  ```
- **Kiểm tra phong cách mã nguồn (Ruff):** **All checks passed**.
  ```bash
  python -m ruff check members/pqquyenn/w1
  ```
- **Kiểm tra trường hợp biên cho bài W1-4 (`transpose` - Chuyển vị ma trận):**
  - Ma trận rỗng: `transpose([]) == []` và `transpose([[]]) == []`.
  - Ma trận chữ nhật $2 \times 3$ và $3 \times 2$: chuyển vị đúng kích thước và giá trị.
  - Ma trận vuông $3 \times 3$, ma trận hàng $1 \times n$, ma trận cột $n \times 1$: kiểm tra đạt 100%.
  - Tính bất biến: Đảm bảo ma trận gốc không bị mutate, trả về đối tượng danh sách mới hoàn toàn.
  - Docstring đầy đủ, giải thích rõ khác biệt giữa C++ (`std::vector<std::vector<int>>` với cấp phát kích thước thủ công) và Python (dùng comprehension / `zip(*matrix)` ngắn gọn và linh hoạt).

---

## 2. Review Bổ sung cho Trần Quốc Huy (TV2)

Theo phân công xoay vòng, Quyền thực hiện review bài của Huy (TV2):

### 2.1 Kiểm chứng độc lập thuật toán `insertion_sort` (W1-4 của Huy)
Đã chạy kiểm tra tự động qua 1.093 trường hợp (độ dài 0–6, giá trị -1/0/1):
```python
from itertools import product
from members.tqhuy0602.w1.translate import insertion_sort
count = 0
for length in range(7):
    for values in product((-1, 0, 1), repeat=length):
        items = list(values)
        result = insertion_sort(items)
        assert result is items, "Phải trả về cùng đối tượng danh sách"
        assert items == sorted(values), "Phải sắp xếp tăng dần"
        count += 1
print(f"Verified {count} cases: in-place mutation and same object.")
```
*Kết quả:* **1.093 / 1.093 cases passed**. Thuật toán của Huy thực hiện sắp xếp tại chỗ (in-place) chuẩn xác và trả về cùng đối tượng `a`.

### 2.2 Nội dung Review bổ sung chi tiết:

#### A. PR [#10](https://github.com/baoduong2342007/python-bootcamp/pull/10) (Bài tập cá nhân của Huy)
* **Question:** Trong `rules.py`, khi sinh viên thiếu cả tín chỉ lẫn GPA, thứ tự các lý do trong danh sách trả về của hàm `missing` có được đảm bảo ưu tiên tín chỉ trước GPA như quy định của nhóm không?
* **Suggestion:** Trong các hàm xử lý văn bản ở `text_tools.py`, bạn có thể bổ sung thêm type hints tường minh hơn cho kiểu trả về để tăng tính nhất quán và dễ đọc.
* **Praise:** Thuật toán `insertion_sort` trong `translate.py` cài đặt rất chuẩn in-place, không dùng hàm có sẵn, docstring phân tích sâu sắc cơ chế truyền tham chiếu của Python so với C++.

#### B. PR [#11](https://github.com/baoduong2342007/python-bootcamp/pull/11) (Phần việc nhóm của Huy)
* **Question:** Bảng danh sách các labels và milestones đã được liên kết đầy đủ với các issue tương ứng của từng thành viên chưa?
* **Suggestion:** Nên chú thích rõ ràng việc TV5 chạy 4 bài chính thức và 1 bài test bổ sung riêng để tránh việc các bạn khác nhầm lẫn chạy `--variant 5`.
* **Praise:** Cấu trúc issue template cho bài tập hàng tuần được thiết kế rất gọn gàng, đúng với mô tả trong giáo trình Chapter 18.

#### C. PR [#25](https://github.com/baoduong2342007/python-bootcamp/pull/25) (Follow-up evidence của Huy)
* **Question:** Script kiểm tra 1.093 ca của bạn đã bao gồm các trường hợp danh sách đã sắp xếp ngược hoàn toàn (worst case) chưa?
* **Suggestion:** Tài liệu follow-up trình bày rất chi tiết, có thể đưa đoạn code kiểm tra `insertion_sort` này vào tài liệu nhóm làm mẫu kiểm thử in-place.
* **Praise:** Quá trình kiểm thử thực nghiệm vô cùng cẩn thận, ghi nhận thời gian thực tế trung thực và minh bạch trong khai báo sử dụng AI.

---

## 3. Triển khai Phần việc Nhóm của TV3: CI & Hướng dẫn Môi trường

Theo phân công trong `plan.md` và `need_to_fix.md`, TV3 (Quyền) đã hoàn thành:

1. **Workflow CI (`.github/workflows/ci.yml`):**
   - Chạy trên môi trường Ubuntu (`ubuntu-latest`) với Python 3.12.
   - Tách riêng biệt job kiểm tra định dạng mã nguồn `lint` (Ruff) và job kiểm thử `pytest`.
   - **Tối ưu hóa PR cá nhân:** Dùng `git diff` nhận diện file thay đổi để chỉ chạy test người mở PR, tránh việc một thành viên bị chặn bởi bài của người khác.
   - **Bảo vệ toàn vẹn khi thay đổi core:** Nếu sửa đổi `tests/` hoặc `.github/workflows/`, CI tự động chuyển sang chế độ chạy kiểm thử toàn bộ 5 thành viên.
   - **Ma trận (Matrix) trên `main`:** Khi merge hoặc push vào `main`, CI chạy kiểm tra toàn bộ 5 thành viên (TV1–TV4 đúng variant 1–4; TV5 chạy 4 bài chính thức + 1 bài test nhóm riêng). Không chấp nhận kết quả skip.

2. **Tài liệu Hướng dẫn Môi trường & CI (`docs/ci-environment.md`):**
   - Hướng dẫn thiết lập môi trường ảo `.venv` trên Windows PowerShell, Git Bash, Linux/macOS.
   - Cài đặt `pytest` và `ruff`.
   - Bảng tổng hợp câu lệnh kiểm thử cụ thể cho từng thành viên kèm lưu ý về cờ `--member`.
   - Sơ đồ kiến trúc CI và hướng dẫn đọc kết quả trên GitHub Actions.

3. **Yêu cầu Review:**
   - Đã chỉ định bạn **Lương Nhật Minh** (`luongnhatinh` - TV4) làm reviewer cho PR này theo đúng sơ đồ phân công của Team03.
