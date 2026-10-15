# Week1 follow-up — Trần Quốc Huy (TV2)

Ngày kiểm tra: 15/10/2026. Nhánh bổ sung bắt đầu từ main
`07b39013b62145d4e035fe8e964c6637aa65c9be`. Python local: 3.14.0.
Reviewer phần cá nhân và phần nhóm của Huy: Quyền (`pqquyenn`).

## Tiến độ và AI

Huy xác nhận trong phiên này: **2 giờ thực tế trước lượt bổ sung**, code năm
bài Week1 tự làm; các thao tác còn lại có AI hỗ trợ. Thời gian này không được
tự tăng để bao gồm phiên bổ sung. Nhật ký tại [ai-use-log.md](../../docs/ai-use-log.md).
PR gốc: [#10](https://github.com/baoduong2342007/python-bootcamp/pull/10)
và [#11](https://github.com/baoduong2342007/python-bootcamp/pull/11).

Issue bổ sung: [#24](https://github.com/baoduong2342007/python-bootcamp/issues/24).
PR bổ sung: chờ liên kết.

## Kiểm tra Huy và workflow TV5

Chạy từ gốc repository, dùng `.venv/bin/python` cho `python` dưới đây:

```bash
python -m pytest -q tests/test_w1.py --member tqhuy0602 --variant 2
python -m ruff check members/tqhuy0602
python -m pytest -q tests/test_w1.py --member simble2k -k "not test_w1_4"
python -m pytest -q tests/test_w1_extra.py --member simble2k
python -m ruff check members/simble2k/w1 tests/test_w1_extra.py
```

- Huy: **5 passed**, không skip; Ruff: **All checks passed**.
- TV5: **4 passed, 1 deselected**; test nhóm riêng: **1 passed**; Ruff sạch.
  Ghi `4 official + 1 extra`, không dùng variant 5.
- Kiểm tra biên Huy: rỗng/âm/chẵn/lẻ và đầu vào của summary; top-k k <= 0,
  rỗng, tần suất bằng nhau; ngưỡng đăng ký khóa luận; timetable giữ môn trùng
  và không sửa entries. Tất cả đạt.
- Insertion sort: **1.093** danh sách độ dài 0–6, phần tử -1/0/1; kết quả
  đúng, sửa tại chỗ và trả cùng đối tượng. Có thể kiểm tra lại bằng:

```bash
python - <<'PY'
from itertools import product
from members.tqhuy0602.w1.translate import insertion_sort
count = 0
for length in range(7):
    for values in product((-1, 0, 1), repeat=length):
        items = list(values)
        result = insertion_sort(items)
        assert result is items
        assert items == sorted(values)
        count += 1
print(f"{count} passed (in-place, same object)")
PY
```

## Review bổ sung Dương

Cả hai PR đã merge trước lượt review này. Không ghi nhận approval trước merge.

| PR | Head đã kiểm tra | Official tests | Ruff |
| --- | --- | --- | --- |
| [#17](https://github.com/baoduong2342007/python-bootcamp/pull/17) | `5ff0b1d90b1b0ede1b86c1c1dbc40bf326685635` | 5 passed, không skip | PLC0206 ở timetable.py:5 |
| [#19](https://github.com/baoduong2342007/python-bootcamp/pull/19) | `10013bbc3c16d12b0c0394bd1ce1301449eb4b1f` | 5 passed, không skip | All checks passed |

Code được xuất bằng `git archive` ra thư mục tạm riêng cho từng head. Head #17
chưa có tests, nên dùng bản sao **không sửa** của hai tests chính thức từ main
nêu trên làm harness; head #19 dùng tests có sẵn trong commit đó. Lệnh kiểm tra
trong từng thư mục:

```bash
python -m pytest -q tests/test_w1.py --member baoduong2342007 --variant 1
python -m ruff check members/baoduong2342007
```

Ngoài tests chính thức, đã kiểm tra các biên chung như Huy và **5.465 trường
hợp binary search** mỗi head: danh sách đã sắp xếp độ dài 0–6, giá trị -1/0/1,
khóa -2 đến 2; giá trị trùng cho phép bất kỳ chỉ số hợp lệ. Tất cả đạt.

- #17 Question: `word_count("a,b")` của Dương thành `a` và `b`, của Huy thành
  `ab`; cần xác nhận cách hiểu dấu câu với yêu cầu môn học.
- #17 Suggestion: docstring binary search nên nêu đầu vào đã sắp xếp và giải
  thích thêm khác biệt quản lý bộ nhớ/kiểu dữ liệu C++–Python.
- #17 Praise: biên binary search thu hẹp đúng; top-k xử lý tần suất bằng nhau
  bằng khóa `(-count, word)`.
- #19 Question: xác nhận việc giữ các môn học trùng trong cùng ngày.
- #19 Suggestion: docstring by_day mô tả việc giữ môn trùng và sắp xếp từng ngày;
  phân biệt ghi chú review Bảo với review đã đăng GitHub.
- #19 Praise: `b.values()` sửa đúng các danh sách trong dictionary, giữ hành
  vi và khắc phục PLC0206; khai báo AI và lịch sử được ghi rõ.

Liên kết review đã đăng:

- [Review #17](https://github.com/baoduong2342007/python-bootcamp/pull/17#pullrequestreview-5526848837).
- [Review #19](https://github.com/baoduong2342007/python-bootcamp/pull/19#pullrequestreview-5526849445).

## Giữ nguyên tests và phạm vi

SHA-256 trước và sau cập nhật tài liệu:

```text
tests/conftest.py: d482fb7e349db5267113db7af53bff7df175e51c48c4e17d60ae80c0ee4f5bb8
tests/test_w1.py: 8ceb5cdf18a85ae066ef5f9fb0bc1249e610a4456e8f925982b73075bb60c6de
```

Không sửa code bài cá nhân, không thay tests giảng viên, không sửa hàng tiến độ
của thành viên khác. Kiểm tra local không xác nhận CI Ubuntu/Python 3.12.
PR bổ sung chờ Quyền review trước khi merge; CI, deadline, tag và nộp bài thuộc
các thành viên được phân công trong kế hoạch.
