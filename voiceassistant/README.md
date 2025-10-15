# ESP32-S3 Voice Assistant

Dự án Voice Assistant sử dụng ESP32-S3 tích hợp với Home Assistant để tạo trợ lý giọng nói thông minh.

## 📋 Thông tin thiết bị

- **Chip**: ESP32-S3 DevKit C-1
- **Flash Size**: 16MB
- **CPU Frequency**: 240MHz
- **PSRAM**: octal mode, 80MHz
- **Framework**: ESP-IDF

## ✨ Tính năng chính

### 🎤 Voice Assistant
- Hỗ trợ wake word (từ đánh thức)
- 2 chế độ wake word:
  - **On device**: Xử lý wake word trực tiếp trên ESP32
  - **In Home Assistant**: Xử lý wake word qua Home Assistant
- Tích hợp Micro Wake Word
- Stop Continue Conversation (tắt chế độ tiếp tục hội thoại)

### 🔊 Audio
- **I2S Microphone**: INMP441
  - Sample Rate: 16kHz
  - Bits per sample: 32-bit
  - Channel: Mono (Left)
- **I2S Speaker**: MAX98357A
  - Sample Rate: 16kHz
  - Bits per sample: 32-bit
  - DAC Type: External
- Volume control (0-100%)
- Mute/unmute functionality

### 💡 LED Indicator
- LED WS2812 RGB (1 LED)
- Các trạng thái hiển thị:
  - **Idle**: Xanh lam nhấp nháy chậm
  - **Listening**: Xanh lam sáng
  - **Thinking**: Xanh lam nhấp nháy nhanh
  - **Replying**: Xanh lá nhấp nháy
  - **Error**: Đỏ nhấp nháy
  - **Muted**: Tắt
  - **Timer Finished**: Vàng nhấp nháy

### ⏲️ Timer
- Hỗ trợ timer qua voice assistant
- Chuông báo khi timer kết thúc
- Tự động tắt sau 15 phút nếu không được xử lý

### 🎵 Sound Effects
- Wake word triggered sound (`start.wav`)
- End sound (`end.flac`)
- Có thể bật/tắt các sound effects

## 🎮 Sử dụng

### Các Switch trong Home Assistant
- **Mute**: Tắt tiếng/bật tiếng trợ lý
- **Wake sound**: Bật/tắt âm thanh khi phát hiện wake word
- **End sound**: Bật/tắt âm thanh khi kết thúc
- **Stop Continue Conversation**: Dừng chế độ tiếp tục hội thoại sau khi trả lời

### Các Sensor
- **Voice Assistant Phase**: Hiển thị trạng thái hiện tại
- **Request**: Hiển thị câu lệnh voice đã nhận
- **Response**: Hiển thị phản hồi từ Home Assistant

## 📡 Kết nối WiFi

### Access Point (fallback)
- **SSID**: ESP32S3 Assistant
- **Password**: 11223344

## 🚀 Cài đặt

### Yêu cầu
1. ESPHome >= 2025.5.0( Hiện đang buil trên ver 2025.9.3)
2. Home Assistant với Voice Assistant được cấu hình
3. ESP32-S3 DevKit C-1 với 16MB flash
4. Microphone INMP441
5. Speaker amplifier MAX98357A
6. LED WS2812

### Bước cài đặt

1. **Chuẩn bị file media**:
   - Upload `start.wav` và `end.flac` vào thư mục của ESPHome

2. **Flash firmware**:
   ```bash
   esphome run voice_assistant_s3.yaml
   ```

3. **Cấu hình trong Home Assistant**:
   - Vào Settings → Devices & Services
   - Tìm thiết bị "ESP32S3 Assistant"
   - Cấu hình Voice Assistant pipeline

4. **Chọn Wake Word Engine**:
   - Vào device trong Home Assistant
   - Chọn "Wake word engine location"
   - Chọn "On device" hoặc "In Home Assistant"

5. **Tự động dừng hội thoại**:
   - nói không cần, cảm ơn...thì sẽ tự động dừng hội thoại ngay, không cần phụ thuộc vào llm, tránh tốn stt và request quote
 
## 🔧 Tùy chỉnh

### Thay đổi wake word
Chỉnh sửa section `micro_wake_word` trong file YAML:
```yaml
micro_wake_word:
  models:
    - model: hey_jarvis  # Thay đổi model tại đây
```

### Thay đổi volume mặc định
```yaml
number:
  - platform: template
    name: "Volume"
    min_value: 0
    max_value: 100
    initial_value: 50  # Thay đổi giá trị này
```

### Thay đổi màu LED
Chỉnh sửa các script `set_led_color_*` trong file YAML.

## 📊 Phases (Trạng thái)

| Phase ID | Trạng thái | Mô tả |
|----------|-----------|-------|
| 1 | Idle | Sẵn sàng, chờ wake word |
| 2 | Listening | Đang lắng nghe lệnh |
| 3 | Thinking | Đang xử lý |
| 4 | Replying | Đang phát lại phản hồi |
| 10 | Not Ready | Chưa sẵn sàng |
| 11 | Error | Lỗi |
| 12 | Muted | Đã tắt tiếng |
| 20 | Timer Finished | Timer đã kết thúc |

## 🐛 Troubleshooting

### Thiết bị không kết nối WiFi
- Kiểm tra SSID và password
- Kết nối vào AP "ESP32S3 Assistant" (password: 11223344)
- Cấu hình lại WiFi qua captive portal

### Microphone không hoạt động
- Kiểm tra kết nối I2S
- Kiểm tra log trong ESPHome
- Đảm bảo channel được set đúng (LEFT hoặc RIGHT)

### Wake word không phát hiện
- Kiểm tra "Wake word engine location" setting
- Nếu dùng "On device", đảm bảo model đã được tải
- Kiểm tra microphone hoạt động tốt
- Thử tăng volume của microphone nếu cần

### LED không sáng
- Kiểm tra kết nối GPIO10
- Kiểm tra nguồn điện cho LED
- Thử test qua button "Test Speaker"

## 📝 License

Dự án này sử dụng các component từ ESPHome.

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh! Hãy tạo issue hoặc pull request.
