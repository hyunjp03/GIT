import os

import cv2
from ament_index_python.packages import get_package_share_directory


def main():
    save_path = os.path.join(
        get_package_share_directory('img_data_pkg'), 'images', 'sample.jpg')

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print('웹캠을 열 수 없습니다. /dev/video0 연결을 확인하세요.')
        return

    cv2.imwrite(save_path, frame)
    print(f'사진 저장 완료: {save_path}')


if __name__ == '__main__':
    main()
