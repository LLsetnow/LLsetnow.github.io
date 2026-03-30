import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["os", "sys", "fitz", "PIL", "pathlib", "io"],
    "include_files": [],
    "excludes": [],
    "optimize": 2,
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PDFtoJPG",
    version="1.0",
    description="将PDF文件逐页转换为JPG图像",
    options={"build_exe": build_exe_options},
    executables=[
        Executable(
            script="pdf_to_jpg.py",
            base=base,
            target_name="PDF转JPG工具.exe",
            icon=None,
        )
    ],
)
