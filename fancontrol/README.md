# Hướng dẫn sử dụng Blueprint Điều Chỉnh Tốc Độ, Xoay Quạt cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn điều chỉnh tốc độ quạt như tăng, giảm tốc theo % bước cài sẵn, điều chỉnh tốc độ quạt theo %, bật tắt chế độ xoay trong Home Assistant với tích hợp LLM (AI). Hỗ trợ điều khiển bằng giọng nói.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2024.10.0.
- Đã cài đặt tích hợp Fan (quạt) và có entity quạt cần điều khiển.
- Đã cấu hình LLM (AI) nếu muốn sử dụng các prompt thông minh.

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Fan Control Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/fancontrol/fan_control_speed_and_oscillation.yaml)

## 4. Hướng dẫn sử dụng

### 4.1. Cấu hình
- Sau khi import blueprint, tạo script từ blueprint.
- Vào phần **Fan Settings** để cài đặt `percentage_step` (mặc định 25%).
- Chỉnh sửa phần **Entity ID Prompt** để cập nhật danh sách quạt của bạn.

### 4.2. Các chức năng

#### **1. Đặt tốc độ cụ thể (Set Percentage)**
Thiết lập tốc độ quạt từ 0-100%.

**Ví dụ:**
- "Đặt quạt phòng khách ở tốc độ 70%"
- "Quạt phòng ngủ 50%"
- "Tắt quạt" (sử dụng 0%)

#### **2. Tăng tốc độ (Increase Speed)**
Tăng tốc độ quạt theo `percentage_step` đã cài đặt.

**Ví dụ:**
- "Tăng tốc độ quạt phòng ngủ"
- "Quạt nhanh hơn"
- "Tăng quạt lên"

#### **3. Giảm tốc độ (Decrease Speed)**
Giảm tốc độ quạt theo `percentage_step` đã cài đặt.

**Ví dụ:**
- "Giảm tốc độ quạt bếp"
- "Quạt chậm lại"
- "Giảm quạt xuống"

#### **4. Bật/tắt chế độ xoay (Oscillate)**
Kiểm soát quạt xoay hoặc giữ nguyên hướng.

**Ví dụ:**
- "Bật xoay quạt phòng khách"
- "Tắt xoay quạt"
- "Quạt đứng yên"

### 4.3. Sử dụng với Voice Assistant
- Expose script ra Assist trong Settings → Voice Assistants → Expose
- Trò chuyện với trợ lý AI để điều khiển quạt

**Ví dụ câu lệnh:**
- "Tăng tốc độ quạt phòng ngủ lên 60%"
- "Tăng quạt phòng khách lên"
- "Tắt xoay quạt phòng ngủ đi"

## 5. Lưu ý

- **Percentage Step:** Giá trị mặc định là 25%. Bạn có thể điều chỉnh từ 5-35% trong cài đặt blueprint.
- **Entity ID:** Đảm bảo entity_id quạt đúng format `fan.ten_quat`.
- **Prompts:** Có thể tùy chỉnh các prompt trong blueprint để phù hợp với LLM model của bạn.

## 6. Troubleshooting

**Lỗi: Invalid entity_id**
- Kiểm tra entity_id có bắt đầu bằng `fan.` không.
- Kiểm tra entity có tồn tại trong Home Assistant không.

**Lỗi: Invalid action**
- Action phải là một trong: `set_percentage`, `increase_speed`, `decrease_speed`, `oscillate`.

**Lỗi: Percentage must be between 0 and 100**
- Giá trị tốc độ phải nằm trong khoảng 0-100.

**Quạt không xoay:**
- Kiểm tra quạt có hỗ trợ chức năng oscillation không.
- Giá trị oscillating phải là `true` hoặc `false`.

## 7. Changelog

**Version 20250112**
- Initial release
- Hỗ trợ 4 actions: set_percentage, increase_speed, decrease_speed, oscillate
- Tích hợp LLM với prompts chi tiết
- Hỗ trợ Voice Assistant
- Cấu hình percentage_step linh hoạt