import colorama

# 初始化 Colorama 函式庫設定
colorama.init(True)

# 樣式設定方式: print(樣式 + 文字 + 樣式 ...)
print("ABC")
# 設定亮度樣式: colorama.Style.樣式名稱
print(colorama.Style.BRIGHT + "ABC")
'''
樣式:
    NORMAL
    BRIGHT
    RESET_ALL (清空樣式)
'''
# 設定文字顏色 colorama.Fore.顏色名稱
print(colorama.Fore.RED + "ABC")

# 設定背景顏色 colorama.Back.顏色名稱
'''
可設定的顏色:
    BLACK
    RED
    GREEN
    YELLOW
    BLUE
    MAGENTA
    CYAN
    WHITE

原始顏色:
    RESET
'''
print(colorama.Fore.GREEN + "ABC")
print(colorama.Back.GREEN + "ABC")
