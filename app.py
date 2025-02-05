import flask
import os
import json

# 这是一个工具网站
# 允许用户上传自己编写的小工具
# 并且以标准输入输出
# 作者：daishuge

# 加载tool文件夹下的工具列表
def load_tools():
    all_items = os.listdir("tools")
    # 过滤出文件夹
    folders = [item for item in all_items if os.path.isdir(os.path.join("tools", item))]
    
    page = ""
    
    for d in folders:
        # 构建info.json路径
        info_path = os.path.join("tools", d, "info.json")
        with open(info_path, 'r',encoding="UTF-8") as f:
            info = json.load(f)
        
        if "logo" not in info or not info["logo"] or info["logo"] == "" or info["logo"] == "null" or "none":
            tool_logo = "https://i.mij.rip/2025/02/05/03bea1b8bb54fa91bbd6de6bd3965c06.th.jpeg"
        else:
            tool_logo = info["logo"]
        
        page = page + f'''
        <a href="/tools/{info["author"]}/{info["name"]}" class="tool-card">
        <div class="tool-logo-wrapper">
            <img src="{tool_logo}" alt="Tool Logo" class="tool-logo">
        </div>
        <div class="tool-content">
            <h3 class="tool-title">{info["name"]}</h3>
            <p class="tool-description">{info["description"]}</p>
        </div>
        </a>
        '''
    
    return page
        
                


app = flask.Flask(__name__)

# 展示首页 templates/index.html
@app.route('/')
def index():
    return flask.render_template('index.html')  # 确保这里的文件名和 templates 文件夹中的一致

# 返回工具列表
@app.route('/tools')
def tools():
    return load_tools()

# 展示登陆页面 templates/login.html
@app.route('/login')
def login():
    return flask.render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
