# 🏠 Home Assistant Blueprints Collection

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.10%2B-blue.svg)](https://www.home-assistant.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Language](https://img.shields.io/badge/Language-Vietnamese%20%26%20English-orange.svg)]()

Bộ sưu tập các Blueprint thông minh cho Home Assistant với tích hợp LLM/AI, hỗ trợ Voice Assistant và điều khiển bằng ngôn ngữ tự nhiên.

---

## 📋 Danh Sách Blueprints

### 🤖 [File Content Analyzer](./filecontent/)
**Phân tích nội dung file với AI**

**Tính năng:**
- ✨ Phân tích và trích xuất thông tin từ ảnh, video, audio, document
- 📸 Hỗ trợ camera entity và file path
- 🎯 Tùy chỉnh system prompt cho AI Task
- 🗣️ Tích hợp Voice Assistant
- 🌐 Hỗ trợ đa ngôn ngữ
- 🔍 OCR - trích xuất văn bản
- 👁️ Nhận diện đối tượng trong ảnh/video

[📖 Xem chi tiết →](./filecontent/)

---

### 📝 [To-Do List Manager](./todolist/)
**Quản lý công việc thông minh**

**Tính năng:**
- ✅ Quản lý danh sách công việc bằng giọng nói
- 🔄 CRUD operations đầy đủ: thêm, xem, sửa, xóa
- ⚠️ Xác nhận an toàn cho thao tác nguy hiểm
- 📅 Hỗ trợ due date và due datetime
- 🎯 Lọc theo trạng thái (completed, needs_action)
- 🇻🇳 Hỗ trợ tiếng Việt đầy đủ
- 🔔 Reminder và thông báo

[📖 Xem chi tiết →](./todolist/)

---

### 🌀 [Fan Control](./fancontrol/)
**Điều khiển quạt thông minh**

**Tính năng:**
- 🎚️ Điều chỉnh tốc độ quạt (0-100%)
- ⬆️ Tăng tốc độ theo bước
- ⬇️ Giảm tốc độ theo bước
- 🔄 Bật/tắt chế độ xoay (oscillation)
- 🗣️ Điều khiển bằng giọng nói
- ⚙️ Tùy chỉnh percentage_step
- 🎯 Hỗ trợ nhiều quạt cùng lúc

[📖 Xem chi tiết →](./fancontrol/)

---

### ❄️ [Climate Control](./climatecontrol/)
**Điều khiển điều hòa thông minh**

**Tính năng:**
- 🌡️ Điều chỉnh chế độ hoạt động (heat, cool, auto, dry, fan_only)
- 🔄 Điều khiển xoay gió (vertical, horizontal, both)
- 🌬️ Điều chỉnh tốc độ quạt (low, medium, high, auto)
- ⚡ Chế độ Turbo - công suất tối đa
- 🌿 Chế độ Econo - tiết kiệm điện
- 🗣️ Điều khiển bằng giọng nói
- 🔧 Hỗ trợ Tasmota IR HVAC
- **Weather Integration:** Yeu cau cho Weather Forecast (AccuWeather, OpenWeatherMap, Met.no...)

[📖 Xem chi tiết →](./climatecontrol/)

---

### ☁️ [Weather Forecast](./weatherforecast/)
**Dự báo thời tiết thông minh**

**Tính năng:**
- 🌡️ Dự báo theo ngày (daily) và theo giờ (hourly)
- 📅 Tìm kiếm dự báo theo datetime cụ thể
- 🌧️ Thông tin đầy đủ: nhiệt độ, mưa, gió, UV...
- 🗣️ Hỏi thời tiết bằng giọng nói
- ⚠️ Thông báo khi không tìm thấy dữ liệu
- 📊 List ngày/giờ có sẵn khi lỗi
- 🌍 Hỗ trợ nhiều weather integration

[📖 Xem chi tiết →](./weatherforecast/)

---
### 📱 [Send Image to Zalo](./sendimagetozalo/)
**Gửi ảnh qua Zalo Bot**

**Tính năng:**
- 📤 Gửi ảnh từ file path
- 📸 Chụp ảnh từ camera và gửi tự động
- ⏱️ Cấu hình delay sau khi chụp
- 👥 Hỗ trợ gửi cho user và group
- 🔐 Tự động xóa file sau khi gửi
- ⏰ TTL - Tự động thu hồi tin nhắn
- 🗣️ Tích hợp Voice Assistant

[📖 Xem chi tiết →](./sendimagetozalo/)

---

### 🚗 [Traffic Fine Lookup](./tracuuphatnguoi/)
**Tra cứu phạt nguội giao thông**

**Tính năng:**
- 🔍 Tra cứu phạt nguội theo biển số xe
- 📊 Phân tích kết quả bằng AI
- 📲 Thông báo tự động qua Zalo
- 🗣️ Hỏi bằng giọng nói
- 🇻🇳 API Cảnh sát giao thông Việt Nam
- ⏰ Tự động tra cứu định kỳ
- 💾 Lưu lịch sử tra cứu

[📖 Xem chi tiết →](./tracuuphatnguoi/)

---

## 🚀 Yêu Cầu Hệ Thống

- **Home Assistant:** >= 2024.10.0
- **AI Integration:** OpenAI, Google Generative AI, hoặc tương thích
- **Voice Assistant:** Home Assistant Assist (tùy chọn)
- **Zalo Bot:** Yêu cầu cho các blueprint Send Image và Traffic Fine
- **Tasmota IR HVAC:** Yêu cầu cho chế độ Turbo/Econo của Climate Control

---

## 📚 Hướng Dẫn

Mỗi blueprint có file README.md riêng với hướng dẫn chi tiết về:
- Cách cài đặt và cấu hình
- Các tham số và prompt settings
- Ví dụ sử dụng cụ thể
- Troubleshooting

Click vào link "Xem chi tiết" ở mỗi blueprint để xem thêm thông tin.

---

## 🤝 Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp! Vui lòng:
1. Fork repository
2. Tạo feature branch
3. Commit changes
4. Mở Pull Request

**Báo lỗi:** [GitHub Issues](https://github.com/smarthomeblack/home-assistant/issues)

---

## 📝 License

MIT License - xem file [LICENSE](LICENSE) để biết thêm chi tiết.

---

## 🌟 Credits

**Author:** smarthomeblack, luuquangvu

**Inspired by:** Home Assistant Community & Vietnamese Smart Home Groups

---

## 👍 Support

Nếu thấy hữu ích, đừng quên ⭐ Star repository này!

- **GitHub:** [@smarthomeblack](https://github.com/smarthomeblack)
- **Issues:** [GitHub Issues](https://github.com/smarthomeblack/home-assistant/issues)

---

**Version:** 2.0 | **Cập nhật:** 2025-01-12
