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

- Trò chuyện với tác nhân AI để yêu cầu thêm công việc vào danh sách, lấy tất cả danh sách công việc, lấy danh sách công việc đã hoàn thành, chưa hoàn thành, xóa công việc, sửa công việc...
