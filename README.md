# OS
Mac OS

# Install Unzip Tools

1. 先使用brew安裝unrar套件以確保系統有該套件的路徑
```
brew install carlocab/personal/unrar
```

2. 安裝Python所需套件
```
python install -r requirement.txt
```

# 使用
啟用unzip.py，並在後面附上所需解壓縮的路徑(因本專案主旨在於解壓縮first文件底下的所有文件中的壓縮檔，因此若要解壓縮**/first/second/third.zip**，請貼上**/first**)
```
python unzip.py [dir]
```