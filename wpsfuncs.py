import micropip

async def install_deps(lib):
    await micropip.install(lib)

await install_deps("pyecharts")

from pyodide.ffi import create_proxy
import json
from pyecharts.charts import Bar
from pyecharts import options as opts
import js

def get_wps_chart_url():
    # 1. 生成图表
    bar = (
        Bar()
        .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
        .add_yaxis("销量", [5, 20, 36, 0, 75, 90])
        .set_global_opts(
            title_opts=opts.TitleOpts(title="衬衫销量统计", pos_left="center")
        )
    )

    # 2. 拿到 JSON 字符串
    options_json = bar.dump_options_with_quotes()

    # 3. 【核心】调用 JS 全局函数 encodeURIComponent
    # js 命名空间直接映射了全局 JS 对象
    encoded_uri = js.encodeURIComponent(options_json)

    # 4. 拼接 URL
    url = f"https://hanmuya.github.io/echarts-tmp/#data={encoded_uri}"
    
    return url

@wps_py_func
def py_add(a, b):
    """
    基础加法函数。
    支持单元格单值直接相加，返回两数之和。
    """
    v1 = clean_val(a)
    v2 = clean_val(b)
    return float(v1) + float(v2)

@wps_py_func
def py_to_upper(text_range):
    """
    大写转换函数。
    支持选择 A1:B5 矩阵区域，将范围内所有英文文本转为大写格式。
    """
    if isinstance(text_range, list):
        return [[str(cell).upper() if cell is not None else "" for cell in row] for row in text_range]
    return str(text_range).upper()

@wps_py_func
def myfun():
    import js

    js.insertMplAsPicture("https://haowallpaper.com/link/common/file/getCroppingImg/40e146ce8bfa8e91abd1fb6576a692e9")
    
    # 需要用户至少有一个sheet
    # js.Application.ActiveWorkbook.Sheets.Item(1).Shapes.AddWebShapeEx("https://hanmuya.github.io/echarts-tmp/#data=%7B%22title%22%3A%7B%22text%22%3A%22%E8%A1%AC%E8%A1%AB%E9%94%80%E9%87%8F%E7%BB%9F%E8%AE%A1%22%2C%22left%22%3A%22center%22%7D%2C%22tooltip%22%3A%7B%7D%2C%22xAxis%22%3A%7B%22type%22%3A%22category%22%2C%22data%22%3A%5B%22%E8%A1%AC%E8%A1%AB%22%2C%22%E7%BE%8A%E6%AF%9B%E8%A1%AB%22%2C%22%E9%9B%AA%E7%BA%BA%E8%A1%AB%22%2C%22%E8%A3%A4%E5%AD%90%22%2C%22%E9%AB%98%E8%B7%9F%E9%9E%8B%22%2C%22%E8%A2%9C%E5%AD%90%22%5D%7D%2C%22yAxis%22%3A%7B%22type%22%3A%22value%22%7D%2C%22series%22%3A%5B%7B%22name%22%3A%22%E9%94%80%E9%87%8F%22%2C%22type%22%3A%22bar%22%2C%22data%22%3A%5B5%2C20%2C36%2C0%2C75%2C90%5D%7D%5D%7D")

    t = get_wps_chart_url()
    js.Application.ActiveWorkbook.Sheets.Item(1).Shapes.AddWebShapeEx(t)

    return t