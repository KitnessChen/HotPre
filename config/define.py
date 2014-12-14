from tornado.options import define

# port config
define("port", default=8000, help="run on the given port", type=int)

# file path config
define("rowdata_path", default="/Users/kitnesschen/spider/HotPre/data/row_data", help="row data path")
define("finaldata_path", default="/Users/kitnesschen/spider/HotPre/data/final_data", help="final data path")
define("sample_path", default="/Users/kitnesschen/spider/HotPre/data/samples", help="samples path")

# static path config
define("template_path", default="/Users/kitnesschen/spider/HotPre/templates", help="templates path")
define("static_path", default="/Users/kitnesschen/spider/HotPre/static", help="static file path")
