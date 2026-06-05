import micropip

async def install_deps(lib):
    await micropip.install(lib)

await install_deps("pyecharts")

from pyodide.ffi import create_proxy
import json
from pyecharts.charts import Bar
from pyecharts import options as opts
import js

from pyecharts.charts import Map
from pyecharts import options as opts
import json as _json

def get_sichuan_map_url():
    data = [
        ("成都市", 120),
        ("绵阳市", 120)
    ]

    m = (
        Map()
        .add("GDP（亿元）", data, maptype="四川")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="四川省各市数据", pos_left="center"),
            visualmap_opts=opts.VisualMapOpts(max_=120, is_piecewise=True),
        )
    )

    options_json = m.dump_options_with_quotes()

    result = _json.loads(save_echart_option(options_json))
    if "error" in result:
        raise RuntimeError(result["error"])

    chart_id = result["chart_id"]
    base = "file:///C:/Users/suma/AppData/Roaming/kingsoft/wps/jsaddons/Py-Excel_1.0.0/ui/echart_renderer.html"
    return f"{base}?chartId={chart_id}"


def get_guizhou_map_url():
    data = [
        ("贵阳市", 120),
        ("遵义市", 95),
        ("六盘水市", 70),
        ("安顺市", 55),
        ("毕节市", 88),
        ("铜仁市", 50),
        ("黔西南布依族苗族自治州", 42),
        ("黔东南苗族侗族自治州", 58),
        ("黔南布依族苗族自治州", 52),
    ]

    m = (
        Map()
        .add("GDP（亿元）", data, maptype="贵州")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="贵州省各市数据", pos_left="center"),
            visualmap_opts=opts.VisualMapOpts(max_=120, is_piecewise=True),
        )
    )

    options_json = m.dump_options_with_quotes()

    result = _json.loads(save_echart_option(options_json))
    if "error" in result:
        raise RuntimeError(result["error"])

    chart_id = result["chart_id"]
    base = "file:///C:/Users/suma/AppData/Roaming/kingsoft/wps/jsaddons/Py-Excel_1.0.0/ui/echart_renderer.html"
    return f"{base}?chartId={chart_id}"

def get_wps_chart_url():
    import json as _json

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

    # 3. 保存到 xlsx 内置 CustomXMLPart
    result = _json.loads(save_echart_option(options_json))
    if "error" in result:
        raise RuntimeError(result["error"])

    chart_id = result["chart_id"]

    # 4. 拼接本地渲染器 URL
    base = "file:///C:/Users/suma/AppData/Roaming/kingsoft/wps/jsaddons/Py-Excel_1.0.0/ui/echart_renderer.html"
    url = f"{base}?chartId={chart_id}"

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
def url():
    import js 
    js.saveEchartOption()
    # js.Application.ActiveWorkbook.Sheets.Item(1).Shapes.AddWebShapeEx("file:///C:/Users/suma/AppData/Roaming/Kingsoft/wps/jsaddons/Py-Excel_1.0.0/ui/charts.html")
    url1 = get_sichuan_map_url() # get_guizhou_map_url() # get_wps_chart_url()
    js.Application.ActiveWorkbook.Sheets.Item(1).Shapes.AddWebShapeEx(url1)
    return url1

@wps_py_func
def hh():
    return 123