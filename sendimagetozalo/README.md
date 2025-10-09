# Hướng dẫn sử dụng Blueprint gửi ảnh qua Zalo cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn gửi ảnh từ camera hoặc từ đường dẫn ảnh tới Zalo thông qua tích hợp Zalo Bot trên Home Assistant. Có 2 kiểu gửi ảnh:
- Gửi ảnh từ snapshot camera Home Assistant.
- Gửi ảnh từ đường dẫn URL Go2rtc hoặc Url Snapshot của camera

## 2. Yêu cầu
- Đã cài đặt Zalo Bot qua HACS và cấu hình tài khoản Zalo Bot.
- Đã cài đặt Home Assistant phiên bản >= 2024.10.0.
- Đã có các camera cần sử dụng hoặc biết URL ảnh cần gửi.

## 3. Cài đặt

Nhấn vào các nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn

Chú ý chỉ chọn 1 trong 2 cách thôi tránh loạn

1. Gửi ảnh từ đường dẫn URL Go2rtc hoặc Url Snapshot của camera

[![Import Voice Traffic Fine Lookup Tool Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/sendimagetozalo/send_image_to_zalo.yaml)

2. Gửi ảnh từ snapshot camera Home Assistant.

[![Import Traffic Fine Notification Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/sendimagetozalo/send_snapshot_to_zalo.yaml)

## 4. Hướng dẫn sử dụng từng kiểu gửi ảnh

### 4.1. Gửi ảnh từ snapshot camera Home Assistant
1. Tạo script mới từ Blueprint vừa import.
2. Điền các thông tin cấu hình:
   - **Account**: Số điện thoại tài khoản Zalo Bot gửi ảnh.
   - **Thread ID**: ID cuộc trò chuyện hoặc nhóm cần gửi.
   - **Type of Receiver**: Chọn User hoặc Group.
   - **TTL**: Thời gian tự thu hồi tin nhắn (ms, mặc định 0).
   - **Snapshot Delay**: Thời gian chờ sau khi chụp ảnh tránh tình trạng chưa chụp xong lưu file(giây, mặc định 3).
3. Điền Prompt settings for the LLM
   - Sửa **Prompt Camera Entity Prompt** theo mẫu có sẵn
4. Khai báo shell_command trong configuration.yaml để kiểm tra và xóa file snapshot sau khi gửi:
   ```yaml
   shell_command:
     check_zalo_snapshot: test -f /config/www/zalo_snapshot.jpg && echo "exists" || echo "missing"
     delete_zalo_snapshot: rm /config/www/zalo_snapshot.jpg
   ```
   - Đảm bảo đã có các file script Python tương ứng trong thư mục `/config/scripts/`.
   - Nếu dùng môi trường khác, chỉnh lại đường dẫn cho phù hợp.

### 4.2. Gửi ảnh từ đường dẫn URL (go2rtc)
1. Tạo script mới từ Blueprint gửi ảnh qua URL.
2. Điền các thông tin cấu hình:
   - **Account**: Số điện thoại tài khoản Zalo Bot gửi ảnh.
   - **Thread ID**: ID cuộc trò chuyện hoặc nhóm cần gửi.
   - **Type of Receiver**: Chọn User hoặc Group.
   - **TTL**: Thời gian tự thu hồi tin nhắn (ms, mặc định 0).
3. Điền Prompt settings for the LLM
   - Sửa **Image Path Prompt** theo mẫu có sẵn

## 5. Cách sử dụng
- Bật Trợ lý giọng nói cho Script để LLM có thể nhận diện công cụ
- Chat với bot qua zalo kêu gửi ảnh từ camera xxx

## 6. Lưu ý
- Nếu gửi ảnh từ camera, cần đảm bảo camera hoạt động.
- Nếu gửi ảnh từ URL Snapshot, cần nhập đúng đường dẫn ảnh hợp lệ (ưu tiên lấy từ go2rtc).
- Kết quả gửi sẽ trả về cho LLM hoặc workflow, không hiện thông báo trên giao diện Home Assistant.
- Nếu gửi ảnh bằng Snapshot thì tăng giảm thời gian delay tùy theo thực tế bạn dùng, chậm quá sẽ gây ra lỗi chưa lưu file xong đã chạy gửi ảnh.

## 7. Ưu nhược điểm của 2 cách
- Qua Url: không cần phải thực hiện snapshot không cần kiểm tra file, gửi thẳng qua zalo nên tốc độ nhanh và không có lỗi 
- Qua snapshot entity: Phải snapshot nên có thể sẽ hơi lâu, cần kiểm tra file có được lưu hay chưa và gửi xong phải xóa file tránh rò rỉ

## 8. Hỗ trợ
Nếu gặp lỗi hoặc cần hỗ trợ, liên hệ tác giả qua Github hoặc Zalo.
