# Hướng dẫn sử dụng Blueprint Gửi Tổng Hợp Buổi Sáng qua Zalo

## 1. Giới thiệu
Blueprint này giúp bạn tự động gửi thông báo tổng hợp buổi sáng qua Zalo với thông tin thời tiết, lịch làm việc, danh sách công việc cần làm, và tin nhắn cá nhân hóa được tạo bởi AI. Blueprint hoàn hảo để bắt đầu ngày mới với đầy đủ thông tin quan trọng.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2023.8.0.
- Đã cài đặt tích hợp Zalo Bot và cấu hình xong.
- Đã cấu hình Conversation Agent (AI) như OpenAI, Google Generative AI, hoặc AI khác.
- Tùy chọn: Entity Weather (thời tiết).
- Tùy chọn: Entity Calendar (lịch).
- Tùy chọn: Entity To-do (danh sách công việc).

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=YOUR_BLUEPRINT_URL_HERE)

Hoặc copy file `send_morning_summary_to_zalo.yaml` vào thư mục `blueprints/automation/` trong Home Assistant.

## 4. Hướng dẫn sử dụng

### 4.1. Cấu hình

Sau khi import blueprint, tạo automation từ blueprint với các thông số sau:

#### **Thông số bắt buộc:**

- **Notification Time** - Giờ gửi thông báo hàng ngày
  - Định dạng: `HH:MM:SS`
  - Ví dụ: `06:15:00` (6 giờ 15 phút sáng)
  - Mặc định: `06:15:00`

- **Zalo Thread ID** - ID của cuộc trò chuyện Zalo
  - Lấy từ Zalo Bot integration
  - Ví dụ: `123456789`

- **Zalo Account Selection** - Định danh tài khoản Zalo
  - Lấy từ cấu hình Zalo Bot

- **Conversation Agent** - AI model để tạo tin nhắn
  - Ví dụ: `conversation.gpt_4o_mini`
  - Ví dụ: `conversation.google_generative_ai`

#### **Thông số tùy chọn:**

- **Calendar** - Các entity calendar để lấy sự kiện
  - Hỗ trợ nhiều calendar
  - Ví dụ: `calendar.personal`, `calendar.work`

- **Calendar Event Timing** - Thời gian xem trước sự kiện
  - Định dạng: duration (giờ:phút:giây)
  - Mặc định: `18:00:00` (18 giờ)

- **To-do List** - Các entity to-do để lấy công việc
  - Hỗ trợ nhiều to-do list
  - Ví dụ: `todo.daily_tasks`, `todo.shopping`

- **Weather Entity** - Entity thời tiết
  - Ví dụ: `weather.home`, `weather.accuweather`

- **Custom Footer Text** - Văn bản tùy chỉnh ở cuối tin nhắn
  - Có thể để trống
  - Hỗ trợ nhiều dòng
  - Ví dụ:
    ```
    ---
    💡 Tip: Nhớ uống đủ nước!
    🏃 Đừng quên tập thể dục buổi sáng
    ```

- **Zalo Message Type** - Loại tin nhắn
  - `0` = Cá nhân (Personal)
  - `1` = Nhóm (Group)
  - Mặc định: `1`

- **Zalo Message TTL** - Thời gian tự động xóa tin nhắn
  - Đơn vị: milliseconds
  - `0` = Không tự động xóa
  - Ví dụ: `3600000` (1 giờ)
  - Mặc định: `0`

- **Conversation Agent Prompt** - Prompt cho AI
  - Tùy chỉnh cách AI tạo tin nhắn
  - Mặc định: Prompt tiếng Việt thân thiện

---

### 4.2. Cách hoạt động

Blueprint thực hiện các bước sau:

1. **Kích hoạt** vào thời gian đã cấu hình
2. **Lấy dữ liệu thời tiết** từ weather entity (dự báo theo giờ)
3. **Lấy sự kiện lịch** từ các calendar entity (trong khoảng thời gian đã cấu hình)
4. **Lấy công việc cần làm** từ các to-do entity (trạng thái: cần làm)
5. **Tạo văn bản tổng hợp** bao gồm:
   - Thời gian hiện tại
   - Dự báo thời tiết (nhiệt độ, điều kiện, xác suất mưa)
   - Danh sách sự kiện lịch
   - Danh sách công việc cần làm
   - Văn bản tùy chỉnh (nếu có)
   - Prompt cho AI
6. **Gửi cho Conversation Agent** để AI xử lý và tạo tin nhắn thân thiện
7. **Gửi tin nhắn** qua Zalo Bot

---

### 4.3. Ví dụ tin nhắn mẫu

```
🌅 Chào buổi sáng!

⏰ Thứ Hai 15. Tháng 1 06:15

☀️ Thời tiết hôm nay: Sunny (24°C, 10% khả năng mưa)
Trời nắng đẹp, bạn nên mặc áo thun và quần short nhé!

📅 Lịch hôm nay:
- 09:00: Họp team standup
- 14:30: Gặp khách hàng tại văn phòng

✅ Công việc cần làm:
- Hoàn thành báo cáo tuần (Hạn: hôm nay)
- Gửi email cho đối tác
- Mua sắm cho tuần này

💪 Chúc bạn một ngày làm việc hiệu quả!
```

---

### 4.4. Tùy chỉnh nâng cao

#### **Tùy chỉnh Prompt cho AI:**

Bạn có thể thay đổi prompt mặc định để AI tạo tin nhắn theo phong cách riêng:

```
Hãy tạo tin nhắn tổng hợp buổi sáng động viên bằng tiếng Việt.
- Sử dụng emoji để làm tin nhắn sinh động
- Tập trung vào tips năng suất
- Giữ tone chuyên nghiệp nhưng thân thiện
- Ưu tiên các công việc khẩn cấp trước
- Thêm quotes truyền cảm hứng
```

#### **Tùy chỉnh Custom Footer:**

```
---
📚 Quote của ngày: "Thành công là tổng của những nỗ lực nhỏ lặp đi lặp lại mỗi ngày."
💧 Nhắc nhở: Uống đủ 2 lít nước mỗi ngày
🧘 Đừng quên: 10 phút thiền buổi sáng
```

---

## 5. Xử lý lỗi

### **Tin nhắn không gửi được:**

Kiểm tra:
- Zalo Bot integration đã hoạt động chưa
- Thread ID có đúng không
- Account Selection có hợp lệ không
- Kết nối mạng có ổn định không

### **AI không tạo tin nhắn hay tin nhắn quá chung chung:**

Thử:
- Thêm chi tiết hơn vào prompt
- Đảm bảo các entity (calendar, weather, to-do) đã cấu hình đúng
- Kiểm tra các entity có dữ liệu thực tế không
- Thử với conversation agent khác

### **Custom Footer không xuất hiện:**

Đảm bảo:
- Trường custom footer không để trống
- Có nội dung văn bản thực sự (không chỉ khoảng trắng)
- Conversation agent nhận được đầy đủ context

### **Weather/Calendar/To-do không hiển thị:**

Kiểm tra:
- Entity đã được chọn trong cấu hình
- Entity có trạng thái `available`
- Entity có dữ liệu thực tế
- Integration tương ứng hoạt động bình thường

---

## 7. Lưu ý

- **Múi giờ:** Thời gian sẽ theo múi giờ được cấu hình trong Home Assistant.
- **AI Model:** Chất lượng tin nhắn phụ thuộc vào conversation agent bạn chọn.
- **Zalo Bot:** Cần cấu hình đúng Zalo Bot integration trước khi sử dụng.
- **Weather Data:** Dữ liệu thời tiết phụ thuộc vào weather integration (AccuWeather, OpenWeatherMap, etc.).
- **Calendar Range:** Thời gian xem trước mặc định là 18 giờ, có thể điều chỉnh.
- **Privacy:** Blueprint này không chia sẻ dữ liệu ra bên ngoài, chỉ sử dụng conversation agent đã cấu hình.

---

## 8. Blueprint liên quan

- [Weather Forecast](../weatherforecast/) - Lấy dự báo thời tiết chi tiết
- [Send Image to Zalo](../sendimagetozalo/) - Gửi hình ảnh qua Zalo

---

## 9. Changelog

**Version 20250115**
- Initial release
- Hỗ trợ weather forecast, calendar, to-do
- Tích hợp conversation agent (AI)
- Tùy chỉnh custom footer
- Hỗ trợ cả tin nhắn cá nhân và nhóm
- Hỗ trợ TTL (tự động xóa tin nhắn)
- Tùy chỉnh prompt cho AI
- Gửi qua Zalo Bot

---

## 10. Tác giả

Tạo bởi **smarthomeblack**

---

*Được làm với ❤️ cho cộng đồng Home Assistant Việt Nam*