# Hướng dẫn sử dụng Blueprint Điều Khiển Điều Hòa cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn điều khiển điều hòa không khí trong Home Assistant với tích hợp LLM (AI). Bạn có thể điều chỉnh chế độ hoạt động, xoay gió, tốc độ quạt, turbo và chế độ tiết kiệm điện một cách thông minh, hỗ trợ điều khiển bằng giọng nói.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2024.10.0.
- Đã cài đặt tích hợp Climate (điều hòa) và có entity điều hòa cần điều khiển.
- Mới chỉ test với điều hòa Tasmota-IRHVAC.
- Đã cấu hình LLM (AI) nếu muốn sử dụng các prompt thông minh.

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Climate Control Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/climatecontrol/climate_control.yaml)

## 4. Hướng dẫn sử dụng

### 4.1. Chỉnh sửa danh sách điều hòa
- Sau khi import blueprint, tạo script từ blueprint.
- Vào phần **Entity ID Prompt** để chỉnh sửa danh sách điều hòa của bạn.

### 4.2. Các chức năng

#### **1. Điều chỉnh chế độ hoạt động (HVAC Mode)**
Các chế độ: `heat` (sưởi), `cool` (lạnh), `heat_cool` (tự động), `auto`, `dry` (hút ẩm), `fan_only` (chỉ quạt)

**Ví dụ:**
- "Đặt điều hòa phòng khách chế độ lạnh"
- "Bật chế độ sưởi điều hòa phòng ngủ"
- "Chế độ hút ẩm"

#### **2. Điều chỉnh chế độ xoay (Swing Mode)**
Các chế độ: `off` (tắt xoay), `vertical` (xoay dọc), `horizontal` (xoay ngang), `both` (xoay cả hai)

**Ví dụ:**
- "Bật xoay dọc điều hòa"
- "Tắt xoay gió"
- "Xoay cả dọc và ngang"

#### **3. Điều chỉnh tốc độ quạt (Fan Mode)**
Các chế độ: `low` (thấp), `medium` (trung bình), `high` (cao), `min` (tối thiểu), `max` (tối đa), `auto` (tự động)

**Ví dụ:**
- "Đặt tốc độ quạt cao"
- "Tốc độ quạt tối thiểu"
- "Quạt tự động"

#### **4. Bật/tắt chế độ Turbo**
Giá trị: `on` (bật), `off` (tắt)

**Ví dụ:**
- "Bật chế độ turbo"
- "Tắt turbo điều hòa"
- "Công suất tối đa"

#### **5. Bật/tắt chế độ tiết kiệm điện (Econo)**
Giá trị: `on` (bật), `off` (tắt)

**Ví dụ:**
- "Bật chế độ tiết kiệm điện"
- "Tắt eco mode"
- "Tiết kiệm năng lượng"

### 4.3. Sử dụng với Voice Assistant
- Expose script ra Assist trong Settings → Voice Assistants → Expose
- Trò chuyện với trợ lý AI để điều khiển

**Ví dụ câu lệnh:**
- "Đặt điều hòa phòng khách chế độ lạnh, tốc độ cao"
- "Bật turbo cho điều hòa phòng ngủ"
- "Xoay dọc và tiết kiệm điện"

## 5. Lưu ý

- **Chế độ Turbo và Econo:** Yêu cầu tích hợp `tasmota_irhvac`. Nếu điều hòa của bạn không hỗ trợ, có thể bỏ qua hai chức năng này.
- **Entity ID:** Đảm bảo entity_id điều hòa đúng format `climate.ten_dieu_hoa`.
- **Prompts:** Có thể tùy chỉnh các prompt trong blueprint để phù hợp với LLM model của bạn.

## 6. Troubleshooting

**Lỗi: Invalid entity_id**
- Kiểm tra entity_id có bắt đầu bằng `climate.` không.
- Kiểm tra entity có tồn tại trong Home Assistant không.

**Lỗi: Invalid action**
- Action phải là một trong: `set_hvac_mode`, `set_swing_mode`, `set_fan_mode`, `set_turbo`, `set_econo`.

**Lỗi: HVAC mode must be one of...**
- Kiểm tra giá trị nhập vào có đúng trong danh sách cho phép không.
- Tất cả giá trị phải là chữ thường.

**Chế độ Turbo/Econo không hoạt động:**
- Đảm bảo đã cài đặt `tasmota_irhvac` integration.
- Kiểm tra điều hòa có hỗ trợ chế độ này không.

## 7. Changelog

**Version 20250112**
- Initial release
- Hỗ trợ 5 actions: set_hvac_mode, set_swing_mode, set_fan_mode, set_turbo, set_econo
- Tích hợp LLM với prompts chi tiết
- Hỗ trợ Voice Assistant