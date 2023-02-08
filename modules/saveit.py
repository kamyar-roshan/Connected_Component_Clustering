import xlsxwriter

def saveit(data1, data2, data3, data4, file_name):
    
    workbook = xlsxwriter.Workbook('clusters_' + file_name + '.xlsx')
    worksheet = workbook.add_worksheet()

    for col, data in enumerate(data1):
        worksheet.write_column(0, 0, data1)
        worksheet.write_column(0, 1, data2)
        worksheet.write_column(0, 2, data3)
        worksheet.write_column(0, 3, data4)

    workbook.close()
