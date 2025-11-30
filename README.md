# Snake Game - OOP Python

## Nhóm thực hiện

| STT | Họ tên             | MSSV       | Phần thực hiện                       |
|-----|------------------|-----------|------------------------------------|
| 1   | Nguyễn Quốc Huy       | 22730075  | Trưởng nhóm, xây dựng `game_class.py`, menu, game loop, score, game over |
| 2   | Trần Hữu Tài             | 22730094   | `snake_class.py`, xử lý di chuyển Snake, collision |
| 3   | Đồng Nguyễn Vũ Anh    | 25730007   | `food_class.py`, spawn food, update food vị trí, draw |

---

## Giới thiệu
Game Snake được viết bằng **Python 3.12.4** và thư viện **Pygame 2.6.1** theo hướng OOP.  
Các tính năng chính:
- Menu chính với lựa chọn **ENTER để bắt đầu**  
- Menu chọn **mức độ khó** (Easy/Medium/Hard)  
- Score hiển thị góc trên bên trái màn hình  
- Khi chết, hiển thị menu **Replay / Exit**  
- Title bar hiển thị: "Snake Game - Powered by 22730075"

---

## Yêu cầu
- Python **3.12.4**  
- Thư viện `pygame==2.6.1`  

---

## Cấu trúc thư mục
```
Snake/
│ main.py
│ run_snake.bat
│ requirements.txt
│ README.md
│ .gitignore
└─ snake_game/
│ **init**.py
│ game_class.py
│ snake_class.py
│ food_class.py

```
- `main.py` : chạy game chính  
- `snake_game/` : chứa các class Game, Snake, Food  
- `run_snake.bat` : script Windows để double-click chạy game  
- `requirements.txt` : liệt kê thư viện cần cài  
- `.gitignore` : bỏ qua venv, file cache, v.v.  

---

## Hướng dẫn cài đặt và chạy
1. Clone repository:
    - git clone <repo-url>
    - cd Snake

2. Tạo **virtual environment** và activate:
    - python -m venv .venv
    - .venv\Scripts\activate

5. Cài các thư viện cần thiết:
    - pip install -r requirements.txt

7. Chạy game:
   - Cách 1 (terminal/PowerShell):
python main.py
    - Cách 2 (Windows double-click):
Double-click vào `run_snake.bat` → game chạy ngay

---

## Hướng dẫn chơi
- Di chuyển Snake: Arrow keys (⬆⬇⬅➡)  
- Menu chính: Nhấn ENTER để bắt đầu  
- Chọn mức độ khó:
- 1: Easy (chậm)
- 2: Medium (trung bình)
- 3: Hard (nhanh)
- Khi chết:
- R: Replay (chơi lại)
- ESC: Exit (thoát game)
- Score: hiển thị góc trên bên trái màn hình

---

## Hình ảnh minh họa
<p align="center" width="100%">
  <img src="https://github.com/user-attachments/assets/b52a7970-ce8b-4e2c-9944-7ffe9fb002a8" width="24%" alt="image1" />
  <img src="https://github.com/user-attachments/assets/28d736ff-3cd8-4be0-9dd4-bba3ac764cf6" width="24%" alt="image2" />
  <img src="https://github.com/user-attachments/assets/75c7a739-8f26-4c3f-b773-ad1c9de19b16" width="24%" alt="image3" />
  <img src="https://github.com/user-attachments/assets/7c935121-41ad-45bd-80a8-58d43a108cb2" width="24%" alt="image4" />
</p>

---

## Lưu ý
- Game **chỉ cần thư viện** *pygame*  
- Đảm bảo **activate venv trước khi chạy** để tránh lỗi thiếu thư viện
