with open('excel.xlsx', 'r') as File:
    print(File)
with open('excel.xlsx', 'r', encoding="UTF-8") as File:
    print(File)
with open('excel.xlsx', 'w', encoding="UTF-8") as File:
    File.write("adsf")
#써지지도 않습니다 하지마세요 ㅋㅋ