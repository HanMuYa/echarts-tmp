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
    url1 = get_wps_chart_url()
    js.Application.ActiveWorkbook.Sheets.Item(1).Shapes.AddWebShapeEx(url1)
    return url1