# Hướng dẫn sử dụng Blueprint Tìm Kiếm và Phát Nhạc Zing MP3 cho Home Assistant

## 1. Giới thiệu
Blueprint này giúp bạn tìm kiếm và phát nhạc từ Zing MP3 trong Home Assistant với tích hợp LLM (AI). Hỗ trợ điều khiển bằng giọng nói, tìm kiếm bài hát, playlist, ca sĩ, album và điều khiển phát nhạc.

## 2. Yêu cầu
- Đã cài đặt Home Assistant phiên bản >= 2025.10.0.
- Đã cài đặt và cấu hình tích hợp **zingmp3_player** (custom component).
- Có entity `media_player.zingmp3_player` hoạt động.
- Đã cấu hình LLM (AI) nếu muốn sử dụng các prompt thông minh.
- Có media player (speaker) để phát nhạc (Chromecast, Sonos, v.v.).

## 3. Cài đặt
Nhấn vào nút dưới đây để import blueprint trực tiếp vào Home Assistant của bạn:

[![Import Zing MP3 Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https://raw.githubusercontent.com/smarthomeblack/home-assistant/refs/heads/main/playmusic/music_zingmp3.yaml)

## 4. Hướng dẫn sử dụng

### 4.1. Cấu hình
- Sau khi import blueprint, tạo script từ blueprint.
- Vào phần **Music Settings** để cấu hình:
  - **Entity ID:** Chọn media_player của Zing MP3 (mặc định: `media_player.zingmp3_player`)
  - **Limit:** Số lượng kết quả tìm kiếm trả về (1-20, mặc định: 5)
- Chỉnh sửa phần **Prompt settings** để tùy chỉnh các prompt cho LLM.
- **Quan trọng:** Expose script ra Assist trong Settings → Voice Assistants → Expose.

### 4.2. Các chức năng

#### **1. Tìm kiếm nhạc (Search)**
Tìm kiếm bài hát, playlist, ca sĩ, album trên Zing MP3.

**Ví dụ:**
- "Tìm bài hát của Sơn Tùng M-TP"
- "Search for playlist nhạc trẻ"
- "Tìm album của Đàm Vĩnh Hưng"

**Kết quả:**
- LLM sẽ chỉ thông báo số lượng kết quả tìm được
- Chỉ đọc danh sách đầy đủ khi người dùng yêu cầu

#### **2. Phát nhạc (Play)**
Phát bài hát hoặc playlist từ kết quả tìm kiếm.

**Lưu ý:**
- Nếu chưa có `media_content_id`, LLM sẽ tự động tìm kiếm trước, sau đó phát bài đầu tiên tìm được
- Nếu đã có `media_content_id` từ lần tìm kiếm trước, có thể phát trực tiếp

**Ví dụ:**
- "Phát bài hát Em của ngày hôm qua"
- "Play playlist nhạc trẻ"
- "Phát bài đầu tiên vừa tìm"

**Cài đặt mặc định khi phát:**
- **Shuffle:** `true` (phát ngẫu nhiên)
- **Repeat:** `off` (không lặp lại)

#### **3. Điều khiển phát nhạc**

##### **Tạm dừng (Pause)**
- "Tạm dừng nhạc"
- "Pause music"
- "Dừng lại"

##### **Tiếp tục (Resume)**
- "Tiếp tục phát nhạc"
- "Resume music"
- "Phát tiếp"

##### **Bài tiếp theo (Next)**
- "Bài tiếp theo"
- "Next track"
- "Skip"

##### **Bài trước (Previous)**
- "Bài trước"
- "Previous track"
- "Quay lại"

##### **Bật/tắt Shuffle (Random)**
- "Bật random"
- "Tắt shuffle"
- "Shuffle on/off"

##### **Thay đổi Repeat Mode**
- "Bật lặp lại"
- "Repeat all"
- "Lặp lại một bài"

**Lưu ý:** Các điều khiển này hoạt động độc lập, không cần tìm kiếm hay `media_content_id`.

### 4.3. Sử dụng với Voice Assistant
- Expose script ra Assist trong Settings → Voice Assistants → Expose
- Trò chuyện với trợ lý AI để tìm kiếm và phát nhạc

**Ví dụ câu lệnh:**
- "Tìm bài hát Em của ngày hôm qua"
- "Phát playlist nhạc trẻ"
- "Tạm dừng nhạc"
- "Bài tiếp theo"
- "Bật random"

## 5. Lưu ý

### 5.1. Entity ID
- Đảm bảo entity_id đúng format `media_player.zingmp3_player`
- `media_player.zingmp3_player` là controller, KHÔNG phải speaker
- Cần chọn speaker riêng (Chromecast, Sonos, v.v.) trong phần **Source**

### 5.2. Tìm kiếm và Phát
- Khi yêu cầu phát mà chưa có `media_content_id`, LLM sẽ tự động tìm kiếm trước
- Kết quả tìm kiếm được lưu trong sensor `sensor.zingmp3_player_extra`
- LLM chỉ đọc số lượng kết quả, không đọc danh sách đầy đủ trừ khi được yêu cầu

### 5.3. Playlist
- Zing MP3 không hỗ trợ phát playlist trực tiếp theo ID
- Blueprint tự động lấy bài đầu tiên trong playlist và phát
- Nếu shuffle = true, sẽ phát bài ngẫu nhiên trong playlist

### 5.4. Prompts
- Có thể tùy chỉnh các prompt trong blueprint để phù hợp với LLM model của bạn
- Prompt mặc định hỗ trợ tiếng Việt và tiếng Anh

## 6. Troubleshooting

**Lỗi: Invalid entity_id**
- Kiểm tra entity_id có bắt đầu bằng `media_player.` không
- Kiểm tra entity có tồn tại trong Home Assistant không
- Đảm bảo tích hợp zingmp3_player đã được cài đặt và cấu hình

**Lỗi: Action zingmp3_player.call_method not found**
- Kiểm tra custom component zingmp3_player đã được cài đặt đúng chưa
- Restart Home Assistant sau khi cài đặt component

**Lỗi: Cannot play without media_content_id**
- LLM cần tìm kiếm trước khi phát
- Kiểm tra xem LLM có tự động tìm kiếm không
- Thử yêu cầu rõ ràng: "Tìm và phát bài hát X"

**Không tìm thấy kết quả:**
- Kiểm tra kết nối internet
- Kiểm tra tích hợp zingmp3_player có hoạt động không
- Thử tìm kiếm với từ khóa khác

**Nhạc không phát:**
- Kiểm tra speaker (source) đã được chọn đúng chưa
- Kiểm tra speaker có đang hoạt động không
- Kiểm tra `media_player.zingmp3_player` không được chọn làm speaker

**Sensor không cập nhật:**
- Kiểm tra sensor `sensor.zingmp3_player_extra` có tồn tại không
- Kiểm tra cấu hình tích hợp có bật extra sensor không

## 7. Cấu trúc dữ liệu

### Search Results
Kết quả tìm kiếm được lưu trong `sensor.zingmp3_player_extra` với các thuộc tính:
- `search`: Danh sách kết quả tìm kiếm (JSON array)
- `tracks`: Danh sách bài hát đang phát
- `total_tracks`: Tổng số bài hát trong playlist/album

Mỗi kết quả tìm kiếm chứa:
- `media_content_id`: ID của bài hát/playlist
- `media_content_type`: Loại (`songs` hoặc `playlists`)
- `title`: Tên bài hát/playlist
- `artist`: Tên ca sĩ
- `albumName`: Tên album
- `images`: URL ảnh bìa

## 8. Changelog

**Version 2026.2.8**
- Initial release
- Hỗ trợ tìm kiếm và phát nhạc từ Zing MP3
- Tích hợp LLM với prompts chi tiết
- Hỗ trợ Voice Assistant
- Điều khiển phát nhạc: pause, resume, next, previous
- Điều khiển shuffle và repeat độc lập
- Tự động tìm kiếm khi phát mà chưa có media_content_id
- Hỗ trợ playlist với tự động lấy bài đầu tiên
