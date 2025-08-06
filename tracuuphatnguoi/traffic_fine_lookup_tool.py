import asyncio
import re
import aiohttp
from bs4 import BeautifulSoup

RETRY_LIMIT = 3
API_URL = 'https://api.phatnguoi.vn/web/tra-cuu/{}/{}'  # Biển số/Loại xe

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Origin': 'https://phatnguoi.vn',
    'Connection': 'keep-alive',
    'Referer': 'https://phatnguoi.vn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site'
}


@pyscript_compile
def extract_violations_from_html(content: str) -> dict:
    soup = BeautifulSoup(content, 'html.parser')

    # Kiểm tra trường hợp không có vi phạm
    no_violation = soup.find(string="Chúc mừng bạn không có lỗi vi phạm")
    if no_violation:
        return dict(status='success', message='Không có vi phạm giao thông', detail='')

    # Tìm các bảng chứa thông tin chi tiết vi phạm
    violation_tables = soup.find_all('table')
    violations = []

    for table in violation_tables:
        violation = {
            'Biển kiểm soát': '',
            'Màu biển': '',
            'Loại phương tiện': '',
            'Thời gian vi phạm': '',
            'Địa điểm vi phạm': '',
            'Hành vi vi phạm': '',
            'Trạng thái': '',
            'Đơn vị phát hiện vi phạm': '',
            'Nơi giải quyết vụ việc': []
        }

        rows = table.find_all('tr')
        for row in rows:
            cells = row.find_all('td')
            if len(cells) == 2:
                key = cells[0].text.strip().rstrip(':')
                value = cells[1].text.strip()

                if key in violation:
                    if key == 'Nơi giải quyết vụ việc':
                        lines = value.split('\n')
                        for line in lines:
                            if line.strip():
                                violation[key].append(line.strip())
                    elif key == 'Hành vi vi phạm':
                        match = re.search(r'(.+?)Xem mức phạt', value)
                        if match:
                            violation[key] = match.group(1).strip()
                        else:
                            violation[key] = value
                    else:
                        violation[key] = value

        if violation['Biển kiểm soát']:  # Chỉ thêm vi phạm nếu có biển số
            violations.append(violation)

    if not violations:
        return dict(status='success', message='Không có vi phạm giao thông', detail='')

    return dict(status='success', message=f'Có {len(violations)} vi phạm giao thông', detail=violations)


@pyscript_compile
async def check_license_plate(license_plate: str, vehicle_type: int, retry_count: int = 1) -> dict:
    url = API_URL.format(license_plate, vehicle_type)

    try:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url, headers=HEADERS, ssl=False) as response:
                    if response.status != 200:
                        return dict(error=f'API response error: {response.status}')

                    text_content = await response.text()
                    return extract_violations_from_html(text_content)

            except asyncio.TimeoutError:
                if retry_count < RETRY_LIMIT:
                    await asyncio.sleep(15)
                    return await check_license_plate(license_plate, vehicle_type, retry_count + 1)
                else:
                    return dict(error=f'Timeout error after {retry_count} attempts')
            except aiohttp.ClientError:
                if retry_count < RETRY_LIMIT:
                    await asyncio.sleep(15)
                    return await check_license_plate(license_plate, vehicle_type, retry_count + 1)
                else:
                    return dict(error=f'Client error after {retry_count} attempts')
    except Exception as error:
        if retry_count < RETRY_LIMIT:
            await asyncio.sleep(15)
            return await check_license_plate(license_plate, vehicle_type, retry_count + 1)
        else:
            return dict(error=f'Unexpected error after {retry_count} attempts: {error}')


@service(supports_response='only')
async def traffic_fine_lookup_tool(license_plate: str, vehicle_type: int) -> dict:
    """
    yaml
    name: Traffic Fine Lookup Tool
    description: Tool to check Vietnam traffic fines.
    fields:
      license_plate:
        name: License Plate
        description: The license plate number of vehicle.
        example: 29A99999
        required: true
        selector:
          text: {}
      vehicle_type:
        name: Vehicle Type
        description: The type of vehicle.
        example: '"1"'
        required: true
        selector:
          select:
            options:
              - label: Ô tô
                value: "1"
              - label: Xe máy
                value: "2"
              - label: Xe đạp điện
                value: "3"
        default: "1"
    """
    try:
        license_plate = str(license_plate).upper()
        vehicle_type = int(vehicle_type)

        if vehicle_type == 1:
            pattern = r'^\d{2}[A-Z]{1,2}\d{4,5}$'
        else:
            pattern = r'^\d{2}[A-Z1-9]{2}\d{4,5}$'
        if not (license_plate and re.match(pattern, license_plate)):
            return dict(error='The license plate number is invalid')

        if vehicle_type not in [1, 2, 3]:
            return dict(error='The type of vehicle is invalid')

        return await check_license_plate(license_plate, vehicle_type)
    except Exception as error:
        return dict(error=f'An unexpected error occurred during processing: {error}')
