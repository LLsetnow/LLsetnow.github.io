import fitz  # PyMuPDF
import os
import sys
from PIL import Image
from pathlib import Path
import io


def pdf_to_images(pdf_path):
    """
    将PDF文件逐页转换为JPG图像
    """
    try:
        pdf_name = Path(pdf_path).stem
        output_dir = Path(pdf_path).parent
        
        print(f"正在处理: {pdf_path}")
        
        # 打开PDF文件
        doc = fitz.open(pdf_path)
        
        # 逐页转换
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            
            # 设置缩放比例（提高清晰度）
            zoom = 2.0
            mat = fitz.Matrix(zoom, zoom)
            
            # 渲染页面为图像
            pix = page.get_pixmap(matrix=mat)
            
            # 转换为PIL Image并保存为JPG
            img_data = pix.tobytes("ppm")
            img = Image.open(io.BytesIO(img_data))
            
            # 保存为JPG
            output_path = output_dir / f"{pdf_name}_page_{page_num + 1}.jpg"
            img.save(output_path, "JPEG", quality=95)
            print(f"  ✓ 第 {page_num + 1} 页已保存")
        
        doc.close()
        print(f"✓ 完成！共转换 {len(doc)} 页")
        
    except Exception as e:
        print(f"✗ 处理失败: {e}")


if __name__ == "__main__":
    # 获取拖入的文件路径
    if len(sys.argv) > 1:
        pdf_files = sys.argv[1:]
    else:
        # 如果没有拖入文件，读取当前目录下的PDF文件
        current_dir = Path.cwd()
        pdf_files = list(current_dir.glob("*.pdf"))
        
        if not pdf_files:
            print("未找到PDF文件，请拖入PDF文件或将其放在当前目录下")
            input("按任意键退出...")
            sys.exit(1)
    
    # 处理每个PDF文件
    for pdf_file in pdf_files:
        if Path(pdf_file).suffix.lower() == ".pdf":
            pdf_to_images(pdf_file)
            print("-" * 50)
    
    print("所有文件处理完成！")
    input("按任意键退出...")
