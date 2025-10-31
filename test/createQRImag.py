import qrcode
from PIL import Image

def create_qrcode(url, logo_path):
    # 生成二维码底座
    qr = qrcode.QRCode(
        error_correction=qrcode.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")
    qr_w, qr_h = qr_img.size  # 二维码尺寸

    # 处理Logo（缩放+加边框）
    logo = Image.open(logo_path).convert("RGBA")
    # 缩放Logo为二维码的1/4（避免遮挡过多）
    scale = 4
    logo_max_w = qr_w // scale
    logo_max_h = qr_h // scale
    logo.thumbnail((logo_max_w, logo_max_h), Image.Resampling.LANCZOS)  # 高画质缩放
    logo_w, logo_h = logo.size

    # 给Logo加白色边框（可选，增强效果）
    border_size = 4  # 边框宽度（像素）
    icon_with_border = Image.new(
        "RGBA", 
        (logo_w + 2*border_size, logo_h + 2*border_size),  # 宽高=Logo+2*边框
        (255, 255, 255, 255)  # 白色边框（最后一个255是不透明度）
    )
    # 把Logo贴在边框中心（边框内边距=border_size）
    icon_with_border.paste(logo, (border_size, border_size), logo)

    # 关键：计算居中粘贴的坐标
    icon_total_w, icon_total_h = icon_with_border.size  # 带边框的总尺寸
    paste_x = (qr_w - icon_total_w) // 2  # x方向居中
    paste_y = (qr_h - icon_total_h) // 2  # y方向居中

    # 粘贴图标到二维码中心
    qr_img.paste(icon_with_border, (paste_x, paste_y), icon_with_border)

    # 保存
    qr_img.save("qrcode_with_logo.png", quality=100)
    print("生成成功，图标已居中")

if __name__ == '__main__':
    create_qrcode("http://127.0.0.1:8000.com", "logo.jpg")  # 确保logo.jpg存在