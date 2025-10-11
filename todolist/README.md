# Hướng dẫn sử dụng Blueprint Quản lý To-Do List cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn quản lý danh sách công việc (to-do list) trong Home Assistant với tích hợp LLM (AI). Bạn có thể thêm, xóa, cập nhật, lấy danh sách, và xóa các công việc đã hoàn thành một cách thông minh, hỗ trợ xác nhận thao tác bằng tiếng Việt.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2024.10.0.
- Đã cài đặt tích hợp To-Do List (todo) và có entity to-do cần quản lý.
- Đã cấu hình LLM (AI) nếu muốn sử dụng các prompt thông minh.

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import To-Do List Manager Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/todolist/to_do_list.yaml)

## 4. Hướng dẫn sử dụng

### 4.1. Cấu hình
- Sau khi import blueprint, tạo script từ blueprint.
- Chọn entity to-do trong phần **To-Do List Entity**.

### 4.2. Các chức năng

#### **1. Thêm công việc (Add Item)**
Thêm công việc mới vào danh sách với tên, mô tả và thời gian hoàn thành.

**Thông tin:**
- **Tên công việc:** Bắt buộc
- **Mô tả:** Tùy chọn
- **Due date/datetime:** Tùy chọn (định dạng ISO 8601 hoặc YYYY-MM-DD)

**Ví dụ:**
- "Thêm công việc mua sữa vào 10h sáng mai"
- "Nhắc tôi họp team lúc 2h chiều"
- "Thêm task hoàn thành báo cáo"

**Xác nhận:** ✅ Cần xác nhận trước khi thêm

---

#### **2. Xem danh sách (Get Items)**
Lấy danh sách công việc, có thể lọc theo trạng thái.

**Lọc theo trạng thái:**
- `needs_action` - Chưa hoàn thành
- `completed` - Đã hoàn thành
- Để trống - Lấy tất cả

**Ví dụ:**
- "Cho tôi xem danh sách công việc"
- "Xem các công việc chưa hoàn thành"
- "Liệt kê task đã xong"

**Xác nhận:** ❌ Không cần xác nhận (chỉ đọc)

---

#### **3. Xóa công việc (Remove Item)**
⚠️ **THAO TÁC NGUY HIỂM - KHÔNG THỂ HOÀN TÁC**

Xóa một công việc cụ thể theo UID.

**Ví dụ:**
- "Xóa công việc mua sữa"
- "Xóa task họp team"

**Xác nhận:** ⚠️ Bắt buộc xác nhận bằng "DELETE" hoặc "CONFIRM"

**Template xác nhận:**
```
⚠️ XÓA VĨNH VIỄN công việc:
✓ Tên: [task_name]
⏰ Thời gian: [due_date_time]
✅ Status: [status]
⚠️ KHÔNG THỂ HOÀN TÁC!
Gõ DELETE hoặc CONFIRM để tiếp tục.
```

---

#### **4. Xóa tất cả đã hoàn thành (Remove Completed Items)**
⚠️ **THAO TÁC NGUY HIỂM - KHÔNG THỂ HOÀN TÁC**

Xóa tất cả các công việc có trạng thái completed.

**Ví dụ:**
- "Xóa tất cả công việc đã hoàn thành"
- "Dọn dẹp danh sách task đã xong"

**Xác nhận:** ⚠️ Bắt buộc xác nhận bằng "DELETE ALL"

**Template xác nhận:**
```
⚠️ XÓA TẤT CẢ công việc đã hoàn thành:
✅ [count] tasks sẽ bị xóa
⚡ CẢNH BÁO: KHÔNG THỂ HOÀN TÁC!
Gõ DELETE ALL để xác nhận.
```

---

#### **5. Cập nhật công việc (Update Item)**
Sửa đổi thông tin công việc: tên, mô tả, due date, trạng thái.

**Có thể cập nhật:**
- Đổi tên (`rename`)
- Thay đổi trạng thái (`status`: needs_action hoặc completed)
- Cập nhật mô tả (`description`)
- Thay đổi thời gian (`due_datetime` hoặc `due_date`)

**Ví dụ:**
- "Đổi tên công việc mua sữa thành mua bánh mì"
- "Đánh dấu task họp team là đã hoàn thành"
- "Dời thời gian họp sang 3h chiều"

**Xác nhận:** ✅ Cần xác nhận trước khi cập nhật

**Template xác nhận:**
```
Tôi sẽ cập nhật công việc:
✓ Tên: [old_name] → [new_name] (nếu thay đổi)
⏰ Thời gian: [old_time] → [new_time] (nếu thay đổi)
✅ Status: [old_status] → [new_status] (nếu thay đổi)
📝 Mô tả: [new_description] (nếu thay đổi)
Bạn xác nhận không?
```

---

### 4.3. Sử dụng với Voice Assistant
- Expose script ra Assist trong Settings → Voice Assistants → Expose
- Trò chuyện với trợ lý AI để quản lý to-do list

**Ví dụ câu lệnh:**
- "Thêm công việc mua sữa vào 10h sáng mai"
- "Cho tôi xem danh sách việc cần làm"
- "Đánh dấu task họp team là đã xong"
- "Xóa công việc mua sữa"

---

## 5. Quy trình xác nhận

### Actions CẦN xác nhận (Steps 1-2-3):
1. **STEP 1:** LLM parse thông tin từ yêu cầu
2. **STEP 2:** Hiển thị thông tin và hỏi xác nhận
3. **STEP 3:** Thực thi sau khi user xác nhận

**Áp dụng cho:**
- ✅ add_item
- ⚠️ remove_item (xác nhận CRITICAL)
- ⚠️ remove_completed_items (xác nhận CRITICAL)
- ✅ update_item

### Actions KHÔNG cần xác nhận:
- ❌ get_items (chỉ đọc)

---

## 6. Lưu ý

- **Xác nhận CRITICAL:** Các thao tác xóa cần xác nhận đặc biệt để tránh mất dữ liệu.

---

## 7. Troubleshooting

**Lỗi: Action type must be one of...**
- Action phải là một trong: `add_item`, `get_items`, `remove_item`, `remove_completed_items`, `update_item`.

**Lỗi: Task name is required**
- Tên công việc là bắt buộc khi thêm mới.

**Lỗi: Item UID is required**
- Cần cung cấp UID khi xóa hoặc cập nhật. Lấy UID từ get_items.

**Lỗi: Invalid datetime format**
- Due datetime phải theo format ISO 8601: `YYYY-MM-DDTHH:MM:SS`
- Due date phải theo format: `YYYY-MM-DD`

---

## 8. Changelog

**Version 20250112**
- Initial release
- Hỗ trợ 5 actions: add_item, get_items, remove_item, remove_completed_items, update_item
- Workflow xác nhận an toàn cho thao tác nguy hiểm
- Tích hợp LLM với prompts chi tiết
- Hỗ trợ Voice Assistant
- Hỗ trợ tiếng Việt đầy đủ