#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*******************************************************************************
# Description:
# Dependances:
# Date:
#*******************************************************************************

""" Basic reg system using webpy 0.3 """
import web
import model
import markdown
from web import form


### Url mappings

urls = (
    '/', 'Login',
    '/login', 'Login',
    '/forget','forget',
    '/reg','register',

)


### Templates
t_globals = {
    'datestr': web.datestr,
    'markdown': markdown.markdown,
}
render = web.template.render('templates', base='base', globals=t_globals)
#render = web.template.render('templates', globals=t_globals)


class Login:
    
    def GET(self):
        f = login_form()
        return render.logins(f)
    def POST(self):
        param = web.input()
        user_name = param.username
        user_password = param.password    
        user_info =  model.get_userbyname(user_name)
        if user_info is not None :
            if user_info['password'] == user_password:
                users = model.get_users()
            return render.showusers(users,user_name)
        else:
            return "false password or User"


def send_mail(send_to, subject, body, cc=None, bcc=None):
    try:
        web.config.smtp_server = 'smtp.163.com'   ##邮件发送服务器
        web.config.smtp_port = 25    ##不设置将使用默认端口
        web.config.smtp_username = '*****'   ##邮件服务器的登录名
        web.config.smtp_password = '******'   ##邮件服务器的登录密码
        web.config.smtp_starttls = True
        send_from = '*****@163.com'    ##发送的邮件
        web.sendmail(send_from, send_to, subject, body, cc=cc, bcc=bcc)
        return 1  #pass
    except Exception, e:
        print e
        return -1 #fail
    
class forget:
    
    def GET(self):
        f = forget_form()
        return render.forget(f)
    
    def POST(self):
        param = web.input()    
        email = param.email
        user_info =  model.get_userbyemail(email)
        password = user_info['password']
        #return password
        #send_mail(email, "password", "%s" %password, cc=None, bcc=None)


vpass = form.regexp(r".{3,20}$", 'must be between 3 and 20 characters')
vemail = form.regexp(r".*@.*", "must be a valid email address")

register_form = form.Form(
    form.Textbox("username", description="Username"),
    form.Textbox("email", vemail, description="E-Mail"),
    form.Password("password", vpass, description="Password"),
    form.Password("password2", description="Repeat password"),
    form.Button("reg", type="submit", description="reg"),

    validators = [
        form.Validator("Passwords did't match", lambda i: i.password == i.password2)]

)

login_form = form.Form(
    form.Textbox("username", description="Username"),
    form.Password("password", vpass, description="Password"),
    form.Button("login", type="submit", description="login")

)


forget_form = form.Form(
    form.Textbox("email", description="email"),
    form.Button("getpass", type="submit", description="getpass")
)

class register:
    def GET(self):
        # do $:f.render() in the template
        f = register_form()
        return render.register(f)

    def POST(self):
        f = register_form()
        if not f.validates():
            return render.register(f)
        else:
            # do whatever is required for registration
            param = web.input()
            user_name = param.username
            user_email = param.email
            user_password = param.password
            model.new_user(name=user_name, password=user_password, email=user_email)
        
        return user_name + " add success"
        #users = model.get_users()
        #return render.showusers(users)        


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
