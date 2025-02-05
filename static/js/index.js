// static/js/index.js

document.addEventListener('DOMContentLoaded', function() {
    loadTools();
});

function loadTools() {
    fetch('/tools')  // 请求后端的 /tools 路由
        .then(response => {
            if (!response.ok) {
                throw new Error('网络响应失败');
            }
            return response.text();  // 读取返回的 HTML 内容
        })
        .then(data => {
            document.getElementById('tool-list').innerHTML = data;  // 插入到页面中的 tool-list 容器
        })
        .catch(error => {
            console.error('加载工具时出错:', error);
        });
}
