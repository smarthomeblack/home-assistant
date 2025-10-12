# Hướng dẫn sử dụng Blueprint Dự Báo Thời Tiết cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn lấy dự báo thời tiết theo ngày hoặc theo giờ trong Home Assistant với tích hợp LLM (AI). Bạn có thể hỏi dự báo thời tiết cho một ngày cụ thể hoặc một giờ cụ thể bằng giọng nói.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2024.10.0.
- Đã cài đặt tích hợp Weather (thời tiết) và có entity thời tiết cần sử dụng.
- Đã cấu hình LLM (AI) nếu muốn sử dụng các prompt thông minh.

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Weather Forecast Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/weatherforecast/weather_forecast.yaml)

## 4. Hướng dẫn sử dụng

### 4.1. Cấu hình
- Sau khi import blueprint, tạo script từ blueprint.
- Chọn entity thời tiết trong phần **Weather Entity**.
  - Ví dụ: `weather.accuweather_hai_duong`

### 4.2. Các chức năng

#### **1. Dự báo theo ngày (Daily Forecast)**
Lấy dự báo thời tiết cho một ngày cụ thể.

**Định dạng ngày:** `YYYY-MM-DD`

**Dữ liệu trả về:**
- `datetime` - Thời gian dự báo
- `condition` - Tình trạng thời tiết (sunny, rainy, cloudy...)
- `temperature` - Nhiệt độ cao nhất
- `templow` - Nhiệt độ thấp nhất
- `precipitation_probability` - Xác suất mưa (%)
- `wind_speed` - Tốc độ gió
- `wind_bearing` - Hướng gió
- `uv_index` - Chỉ số UV

**Ví dụ:**
- "Thời tiết ngày mai thế nào?"
- "Dự báo thời tiết ngày 15 tháng 1"
- "Ngày 20/01/2025 trời có mưa không?"

---

#### **2. Dự báo theo giờ (Hourly Forecast)**
Lấy dỹ báo thời tiết cho một giờ cụ thể.

**Định dạng giờ:** `HH:00` (luôn dùng 00 cho phút)

**Dữ liệu trả về:**
- `datetime` - Thời gian dự báo
- `condition` - Tình trạng thời tiết
- `temperature` - Nhiệt độ
- `apparent_temperature` - Nhiệt độ cảm nhận
- `precipitation_probability` - Xác suất mưa (%)
- `wind_speed` - Tốc độ gió
- `wind_bearing` - Hướng gió
- `cloud_coverage` - Độ phủ mây (%)
- `uv_index` - Chỉ số UV
- `humidity` - Độ ẩm (%)
- `native_visibility` - Tầm nhìn xa (km)

**Ví dụ:**
- "Thời tiết lúc 10 giờ sáng hôm nay?"
- "Dự báo thời tiết lúc 2 giờ chiều"
- "Trời có mưa vào 14h không?"

---

### 4.3. Định dạng datetime

#### **Daily (Theo ngày):**
```
Format: YYYY-MM-DD
Ví dụ:
  - 2025-01-13 (ngày 13 tháng 1 năm 2025)
  - 2025-02-15 (ngày 15 tháng 2 năm 2025)
```

#### **Hourly (Theo giờ):**
```
Format: HH:00 (luôn dùng 00 cho phút)
Ví dụ:
  - 10:00 (10 giờ sáng)
  - 14:00 (2 giờ chiều)
  - 09:00 (9 giờ sáng - có số 0 đầu)
  - 23:00 (11 giờ tối)

Lưu ý:
  - Dùng định dạng 24 giờ (00:00 đến 23:00)
  - Luôn thêm số 0 đầu cho giờ < 10
  - Phút luôn là :00
```

---

### 4.4. Sử dụng với Voice Assistant
- Expose script ra Assist trong Settings → Voice Assistants → Expose
- Trò chuyện với trợ lý AI để hỏi thời tiết

**Ví dụ câu lệnh:**
- "Thời tiết ngày mai thế nào?"
- "Dự báo thời tiết lúc 10 giờ sáng hôm nay"
- "Ngày 15 tháng 1 trời có mưa không?"
- "Nhiệt độ lúc 2 giờ chiều bao nhiêu?"

---

## 5. Kết quả trả về

### **Daily Forecast:**
```json
{
  "status": "success",
  "type": "daily",
  "forecast": {
    "datetime": "2025-01-12T12:00:00",
    "condition": "rainy",
    "temperature": 33,
    "templow": 25,
    "precipitation_probability": 55,
    "wind_speed": 11,
    "wind_bearing": "ĐĐN",
    "uv_index": 7
  }
}
```

### **Hourly Forecast:**
```json
{
  "status": "success",
  "type": "hourly",
  "forecast": {
    "datetime": "2025-01-12T10:00:00+07:00",
    "condition": "sunny",
    "temperature": 31,
    "apparent_temperature": 41,
    "precipitation_probability": 37,
    "wind_speed": 9,
    "wind_bearing": "ĐN",
    "cloud_coverage": 25,
    "uv_index": 6.7,
    "humidity": 67,
    "native_visibility": 16
  }
}
```

---

## 6. Xử lý lỗi

**Nếu không tìm thấy dữ liệu:**

Script sẽ trả về thông báo lỗi kèm danh sách ngày/giờ có sẵn:

**Daily:**
```
No forecast data found for date 2025-01-20. 
Available dates: 2025-01-12, 2025-01-13, 2025-01-14, 2025-01-15
```

**Hourly:**
```
No forecast data found for time 15:00. 
Available times: 10:00, 11:00, 12:00, 13:00, 14:00
```

---

## 7. Lưu ý

- **Weather Entity:** Có thể thay đổi entity thời tiết trong cài đặt blueprint.
- **Dữ liệu phụ thuộc vào Weather Integration:** Mỗi integration (AccuWeather, OpenWeatherMap, Met.no...) có thể cung cấp các fields khác nhau.
- **Forecast Range:** Dự báo thường có sẵn cho 7-14 ngày tới (daily) và 48 giờ tới (hourly).
- **Datetime Format:** Đảm bảo nhập đúng định dạng để tìm được kết quả.

---

## 8. Troubleshooting

**Lỗi: Forecast type must be daily or hourly**
- Type phải là `daily` hoặc `hourly` (chữ thường).

**Lỗi: Datetime is required**
- Phải cung cấp datetime theo đúng format:
  - Daily: `YYYY-MM-DD`
  - Hourly: `HH:00`

**Lỗi: No forecast data found**
- Ngày/giờ yêu cầu không có trong dữ liệu dự báo.
- Kiểm tra danh sách ngày/giờ có sẵn trong thông báo lỗi.
- Đảm bảo weather integration hoạt động bình thường.

**Weather entity không trả về dữ liệu:**
- Kiểm tra weather integration đã cài đặt và cấu hình chưa.
- Kiểm tra API key (nếu dùng AccuWeather, OpenWeatherMap...).
- Kiểm tra entity có trạng thái `available` không.

---

## 9. Changelog

**Version 20250112**
- Initial release
- Hỗ trợ dự báo daily và hourly
- Tích hợp LLM với prompts chi tiết
- Hỗ trợ Voice Assistant
- Tự động lọc và tìm kiếm forecast theo datetime
- Thông báo lỗi với danh sách ngày/giờ có sẵn
- Trả về toàn bộ dữ liệu forecast item