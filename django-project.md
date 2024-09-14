[TOC]

# django入门课程

# bibi地址：

https://www.bilibili.com/video/BV1KJ41117HL?p=15&vd_source=e2bc0dbeb8bf8c7b4120d5ee387d29bc



# 第二课：

安装python环境

 https://www.python.org/ 

查看是否安装成功:

python -V

![1597493699201](E:\md文件资源\1597493699201.png)

# 第三课：

<u>虚拟环境：</u> 

在powershell中输入：Set-ExecutionPolicy Unrestricted, 让powershell执行命令时不受限制。

查看现在安装的模块：

pip freeze

![1597494151285](E:\md文件资源\1597494151285.png)

安装虚拟环境：（比如虚拟机中的windows系统是独立的）

pip install virtualenv  

![1597494348068](E:\md文件资源\1597494348068.png)

把一个目录做成一个虚拟空间：

virtualenv . 

![1597494723062](E:\md文件资源\1597494723062.png)

切换虚拟环境：

.\Scripts\activate 

![1597495023826](E:\md文件资源\1597495023826.png)

取消虚拟环境：

![1597495193395](E:\md文件资源\1597495193395.png)



# 第四课：

安装django包

pip install django

![1597575218945](E:\md文件资源\1597575218945.png)



# 第五课：创建django项目

创建一个项目

django-admin startproject mysite 

![1597669331704](E:\md文件资源\1597669331704.png)

mysite文件夹的目录结构：

![1597669562841](E:\md文件资源\1597669562841.png)

在vscode中打开工程：

code .

![1597669408641](E:\md文件资源\1597669408641.png)

目录结构：

![1597670076961](E:\md文件资源\1597670076961.png)

启动server：

python .\manage.py runserver

![1597670523428](E:\md文件资源\1597670523428.png)

实际效果：

![1597670594768](E:\md文件资源\1597670594768.png)

有一个警告，解决一下：

![1597670737455](E:\md文件资源\1597670737455.png)



# 第六课：

再创建一个子项目：

​	  （和上面创建项目中命令不同！

​	）

![1597671221660](E:\md文件资源\1597671221660.png)

新的目录结构：

![1597671353387](E:\md文件资源\1597671353387.png)

vscode中的目录结构：

![1597671509151](E:\md文件资源\1597671509151.png)

新建一个app后，需要把子项目和主项目进行关联，切记！

![1597671743724](E:\md文件资源\1597671743724.png)

url设置：

![1597672052511](E:\md文件资源\1597672052511.png)

现在我们的misterwu中还没有urls.py,所以新建：

![1597757587012](E:\md文件资源\1597757587012.png)



# 第七课：

修改misterwu中的urls.py

![1597758998661](E:\md文件资源\1597758998661.png)

在views.py中添加home方法：

![1597759077660](E:\md文件资源\1597759077660.png)

但是我们现在还没有home.html文件：

新建home.html：（放在templates文件夹中	）

![1597759263772](E:\md文件资源\1597759263772.png)

编写html

![1597760571951](E:\md文件资源\1597760571951.png)

启动server，观察效果：

![1597760641628](E:\md文件资源\1597760641628.png)

manage.py //运行项目

# 8 创建公共html模板

bootsharp

新建base.html

类似于php的写法： {% block content %}



# 补充：在 Django 模板中，`{{ }}` 和 `{% %}` 是两种不同的语法，用于不同的目的：

1. 

在 Django 模板中，`{{ }}` 和 `{% %}` 是两种不同的语法，用于不同的目的：

1. **`{{ }}`（双大括号）**：
   - 用于输出变量的值。
   - 在 HTML 中插入动态数据。
- 例如，将变量 `username` 的值插入到模板中。
  
   示例：
   ```html
   <p>用户名是：{{ username }}</p>
   ```
   如果 `username` 的值是 `JohnDoe`，渲染后的 HTML 会是：
   ```html
   <p>用户名是：JohnDoe</p>
   ```
```
   
2. **`{% %}`（百分号加大括号）**：
   - 用于执行模板标签或控制语句。
   - 包含模板语言的逻辑，例如循环、条件判断、模板继承等。
   - 例如，`for` 循环、`if` 条件判断、`block` 标签。

   示例：
   ```html
   {% if user.is_authenticated %}
       <p>欢迎回来，{{ user.username }}!</p>
   {% else %}
       <p>请登录。</p>
   {% endif %}
```

### 总结
- **`{{ }}`**：用于输出变量的值。
- **`{% %}`**：用于执行模板逻辑（如循环和条件判断）。

### 示例代码

结合两者的一个完整示例：

```html
{% extends 'base.html' %}

{% block content %}
    <h1>GitHub 用户列表</h1>

    <div class="container">
        <div class="row">
            {% if api %} <!-- 检查api是否有数据 -->
                {% for x in api %} <!-- 遍历传递过来的api数据 -->
                    <div class="col-sm-4"> <!-- 设置列宽，确保响应式布局 -->
                        <div class="card mb-4" style="width: 18rem;"> <!-- 卡片布局，增加底部边距 -->
                            <img class="card-img-top" src="{{ x.avatar_url }}" alt="Avatar of {{ x.login }}"> <!-- 显示用户头像 -->
                            <div class="card-body">
                                <h5 class="card-title">{{ x.login }}</h5> <!-- 显示用户登录名 -->
                                <p class="card-text">{{ x.login }}的 GitHub</p> <!-- 显示描述文字 -->
                                <a href="{{ x.html_url }}" class="btn btn-primary">访问</a> <!-- 链接到用户的GitHub页面 -->
                            </div>
                        </div>
                    </div>
                {% endfor %}
            {% else %}
                <p>未找到用户。</p> <!-- 当api为空时显示 -->
            {% endif %}
        </div>
    </div>
{% endblock %}
```

在这个示例中：
- **`{% extends 'base.html' %}`** 和 **`{% block content %}`** 等用于模板逻辑。
- **`{{ x.avatar_url }}`** 和 **`{{ x.login }}`** 等用于输出变量的值。





# {% url 'home' %}的作用：

在Django模板中，`{% url 'home' %}` 是用来生成一个特定URL的标记。它的作用是根据URL的名字动态生成对应的URL地址，通常用于链接到不同的视图。

### 用法示例：

#### 1. **定义 URL 名称**：
首先，在 `urls.py` 文件中定义一个命名的URL模式。例如，假设你有一个指向主页的视图：

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 这里的 'home' 就是 URL 名称
]
```

#### 2. **模板中的用法**：
在模板中，你可以使用 `{% url %}` 标签来引用这个命名的 URL：

```html
<a href="{% url 'home' %}">Home</a>
```

这个代码会根据你在 `urls.py` 中定义的 URL 名称 `'home'` 自动生成相应的 URL 地址。例如，如果你的主页地址是 `/`，那么上面的代码生成的 HTML 可能是：

```html
<a href="/">Home</a>
```

### 适用于的场景：
- **动态生成URL**：如果你修改了 URL 配置（比如把 `home` 对应的路径从 `'/'` 改为 `'/homepage/'`），你只需要在 `urls.py` 中更新，而模板中的 `{% url 'home' %}` 会自动反映这种变化。
- **减少硬编码**：避免在模板中直接写死URL地址，有利于维护和代码的可读性。

### 传递参数：
如果某个URL需要参数，你可以在 `{% url %}` 标签中传递。例如：

```python
# urls.py
path('article/<int:id>/', views.article_detail, name='article_detail'),
```

```html
<a href="{% url 'article_detail' id=5 %}">Read Article</a>
```

这会生成类似 `"/article/5/"` 的URL。



# 9 展示导航信息

上下左右有间隙：

navbar

# 10 api接口

api测试网站：api.github和jsonhoder

restapi

# 11 接口请求和解析

安装request模块

pip install requests



![puthon_111](E:\md文件资源\puthon_111.PNG)

![python_222](E:\md文件资源\python_222.png)

home.html中：

{{api}}

# 12 展示数据信息

遍历：

{% for x in api%}

{% endfor%}

# 13 搜索

## 1

base.html中：

![us](C:\Users\WGJ\Desktop\python_md\us.png)

urls.py中：

![us1](C:\Users\WGJ\Desktop\python_md\us1.png)

## 二

![1650443028281](C:\Users\WGJ\Desktop\python_md\1650443028281.png)

传递输入框的文字



![1650443143200](C:\Users\WGJ\Desktop\python_md\1650443143200.png)

这两处保持一致



# 14

