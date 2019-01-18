from django.db import models

# 参照群内上传的数据库表
"""
--------------------------------------------------------------------------------------------------------
类型参照表
--------------------------------------------------------------------------------------------------------
                                models                                            mysql/oracle
                                
自增类型                       AutoField                                 

整数           IntegerField/TinyintField/BigIntegerField                             int/number 

单精度浮点                    FloatField/                                              float   

高精度浮点                    DecimalField                                            decimal
                                                                                                                                                       
                                                                                      char
字符                           CharField                                                       
                                                                                 varchar/varchar2   
                               
文本域                        TextField                                               text

日期                          DateField                                               date

时间                        DateTimeField                                           datetime/timestamp

---------------------------------------------------------------------------------------------------------
字段约束参照表
---------------------------------------------------------------------------------------------------------
主键约束       primary_key = True | False 

唯一约束       unique = True | False 

最大长度       max_length =

默认值         default = 0 | True | False

空值约束       null = True | False  

索引字段        db_index = True

               DateTimeField(auto_now=True | auto_now_add=True)    auto_now每次更新数据库重新赋予时间    
时间约束                                                           auto_now_add 永远为第一次创建的时间 
               DateField 

外键约束

---------------------------------------------------------------------------------------------------------

"""


class Banner(models.Model):
    pass

    class Meta:
        db_table = 'banner'
