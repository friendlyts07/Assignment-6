#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install emails')


# In[14]:


get_ipython().system('pip install emails')


# In[15]:


import emails


# In[18]:


html_text ='''<html>

             <head>
             <meta charset="utf-8">
             <meta name="viewport" content="width=device-width, initial-scale=1.0">
             <title></title>
             </head>

             <body style="color: rgb(0, 0, 0); background-color: rgb(49, 175, 40);">
             <p>Hello Everyone😊,</p>
             <p>Tirth Shah your classmate is Here.</p>
             <p>Hope you all are fine. How are your studies going on and do you like the subject you have taken? I am not mailing this to you to ask such question it was just a fun. I have learned a project that how can we send mail using python. So for checking purpose i am sending this mail.</p>
             <p>I know i have returned that the message will contain some special message and the special message is Don&apos;t be sad when you fail because failure is the key to success. Hope you all like it&nbsp;</p>
             <p><strong>Tirth Shah</strong></p>
             <p><strong>8000914488</strong></p>
             <p><br></p>
             <p><br></p>
             <p><br></p>
             </body>

             </html>'''
message = emails.html(html=html_text,
                          subject="Email from python",
                          mail_from=('Secret Superstar', 'sai@xyz.com'))


# In[19]:


mail_via_python = message.send(to='shahti42@gmail.com', 
                               smtp={'host': 'smtp.gmail.com', 
                                     'timeout': 5,
                                    'port':587,
                                    'user':'youremail',
                                    'password':'youremailpas',
                                    'tls':True})


# In[20]:


mail_via_python.status_code


# In[26]:


def personalemails(email):
    html_text ='''<html>

                  <head>
                  <meta charset="utf-8">
                  <meta name="viewport" content="width=device-width, initial-scale=1.0">
                  <title></title>
                  </head>

                  <body style="color: rgb(0, 0, 0); background-color: rgb(49, 175, 40);">
                  <p>Hello Everyone😊,</p>
                  <p>Tirth Shah your classmate is Here.</p>
                  <p>Hope you all are fine. How are your studies going on and do you like the subject you have taken? I am not mailing this to you to ask such question it was just a fun. I have learned a project that how can we send mail using python. So for checking purpose i am sending this mail.</p>
                  <p>I know i have returned that the message will contain some special message and the special message is Don&apos;t be sad when you fail because failure is the key to success. Hope you all like it&nbsp;</p>
                  <p><strong>Tirth Shah</strong></p>
                  <p><strong>8000914488</strong></p>
                  <p><br></p>
                  <p><br></p>
                  <p><br></p>
                  </body>

                  </html>'''
    message = emails.html(html=html_text,
                          subject="Email from python",
                          mail_from=('Secret Superstar', 'sai@xyz.com'))
    mail_via_python = message.send(to=email, 
                               smtp={'host': 'smtp.gmail.com', 
                                     'timeout': 5,
                                    'port':587,
                                    'user':'youremail',
                                    'password':'youremailpas',
                                    'tls':True})
    return mail_via_python.status_code

    


# In[30]:


personalemails("machhisudha11111@gmail.com")


# In[31]:


personalemails("bhagatmanan2@gmail.com")


# In[32]:


personalemails("ranarutvik100@gmail.com")


# In[33]:


personalemails("kishlayshah21102000@gmail.com")


# In[34]:


personalemails("deepvaikunth05@gmail.com")


# In[35]:


personalemails("vss11101995@gmail.com")


# In[36]:


personalemails("sonalashu2000@gmail.com")


# In[37]:


personalemails("dhvanichampaneri5@gmail.com")


# In[38]:


personalemails("sharmashivani85307@gmail.com")


# In[39]:


personalemails("shivammishra1013@gmail.com")


# In[40]:


personalemails("mohansuryavanshi1999@gmail.com")


# In[41]:


personalemails("ashu12345ti@gmail.com")


# In[42]:


personalemails("jaypatel180140111061@gmail.com")


# In[ ]:




