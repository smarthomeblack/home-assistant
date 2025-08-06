# Hệ Thống Tra Cứu Phạt Nguội cho Home Assistant

Hệ thống này giúp bạn tự động tra cứu thông tin phạt nguội giao thông từ trang PhatNguoi.vn và nhận thông báo trên thiết bị di động khi có vi phạm mới.

## Import Nhanh Blueprint

Nhấn vào các nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Voice Traffic Fine Lookup Tool Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/tracuuphatnguoi/traffic_fine_lookup_full_llm.yaml)

[![Import Traffic Fine Notification Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/tracuuphatnguoi/traffic_fine_notification.yaml)

## Tổng Quan

Hệ thống gồm 3 thành phần chính:
1. **Script Python tra cứu phạt nguội** - Kết nối với API phatnguoi.vn và trả về kết quả
2. **LLM** - Tra cứu qua assistant chat, voice
3. **Template Sensors** - Tự động tra cứu theo lịch định sẵn và lưu kết quả
4. **Automation thông báo** - Gửi thông báo khi phát hiện vi phạm

## Yêu Cầu

- Home Assistant đã cài đặt
- Tích hợp Pyscript (cài đặt qua HACS)
- Thiết bị di động cài đặt ứng dụng Home Assistant

## Hướng Dẫn Cài Đặt

### Bước 1: Cài đặt tích hợp Pyscript

1. Cài đặt HACS nếu chưa có
2. Trong HACS, thêm tích hợp Pyscript
3. Khởi động lại Home Assistant

### Bước 2: Cấu hình Pyscript

Thêm vào file `configuration.yaml` của bạn:

```yaml
pyscript:
  allow_all_imports: true
  hass_is_global: true
```

### Bước 3: Sao chép các file

1. Tạo thư mục `pyscript` trong thư mục cấu hình Home Assistant (nếu chưa có)
2. Sao chép file `traffic_fine_lookup_tool.py` vào thư mục này
3. Sao chép file `requirements.txt` vào thư mục này

### Bước 4: Khởi động lại Home Assistant

### Bước 5: Thêm Template Sensor cho mỗi xe

Thêm vào `configuration.yaml` của bạn (thay thế biển số xe với biển số của bạn):

```yaml
template:
  - trigger:
      - trigger: time_pattern
        hours: /12
      - trigger: event
        event_type: event_template_reloaded
    sensor:
      - name: Time to Check 30G12345      # Biển số xe
        unique_id: time_to_check_30g12345     # Biển số xe
        icon: mdi:clock-digital
        device_class: timestamp
        state: "{{ (now() + timedelta(minutes=range(1,181) | random)).isoformat() }}"
  - trigger:
      - trigger: time
        at: sensor.time_to_check_30g12345     # Biển số xe
    action:
      - action: pyscript.traffic_fine_lookup_tool
        data:
          license_plate: 30G12345     # Biển số xe
          vehicle_type: "1"     # Kiểu phương tiện
        response_variable: response
    sensor:
      - name: 30G12345      # Biển số xe
        unique_id: 30g12345     # Biển số xe
        icon: mdi:car
        state: "{{ response.message if response.get('status') else response.get('error') }}"
        attributes:
          data: "{{ response }}"
```

**Ghi chú về loại phương tiện**:
- `"1"`: Ô tô
- `"2"`: Xe máy
- `"3"`: Xe đạp điện

**Tùy chọn icon**:
- `"mdi:car"`: Ô tô
- `"mdi:motorbike"`: Xe máy
- `"mdi:motorbike-electric"`: Xe máy điện

### Bước 6: Cài đặt Blueprint tự động hóa thông báo

1. Đi đến Settings > Automations & Scenes > Blueprints
2. Nhấp vào "Import Blueprint"
3. Nhập URL của file `traffic_fine_notification.yaml` hoặc tải lên file này
4. Tạo một automation từ blueprint này, chọn:
   - Các sensor xe đã tạo ở bước 5
   - Các thiết bị cần nhận thông báo

### Bước 7: Hoàn tất cài đặt

1. Khởi động lại Home Assistant
2. Tải lại Template Entities (Developer Tools > YAML > Reload Template Entities)

## Cách Sử Dụng

Sau khi cài đặt, hệ thống sẽ tự động:

1. Kiểm tra vi phạm 2 lần mỗi ngày theo lịch ngẫu nhiên
2. Cập nhật trạng thái của các sensor
3. Gửi thông báo khi phát hiện vi phạm

Bạn có thể:
- Xem thông tin phạt nguội trong mục Entities
- Thủ công kích hoạt tra cứu từ Developer Tools > Services > pyscript.traffic_fine_lookup_tool
- Nhận thông báo tự động trên thiết bị di động khi có vi phạm mới

## Xử Lý Sự Cố

### Sensor hiển thị 'unavailable'
- Kiểm tra lại biển số xe đã nhập đúng chưa
- Đảm bảo script Python đã được sao chép đúng vị trí
- Kiểm tra logs của Home Assistant

### Không nhận được thông báo
- Kiểm tra xem thiết bị di động có được chọn trong automation
- Đảm bảo thiết bị có cài đặt ứng dụng Home Assistant
- Kiểm tra quyền thông báo trong ứng dụng

### Lỗi khi tra cứu
- Kiểm tra định dạng biển số xe
- Kiểm tra kết nối internet
- Xem logs để biết thêm chi tiết

## Tùy Chỉnh Nâng Cao

### Thay đổi tần suất kiểm tra
Sửa `hours: /12` trong template sensor để thay đổi tần suất kiểm tra. Ví dụ:
- `hours: /6` - Kiểm tra 4 lần/ngày
- `hours: /24` - Kiểm tra 1 lần/ngày

### Thêm nhiều xe
Lặp lại Bước 5 với biển số và loại phương tiện khác nhau.

### Tùy chỉnh nội dung thông báo
Sửa phần `title` và `message` trong blueprint traffic_fine_notification.yaml.

---

Chúc bạn sử dụng hệ thống tra cứu phạt nguội một cách hiệu quả! Liên hệ tác giả nếu cần thêm hỗ trợ. 
