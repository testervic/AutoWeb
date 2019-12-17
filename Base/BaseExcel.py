import xlsxwriter
import os

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperateReport:
    def __init__(self, wd):
        self.wd = wd

    def init(self, worksheet, data):
        # 设置列行的宽高
        worksheet.set_column("A:A", 15)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)

        worksheet.set_row(1, 30)
        worksheet.set_row(2, 30)
        worksheet.set_row(3, 30)
        worksheet.set_row(4, 30)

        define_format_H1 = get_format(self.wd, {'bold': True, 'font_size': 18})
        define_format_H2 = get_format(self.wd, {'bold': True, 'font_size': 14})
        define_format_H1.set_border(1)

        define_format_H2.set_border(1)
        define_format_H1.set_align("center")
        define_format_H2.set_align("center")
        define_format_H2.set_bg_color("blue")
        define_format_H2.set_color("#ffffff")

        worksheet.merge_range('A1:D1', '测试报告总概况', define_format_H1)
        worksheet.merge_range('A2:D2', '自动化测试项目', define_format_H2)

        _write_center(worksheet, "A3", '测试日期', self.wd)
        _write_center(worksheet, "A4", '耗时', self.wd)
        _write_center(worksheet, "A5", '总用例', self.wd)

        _write_center(worksheet, "B3", data['testDate'], self.wd)
        _write_center(worksheet, "B4", data['testSumDate'], self.wd)
        _write_center(worksheet, "B5", data['sum'], self.wd)

        _write_center(worksheet, "C3", "通过", self.wd)
        _write_center(worksheet, "C4", "失败", self.wd)
        _write_center(worksheet, "C5", "脚本版本", self.wd)

        _write_center(worksheet, "D3", data['pass'], self.wd)
        _write_center(worksheet, "D4", data['fail'], self.wd)
        _write_center(worksheet, "D5", data['version'], self.wd)

        pie(self.wd, worksheet)

    def detail(self, worksheet, info):
        # 设置列行的宽高
        worksheet.set_column("A:A", 20)
        worksheet.set_column("B:B", 20)
        worksheet.set_column("C:C", 20)
        worksheet.set_column("D:D", 20)
        worksheet.set_column("E:E", 20)
        worksheet.set_column("F:F", 20)
        worksheet.set_column("G:G", 20)
        worksheet.set_column("H:H", 20)
        worksheet.set_column("I:I", 30)
        worksheet.set_column("J:J", 30)

        worksheet.set_row(1, 40)
        worksheet.set_row(2, 40)
        worksheet.set_row(3, 40)
        worksheet.set_row(4, 40)
        worksheet.set_row(5, 40)
        worksheet.set_row(6, 40)
        worksheet.set_row(7, 40)
        worksheet.set_row(8, 40)
        worksheet.set_row(9, 40)
        worksheet.set_row(10, 40)

        worksheet.merge_range('A1:J1', '测试详情', get_format(self.wd, {'bold': True, 'font_size': 18, 'align': 'center',
                                                                    'valign': 'vcenter', 'bg_color': 'blue',
                                                                    'font_color': '#ffffff'}))
        _write_center(worksheet, "A2", '设备', self.wd)
        _write_center(worksheet, "B2", '用例ID', self.wd)
        _write_center(worksheet, "C2", '用例介绍', self.wd)
        _write_center(worksheet, "D2", '用例函数', self.wd)
        _write_center(worksheet, "E2", '前置条件', self.wd)
        _write_center(worksheet, "F2", '操作步骤 ', self.wd)
        _write_center(worksheet, "G2", '检查点 ', self.wd)
        _write_center(worksheet, "H2", '测试结果 ', self.wd)
        _write_center(worksheet, "I2", '截图', self.wd)

        temp = 3
        for item in info:
            _write_center(worksheet, "A" + str(temp), item["name"], self.wd)
            _write_center(worksheet, "B" + str(temp), item["id"], self.wd)
            _write_center(worksheet, "C" + str(temp), item["title"], self.wd)
            _write_center(worksheet, "D" + str(temp), item["caseName"], self.wd)
            _write_center(worksheet, "E" + str(temp), item["info"], self.wd)
            _write_center(worksheet, "F" + str(temp), item["step"], self.wd)
            _write_center(worksheet, "G" + str(temp), item["checkStep"], self.wd)
            _write_center(worksheet, "H" + str(temp), item["result"], self.wd)
            _write_center(worksheet, "I" + str(temp), "", self.wd)
            if item.get("img", "false") == "false":
                _write_center(worksheet, "I" + str(temp), "", self.wd)
                worksheet.set_row(temp, 30)
            else:
                worksheet.insert_image('I' + str(temp), item["img"],
                                       {'x_scale': 0.2, 'y_scale': 0.2, 'border': 1})
                worksheet.set_row(temp - 1, 110)
            temp += 1

    def close(self):
        self.wd.close()


def get_format(wd, option={}):
    return wd.add_format(option)


def get_format_center(wd, num=1):
    return wd.add_format({'align': 'center', 'valign': 'vcenter', 'border': num})


def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)


def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))


def set_row(worksheet, num, height):
    worksheet.set_row(num, height)

    # 生成饼形图


def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
        'name': '自动化测试统计',
        'categories': '=测试总况!$C$3:$C$4',
        'values': '=测试总况!$D$3:$D$4',
    })
    chart1.set_title({'name': '测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})


if __name__ == '__main__':
    pass
