"""配置导出/导入示例：展示 export_config 和 from_config 的使用。

通过 export_config() 将图表的完整配置导出为可序列化字典，
再通过 from_config() 从配置字典重建图表实例，实现配置的保存与复用。
"""
import simplejson as json

from pyantv import Line

# 1. 创建并配置一个图表
original_chart = (
    Line()
    .set_data(
        data=[
            {"month": "Jan", "sales": 120},
            {"month": "Feb", "sales": 180},
            {"month": "Mar", "sales": 250},
            {"month": "Apr", "sales": 210},
            {"month": "May", "sales": 340},
        ]
    )
    .set_encode(x_field_name="month", y_field_name="sales")
    .set_title("Monthly Sales")
    .set_theme("dark")
    .set_size(is_auto_fit=True)
)

# 2. 导出配置为字典
config = original_chart.export_config()
print("Exported config keys:", list(config.keys()))
print("Chart class:", config["chart_class"])

# 3. 序列化为 JSON（可保存到文件）
config_json = json.dumps(config, indent=2, ignore_nan=True)
print("\nConfig JSON preview (first 200 chars):")
print(config_json[:200], "...")

# 4. 从配置字典重建图表
restored_chart = Line.from_config(config)
print("\nRestored chart data:", restored_chart.get_options().get("data"))
print("Restored chart encode:", restored_chart.get_options().get("encode"))

# 5. 渲染重建后的图表
restored_chart.render("config_export_restored.html")
print("\nRestored chart rendered to config_export_restored.html")
