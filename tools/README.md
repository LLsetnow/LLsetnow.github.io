# PDF转JPG工具

## 功能
将PDF文件逐页转换为高质量JPG图像，支持拖入PDF文件自动转换。

## 使用方法

### 方式一：打包为EXE使用
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   pip install cx_Freeze
   ```

2. 打包EXE：
   ```bash
   python setup.py build
   ```

3. 使用：
   - 将生成的 `PDF转JPG工具.exe` 放在任意文件夹
   - 拖入PDF文件到EXE图标上即可自动转换
   - 或双击EXE，自动转换当前目录下的PDF文件

### 方式二：直接使用Python脚本
1. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

2. 运行：
   ```bash
   python pdf_to_jpg.py
   ```

## 输出
- 转换后的JPG图像保存在PDF文件所在目录
- 文件名格式：`原文件名_page_页码.jpg`
- 图像质量：95%（可调整）

## 依赖
- PyMuPDF：PDF解析
- Pillow：图像处理
